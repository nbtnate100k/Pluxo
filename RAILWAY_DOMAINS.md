# “The train has not arrived at the station” / Application not found

That page means **DNS reaches Railway**, but **no running deployment is linked to your custom domain** (`pluxo.net` / `www.pluxo.net`). The code can be fine; Railway just has nothing to route to.

## Fix checklist (do in this order)

### 1. Get the default Railway URL working first

1. [Railway](https://railway.com) → your **Pluxo** project (e.g. **discerning-unity**).
2. Click the **web service** (the one connected to GitHub repo `nbtnate100k/Pluxo`), not the empty project shell.
3. **Settings → Networking → Public networking → Generate domain** (if you do not already have `something.up.railway.app`).
4. Open **`https://YOUR-SERVICE.up.railway.app/pluxo-ok`** in a browser.  
   You **must** see JSON like: `{"pluxo": true, ...}`  
   If this fails, open **Deployments → latest → View logs** and fix the crash (missing env vars usually still start the web app; look for Python tracebacks).

### 2. Attach custom domains to **that same service**

Still on **that service** (not project-level DNS only):

1. **Settings → Networking → Custom domain**
2. Add **`pluxo.net`**
3. Add **`www.pluxo.net`**
4. Copy the **CNAME / target** Railway shows for each.

### 3. Fix DNS (Cloudflare or registrar)

| Host | Should point to |
|------|------------------|
| `pluxo.net` | Railway target from step 2 (often `*.up.railway.app` CNAME) |
| `www.pluxo.net` | **Same Railway target** — **not** `nbtnate100k.github.io` |

**Cloudflare:** After it works, you can proxy (orange cloud). If verification stalls, try **DNS only** (grey cloud) until Railway shows the domain as active.

### 4. Turn off GitHub Pages

GitHub → **nbtnate100k/Pluxo** → **Settings → Pages** → **Source: None**.

Otherwise `www` keeps hitting GitHub instead of your shop.

### 5. Wait and verify

Provisioning can take a few minutes. Then:

```bash
curl -s https://pluxo.net/pluxo-ok
curl -sI https://pluxo.net/ | head -3
```

- `/pluxo-ok` → JSON with `"pluxo": true`
- `/` → **`content-type: text/html`** (the login shop), not JSON `Application not found`

## Env + volume (same service)

| Variable | Notes |
|----------|--------|
| `TELEGRAM_BOT_TOKEN` | Pluxo bot only |
| `OWNER_TELEGRAM_ID` | Your Telegram numeric id |
| `PLUXO_WEBHOOK_SECRET` | e.g. match frontend default or set both |
| `PLUXO_STATE_PATH` | `/app/data/state.json` |
| Volume | Mount **`/app/data`** on this service |

One replica, Gunicorn **1 worker** (`Procfile` / `railway.json`).

## Still stuck?

- Domain added on **project** but not on the **service** → remove domain and re-add under the **service** Networking tab.
- Two services in the project → domain may be on the wrong one; move it to the service that runs `gunicorn pluxo_backend:app`.
- Deploy **Failed** → fix logs first; the train page stays until a deploy is **Active** and linked.

Request IDs like `7ZYjWNCAQRO85O4Z8u2xcg` are from Railway’s edge when no backend is bound — fixing steps 1–2 resolves them.
