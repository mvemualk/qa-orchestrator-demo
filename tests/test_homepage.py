import re

from playwright.sync_api import Page, expect


def test_tc01_homepage_loads_with_title(home: Page):
    expect(home).to_have_title("Google")


def test_tc02_logo_is_visible(home: Page):
    expect(home.get_by_role("img", name="Google").first).to_be_visible()


def test_tc03_search_box_is_visible_and_focusable(home: Page):
    box = home.get_by_role("combobox", name="Search")
    expect(box).to_be_visible()
    box.click()
    expect(box).to_be_focused()


def test_tc04_search_buttons_present(home: Page):
    expect(home.locator("input[name='btnK']").first).to_be_attached()
    expect(home.locator("input[name='btnI']").first).to_be_attached()


def test_tc05_gmail_link_points_to_gmail(home: Page):
    gmail = home.get_by_role("link", name="Gmail")
    expect(gmail).to_be_visible()
    expect(gmail).to_have_attribute("href", re.compile(r"mail\.google\.com"))


def test_tc06_images_link_points_to_image_search(home: Page):
    images = home.get_by_role("link", name=re.compile(r"^(Images|Search for Images)", re.I)).first
    expect(images).to_be_visible()
    expect(images).to_have_attribute("href", re.compile(r"(imghp|tbm=isch|udm=2)"))


def test_tc07_sign_in_link_points_to_accounts(home: Page):
    sign_in = home.get_by_role("link", name="Sign in")
    expect(sign_in).to_be_visible()
    expect(sign_in).to_have_attribute("href", re.compile(r"accounts\.google\.com"))


def test_tc08_footer_privacy_and_terms_links(home: Page):
    expect(home.get_by_role("link", name="Privacy")).to_have_attribute("href", re.compile(r"policies\.google\.com/privacy"))
    expect(home.get_by_role("link", name="Terms")).to_have_attribute("href", re.compile(r"policies\.google\.com/terms"))


def test_tc09_empty_search_stays_on_homepage(home: Page):
    home.get_by_role("combobox", name="Search").press("Enter")
    expect(home).not_to_have_url(re.compile(r"/search"))


def test_tc10_mobile_viewport_shows_search_box(home: Page):
    home.set_viewport_size({"width": 390, "height": 844})
    expect(home.get_by_role("combobox", name="Search")).to_be_visible()
