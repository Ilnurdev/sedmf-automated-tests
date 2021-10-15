import pytest
from pages.main_functions import MainFunc
from pages.urls import URLs
from pages.value_for_fields import EnterRequestValues
from pages.authorization_page import AuthPage
from pages.all_document_fields_page import AllDocumentFieldPage
from pages.main_page import SoglDocumentsBlock
from pages.enter_request_document_page import EnterRequestDocumentPage


def setup(driver, root=None):
    link = URLs.AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account(root)


@pytest.mark.enter_request
class TestUIEnterOpenLink:
    def test_open_enter_request_document(self, driver):
        setup(driver)
        page = SoglDocumentsBlock(driver)
        page.go_to_sogl_block_new_document()
        page.should_be_correct_elements_sogl_new_window()
        page.choose_sogl_new_window(5)
        page.should_be_correct_elements_sogl_request_new_window()
        page.choose_request_block_documents(2)

        page = AllDocumentFieldPage(driver)
        page.should_be_required_fields(
            EnterRequestValues.SOGL_ENTER_REQUEST_TITLE)
        page.should_be_correct_url(URLs.ENTER_REQUEST_LINK)


@pytest.mark.enter_request
class TestAddBlockButtons:
    def test_change_info_add_button(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.ENTER_REQUEST_LINK, driver.current_url)
        page = EnterRequestDocumentPage(driver, link)
        page.open()

        types = [((None), (0, 0)), ((1, 0), (1, 0)), ((2, 0), (0, 1)), ((1, 1), (1, 1))]

        for i in range(len(types)):
            num, parent = types[i][1][0], types[i][1][1]

            if i != 0:
                page.enter_request_add_buttons(types[i][0][0], types[i][0][1])

            page.should_be_request_type_field(num, parent)
            page.should_be_information_field(num, parent)
            page.should_be_fio_field(num, parent)
            page.should_be_information_resource_field(num, parent)
            page.should_be_action_type_field(num, parent)
            page.should_be_functional_role_field(num, parent)

        page.delete_block_locator(2)
        page.delete_block_locator(2)

    def test_official_mf_add_button(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.ENTER_REQUEST_LINK, driver.current_url)
        page = EnterRequestDocumentPage(driver, link)
        page.open()

        page.should_be_request_type_fields(
            0, 0, True, EnterRequestValues.OFFICIAL_MF)

        types = [(0, 0), (1, 0), (2, 0)]

        for i in range(len(types)):
            num, parent = types[i][0], types[i][1]

            if i != 0:
                page.enter_request_add_buttons(3)

            page.should_be_request_type_field(num, parent)
            page.should_be_change_type_field(num, parent)
            page.should_be_path_field(num, parent)
            page.should_be_publish_date_field(num, parent)
            page.should_be_responsible_field(num, parent)
            page.should_be_phone_field(num, parent)
            page.should_be_comment_field(num, parent)
            page.should_be_operation_field(num, parent)
            page.should_be_document_field(num, parent)
            page.should_be_application_field(num, parent)
            page.should_be_information_type_field(num, parent)
            page.should_be_info_composition_field(num, parent)

        page.delete_block_locator(1)

    def test_official_mf_rubic_add_button(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.ENTER_REQUEST_LINK, driver.current_url)
        page = EnterRequestDocumentPage(driver, link)
        page.open()

        page.should_be_request_type_fields(
            0, 0, True, EnterRequestValues.OFFICIAL_MF)
        page.should_be_change_type_fields(
            0, 0, True, EnterRequestValues.DOC_CHANGE_RUBIC)

        page.should_be_request_type_field(0, 0)
        page.should_be_change_type_field(0, 0)
        page.should_be_path_field(0, 0)
        page.should_be_responsible_field(0, 0)
        page.should_be_phone_field(0, 0)
        page.should_be_comment_field(0, 0)
        page.should_be_operation_field(0, 0)
        page.should_be_name_field(0, 0)
        page.should_be_application_rubic_field(0, 0, True)

    def test_enter_mf_add_button(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.ENTER_REQUEST_LINK, driver.current_url)
        page = EnterRequestDocumentPage(driver, link)
        page.open()

        page.should_be_request_type_fields(
            0, 0, True, EnterRequestValues.ENTER_MF)

        types = [(0, 0), (1, 0), (2, 0)]

        for i in range(len(types)):
            num, parent = types[i][0], types[i][1]

            if i != 0:
                page.enter_request_add_buttons(3)

            page.should_be_request_type_field(num, parent)
            page.should_be_change_type_field(num, parent)
            page.should_be_path_field(num, parent)
            page.should_be_publish_date_field(num, parent)
            page.should_be_responsible_field(num, parent)
            page.should_be_phone_field(num, parent)
            page.should_be_comment_field(num, parent)
            page.should_be_operation_field(num, parent)
            page.should_be_document_field(num, parent)
            page.should_be_application_field(num, parent)

        page.delete_block_locator(1)

    def test_enter_mf_rubic_add_button(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.ENTER_REQUEST_LINK, driver.current_url)
        page = EnterRequestDocumentPage(driver, link)
        page.open()

        page.should_be_request_type_fields(
            0, 0, True, EnterRequestValues.ENTER_MF)
        page.should_be_change_type_fields(
            0, 0, True, EnterRequestValues.DOC_CHANGE_RUBIC)

        page.should_be_request_type_field(0, 0)
        page.should_be_change_type_field(0, 0)
        page.should_be_path_field(0, 0)
        page.should_be_responsible_field(0, 0)
        page.should_be_phone_field(0, 0)
        page.should_be_comment_field(0, 0)
        page.should_be_operation_field(0, 0)
        page.should_be_name_field(0, 0)
        page.should_be_application_rubic_field(0, 0, True)

    def test_enter_provision_software_hardware_add_button(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.ENTER_REQUEST_LINK, driver.current_url)
        page = EnterRequestDocumentPage(driver, link)
        page.open()

        page.should_be_request_type_fields(
            0, 0, True, EnterRequestValues.PROVISION_SH)

        types = [(0, 0), (1, 0), (2, 0)]

        for i in range(len(types)):
            num, parent = types[i][0], types[i][1]

            if i != 0:
                page.enter_request_add_buttons(4)

            page.should_be_request_type_field(num, parent)
            page.should_be_work_type_field(num, parent)
            page.should_be_remove_from_field(num, parent)
            page.should_be_svt_card_field(num, parent)
            page.should_be_justification_field(num, parent)

        page.delete_block_locator(1)


