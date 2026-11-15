# Evidence instructions

Evidence must come from your own local execution. Capture screenshots of:

1. The baseline starter review (`reports/baseline/STARTER_REVIEW.md`) as a static code-review record, not a test run.
2. The actual failing or missing-control behaviour only if you reproduce it against the original starter locally. Do not label static observations as runtime failures.
3. The final full pytest run after installing dependencies.
4. GitHub Actions passing after pushing the repository.

Save screenshots in `evidence/baseline/` and `evidence/final/`. Never fabricate terminal output or screenshots. The original starter has no access-control routes, so those controls are added in the extended local training app to make the category testable.
