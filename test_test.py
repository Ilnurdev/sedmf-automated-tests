import pytest
from pages.main_functions import MainFunc
from pages.urls import URLs
from pages.value_for_fields import RegulationFields
from pages.authorization_page import AuthPage
from pages.all_document_fields_page import AllDocumentFieldPage
from pages.enter_documets_page import EnterDocumentsPage
from pages.regulation_document_page import RegulationDocumentPage, ChangeResponsibleInfo, RegulationRefuseDocument, RegulationChainShowInstrument
from pages.settings_pages import SystemNotificationPage, RegulationControlPage
from pages.main_page import MainPage, SoglDocumentsBlock


def setup(driver, root=None):
    link = URLs.AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account(root)


class TestTest:
    def test_test(self, driver):
        setup(driver)
        page = MainPage(driver, driver.current_url)
        page.should_be_correct_fields()




