# 🤖 AI Group Management Bot + Web Panel

A professional **Rose-bot-style group management bot** with a built-in **Groq-powered AI assistant**, an integrated **Flask web admin panel**, and one-click **Render.com** deployment. Single file (`ai_group1.py`) runs both the Telegram bot (long-polling) and the web panel.

---

## ✨ Features

### 🛡️ Group Management (Rose-bot style)
- **Mute / Unmute / Ban / Unban** (permanent + timed `tmute`/`tban`)
- **Kick** (`/kick` on reply) + **self-kick** (`/kickme`)
- **Warn system** with configurable limit + action (mute/ban/tmute)
- **Delete messages** (`/del` on reply)
- **Admin list**, **user info lookup** (`/userinfo`)
- **Silent ban/mute** (no notification)

### 🔍 Filters (Rose-bot style)
- `/filter {name} {message}` — save a filter; typing the name in group → bot replies
- `/filters` — list all, `/remove {name}` — delete
- **Formatting engine**: `<b>bold</b>`, `<u>underline</u>`, `<i>italic</i>`, `<s>strike</s>`, `<code>code</code>`, `<c>copy-on-click</c>`, `<spoiler>...</spoiler>`
- **Buttons**: `[btn:Button Label]<https://link>` (multiple supported)
- **Placeholders**: `<first>`, `<username>`, `<id>`, `<mention>` (replied user info)

### 👋 Welcome System
- `/setwelcom {message}` — set custom welcome (with formatting + placeholders)
- `/welcome` — show current, `/welcome on|off` — toggle
- New member → mentioned + welcome message
- AI can auto-generate a group-name-related welcome with emojis + rules

### 📢 Promote / Force-Join
- `/promote {time} {channel_link}` (owner only) — non-admin messages deleted + "please join first" notice (English + Bengali) with **Join Now** button(s), auto-deletes after 15s
- Multiple promote links → multiple buttons
- Bot must be admin in the channel/group, else rejected
- No time → unlimited expiry; bot removed from channel → auto-deactivate link

### 🚫 Banned Keywords
- `/banned keyword {word}` — add banned word
- `/banned keyword action {mute|ban|kick|tmute} {time}` — set action
- Message containing the word → configured action executes

### 🛡️ Protection System
- `/setprotection admin {user_id}` (owner) — set protection admin
- `/protection on|off` — toggle
- New member joins → **muted** + admins mentioned with new user's details + **Unmute** button (admin type)
- Or new user mentioned with self-**Unmute** button (user type)

### 📢 Mention Protection
- `/mention on|off`, `/set mention action {mute|ban|tmute|none}`
- @-mentions deleted + warning/action; `none` = delete only
- Admin/owner mentions allowed

### 📢 Announcement / Broadcast
- `/announcement {message}` (owner) — broadcasts to all groups/channels where bot is admin AND all users who started the bot
- Formatted + multiple buttons

### 🤖 AI Assistant (Groq-powered)
- **AI on `/start`** — explains in detail (with examples) how to use the bot, add to a group, set commands
- Answers questions about **any command** with detail + example
- **Executes bot commands** when an admin asks via reply (mute/unmute/ban/unban/tmute/tban/kick)
- Gives **user details** when admin asks
- **Manages filters / welcome / promote links / banned keywords** when asked
- **Full DB access/control** via ACTION-line protocol
- **Multiple trigger words** (maisha, মাইশা, maisa, …) — editable from the web panel
- Per-group AI gating (`/allow_ai` by owner)

### 🌐 Web Admin Panel (mobile-responsive)
- **Dashboard**: total groups, allowed, AI-enabled, bans, mutes, warns, filters, welcomes, promote links, banned keywords, bot starters, tracked members
- **Group detail** with tabs: Moderation, Members, Filters, Welcome, Promote, Banned KW, Protection, Mention
- Manage **everything** from the panel (add/remove filters, welcome, promote links, banned keywords, protection, mention settings)
- **User lookup** by Telegram ID (name, username, profile photo, bio, active actions)
- **Settings page**: Bot Token, Groq API Key, Owner ID, Support Link, AI toggle, **AI trigger words management**, admin password
- Fully **mobile-responsive** CSS

---

## 📋 All Commands

