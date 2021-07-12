from pages.urls import URLs
from pages.authorization_page import AuthPage
from pages.main_page import MainPage, SoglDocumentsBlock


def setup(driver, root=None):
    link = URLs.AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account(root)

class TestAllLinks:
    def test_links_active(self, driver):
        setup(driver)
        page = MainPage(driver)
        page.should_be_correct_fields()


class TestSoglBlock:
    def test_new_document_link(self, driver):
        setup(driver)
        page = SoglDocumentsBlock(driver)
        page.go_to_sogl_block_new_document()
        page.should_be_correct_elements_sogl_new_window()
        page.choose_request_document()
        page.should_be_correct_elements_sogl_request_new_window()
        page.choose_request_regulation_document()
