import re

import pytest
from playwright.sync_api import Page

CONSENT_BUTTON = re.compile(r"^(Accept all|Reject all|I agree)$", re.I)


@pytest.fixture
def browser_context_args(browser_context_args):
    return {**browser_context_args, "locale": "en-US", "viewport": {"width": 1280, "height": 800}}


def dismiss_consent(page: Page) -> None:
    button = page.get_by_role("button", name=CONSENT_BUTTON)
    if button.count():
        button.first.click()


def skip_if_blocked(page: Page) -> None:
    if "/sorry/" in page.url or page.locator("#captcha-form, iframe[title*='reCAPTCHA']").count():
        pytest.skip("Google served a CAPTCHA / unusual-traffic page to this IP")


@pytest.fixture
def home(page: Page) -> Page:
    page.goto("/?hl=en")
    dismiss_consent(page)
    skip_if_blocked(page)
    return page


@pytest.fixture
def search(home: Page):
    def _search(query: str) -> Page:
        box = home.get_by_role("combobox", name="Search")
        box.fill(query)
        box.press("Enter")
        home.wait_for_load_state("domcontentloaded")
        skip_if_blocked(home)
        return home

    return _search


@pytest.fixture(scope="session")
def browser(launch_browser, playwright):
    """Set CDP_URL (e.g. http://localhost:9222) to run against an already-running Chrome."""
    import os

    cdp_url = os.environ.get("CDP_URL")
    browser = playwright.chromium.connect_over_cdp(cdp_url) if cdp_url else launch_browser()
    yield browser
    if not cdp_url:
        browser.close()
