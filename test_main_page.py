import pytest
from pages.urls import URLs
from pages.authorization_page import AuthPage
from pages.main_page import MainPage, SoglDocumentsBlock


def setup(driver, root=None):
    link = URLs.AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account(root)


@pytest.mark.main_page_links
class TestAllLinks:
    def test_links_active(self, driver):
        setup(driver)
        page = MainPage(driver)
        page.should_be_correct_fields()


@pytest.mark.main_page_links
class TestSoglBlock:
    @pytest.mark.parametrize("field_type", [2, 3, 4])
    def test_request_new_document_links(self, driver, field_type):
        setup(driver)
        page = SoglDocumentsBlock(driver)
        page.go_to_sogl_block_new_document()
        page.should_be_correct_elements_sogl_new_window()
        page.choose_request_block_documents(1)
        # page.choose_request_document()
        page.should_be_correct_elements_sogl_request_new_window()
        page.choose_request_block_documents(field_type)
        # page.choose_request_regulation_document()
