import pytest
from pages.main_functions import MainFunc
from pages.urls import URLs
from pages.settings_pages import DirectoryVEDPage
from pages.authorization_page import AuthPage


@pytest.fixture(scope="function", autouse=True)
def setup(driver, root=None):
    link = URLs.AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account(root)
    yield
    link = MainFunc.take_DNSID(URLs.DIRECTORY_VED_LINK, driver.current_url)
    page = DirectoryVEDPage(driver, link)
    page.open()
    page.delete_created_ea_type()


@pytest.mark.regulation
class TestDirectoryVED:
    @pytest.mark.parametrize("field_type,new_window", [
        pytest.param(1, False),
        pytest.param(2, True, marks=pytest.mark.xfail),
    ])
    def test_created_element_show_in_regulation_ea_field(self, driver, field_type, new_window):
        link = MainFunc.take_DNSID(URLs.DIRECTORY_VED_LINK, driver.current_url)
        page = DirectoryVEDPage(driver, link)
        page.open()
        page.should_be_all_correct_fields()
        page.click_to_add_ea_type_button()
        page.fill_ea_type_fields(field_type)
        page.should_be_сreated_ea_type(field_type)

        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = DirectoryVEDPage(driver, link)
        page.open()
        page.ea_type_should_be_in_regulation_document(field_type, new_window)

    @pytest.mark.parametrize("field_type_1,field_type_2,new_window", [
        pytest.param(3, 1, True),
        pytest.param(1, 3, False, marks=pytest.mark.xfail),
    ])
    def test_edit_created_element_show_in_regulation_ea_field(self, driver, field_type_1, field_type_2, new_window):
        link = MainFunc.take_DNSID(URLs.DIRECTORY_VED_LINK, driver.current_url)
        page = DirectoryVEDPage(driver, link)
        page.open()
        page.should_be_all_correct_fields()
        page.click_to_add_ea_type_button()
        page.fill_ea_type_fields(field_type_1)
        page.should_be_сreated_ea_type(field_type_1)

        page.edit_created_ea_button(field_type_1)
        page.fill_ea_type_fields(field_type_2)
        page.should_be_сreated_ea_type(field_type_2)

        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = DirectoryVEDPage(driver, link)
        page.open()
        page.ea_type_should_be_in_regulation_document(field_type_2, new_window)
