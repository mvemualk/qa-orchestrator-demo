# qa-orchestrator-demo

UI test suite for google.com (home page + search), written with [Playwright for Python](https://playwright.dev/python/) and pytest.

- `TEST_CASES.md` – 30 test cases (20 automated, 10 manual)
- `tests/` – automated tests (`test_tcNN_*` maps to the IDs in `TEST_CASES.md`)

## Run

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m playwright install --with-deps chromium
pytest -v              # headless
pytest -v --headed     # watch the browser
pytest -m "not search" # home-page tests only
```

## Google bot detection

Google often serves a CAPTCHA ("unusual traffic") page to headless browsers and cloud/CI IPs when a search is submitted.
Tests detect this and are **skipped** (not failed) with a clear reason. To run search tests reliably, point the suite at a regular Chrome you already have open:

```bash
google-chrome --remote-debugging-port=9222 &
CDP_URL=http://localhost:9222 pytest -v
```
