# csb_project1

Cyber Security Base 2025/2026, Project 1.

## What this is

A small Django notes app with five intentional security flaws and commented fixes. The project is meant for the course report and screenshots, not for production use.

## Run the project

```bash
source .venv/bin/activate
python manage.py migrate
python manage.py runserver
```

If your system needs `python3`, use this instead:

```bash
python3 manage.py migrate
python3 manage.py runserver
```

Open http://127.0.0.1:8000/

## Demo login

- Username: `björn`
- Password: `password123`

## Intentional flaws

1. Broken access control
2. CSRF
3. Stored XSS
4. Security misconfiguration (`DEBUG = True`)
5. Identification and authentication failures

## Report notes

- Each flaw has a commented fix in the code.
- Screenshots should go in the `screenshots` folder.
- The report should link directly to the relevant source lines in GitHub.
