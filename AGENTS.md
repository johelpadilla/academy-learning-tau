# AGENTS — identity (do not confuse)

## THIS app is Academy Learning Tau

| What | Value |
|------|--------|
| Local folder | `~/grok-safe/systemic-tau-platform` |
| Local URL | http://localhost:8501 |
| Entry point | `app/Home.py` |
| Public brand | **Academy Learning Tau** |
| Public URL | https://academylearningtau.streamlit.app |
| Deploy repo | https://github.com/johelpadilla/academylearningtau |
| Mirror repo | https://github.com/johelpadilla/systemic-tau-platform |

## Rules

1. **The product users deploy is THIS codebase** — Systemic Tau Platform content, branded **Academy Learning Tau**.
2. Never treat `academylearningtau` as “another app to leave alone forever.” That URL/repo is the **production** home of this work.
3. Never deploy a different product (other Streamlit apps, old demos, learningtau test clones) to `academylearningtau.streamlit.app`.
4. Dual remotes: `origin` = systemic-tau-platform, `academy` = academylearningtau. Push both after meaningful changes:  
   `git push origin main && git push academy main`
5. Streamlit Cloud cannot switch source repo in-place: **Delete** the old Cloud app (not GitHub), then Deploy from `johelpadilla/academylearningtau` / `main` / `app/Home.py` with App URL `academylearningtau`.
6. Contact: joel.padilla2@upr.edu

## Deploy link

https://share.streamlit.io/deploy?repository=johelpadilla/academylearningtau&branch=main&mainModule=app/Home.py
