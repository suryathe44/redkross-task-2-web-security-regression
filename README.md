# Local Web Security Regression Framework — Intern 2418

A defensive, local-only Flask training project that automates repeatable regression checks for input validation, access control, and HTTP security headers. It extends the supplied fictional `secure-service` starter and uses Intern 2418's assigned `local_api_test_cases.csv` for API-01 to API-05.

## Safety and scope
- Tests run in Flask's in-process test client; they do not contact an external host.
- Roles (`user`, `admin`) are synthetic training identities. `/login/<role>` is a test fixture, not production authentication.
- Do not point these tests at public or third-party systems. Obtain written authorization before testing any other target.
- The local default secret and HTTP cookie setting are for localhost training only. Do not deploy this app as-is.

## Requirements
- Python 3.10 or newer
- Dependencies in `requirements.txt` (Flask and pytest)

## Setup on Linux / Lubuntu
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the demo app (optional)
```bash
python -m app.app
```
Open `http://127.0.0.1:5000/health`, then stop with Ctrl+C. The test suite itself does not require starting a separate server.

## Run tests
```bash
python -m pytest -v
```
Run a single category:
```bash
python -m pytest -v tests/test_input_validation.py
python -m pytest -v tests/test_access_control.py
python -m pytest -v tests/test_security_headers.py
```
Save genuine execution output:
```bash
python -m pytest -v | tee reports/final/pytest.txt
```

## Test coverage
- **Input validation:** API-01 health; API-02 valid display name; API-03 wrong type; API-04 actual 500-character value (the supplied CSV contains a human-readable placeholder); API-05 missing optional field; plus whitespace trimming, unexpected fields, and non-object JSON.
- **Access control:** unauthenticated access (401), ordinary user denied admin access (403), admin allowed, and logout invalidates the session.
- **Security headers:** `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, Content-Security-Policy, and `Cache-Control: no-store`.

## CI
GitHub Actions runs pytest on push and pull request with read-only repository permissions. The CI result is only available after the repository is pushed to GitHub and the workflow executes.

## Evidence and report
- `docs/TECHNICAL_REPORT.md` — technical report draft; update it with your actual run results.
- `docs/LEARNING_JOURNAL.md` — six concepts covered.
- `docs/VIDEO_DEMO_SCRIPT.md` — suggested 5–8 minute video outline.
- `evidence/README.md` — instructions for genuine screenshots.
- `reports/baseline/STARTER_REVIEW.md` — static review of supplied starter, not a runtime test log.
- `reports/final/EXECUTION_STATUS.md` — authoring-environment test limitation and local run steps.

## Limitations
The app uses a simplified session-based training login and synthetic role assignment. It does not implement password verification, account storage, CSRF protection, rate limiting, persistent audit logging, TLS termination, or production secret management. The header policy is a training baseline and must be reviewed against actual application requirements. Passing these tests proves only that the implemented assertions pass; it is not a security certification.

## References
- PortSwigger Web Security Academy: https://portswigger.net/web-security
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- OWASP Juice Shop: https://owasp.org/www-project/juice-shop/ (optional resource; not used as this project's target)
- Supplied RedKross starter repository and Intern 2418 `local_api_test_cases.csv`.

## Author
Surya Singh Chauhan · Intern ID 2418 · RedKross Research Foundation · Group A
