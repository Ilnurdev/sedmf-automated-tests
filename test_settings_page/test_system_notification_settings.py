import pytest
from pages.main_functions import MainFunc
from pages.settings_pages import SystemNotificationPage, RegulationControlPage
from pages.regulation_document_page import RegulationDocumentPage
from pages.authorization_page import AuthPage
from datetime import timedelta, datetime

import time

SERVER = MainFunc.config()
AUTH_LINK = SERVER + "/auth.php"
SYSTEM_NOTIFY_LINK = SERVER + "/public/notify/system/?"
OPENED_DOCUMENT_LINK = SERVER + "/document.card.php?"
REGULATION_LINK = OPENED_DOCUMENT_LINK + "category=6&r_category=4&card_type=2&version_id=2"


@pytest.fixture(scope="function", autouse=True)
def setup(driver):
    link = AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account()

    yield
    link = MainFunc.take_DNSID(SYSTEM_NOTIFY_LINK, driver.current_url)
    page = SystemNotificationPage(driver, link)
    page.open()
    page.delete_notification_email()



class TestSystemNotificationSettings:
    def test_add_email_regulation_discuss_npa_notification(self, driver):
        link = MainFunc.take_DNSID(SYSTEM_NOTIFY_LINK, driver.current_url)
        page = SystemNotificationPage(driver, link)
        page.open()
        page.enter_email_regulation_discuss_npa_notification()
        page.click_to_save_button()


@pytest.mark.regulation
@pytest.mark.regulation_notification
class TestRegulationNotification:
    REGULATION_CONTROL_LINK = SERVER + "/public/regulation/settings/control/?"

    REGULATION_DEADLINE = "Уведомлять об окончании срока исполнения заявок regulation"
    REGULATION_DISCUSS_NPA = "Уведомлять о завершении обсуждения/экспертизы проекта НПА на сайте regulation.gov.ru"

    NPA_851 = "851"
    NPA_1318 = "1318"
    NPA_96 = "96"
    NPA_83 = "83"

    REGULATION_TYPE_851_1 = "1. Заявка на размещение уведомления о подготовке проекта НПА"
    REGULATION_TYPE_1318_2 = "2. Заявка на размещение уведомления о подготовке проекта НПА"
    REGULATION_TYPE_851_7 = "7. Заявка на размещение проекта НПА"
    REGULATION_TYPE_1318_10 = "10. Заявка на размещение проекта НПА (параллельное размещение)"
    REGULATION_TYPE_1318_11 = "11. Заявка на размещение проекта решения ЕЭК"
    REGULATION_TYPE_96_22 = "22. Заявка на размещение проекта НПА для проведения независимой антикоррупционной экспертизы"
    REGULATION_TYPE_83_32 = "32. Заявка на размещение НПА и отчета об оценке фактического воздействия"

    DATE = (datetime.today() - timedelta(days=1)).strftime("%d.%m.%Y")
    CURRENT_DATE = (datetime.today()).strftime("%d.%m.%Y")
    
    def enter_in_acc(self, driver, root=None):
        link = AUTH_LINK
        page = AuthPage(driver, link)
        page.open()
        page.enter_in_account(root)
    
   
    @pytest.mark.parametrize("npa_number,regulation_type,chain_index,first,field_name,date,not_type", [
        pytest.param(NPA_851, REGULATION_TYPE_851_1, 1, True, REGULATION_DISCUSS_NPA, DATE, 1),
        pytest.param(NPA_851, REGULATION_TYPE_851_7, 2, True, REGULATION_DISCUSS_NPA, DATE, 1),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_10, 7, True, REGULATION_DISCUSS_NPA, DATE, 1),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_11, 8, True, REGULATION_DISCUSS_NPA, DATE, 1),
        pytest.param(NPA_96, REGULATION_TYPE_96_22, 13, True, REGULATION_DISCUSS_NPA, DATE, 1),
        pytest.param(NPA_83, REGULATION_TYPE_83_32, 14, True, REGULATION_DISCUSS_NPA, DATE, 1),

        pytest.param(NPA_851, REGULATION_TYPE_851_1, 1, True, REGULATION_DEADLINE, CURRENT_DATE, 2),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_2, 6, True, REGULATION_DEADLINE, CURRENT_DATE, 2),
        pytest.param(NPA_851, REGULATION_TYPE_851_7, 2, True, REGULATION_DEADLINE, CURRENT_DATE, 2),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_10, 7, True, REGULATION_DEADLINE, CURRENT_DATE, 2),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_11, 8, True, REGULATION_DEADLINE, CURRENT_DATE, 2),
        pytest.param(NPA_83, REGULATION_TYPE_83_32, 14, True, REGULATION_DEADLINE, CURRENT_DATE, 2),
    ])
    def test_regulation_notification_documet(self, driver, npa_number, regulation_type, chain_index, first, field_name, date, not_type):
        link = MainFunc.take_DNSID(SYSTEM_NOTIFY_LINK, driver.current_url)
        page = SystemNotificationPage(driver, link)
        page.open()
        page.enter_email_notification(field_name)
        page.click_to_save_button()

        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(npa_number, regulation_type, chain_index, False, first)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        self.enter_in_acc(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        index = page.modify_npa_type(regulation_type, 1)
        page.register_and_send_enter_regulation_document()
        page.send_medo()

        page.create_and_send_answer(index, chain_index, first)

        self.enter_in_acc(driver)
        link = MainFunc.take_DNSID(self.REGULATION_CONTROL_LINK, driver.current_url)
        page = RegulationControlPage(driver, link)
        page.open()
        page.enter_npa_identificator_field(chain_index)
        page.send_message_key_date(date, not_type)

        link = MainFunc.take_DNSID(SYSTEM_NOTIFY_LINK, driver.current_url)
        page = SystemNotificationPage(driver, link)
        page.open()
        page.write_in_doc(chain_index, field_name, not_type, date)


