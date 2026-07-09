# Deploy — Academy Learning Tau

## Canonical product

| Piece | Value |
|-------|--------|
| **Public web** | https://academylearningtau.streamlit.app |
| **GitHub repo (brand)** | https://github.com/johelpadilla/academylearningtau |
| **Code twin** | https://github.com/johelpadilla/systemic-tau-platform (same platform) |
| **Main file** | `app/Home.py` |
| **Branch** | `main` |

This Streamlit app **is** Academy Learning Tau. Deploy **this** codebase to that URL.

## One-shot deploy / rebind Cloud app

Streamlit binds **one GitHub repo + entry file** per Cloud app. Settings cannot “switch repo” in place.

### If `academylearningtau.streamlit.app` already exists (old code)

1. [share.streamlit.io](https://share.streamlit.io) → app **academylearningtau**.
2. ⋮ → **Delete app** (only the Cloud deployment — GitHub repos stay).  
   Subdomain becomes free immediately.
3. Immediately create the new deploy (next section) with App URL `academylearningtau`.

### Deploy this platform as Academy

**Direct link:**  
https://share.streamlit.io/deploy?repository=johelpadilla/academylearningtau&branch=main&mainModule=app/Home.py

| Field | Value |
|-------|--------|
| Repository | `johelpadilla/academylearningtau` |
| Branch | `main` |
| Main file path | `app/Home.py` |
| **App URL** | `academylearningtau` |

Click **Deploy**. After build: **https://academylearningtau.streamlit.app**

### Sharing

Settings → Sharing → **Public** if the Academy audience should open without GitHub login.

## Repo files Cloud uses

| File | Role |
|------|------|
| `app/Home.py` | Entry (multipage) |
| `requirements.txt` | pip (no `packages.txt` unless real apt packages, no comments with `/`) |
| `.streamlit/config.toml` | theme, `maxUploadSize=15` |

Pages inject `src/` on `sys.path` so `import stp` works on Cloud.

## Sync both GitHub remotes (maintainers)

Local clones may have:

- `origin` → `systemic-tau-platform`
- `academy` → `academylearningtau`

After commits:

```bash
git push origin main
git push academy main
```

## Local run

```bash
pip install -r requirements.txt
streamlit run app/Home.py
```
