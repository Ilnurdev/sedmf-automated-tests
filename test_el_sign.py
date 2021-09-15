import pytest
from pages.urls import URLs
from pages.authorization_page import AuthPage
from pages.ep_url_add_page import ElSignExtensionPage
from pages.main_functions import MainFunc
from pages.all_document_fields_page import AllDocumentFieldPage

import time


def open_link(driver):
    link = "C:\\Program Files (x86)\\Crypto Pro\\CAdES Browser Plug-in\\config.html"
    page = ElSignExtensionPage(driver, link)
    page.open()
    return page

def setup(driver, root=None):
    link = URLs.AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account(root)


@pytest.mark.test
class TestElSignature:

    def test_setup(self, driver):
        page = open_link(driver)
        page.add_url()

    @pytest.mark.parametrize("a", [
        [],[],[],[],[],[],[],[],[],[],[],
    ])
    def test_sign(self, driver, a):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.ENTER_SOGL_LINK, driver.current_url)
        page = AllDocumentFieldPage(driver, link)
        page.open()
        page.fill_in_all_document_required_fields(
                "суперадмин", "администратор", 3)
        link = "C:\\Program Files (x86)\\Crypto Pro\\CAdES Browser Plug-in\\config.html"
        page = ElSignExtensionPage(driver, link)
        page.open()
        page.added_test()
    
    def test_teardown(self, driver):
        page = open_link(driver)
        page.delete_url()

                