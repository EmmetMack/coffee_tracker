# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Activate the virtual environment first (it lives outside the project root):
```bash
source ~/.virtualenvs/coffee-tracker/bin/activate
```

```bash
python manage.py runserver          # start dev server
python manage.py migrate            # apply migrations
python manage.py makemigrations     # generate migration after model changes
python manage.py test               # run all tests
python manage.py test coffee_tracker.tests.SomeTestClass  # run a single test
python manage.py shell              # Django shell
```

## Architecture

**Project layout**: `coffeesite/` is the Django project config (settings, root URLs, wsgi/asgi). `coffee_tracker/` is the single Django app containing all models, views, templates, and URLs.

**Database**: PostgreSQL, configured via pg_service (`my_service`) and `.my_pgpass` in the project root — no direct DB credentials in settings.

**URL routing**: `coffeesite/urls.py` mounts the app at `/` via `include('coffee_tracker.urls')`. The admin is at `/admin/`. App-level routes are in `coffee_tracker/urls.py`.

**Data model** (all in `coffee_tracker/models.py`):
- `Roaster` — a coffee roaster (name, location, website, notes)
- `BeanBag` → `Roaster` (FK) — a specific bag of beans with roast details and tasting notes
- `BrewMethod` — e.g. pour-over, espresso, AeroPress
- `Recipe` → `BrewMethod` (FK) — a reusable brew recipe with dose, grind, temp, instructions
- `Cup` → `BeanBag` + `Recipe` (both nullable FKs) — a logged brew session with actual parameters and a 1–10 rating

**Views**: Class-based `ListView`s only so far (`RoasterListView`, `BeanBagListView`). All remaining models need list, detail, and create views following the same pattern.

**Templates**: Stored at `coffee_tracker/templates/coffee_tracker/<name>.html`. No base template exists yet; each template is standalone HTML.

**Admin**: All five models are registered in `coffee_tracker/admin.py` — this is the current primary way to add data.

## Roadmap context

The project is in Phase 1 (core CRUD). List views for Roaster and BeanBag are done; the remaining models (BrewMethod, Recipe, Cup) need list, detail, and create views. HTMX interactivity and Tailwind styling are planned for Phase 2. A GenAI coffee chat/recommendation feature is planned for Phase 3.
