# Pluxo deploy (new instance)

This tree is a **copy of goat3x** with Pluxo branding. It does **not** share `state.json`, stock, or users with goat3x.

## GitHub

Repo: **https://github.com/nbtnate100k/Pluxo**

Push `main`; Railway auto-deploys if connected.

### If the domain shows README text instead of the shop

That means **GitHub Pages** is serving the repo (Jekyll renders `README.md`). Fix:

1. GitHub → **nbtnate100k/Pluxo** → Settings → **Pages** → Source: **None** (disable Pages).
2. Railway → your Pluxo service → **Settings → Networking** → custom domains **`pluxo.net`** and **`www.pluxo.net`**.
3. DNS:
   - **`pluxo.net`** and **`www.pluxo.net`** → Railway (custom domains on the web service), **or**
   - **`www.pluxo.net`** → GitHub Pages (HTML only) and **`api.pluxo.net`** → Railway (API). The site defaults to `https://api.pluxo.net` for login/stock when opened on `www`.

The shop file is **`index.html`** at repo root; Flask serves it at `/` on Railway.

Until Railway is live, login/signup will show a clear API error — `pluxo.net` currently returns Railway “Application not found”.

## Railway

1. Project deploys from **nbtnate100k/Pluxo** (not goat3x).
2. Add a volume mounted at `/app/data`.
3. Variables (minimum):

| Variable | Value |
|----------|--------|
| `TELEGRAM_BOT_TOKEN` | Your **Pluxo** bot token from @BotFather |
| `OWNER_TELEGRAM_ID` | Your numeric Telegram user id |
| `PLUXO_WEBHOOK_SECRET` | Strong secret (must match site if you customize frontend) |
| `PLUXO_STATE_PATH` | `/app/data/state.json` |
| `DISABLE_TELEGRAM_BOT` | unset or `0` on the **one** service that runs the bot |

4. **Single replica**, Gunicorn **1 worker** (see `Procfile`).

Never commit bot tokens to git. Set them only in Railway Variables or a local `.env` (gitignored).

## Bot note

Use **one** Telegram token per deployed instance. Running the same token on goat3x and Pluxo at the same time will conflict.
