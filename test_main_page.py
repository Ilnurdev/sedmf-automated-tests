import pytest
from pages.urls import URLs
from pages.authorization_page import AuthPage
from pages.main_page import MainPage, SoglDocumentsBlock
from pages.value_for_fields import DocumentTitles
from pages.all_document_fields_page import AllDocumentFieldPage


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
    @pytest.mark.parametrize("field_type", [[1, DocumentTitles.OUTGOING_SOGL], [2, DocumentTitles.OUTGOING_ANSWER_SOGL], 
                                            [3, DocumentTitles.ENTER_SOGL], [4, DocumentTitles.ORD_SOGL]])
    def test_request_new_document_links(self, driver, field_type):
        setup(driver)
        page = SoglDocumentsBlock(driver)
        title_check = AllDocumentFieldPage(driver)
        page.go_to_sogl_block_new_document()
        page.should_be_correct_elements_sogl_new_window()
        page.choose_sogl_new_window(field_type[0])
        title_check.should_be_correct_title(field_type[1])
