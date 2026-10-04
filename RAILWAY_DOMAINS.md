# pluxo.net / www — Railway “Application not found”

If `https://pluxo.net/` shows JSON like `Application not found`, or the site says **network error**, the **domain is pointed at Railway but no running service is bound to it**.

## Fix (5 minutes)

1. Open [Railway](https://railway.com) → project **discerning-unity** (or your Pluxo project) → **the web service** that runs `gunicorn pluxo_backend:app`.
2. **Deployments** → latest must be **Success / Active** (not crashed). Open logs if it restarts.
3. **Settings → Networking → Public networking** → **Generate domain** if you do not have one yet.  
   Open `https://YOUR-SERVICE.up.railway.app/pluxo-ok` — you must see JSON with `"pluxo": true`.
4. **Custom domain** → add **`pluxo.net`** and **`www.pluxo.net`** on **that same service** (copy the CNAME/target Railway shows).
5. **DNS** (Cloudflare/registrar):
   - **`pluxo.net`** → Railway target (CNAME or A/AAAA as Railway instructs).
   - **`www.pluxo.net`** → **same Railway target** (not `nbtnate100k.github.io`).
6. GitHub → **nbtnate100k/Pluxo** → **Settings → Pages** → **Disable** (Source: None).

Do **not** use `api.pluxo.net` unless you create a DNS record for it. The shop uses **`https://pluxo.net`** for the API when `www` is static.

## Env + volume (same service)

- `TELEGRAM_BOT_TOKEN`, `OWNER_TELEGRAM_ID`, `PLUXO_WEBHOOK_SECRET`
- Volume mount `/app/data`, `PLUXO_STATE_PATH=/app/data/state.json`
- One replica, `--workers 1` (see `Procfile`)

## Verify

```bash
curl -s https://pluxo.net/pluxo-ok
curl -sI https://pluxo.net/ | head -5   # should be text/html from Flask, not application/json 404
```
