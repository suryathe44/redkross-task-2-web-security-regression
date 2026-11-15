# Execution status

The project source and tests are prepared. In the assistant authoring environment, `python -m pytest -q` could not start because Flask was not installed. Installing Flask also failed because package-index DNS/network access was unavailable. This is an environment limitation; it is neither a passing nor failing test result.

**Before submission, run these commands on your Lubuntu laptop:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v | tee reports/final/pytest.txt
```

If tests fail, inspect the first failure, fix the code, and rerun the full suite. Only report the actual counts shown by pytest. Add genuine screenshots to `evidence/final/`.
