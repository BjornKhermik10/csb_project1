# csb_project1

Cyber Security Base 2025/2026, Project 1.

## note app

A small notes app with five intentional security flaws and commented fixes. 

The vulnerabilities follow the OWASP 2021 list.

LINK: [https://github.com/BjornKhermik10/csb_project1](https://github.com/BjornKhermik10/csb_project1)

Install Instructions:

Requirements:

```
I use macOS, linux should work commands might differ
python3
Django
```

Setup:

```
Open a terminal in the project root.
Create a virtual environment: python3 -m venv .venv
Activate it: source .venv/bin/activate

```

Initialize Database and Run The App:

```
Run: python3 manage.py migrate
Start server: python3 manage.py runserver
Open: http://127.0.0.1:8000/
```

Demo login:

```
username: björn
password: password123
```

---
FLAW 1: [https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L39](https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L39) [https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L41](https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L41) [https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L49](https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L49)

Broken access control

The note_detail view loads a note by its id only. It does not check that the current user owns the note before showing or updating it, Because of that, one logged in user can change the note id in the URL and open another user’s note.

The fix is to filter the note by both id and owner, for example by using owner=request.user in the query. That way users can only access their own notes.

FLAW 2: [https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L37](https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L37) [https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L46](https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L46)

CSRF

The note edit view is marked with @csrf_exempt, so the POST request does not require a CSRF token. A different site could send a forged form submission and change the note without the user intending it.

The fix is to remove @csrf_exempt and keep Django’s normal {% csrf_token %} in the form. Then Django will reject forged requests correctly.

FLAW 3: [https://github.com/BjornKhermik10/csb_project1/blob/main/polls/templates/polls/note_detail.html#L15](https://github.com/BjornKhermik10/csb_project1/blob/main/polls/templates/polls/note_detail.html#L15)

Stored XSS

The note preview uses "{{ note.body|safe }}". This tells Django to trust the note body as HTML. If a user stores script code or HTML in the note, it can run in the browser later. Because the content is stored in the database and shown later, this is stored XSS.

The fix is to remove "|safe" so Django escapes the content automatically.

FLAW 4: [https://github.com/BjornKhermik10/csb_project1/blob/main/mysite/settings.py#L30](https://github.com/BjornKhermik10/csb_project1/blob/main/mysite/settings.py#L30)

Security misconfiguration

DEBUG is enabled in the settings file. In production, this can expose stack traces and other internal details and another example of security misconfiguration is hardcoding the SECURITY_KEY in it's source file.

The fix is to set DEBUG = False in production and remove the SECURITY_KEY from the source file.

FLAW 5: [https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L10](https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L10) [https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L13](https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L13) [https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L14](https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L14)

Identification and authentication failures

The login form has no lockout or rate limiting, so an attacker can keep guessing passwords many times.

The fix is to add a failed-attempt counter and block or slow repeated bad logins.
