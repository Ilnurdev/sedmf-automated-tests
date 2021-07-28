import pytest
from pages.main_functions import MainFunc
from pages.urls import URLs
from pages.value_for_fields import EnterRequestValues, OSMFInformationValues
from pages.main_page import MainPage
from pages.settings_pages import SettingsPage
from pages.enter_request_document_page import EnterRequestDocumentPage
from pages.settings_pages import OSMFInformationSettings
from pages.authorization_page import AuthPage


@pytest.fixture(scope="function", autouse=True)
def setup(driver, root=None):
    link = URLs.AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account(root)


def create_osmf_info(driver, osmf_type, text):
    link = MainFunc.take_DNSID(osmf_type, driver.current_url)
    page = OSMFInformationSettings(driver, link)
    page.open()
    page.create_information_type(text)


def delete_osmf_info(driver, osmf_type, text):
    link = MainFunc.take_DNSID(osmf_type, driver.current_url)
    page = OSMFInformationSettings(driver, link)
    page.open()
    page.delete_information_type(text)


@pytest.mark.enter_request
class TestOSMFInformation:
    def test_osmf_directory_ui_open(self, driver):
        page = MainPage(driver)
        page.go_to_settings_pages()
        page = SettingsPage(driver)
        page.go_to_osmf_information()

    def test_osmf_place_directory_ui_open(self, driver):
        page = MainPage(driver)
        page.go_to_settings_pages()
        page = SettingsPage(driver)
        page.go_to_osmf_place_information()

    def test_osmf_information_correct_fields(self, driver):
        link = MainFunc.take_DNSID(
            URLs.OSMF_INFORMATION_LINK, driver.current_url)
        page = OSMFInformationSettings(driver, link)
        page.open()
        page.should_be_osmf_information_correct_fields(
            'Справочник "Вид информации"')
        page.back_osmf_information_button()

    def test_osmf_information_place_correct_fields(self, driver):
        link = MainFunc.take_DNSID(
            URLs.OSMF_INFORMATION_PLACE_LINK, driver.current_url)
        page = OSMFInformationSettings(driver, link)
        page.open()
        page.should_be_osmf_information_correct_fields(
            'Справочник "Состав информации, размещаемой на ОСМФ"')
        page.back_osmf_information_button()

    def test_osmf_information_edit(self, driver):
        create_osmf_info(driver, URLs.OSMF_INFORMATION_LINK,
                         OSMFInformationValues.INFORMATION_TYPE)

        page = OSMFInformationSettings(driver)
        page.edit_information_type(
            OSMFInformationValues.INFORMATION_TYPE, OSMFInformationValues.INFORMATION_TYPE_EDIT)
        
        delete_osmf_info(driver, URLs.OSMF_INFORMATION_LINK,
                         OSMFInformationValues.INFORMATION_TYPE_EDIT)

    def test_osmf_information_place_edit(self, driver):
        create_osmf_info(driver, URLs.OSMF_INFORMATION_PLACE_LINK,
                         OSMFInformationValues.INFORMATION_TYPE)

        page = OSMFInformationSettings(driver)
        page.edit_information_type(
            OSMFInformationValues.INFORMATION_TYPE, OSMFInformationValues.INFORMATION_TYPE_EDIT)
        
        delete_osmf_info(driver, URLs.OSMF_INFORMATION_PLACE_LINK,
                         OSMFInformationValues.INFORMATION_TYPE_EDIT)

    def test_created_element_show_in_osmf_field(self, driver):
        create_osmf_info(driver, URLs.OSMF_INFORMATION_LINK,
                         OSMFInformationValues.INFORMATION_TYPE)

        link = MainFunc.take_DNSID(URLs.ENTER_REQUEST_LINK, driver.current_url)
        page = EnterRequestDocumentPage(driver, link)

        page.open()
        page.should_be_request_type_fields(
            0, 0, True, EnterRequestValues.OFFICIAL_MF)
        page.should_be_information_type_fields(
            0, 0, True, OSMFInformationValues.INFORMATION_TYPE)

        delete_osmf_info(driver, URLs.OSMF_INFORMATION_LINK,
                         OSMFInformationValues.INFORMATION_TYPE)

        page.open()
        page.should_be_request_type_fields(
            0, 0, True, EnterRequestValues.OFFICIAL_MF)
        page.should_be_information_type_fields(
            0, 0, True, OSMFInformationValues.INFORMATION_TYPE, True)

    def test_created_element_show_in_osmf_place_field(self, driver):
        create_osmf_info(driver, URLs.OSMF_INFORMATION_PLACE_LINK,
                         OSMFInformationValues.INFORMATION_TYPE)

        link = MainFunc.take_DNSID(URLs.ENTER_REQUEST_LINK, driver.current_url)
        page = EnterRequestDocumentPage(driver, link)

        page.open()
        page.should_be_request_type_fields(
            0, 0, True, EnterRequestValues.OFFICIAL_MF)
        page.should_be_info_composition_fields(
            0, 0, True, OSMFInformationValues.INFORMATION_TYPE)

        delete_osmf_info(driver, URLs.OSMF_INFORMATION_PLACE_LINK,
                         OSMFInformationValues.INFORMATION_TYPE)

        page.open()
        page.should_be_request_type_fields(
            0, 0, True, EnterRequestValues.OFFICIAL_MF)
        page.should_be_info_composition_fields(
            0, 0, True, OSMFInformationValues.INFORMATION_TYPE, True)
