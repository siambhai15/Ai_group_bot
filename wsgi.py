#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wsgi.py — WSGI entry point for Render.com (and any gunicorn/uvicorn host).

This module exposes a top-level `application` (and `app`) callable that
gunicorn can serve.  It also starts the Telegram bot's long-polling loop
in a background daemon thread, so a single Render Web Service runs BOTH:

    * the public Flask web panel  (served by gunicorn on $PORT)
    * the Telegram bot polling    (background thread inside this process)

Usage on Render:
    Start Command:  gunicorn wsgi:application --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 120

IMPORTANT: use exactly ONE worker (--workers 1) so there is only a single
bot instance polling Telegram.  Multiple workers would cause conflicting
polling and Telegram "409 Conflict" errors.
"""
import os
import sys
import time
import threading
import logging

# Make sure the bot module is importable (this file sits next to ai_group1.py)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import ai_group1 as bot_mod

log = logging.getLogger("wsgi")
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s")

# 1) Always create / migrate the database (uses DATA_DIR env if set).
db = bot_mod.Database(bot_mod.DB_PATH)

# 2) Build the Flask app in "setup mode" (bot_app=None).  The bot, once
#    started, registers itself via set_bot_instance() so the panel picks it up.
flask_app = bot_mod.create_web_panel(bot_app=None, shared_db=db)
if flask_app is None:
    raise RuntimeError("Flask could not be imported / panel not created. "
                       "Did you `pip install flask`?")
flask_app._ensure_password()

# Expose WSGI callables
application = flask_app
app = flask_app  # some hosts look for `app`


# 3) Start the Telegram bot in a background thread IF a valid token exists.
def _bot_thread():
    while True:
        try:
            tok = db.get_setting("bot_token", "")
            if not bot_mod._token_is_valid(tok):
                # No token yet — wait for the user to set it via the web panel.
                time.sleep(5)
                continue
            log.info("🤖 Starting Telegram bot (token detected)...")
            bot = bot_mod._start_bot_thread(db)
            if bot is not None:
                # _start_bot_thread runs bot.run() which BLOCKS until the bot stops.
                # If it returns, the bot exited — loop and try to restart.
                log.warning("⚠️ Bot loop returned. Restarting in 5s...")
            else:
                log.warning("⚠️ Bot failed to start (bad token?). Will retry in 10s.")
            time.sleep(10)
        except Exception as exc:
            log.error("Bot thread error: %s — retrying in 15s", exc)
            time.sleep(15)


_bot_runner = threading.Thread(target=_bot_thread, name="telegram-bot", daemon=True)
_bot_runner.start()

log.info("✅ wsgi.py ready — Flask panel served by gunicorn, bot polling in background thread.")
