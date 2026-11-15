# Technical Report — Local Web Security Regression Framework

**Author:** Surya Singh Chauhan  
**Intern ID:** 2418  
**Track:** Group A — Ethical Hacking & Web Application Security  
**Deadline:** 15 November 2026  
**Status:** Implementation prepared; populate execution summary from the latest actual test run before submission.

## 1. Objective
The objective is to automate repeatable, authorised regression checks for input validation, access control, and HTTP security headers against the supplied fictional Flask demo service. The project extends the provided `secure-service` starter and preserves the five assigned API cases from `local_api_test_cases.csv`.

## 2. Scope and methodology
All tests use Flask's in-process test client against an app instance created locally by the test suite. The suite does not send requests to external hosts. The five assigned API cases are loaded from the provided CSV. Additional pytest cases cover field allow-listing, JSON shape, role separation, logout, and response headers. Tests are deterministic and use synthetic roles only.

## 3. Implementation
The application factory in `app/app.py` defines `/health`, `/profile`, synthetic `/login/<role>` and `/logout`, authenticated `/account`, and admin-only `/admin`. Input validation rejects non-object JSON, unexpected fields, non-string display names, and display names longer than 80 characters. The response hook adds baseline security headers. Access-control checks are enforced on the server route, not by UI visibility.

## 4. Test coverage
- Assigned API-01 to API-05: health response, valid input, wrong type, oversized value, and missing optional field.
- Additional input checks: whitespace trimming, unexpected fields, non-object JSON.
- Access control: unauthenticated request, regular-user denial, admin success, logout invalidation.
- Headers: MIME sniffing protection, frame restriction, referrer policy, CSP, and no-store cache directive.

## 5. Findings and remediation
The supplied starter included basic type and length checks for `display_name`, but had no authentication/authorization routes and did not set security headers. The extension adds a synthetic role-based route guard and a response-header policy for training. The exact test outcomes must be taken from the generated pytest log; do not report unexecuted checks as passed. The synthetic login is not suitable for deployment and must be replaced by a proper authentication system before real use.

## 6. Results
**Execution results:** The suite could not be executed in the authoring environment because Flask was not installed and package installation was blocked by unavailable network/DNS. See `reports/final/EXECUTION_STATUS.md`. Record actual passed, failed, or skipped counts only after running the suite locally. A green test suite covers only the assertions implemented and is not a comprehensive security certification.

## 7. Limitations and future work
The app uses a local demo secret and synthetic roles, has no password verification, database, CSRF protection, rate limiting, TLS, or production secret management. Future work could add secure authentication fixtures, CSRF testing, dependency auditing against live advisory data, and deployment-specific header review. Any additional testing must remain in a local lab or have explicit written authorization.

## 8. References
- PortSwigger Web Security Academy — https://portswigger.net/web-security
- OWASP Web Security Testing Guide — https://owasp.org/www-project-web-security-testing-guide/
- OWASP Cheat Sheet Series — https://cheatsheetseries.owasp.org/
- OWASP Juice Shop — https://owasp.org/www-project/juice-shop/ (recommended training resource; not the target used here)
- Supplied RedKross starter: `secure-service` and Intern 2418 `local_api_test_cases.csv`.
