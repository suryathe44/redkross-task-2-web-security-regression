# Learning Journal — Intern 2418

This journal records the concepts applied in the local training project. The explanations are learning notes, not a claim of formal certification.

## 1. Input validation
Servers should validate data at the trust boundary: expected JSON shape, field names, data types, and length limits. The profile endpoint rejects non-object JSON, unexpected fields, non-text display names, and values longer than 80 characters. Validation is repeated server-side even if a browser UI also validates input.

## 2. Authentication
Authentication establishes who is making a request. The sample's `/login/<role>` endpoint is deliberately synthetic and sets a test session; it is not a real credential check. A production system needs secure identity verification, protected session handling, and appropriate account lifecycle controls.

## 3. Authorization / access control
Authorization determines what an authenticated identity may do. The project distinguishes a regular `user` from an `admin`: a user may access `/account` but receives 403 from `/admin`; an unauthenticated request receives 401. This demonstrates why hiding a button in the UI is not an access-control mechanism.

## 4. HTTP security headers
Response headers let a server express browser-side security policies. This project checks `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, Content Security Policy, and `Cache-Control`. Header choices must be adapted to the application's functionality and deployment model.

## 5. Regression testing
A regression test repeats a known check after a code change to detect unintended breakage. Pytest runs the same assertions locally and in CI. A passing suite means only that the tested conditions matched their expected results; it is not proof that the application is secure.

## 6. Least privilege in CI
The workflow requests only `contents: read` because it needs to check out and test code, not modify repository contents. Narrow permissions reduce the impact of a compromised workflow step.

## Reflection
The supplied starter already included basic type and length checks, but did not include a role-protected route or security response headers. The extended local training app adds explicit testable examples for those missing task areas. The sample login remains intentionally limited and must not be reused as production authentication.
