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

`https://systemic-tau-platform-<user>.streamlit.app`

You can rename the subdomain in **App settings → General**.

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
