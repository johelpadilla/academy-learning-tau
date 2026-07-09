# AGENTS — identity (do not confuse)

## THIS app is Academy Learning Tau

| What | Value |
|------|--------|
| Local folder | `~/grok-safe/systemic-tau-platform` ONLY |
| Local URL | http://localhost:8501 |
| Entry point | `app/streamlit_app.py` (Cloud) / `app/Home.py` (local) |
| Public brand | **Academy Learning Tau** |
| Public URL | https://academylearningtau.streamlit.app |
| Deploy repo | https://github.com/johelpadilla/academylearningtau |
| Mirror repo | https://github.com/johelpadilla/systemic-tau-platform |

## NEVER push these (other products)

| Path | Why |
|------|-----|
| `~/grok-safe/systemictau` | Other product (PyPI systemictau studio) |
| `~/grok-safe/Gemini/**` | Old experiments / antigravity-era copies |
| `~/grok-safe/systemic-tau-platform-copy` | Snapshot copy, not source of truth |

## Rules

1. **Source of truth** = this directory only: `systemic-tau-platform`.
2. After every meaningful change:  
   `git push origin main && git push academy main`  
   from **this** folder only.
3. Streamlit Cloud main file: `app/streamlit_app.py`  
   Repo: `johelpadilla/academylearningtau` branch `main`.
4. Contact: joel.padilla2@upr.edu
5. Verify deploy: open the app → expander **Build / deploy identity**.

## Deploy link

https://share.streamlit.io/deploy?repository=johelpadilla/academylearningtau&branch=main&mainModule=app/streamlit_app.py
