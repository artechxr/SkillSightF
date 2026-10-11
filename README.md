# SkillSight — AI Labour Market Intelligence Prototype

SkillSight is a Next.js dashboard with a FastAPI backend. The included labour-market dataset is **demo/simulated data**; do not present it as live NCS or e-Shram data.

## Requirements
- Node.js 20.9+ (recommended Node 22 LTS) and npm
- Python 3.11+ (Render config uses Python 3.12.8)

## Run locally

### 1. Backend (terminal 1)
```bash
cd Backend
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
Health: http://127.0.0.1:8000/health
API docs: http://127.0.0.1:8000/docs

### 2. Frontend (terminal 2, project root)
```bash
npm ci
# Windows PowerShell: Copy-Item .env.example .env.local
# macOS/Linux: cp .env.example .env.local
npm run dev
```
Open http://localhost:3000. `.env.example` sets the local API base URL.

## Checks
```bash
npx tsc --noEmit
npm run lint
npm run build
```
Run these after `npm ci`. Do not deploy until all checks pass in your environment.

## Deployment

### Frontend — Vercel
1. Import this repository/project into Vercel; set the root directory to the folder containing `package.json`.
2. Add `NEXT_PUBLIC_API_URL` with the deployed backend URL including `/api`, for example `https://YOUR-BACKEND.onrender.com/api`.
3. Deploy.

### Backend — Render
1. Create a Web Service from this project.
2. Set root directory to `Backend`.
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Set `CORS_ORIGINS` to the exact deployed frontend origin (e.g. `https://YOUR-FRONTEND.vercel.app`), comma-separated if multiple origins.
6. Confirm `/health` returns `{"status":"ok"}` and then update Vercel's `NEXT_PUBLIC_API_URL` to `https://YOUR-BACKEND.onrender.com/api`.

A Render blueprint is provided in `render.yaml`. Configure the `CORS_ORIGINS` environment variable before relying on cross-origin requests.

## Data and limitations
- The included CSV is prototype/demo data and not a verified live government feed.
- The map only represents records supported by the supplied dataset; missing districts should not be interpreted as zero demand or supply.
- External data connectors, credentials, and production data agreements are not bundled.

## Safety
- Never commit `.env.local`, `.env`, API keys, or credentials.
- `node_modules`, `.next`, Python virtual environments and caches are intentionally excluded from the delivery ZIP. Run `npm ci` and install backend requirements locally.
