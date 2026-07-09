# Deploy guide — Streamlit Community Cloud

## One-click (recommended)

1. Open: [Deploy on Streamlit Community Cloud](https://share.streamlit.io/deploy?repository=johelpadilla/systemic-tau-platform&branch=main&mainModule=app/Home.py)
2. Sign in with **GitHub** (`johelpadilla`).
3. Confirm settings:
   - **Repository:** `johelpadilla/systemic-tau-platform`
   - **Branch:** `main`
   - **Main file path:** `app/Home.py`
   - **Python version:** 3.11 (or 3.12 if offered)
4. Click **Deploy**.

After the first build (2–5 min), the app URL looks like:

`https://learningtau.streamlit.app` (or whatever subdomain you chose)

### Canonical public URL (Academy)

**Target:** [`https://academylearningtau.streamlit.app`](https://academylearningtau.streamlit.app)

That subdomain is almost certainly already bound to **another** Streamlit Cloud app (different GitHub repo / entry file).  
Streamlit **does not** let you “point an existing Cloud app at a new repo” in Settings — the GitHub source is fixed at deploy time. To put **this** repo on that URL:

#### Recommended: free the subdomain, then redeploy this platform

1. Open [share.streamlit.io](https://share.streamlit.io) (GitHub `johelpadilla`).
2. Find the **existing** app whose URL is `academylearningtau.streamlit.app` (whatever repo it uses today).
3. Either:
   - **A — Keep a backup of the old app:** ⋮ → **Settings** → **General** → change its App URL to e.g. `academylearningtau-legacy` → Save.  
   - **B — Drop the old app:** ⋮ → **Delete app** (subdomain is free right away).
4. **New app** (or deploy again):
   - Repo: `johelpadilla/systemic-tau-platform`
   - Branch: `main`
   - Main file: `app/Home.py`
   - **App URL:** `academylearningtau`  
   - Direct link:  
     https://share.streamlit.io/deploy?repository=johelpadilla/systemic-tau-platform&branch=main&mainModule=app/Home.py  
     (set the subdomain field before Deploy).
5. Optional: delete or keep the temporary app `learningtau` (from earlier tests) so you only maintain one Cloud app for this platform.

Result: **https://academylearningtau.streamlit.app** serves Systemic Tau Platform.

#### Alternative: overwrite the *old GitHub repo* that Academy already uses

Only if you intentionally want the Academy Cloud app to keep the same GitHub connection:

1. In the existing Academy app → Manage app → note **which repo + main file** it deploys.
2. Replace that repo’s entrypoint / content with this platform (or change that repo to mirror `systemic-tau-platform`).
3. Reboot the app.

Usually worse than delete + redeploy (history, secrets, wrong stack). Prefer the recommended path.

## Manual from the dashboard

1. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**.
2. Select the repo and branch `main`.
3. **Main file path:** `app/Home.py`
4. Deploy.

## Repo files used by Cloud

| File | Role |
|------|------|
| `app/Home.py` | Entry point (multipage root) |
| `requirements.txt` | pip deps only (no `-e .`) |
| `.streamlit/config.toml` | theme, `maxUploadSize=15`, no usage stats |

**Do not add `packages.txt`** unless you need real Debian packages (one package name per line, **no comments** with `/`). Empty or commented `packages.txt` breaks Cloud’s apt installer (`E: Unsupported file /`).

Pages under `app/pages/` inject `src/` into `sys.path`, so `import stp` works without installing the local wheel.

## Advanced settings (optional)

In Cloud **App settings → Advanced**:

| Setting | Value |
|---------|--------|
| Python version | 3.11 |
| Secrets | none required for the public demo |

Optional env vars:

| Variable | Effect |
|----------|--------|
| `STP_LANG` | Default language (`es`, `en`, `fr`) if the code reads it |

## Local parity with Cloud

```bash
pip install -r requirements.txt
streamlit run app/Home.py --server.port 8501 --server.headless true
```

## Notes for public traffic

- Lab uploads are capped at **15 MB** (`.streamlit/config.toml`).
- Prefer **Fast** mode and few surrogates on Cloud; heavy Full / IAAFT jobs belong on a local machine or Docker.
- Do not commit secrets; this app needs none for the educational demo.

## Docker (alternative)

```bash
docker build -t systemic-tau-platform .
docker run --rm -p 8501:8501 systemic-tau-platform
```

(Only if a `Dockerfile` is present in the branch.)
