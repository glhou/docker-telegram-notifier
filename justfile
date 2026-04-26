default:
  just -l

fastapi:
    uv run fastapi dev --port 8000

vite:
  cd frontend && npm run dev


prod:
  just build
  uv run fastapi run

build:
  cd frontend && npm run build

install:
  uv sync
  cd frontend && npm install