### Owner / Admin commands (group only)
| Command | Description |
|---|---|
| `/ban` (reply) | Ban user permanently |
| `/unban` (reply) | Unban user |
| `/mute` (reply) | Mute permanently |
| `/unmute` (reply) | Unmute |
| `/tmute {time}` (reply) | Timed mute (e.g. `/tmute 1h30m`) |
| `/tban {time}` (reply) | Timed ban |
| `/silentban` / `/silentmute` (reply) | Ban/mute without notification |
| `/kick` (reply) | Kick user (can rejoin) |
| `/warn` (reply) | Warn user |
| `/warnings` (reply) | Show warning count |
| `/resetwarns` (reply) | Reset warnings |
| `/warnlimit {n}` | Set warn limit |
| `/setwarnaction {mute\|ban\|tmute}` | Set warn action |
| `/show_warnaction` | Show current warn action |
| `/del` (reply) | Delete message |
| `/userinfo {user_id}` | Look up a user |
| `/admins` | List group admins |
| `/id` | Show your Telegram ID |
| `/filter {name} {message}` | Add a filter |
| `/filters` | List all filters |
| `/remove {name}` | Remove a filter |
| `/setwelcom {message}` | Set welcome message |
| `/welcome` | Show / toggle welcome (`/welcome on\|off`) |
| `/promote {time} {link}` (owner) | Add force-join promote link |
| `/banned keyword {word}` | Add banned keyword |
| `/banned keyword action {action} {time}` | Set banned keyword action |
| `/mention on\|off` | Toggle mention protection |
| `/setmention {action}` | Set mention action |
| `/setprotection admin {user_id}` (owner) | Set protection admin |
| `/protection on\|off` | Toggle protection |
| `/announcement {message}` (owner) | Broadcast to all groups + starters |
| `/allow_ai` (owner) | Enable AI in this group |
| `/disallow_ai` (owner) | Disable AI in this group |
| `/showai` | Show AI status |
| `/panel` | In-bot owner panel |

### Member commands
| Command | Description |
|---|---|
| `/kickme` | Kick yourself |
| `/start` | Start bot (AI explains everything) |
| `/help` | Full command help |
| `/newchat` | Clear your AI chat memory |

### AI trigger
Type any **trigger word** (e.g. `maisha`, `মাইশা`) in an AI-enabled group, or reply to a user and ask the AI to act (admins only).

---

## 🚀 Deploy on Render.com (recommended)

