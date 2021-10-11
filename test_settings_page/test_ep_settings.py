import pytest
from pages.urls import URLs
from pages.authorization_page import AuthPage
from pages.ep_url_add_page import ElSignFixtures
from pages.main_page import MainPage
from pages.settings_pages import SettingsPage, ElSignPage


def setup(driver, root=None):
    link = URLs.AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account(root)

@pytest.mark.el_sign
class TestElSignSettings:
    @pytest.mark.dependency()
    def test_setup(self, driver):
        ep = ElSignFixtures(driver)
        ep.ep_setup()

    @pytest.mark.dependency(depends=["TestElSignSettings::test_setup"])
    def test_sign(self, driver):
        setup(driver)
        MainPage(driver).go_to_settings_pages()
        SettingsPage(driver).go_to_el_sign_settings()

        ep_check_page = ElSignPage(driver)
        ep_check_page.click_to_sign_ep()
        ep_check_page.click_to_send_sign()
        ep_check_page.should_be_sign_correct_message()

    @pytest.mark.dependency(depends=["TestElSignSettings::test_setup"])
    def test_teardown(self, driver):
        ep = ElSignFixtures(driver)
        ep.ep_teardown()
