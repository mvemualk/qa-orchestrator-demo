import re

import pytest
from playwright.sync_api import Page, expect

pytestmark = pytest.mark.search


def test_tc11_search_via_enter_shows_results(search):
    page: Page = search("playwright testing")
    expect(page).to_have_url(re.compile(r"/search\?.*q=playwright\+testing"))
    expect(page.locator("#search")).to_be_visible()
    expect(page.locator("#search a h3").first).to_be_visible()


def test_tc12_query_is_kept_in_search_box(search):
    page: Page = search("selenium vs playwright")
    expect(page.locator("textarea[name='q'], input[name='q']").first).to_have_value("selenium vs playwright")


def test_tc13_results_page_title_contains_query(search):
    page: Page = search("pytest fixtures")
    expect(page).to_have_title(re.compile(r"pytest fixtures", re.I))


def test_tc14_special_characters_query(search):
    page: Page = search("c++ & c# <tags>")
    expect(page.locator("#search")).to_be_visible()


def test_tc15_long_query_is_handled(search):
    page: Page = search("software testing " * 15)
    expect(page.locator("#center_col")).to_be_visible()
    expect(page).to_have_title(re.compile(r"software testing", re.I))


def test_tc16_nonsense_query_is_handled_gracefully(search):
    page: Page = search("qzxwvjklmnbpqqqzzzxxx0987654321qzxwv")
    expect(page).to_have_title(re.compile(r"qzxwvjklmnbpqqqzzzxxx0987654321qzxwv"))
    expect(page.locator("#center_col")).to_be_visible()


def test_tc17_calculator_answer(search):
    page: Page = search("12*12")
    expect(page.get_by_text("144", exact=True).first).to_be_visible()


def test_tc18_autocomplete_suggestions_appear(home: Page):
    box = home.get_by_role("combobox", name="Search")
    box.press_sequentially("weather in", delay=80)
    expect(home.get_by_role("listbox").first).to_be_visible()
    expect(home.get_by_role("option").first).to_be_visible()


def test_tc19_images_tab_from_results(search):
    page: Page = search("golden retriever")
    page.get_by_role("link", name="Images", exact=True).first.click()
    expect(page).to_have_url(re.compile(r"(tbm=isch|udm=2)"))


def test_tc20_next_page_of_results(search):
    page: Page = search("python unittest")
    next_link = page.locator("#pnnext")
    if not next_link.count():
        pytest.skip("Results use continuous scroll instead of pagination")
    next_link.click()
    expect(page).to_have_url(re.compile(r"start=10"))
