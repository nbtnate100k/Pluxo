# “The train has not arrived at the station” — fix in Railway

That page usually means **`pluxo.net` (no www) is not attached to your service**, while **`www.pluxo.net` may already work**.

**Check:** open **https://www.pluxo.net/pluxo-ok** — if you see `"pluxo": true`, the app is live; only the **apex** domain needs to be added in Networking.

Request IDs like `SavR8YyBSP-HYrPHH4GxDA` are normal until step 4 below is done.

## Do this exactly (10 minutes)

### 1. Open the right place in Railway

1. Go to [railway.com](https://railway.com) → project **discerning-unity** (or your Pluxo project).
2. Click the **service** that is connected to GitHub repo **`nbtnate100k/Pluxo`** (not the empty project title bar).
3. Tab **Deployments** → latest must be **Success / Active**.  
   - If **Failed** or **Crashed**, open **View logs** and fix (usually missing env is OK for web; look for Python traceback).

### 2. Public URL must work BEFORE custom domain

1. Same service → **Settings** → **Networking**.
2. Turn **Public networking** **ON**.
3. Click **Generate domain** if you do not have `something.up.railway.app`.
4. Open in browser: **`https://YOUR-SERVICE.up.railway.app/pluxo-ok`**  
   - Must show: `{"pluxo": true, ...}`  
   - Must open **`https://YOUR-SERVICE.up.railway.app/`** → Pluxo **login page** (HTML).

**Until this works, ignore `pluxo.net` — custom domain will always show the train.**

### 3. Attach custom domain to THIS service

Still on **that same service** → **Networking** → **Custom domain**:

1. Add **`pluxo.net`**
2. Add **`www.pluxo.net`**

Railway shows a **CNAME target** (e.g. `xxxx.up.railway.app`). Copy it.

### 4. Fix DNS (Cloudflare or registrar)

| Name | Type | Value |
|------|------|--------|
| `@` or `pluxo.net` | CNAME (or A/AAAA if Railway says so) | Target from step 3 |
| `www` | CNAME | **Same target** as apex |

**Remove** any `www` record pointing to **`nbtnate100k.github.io`**.

Cloudflare: if it fails to verify, set records to **DNS only** (grey cloud) until Railway shows the domain active.

### 5. Remove conflicting GitHub Pages

GitHub → **nbtnate100k/Pluxo** → **Settings → Pages** → **Source: None**.

### 6. Verify

```text
https://pluxo.net/pluxo-ok     → JSON with "pluxo": true
https://pluxo.net/             → login page (HTML), NOT the train page
```

Then create account / login → full shop (same as goat3x, Pluxo branding).

## Common mistakes

| Mistake | Result |
|---------|--------|
| Custom domain on **project** but deploy on **different service** | Train / Application not found |
| Domain on Service A, GitHub deploys to Service B | Train |
| Only `pluxo.net` on Railway, `www` still on GitHub | www broken or static-only |
| Deploy **Failed** | Train |
| Public networking **off** | No `*.railway.app` URL works |

## Env (after site loads)

`TELEGRAM_BOT_TOKEN`, `OWNER_TELEGRAM_ID`, `PLUXO_WEBHOOK_SECRET`, volume `/app/data`, `PLUXO_STATE_PATH=/app/data/state.json`.
