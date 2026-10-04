# Pluxo

Shop + Telegram admin (Flask). **The site is `index.html`** — served at `/` when you run the backend.

## Deploy (Railway)

1. Connect this repo to Railway and deploy `main`.
2. **Turn off GitHub Pages** (Settings → Pages → *None*). Point **`www.pluxo.net`** at Railway, not GitHub.
3. **“Train has not arrived at the station”?** → **[STATION_FIX.md](./STATION_FIX.md)** (custom domain not linked to the running service).
4. Attach **`pluxo.net`** and **`www.pluxo.net`** to the **running** Railway service — see also **[RAILWAY_DOMAINS.md](./RAILWAY_DOMAINS.md)**.
4. Set env vars — see **[SETUP.md](./SETUP.md)** and **[RAILWAY.md](./RAILWAY.md)**.

Health: `GET /pluxo-ok`
