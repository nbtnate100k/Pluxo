# Pluxo

Shop + Telegram admin (Flask). **The site is `index.html`** — served at `/` when you run the backend.

## Deploy (Railway)

1. Connect this repo to Railway and deploy `main`.
2. **Turn off GitHub Pages** for this repo (Settings → Pages → Source: *None*). Otherwise `www.pluxo.net` shows this README instead of the shop.
3. In Railway, add custom domains **`pluxo.net`** and **`www.pluxo.net`** on the **same** web service (Gunicorn / `Procfile`).
4. Set env vars — see **[SETUP.md](./SETUP.md)** and **[RAILWAY.md](./RAILWAY.md)**.

Health: `GET /pluxo-ok`