@pytest.mark.enter_request
class TestEnterRequests:
    @pytest.mark.parametrize("num,with_del", [
        pytest.param(1, False), pytest.param(2, False), pytest.param(3, False),
        pytest.param(4, False), pytest.param(5, False), pytest.param(6, False),
        pytest.param(7, False), pytest.param(8, False), pytest.param(9, False),
        pytest.param(10, False), pytest.param(11, False), pytest.param(12, False),
        pytest.param(13, False), pytest.param(14, False), pytest.param(15, False),
        pytest.param(16, False), pytest.param(17, False), pytest.param(18, False),
        pytest.param(19, False), pytest.param(20, False), pytest.param(21, False),
        pytest.param(22, False)
    ])
    def test_enter_requests(self, driver, num, with_del):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.ENTER_REQUEST_LINK, driver.current_url)
        page = EnterRequestDocumentPage(driver, link)
        page.open()
        page.enter_reqests_fields(num, True, False)
        page.enter_reqests_fields(num, False, False)
        page.enter_reqests_fields(num, True, True)
        page.enter_reqests_fields(num, False, True)
        page.create_and_send_agree_sheet(delete=with_del)
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        EnterRequestDocumentPage(driver, link).open()
        AllDocumentFieldPage(driver).register_doc(
            EnterRequestValues.ENTER_REQUEST_TITLE)
