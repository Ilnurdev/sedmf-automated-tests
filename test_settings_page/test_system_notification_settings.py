import pytest
from pages.main_functions import MainFunc
from pages.urls import URLs
from pages.settings_pages import SystemNotificationPage, RegulationControlPage
from pages.regulation_document_page import RegulationDocumentPage
from pages.authorization_page import AuthPage
from pages.value_for_fields import RegulationFields, DateValues, SettingsValues


@pytest.fixture(scope="function", autouse=True)
def setup(driver):
    link = URLs.AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account()

    yield
    link = MainFunc.take_DNSID(URLs.SYSTEM_NOTIFY_LINK, driver.current_url)
    page = SystemNotificationPage(driver, link)
    page.open()
    page.delete_notification_email()


@pytest.mark.regulation
@pytest.mark.regulation_notification
class TestRegulationNotification:
    NPA_ID = None

    def enter_in_acc(self, driver, root=None):
        link = URLs.AUTH_LINK
        page = AuthPage(driver, link)
        page.open()
        page.enter_in_account(root)

    @pytest.mark.parametrize("npa_number,regulation_type,field_name,date,message_type", [
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_1, SettingsValues.SystemNotification.REGULATION_DISCUSS_NPA, DateValues.DATE_YESTERDAY, 1),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_7, SettingsValues.SystemNotification.REGULATION_DISCUSS_NPA, DateValues.DATE_YESTERDAY, 2),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_10, SettingsValues.SystemNotification.REGULATION_DISCUSS_NPA, DateValues.DATE_YESTERDAY, 3),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_11, SettingsValues.SystemNotification.REGULATION_DISCUSS_NPA, DateValues.DATE_YESTERDAY, 4),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_22, SettingsValues.SystemNotification.REGULATION_DISCUSS_NPA, DateValues.DATE_YESTERDAY, 5),
        pytest.param(RegulationFields.NPA_83, RegulationFields.REGULATION_TYPE_83_32, SettingsValues.SystemNotification.REGULATION_DISCUSS_NPA, DateValues.DATE_YESTERDAY, 6),

        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_1, SettingsValues.SystemNotification.REGULATION_DEADLINE, DateValues.DATE_TODAY, 7),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_2, SettingsValues.SystemNotification.REGULATION_DEADLINE, DateValues.DATE_TODAY, 8),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_7, SettingsValues.SystemNotification.REGULATION_DEADLINE, DateValues.DATE_TODAY, 9),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_10, SettingsValues.SystemNotification.REGULATION_DEADLINE, DateValues.DATE_TODAY, 10),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_11, SettingsValues.SystemNotification.REGULATION_DEADLINE, DateValues.DATE_TODAY, 11),
        pytest.param(RegulationFields.NPA_83, RegulationFields.REGULATION_TYPE_83_32, SettingsValues.SystemNotification.REGULATION_DEADLINE, DateValues.DATE_TODAY, 12),
    ])
    def test_regulation_notification_document(self, driver, npa_number, regulation_type, field_name, date, message_type):
        link = MainFunc.take_DNSID(URLs.SYSTEM_NOTIFY_LINK, driver.current_url)
        page = SystemNotificationPage(driver, link)
        page.open()
        page.enter_email_notification(field_name)
        page.click_to_save_button()

        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(npa_number, regulation_type, TestRegulationNotification.NPA_ID, False, True)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        self.enter_in_acc(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()

        TestRegulationNotification.NPA_ID = page.create_and_send_answer(page.modify_npa_type(regulation_type, 1), TestRegulationNotification.NPA_ID, True)

        self.enter_in_acc(driver)
        link = MainFunc.take_DNSID(
            URLs.REGULATION_CONTROL_LINK, driver.current_url)
        page = RegulationControlPage(driver, link)
        page.open()
        page.enter_npa_identificator_field(TestRegulationNotification.NPA_ID)
        page.send_message_key_date(date, message_type)

        link = MainFunc.take_DNSID(URLs.SYSTEM_NOTIFY_LINK, driver.current_url)
        page = SystemNotificationPage(driver, link)
        page.open()
        page.write_in_doc(TestRegulationNotification.NPA_ID, field_name, message_type, date)
