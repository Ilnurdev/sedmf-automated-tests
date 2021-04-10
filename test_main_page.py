import pytest
from pages.main_functions import MainFunc
from pages.authorization_page import AuthPage
from pages.all_document_fields_page import AllDocumentFieldPage, PictogramsShow, AgreeSheetPage
from pages.enter_documets_page import EnterDocumentsPage
from pages.regulation_document_page import RegulationDocumentPage
from pages.main_page import EnterDocumentsBlock, SoglDocumentsBlock

import time


AUTH_LINK = MainFunc.config() + "/auth.php"

def setup(driver, root=None):
    link = AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account(root)

class TestSoglBlock:
    def test_new_document_link(self, driver):
        setup(driver)
        page = SoglDocumentsBlock(driver, driver.current_url)
        page.go_to_sogl_block_new_document()
        page.should_be_correct_elements_sogl_new_window()
        page.choose_request_document()
        page.should_be_correct_elements_sogl_request_new_window()
        page.choose_request_regulation_document()

        

