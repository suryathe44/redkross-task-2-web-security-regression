# 5–8 minute demo video plan

Record your own screen and narration after you have run the tests locally. Do not claim results that are not visible in your terminal.

## Suggested timeline (about 6 minutes)

1. **0:00–0:40 — Introduction:** State the task, your name/Intern ID 2418, and that the target is the supplied fictional Flask app running locally.
2. **0:40–1:20 — Objective and scope:** Explain the three categories: input validation, access control, and security headers. Confirm that no public website is being tested.
3. **1:20–2:10 — Project structure:** Show `app/app.py`, `tests/`, `data/local_api_test_cases.csv`, and the README. Explain the app factory and pytest test client.
4. **2:10–3:10 — Input validation:** Run `python -m pytest -v tests/test_input_validation.py`. Explain API-01 through API-05, including why API-04 expands the CSV placeholder into 500 actual characters.
5. **3:10–4:10 — Access control:** Run `python -m pytest -v tests/test_access_control.py`. Explain 401 (not authenticated) versus 403 (authenticated but not allowed), and the synthetic user/admin roles.
6. **4:10–5:00 — Security headers:** Run `python -m pytest -v tests/test_security_headers.py`. Explain the purpose of `nosniff`, frame restrictions, CSP, Referrer-Policy, and no-store.
7. **5:00–5:40 — Results and CI:** Run the full suite, show the actual terminal result, then show the GitHub Actions workflow. Do not invent pass counts.
8. **5:40–6:20 — Limitations and conclusion:** Explain that the login is a test fixture, not production authentication; mention missing CSRF, rate limiting, TLS/deployment configuration, and future improvements.

## Recording checklist
- [ ] Run tests successfully on your own laptop.
- [ ] Save terminal output to `reports/final/pytest.txt`.
- [ ] Capture genuine screenshots in `evidence/final/`.
- [ ] Show the repository URL in the video only after it is public and verified.
- [ ] Keep the video between 5 and 8 minutes.
