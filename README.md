# unit4-lab-2400291520117

AI316B — Unit 4: Orchestration & Automation lab submission (KIET 2026-27)
**Name:** Harshit Singh Patel · **Reg No:** 2400291520117

## Contents

| Folder | Lab |
|---|---|
| `swarm/` | Lab 1 — Docker Swarm: stack.yml (deploy block, replicas, rolling update config) |
| `k8s/` | Lab 2 — Kubernetes: deployment.yaml, service.yaml, env-demo.yaml |
| `helm/` | Lab 3 — Helm: `banking-chart/` (lifecycle proven: install → upgrade → rollback → --atomic) + values-prod.yaml |
| `ansible/` | Lab 4 — Configuration management: site.yml, inventory.ini (idempotency + drift repair proven) |
| `pipeline/` | Lab 5 & 6 — NovaBank demo app, Dockerfile, GitHub Actions workflow, values-novabank.yaml |
| `screenshots/` | Numbered evidence (1A–1C, 2A–2D, 3A–3B, 4A–4D, 5A–5C, 6A–6C) |

## Lab 5 repository (CI/CD)

**https://github.com/Harshit-Patel01/novabank-pipeline**

- Actions: 6 runs — green (test + build-and-push), red (deliberate break, build-and-push skipped), PR test-only run, post-merge build
- Packages: GHCR image `ghcr.io/harshit-patel01/novabank-pipeline` tagged with full commit SHAs
- PR #1 (feature/rate-change → main): test-only checks, merged

## Pipeline map (Lab 6.7)

| Stage | Tool | What was done |
|---|---|---|
| Push + review | Git / GitHub | per-lab commits; PR gate (test-only) on feature/rate-change |
| Build + test | GitHub Actions | unittest on every push/PR; build-and-push gated by `needs: test` + `if: main` |
| Package | Docker + GHCR | images tagged with commit SHA (immutable, traceable) |
| Prepare servers | Ansible | nginx + webteam group + deploy user + site page; idempotent (changed=0); drift repaired |
| Deploy | Helm | banking-chart via values files (--set one-off; values-prod / values-novabank per environment) |
| Run + self-heal | Kubernetes | Deployments/ReplicaSets keep desired replicas; killed pod replaced automatically |
| Recover | helm rollback / --atomic | bad tag releases auto-rolled back; manual rollback to revision 1 restored novabank:v1 |