### Prerequisites
1. A **Telegram Bot Token** from [@BotFather](https://t.me/BotFather)
2. A **Groq API Key** from [console.groq.com](https://console.groq.com) (free)
3. Your **Telegram user ID** (get it from [@userinfobot](https://t.me/userinfobot))
4. A [GitHub](https://github.com) or [GitLab](https://gitlab.com) account

### Step 1 — Push to Git
Upload the entire `bot_project` folder contents to a new GitHub/GitLab repo. The repo must contain:
```
ai_group1.py
wsgi.py
render.yaml
requirements.txt
templates/   (base.html, dashboard.html, group.html, login.html, settings.html)
```

### Step 2 — Create the Render Blueprint
1. Go to **https://dashboard.render.com** → **New** → **Blueprint**
2. Select your repository. Render reads `render.yaml` and creates a **Web Service**.
3. The service runs: `gunicorn wsgi:application --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 120`

### Step 3 — (Recommended) Add a Persistent Disk
The SQLite database is stored on the filesystem. On Render's **free tier** the filesystem is **ephemeral** — it resets on every redeploy, which means your settings/groups would be lost. To keep data permanently:

- **Option A (free tier, manual backup):** After setup, periodically export the DB. Not recommended for production.
- **Option B (Starter plan + disk):** Upgrade to the **Starter** plan ($7/mo) in the Render dashboard, then:
  - Service → **Disks** → **Add Disk**
  - **Mount Path:** `/var/data`
  - **Size:** 1 GB
  - Set the env var `DATA_DIR=/var/data` (already in `render.yaml`)
  - This keeps your `group_manager.db` across redeploys.

> ℹ️ The bot already auto-creates the `DATA_DIR` if it doesn't exist, and stores the DB there when `DATA_DIR` is set.

### Step 4 — Set Environment Variables
In the Render dashboard → **Environment**, set:
| Variable | Value | Required? |
|---|---|---|
| `WEB_SECRET_KEY` | (auto-generated by Blueprint) | Yes (auto) |
| `BOT_TOKEN` | Your BotFather token | Optional* |
| `GROQ_API_KEY` | Your Groq key | Optional* |
| `OWNER_ID` | Your Telegram user ID | Optional* |
| `SUPPORT_LINK` | `https://t.me/your_support` | Optional |
| `DATA_DIR` | `/var/data` (with disk) | Optional |

\* You can leave `BOT_TOKEN`/`GROQ_API_KEY`/`OWNER_ID` **blank** and set them later from the web panel **Settings** page. The bot auto-starts a few seconds after you save a valid token.

### Step 5 — First Login
1. Once deployed, Render gives you a public URL like `https://ai-group-management-bot.onrender.com`.
2. Open the **Logs** tab in Render and find the banner:
   ```
   WEB PANEL ADMIN PASSWORD (save this!):
   xxxxxxxxxxxxxxxx
   ```
3. Open the public URL, log in with that password.
4. Go to **Settings** → enter your **Bot Token**, **Groq API Key**, **Owner ID** → **Save**.
5. The bot **auto-starts** within ~5 seconds. The status banner turns green 🟢.
6. Add the bot to your Telegram group, make it **admin** with permissions: *Delete messages*, *Ban users*, *Restrict members*, *Invite users*.
7. In the group, the owner runs `/allow_ai` to enable AI features.

### ⚠️ Important Render Notes
- **Use `--workers 1`** (already set). Multiple workers = multiple bot instances polling Telegram = `409 Conflict` errors.
- **Free tier sleeps** after 15 min of inactivity. The bot stops polling while asleep. The first web request wakes it. For 24/7 uptime, use the **Starter** plan or an external uptime ping (e.g. [cron-job.org](https://cron-job.org)) hitting your URL every 10 min.
- **Re-login after redeploy** if you didn't set a persistent disk (session is in-memory/ephemeral). Set a custom admin password in Settings to make it predictable.

---

## 💻 Run Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run (starts web panel + bot when token is set)
python3 ai_group1.py
#    -> Opens web panel on http://localhost:8080
#    -> Prints the admin password in the console
#    -> Log in, set Bot Token + Groq Key in Settings, bot auto-starts

# OR run with gunicorn (web panel public, bot in background thread)
gunicorn wsgi:application --bind 0.0.0.0:8080 --workers 1 --threads 4
```

### Environment variables (optional, all overridable from web panel)
| Variable | Default | Description |
|---|---|---|
| `BOT_TOKEN` | `PUT-YOUR-...` | Telegram bot token |
| `GROQ_API_KEY` | `PUT-YOUR-...` | Groq API key |
| `OWNER_ID` | `7970107324` | Bot owner Telegram ID |
| `SUPPORT_LINK` | `https://t.me/` | Support contact link |
| `WEB_PORT` | `8080` | Web panel port |
| `WEB_SECRET_KEY` | random | Flask session secret |
| `DATA_DIR` | (none) | Persistent DB directory |

---

## 🧪 Tests

Two smoke tests are included (run them before deploying):
```bash
python3 _test_bot.py   # bot core: formatting engine, AI action parsing, all methods
python3 _test_web.py   # web panel: all routes render + POST routes work
```

---

## 📁 Project Structure
```
bot_project/
├── ai_group1.py        # Main bot + Flask panel (single file, ~4400 lines)
├── wsgi.py             # WSGI entry for Render/gunicorn (starts bot in background thread)
├── render.yaml         # Render.com Blueprint
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── _test_bot.py        # Bot core smoke test
├── _test_web.py        # Web panel smoke test
└── templates/
    ├── base.html       # Mobile-responsive layout + nav
    ├── login.html      # Admin login
    ├── dashboard.html  # Stats + group lists
    ├── group.html      # Group detail with 8 tabs (Moderation, Members, Filters, Welcome, Promote, Banned KW, Protection, Mention)
    └── settings.html   # Bot config + AI trigger words management
```

---

## 🔧 Tech Stack
- **Python 3.11**
- **pyTelegramBotAPI** (telebot) — Telegram Bot API
- **Flask** — web admin panel
- **Groq** — AI (chat completions, model-chain fallback)
- **SQLite** — database (thread-safe with RLock)
- **gunicorn** — WSGI server for Render

---

## ❓ Troubleshooting

**Bot not starting?** Check the Render logs. The most common cause is an invalid `BOT_TOKEN`. Set it in the web panel Settings page.

**409 Conflict from Telegram?** You have more than one instance polling the same token. Ensure `--workers 1` and that you're not running the bot locally AND on Render with the same token.

**Web panel says "bot not started"?** Save a valid Bot Token in Settings. The bot auto-starts within ~5 seconds.

**Settings lost after redeploy?** You're on the free tier without a persistent disk. Add a disk (Starter plan) with mount path `/var/data` and set `DATA_DIR=/var_data`.

**AI not responding?** Ensure: (1) Groq API key is set, (2) AI chat is enabled in Settings, (3) owner ran `/allow_ai` in the group, (4) you typed a trigger word or replied to a message.

**Permission errors in group?** The bot must be an **admin** with *Delete messages*, *Ban users*, *Restrict members* permissions. Use a **supergroup** for reliable moderation.

---

Made with 🤖 by expanding a Telegram group management bot into a full AI-powered platform.
