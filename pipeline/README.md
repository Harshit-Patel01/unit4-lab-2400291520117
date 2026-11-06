# novabank-pipeline

Unit 4 Lab 5 — CI/CD pipeline for the NovaBank demo app (AI316B, KIET 2026-27).

- `app/` — Flask-less Python HTTP server (`main.py`) + unittest suite (`test_main.py`)
- `Dockerfile` — Python 3.12-alpine image, port 8000
- `.github/workflows/ci-cd.yml` — GitHub Actions:
  - `test` — runs on every push and pull request
  - `build-and-push` — runs only on `main` (needs: test), pushes image to GHCR tagged with the commit SHA

Repo: https://github.com/Harshit-Patel01/novabank-pipeline
