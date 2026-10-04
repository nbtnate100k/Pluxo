# Deploy to Railway (Pluxo)

GitHub **`nbtnate100k/Pluxo`** must receive commits before Railway auto-deploys from Git.

## Git push

```bash
git remote set-url origin https://github.com/nbtnate100k/Pluxo.git
git push origin main
```

Railway redeploys when `main` updates (service linked to this repo).

## Required Railway variables

See **[SETUP.md](./SETUP.md)** and **[RAILWAY.md](./RAILWAY.md)**. Minimum:

- `TELEGRAM_BOT_TOKEN` — Pluxo bot only (not goat3x)
- `OWNER_TELEGRAM_ID`
- `PLUXO_WEBHOOK_SECRET`
- `PLUXO_STATE_PATH=/app/data/state.json` with volume on `/app/data`

Single replica, one Gunicorn worker.

## Railway CLI (optional)

1. Token: [Railway → Account → Tokens](https://railway.com/account/tokens)
2. `railway link` in this folder
3. `railway up`
