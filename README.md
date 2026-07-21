# csb_project1
Cyber Security Base 2025/2026 Project 1 - 5 Flaws / 5 Fixes

## Run locally

### macOS / Linux

```bash
source .venv/bin/activate
python manage.py migrate
python manage.py runserver
```

If `python` does not work on your system, use:

```bash
python3 manage.py migrate
python3 manage.py runserver
```

Open http://127.0.0.1:8000/

### Windows

```bash
.venv\Scripts\activate
python manage.py migrate
python manage.py runserver
```

## Demo credentials

- Username: `björn`
- Password: `password123`

## Broken access control demo

After logging in as Björn, open `/notes/3/`. That page belongs to Bob, but the current backend view does not check ownership before loading or updating the note.
