# A project with five vulnerabilities that are mentioned in the OWASP 2021 list and “csrf”.

Link to OWASP 2021: https://owasp.org/Top10/2021/
Repository link: https://github.com/BjornKhermik10/csb_project1/tree/main

Installation guide:

Requirements:
- MacOS/Linux
- Python3/Python
- Django

Setup:
- Clone repo: `git clone https://github.com/BjornKhermik10/csb_project1.git`
- Create virtual env: `python3 -m venv .venv`
- Activate virtual env: `source .venv/bin/activate`

Starting app:
- Run: `python3 manage.py migrate`
- Start server: `python3 manage.py runserver`
- Open: `http://127.0.0.1:8000/`

Test user for demo:
- Username: `björn`
- Password: `password123`

---

## FLAW 1: A01:2021 Broken Access Control

Links to the flaw in project:
- https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L39
- https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L41
- https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L49

Access control refers to a flaw in which a user can act outside of their intended permission accessing parts of the application they are not supposed to. Within my application the flaw is present, since a user can force his way into other users' notes by simply modifying the url. My application does not check the user-id when accessing anyone's notes. Once you get to other users' notes you can freely edit them and access information that should be out of your reach. A straightforward implementation to fix this exact version of broken access control would be to request both the notes owner id and the users id upon opening notes pages and checking if they match and only then granting access, otherwise blocking access.

---

## FLAW 2: CSRF vulnerability (Not included in the list)

Links to the flaw in project: 
- https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L37
- https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L46

CSRF stands for Cross-Site Request Forgery. In this case, the @csrf_exempt decorator tells Django to ignore CSRF checks for the specific URL. Because of this exemption, Django's CSRF middleware no longer protects POST requests by requiring a secret token, which allows unauthorized POST requests from attackers. In a scenario of a malicious attack, they could submit a hidden HTML form pointing at your note_detail URL, and an attacker could then edit the logged-in user's notes to something malicious or harmful. This vulnerability is straightforward to fix simply by removing the @csrf_exempt decorator. Doing so allows Django’s built-in automatic middleware to protect the route as intended. This flaw is easier to avoid in modern software development because a lot of frameworks such as Django have their own middleware to protect from this flaw.

---

## FLAW 3: A03:2021 XSS injection

Links to the flaw in project:
- https://github.com/BjornKhermik10/csb_project1/blob/main/polls/templates/polls/note_detail.html#L15

XSS stands for Cross-Site Scripting. XSS occurs when malicious or otherwise untrusted data is rendered without proper escaping. In my app the “|safe” filter is forcing Django to render the note body raw, making it possible for attackers to inject HTML or JavaScript scripts directly in the browser. An example of something an attacker could do in this scenario, they could store malicious script tags in a note making it possible for them to steal session cookies when the note gets viewed. This flaw is straightforward to fix by simply removing the “|safe” filter from the code to allow Django to automatically block malicious code from running. Most modern frameworks also protect from this vulnerability unless overridden.

---

## FLAW 4: A05:2021 Security misconfiguration

Links to the flaw in project:
- https://github.com/BjornKhermik10/csb_project1/blob/main/mysite/settings.py#L30

Security misconfiguration occurs when the security settings of a project are misconfigured. In my case the debug mode is enabled whilst in production (DEBUG=True). This can expose sensitive internal details to malicious attackers. There are actually two misconfigurations as there is also a hardcoded SECRET_KEY directly in the source code. If this SECURITY_KEY would be exposed to attackers, they could forge cryptographic tokens or compromise session security. This flaw is fixed by setting DEBUG to false and moving the SECRET_KEY from the source code to environment variables. This is yet again an example of what could happen if you are sloppy and misconfigure your security settings or forget to change them before deploying to production.

---

## FLAW 5: A07:2021 Identification and authentication failures

Links to the flaw in the project:
- https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L10
- https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L13
- https://github.com/BjornKhermik10/csb_project1/blob/main/polls/views.py#L14

Identification and authentication failures occur when the authentication features are improperly or sloppily implemented. This kind of security vulnerability can be very costly allowing attackers to compromise user credential and sensitive information. In my app this vulnerability is present because of the lack of rate limiting, missing CAPTCHA protection and lack of account lockout controls. This allows for several different types of malicious attack, such as automated brute-force or credential stuffing attacks. They could literally try passwords an unlimited amount of times until they guess it, fully compromising a user's account. This flaw can be fixed by implementing failed attempt counters and rate limiting. This flaw is not as easy to avoid as the previous flaws as it is necessary to know how to implement the necessary security layers. Probably present in a lot of vibecoded apps, to some degree.

