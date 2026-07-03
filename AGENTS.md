# AGENTS: How to be productive in this repository

This file gives focused, actionable information for AI coding agents working on tacleapp.

## Checklist (what I'll do first)
- Read `tacleapp/tacleapp.py` and `tacleapp/state.py` to understand the app and global state
- Inspect `tacleapp/components/` for UI composition patterns (raw HTML injection, embeds)
- Use `remote_build.sh` and `requirements.txt` as the primary build/run hints

## Big picture
- This is a Reflex (rx) single-page web app. The central app instance is created in `tacleapp/tacleapp.py` (see `app = rx.App(...)`).
- Pages are assembled from modular components in `tacleapp/components/` and composed in `index()` inside `tacleapp/tacleapp.py`.
- Global UI state and actions live in `tacleapp/state.py` (State class passed as `_state` to `rx.App`).

## Important files & patterns (quick reference)
- `tacleapp/tacleapp.py`: app creation, global styles, head components, `index()` page composition.
- `tacleapp/state.py`: reactive fields and helper methods (`toggle_mobile_menu`, `spotify_playlist_id`, derived URLs).
- `tacleapp/components/*.py`: each component returns rx components (commonly `rx.box`) and often embeds raw HTML using `rx.Html` or `rx.script`.
- `remote_build.sh`: canonical build/export commands used by CI/remote build (`reflex init` and `reflex export --frontend-only`).
- `requirements.txt`: runtime dependencies (notably `reflex` and `httpx`).

## Run / build workflows
- Local development (inferred):
  1. Create a virtualenv and install dependencies: `pip install -r requirements.txt`.
  2. Typical Reflex commands used here (seen in `remote_build.sh`):
     - `reflex init` — initializes build artifacts
     - `reflex export --frontend-only` — exports a static frontend into `.web` / `public`
  3. The repo includes a `.web` build output and a `10tacle_frontend_bundle/` static deployment with `docker-compose` and `nginx.conf`.

## Project-specific conventions and gotchas
- Components frequently inject third-party embed iframes (Spotify, SoundCloud, Mixcloud). Treat these as static HTML embedded via `rx.Html`.
- Contact form: the repo expects SMTP environment variables (see top-level `README.md` for exact names: `CONTACT_SMTP_HOST`, `CONTACT_SMTP_PORT`, `CONTACT_SMTP_USER`, `CONTACT_SMTP_PASSWORD`, `CONTACT_SMTP_USE_TLS`, `CONTACT_FROM_EMAIL`, `CONTACT_TO_EMAIL`).
- Head components: `tacleapp/tacleapp.py` adds head scripts and a JSON-LD script via `rx.script(_structured_data(), type_="application/ld+json")`. This repo has produced the runtime warning: "Warning: rx.script does not support the following properties: ['type_']". If you need to fix it, search for usages of `rx.script(..., type_=...)` and either use the API that accepts plain `type` (or pass attributes differently) — do not change blindly; run tests first.

## Debugging tips
- Built frontend is under `.web/` — inspect `.web/build` and `.web/build/client/index.html` when investigating SSR or export issues.
- Use `remote_build.sh` locally to reproduce CI/export: it runs `pip install -r requirements.txt && reflex init && reflex export --frontend-only` and unpacks `frontend.zip` into `public/`.
- When editing components that inject raw HTML/JS, review the generated `.web/build` output to confirm escaping/attributes are correct.

## Where AI agents should make changes (guidance)
- Small UI changes: edit files in `tacleapp/components/` and run `reflex export --frontend-only` to verify static output in `.web`.
- Cross-cutting changes (styles, global head): edit `tacleapp/tacleapp.py` (head_components, `get_custom_css`) and re-run export.
- Fixing the `rx.script(..., type_="...")` warning: locate occurrences (currently `tacleapp/tacleapp.py`) and prefer the API expected by the installed `reflex` version. Run `remote_build.sh` to validate the fix.

## Quick grep examples
- Show all component files: `ls tacleapp/components`.
- Find `rx.Html` or raw HTML injection: `grep -R "rx.Html" -n tacleapp`.

## Where to look next
- `tacleapp/components/contact.py` — contact form implementation and where SMTP/email flow originates.
- `tacleapp/components/music.py` — examples of multiple third-party embeds and how playlist ids are composed from `State`.

---
References: top-level `README.md`, `remote_build.sh`, `requirements.txt`, `tacleapp/tacleapp.py`, `tacleapp/state.py`, `tacleapp/components/`.

