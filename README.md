# railway-hello
A minimal, normal demo web app for verifying a Railway account/deployment flow.
- `GET /` — HTML page
- `GET /health` — {"status":"ok"}
Listens on $PORT (Railway provides it). No dependencies.
Deploy: push these files to a GitHub repo, then in Railway: New Project -> Deploy from GitHub repo -> select repo -> Generate Domain.
Or locally with Railway CLI: `railway login && railway init && railway up`
