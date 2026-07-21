# CyberSecurity Project 1

Cyber Security Base 2025/2026, Project 1.

## Note's app

A small notes app with five intentional security flaws and commented fixes. 

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
4. Security misconfiguration
5. Identification and authentication failures

