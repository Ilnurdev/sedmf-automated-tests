from .main_functions import MainFunc
from .all_document_fields_page import AllDocumentFieldPage
from .regulation_document_page import RegulationDocumentPage
from .locators import DirectoryVEDLocators, SystemNotificationLocators, RegulationControlLocators
from datetime import timedelta, datetime
import os


EMAIL = MainFunc.config("email")


class AdministrationRegulationPage:
    def should_be_administration_regulation_fields(self):
        main_link = [RegulationControlLocators.VERSON_LINK_LOCATOR, RegulationControlLocators.PROCESS_LINK_LOCATOR, RegulationControlLocators.TYPE_LINK_LOCATOR, RegulationControlLocators.REF_EA_TYPE_LINK_LOCATOR, RegulationControlLocators.CONTROL_LINK_LOCATOR]

        for i in main_link:
            assert self.is_element_present(*i)


class DirectoryVEDPage(RegulationDocumentPage, AdministrationRegulationPage):
    CODE = "CODE-AUTOTEST"
    CODE_EDIT = "CODE-EDIT-AUTOTEST"
    NAME = "ААА-Тестовая экономическая деятельность"
    NAME_EDIT = "ААА-Редактирование экономической деятельности"
    
    START_DATE_CORRECT = (datetime.today() - timedelta(days=1)).strftime("%d.%m.%Y")
    END_DATE_CORRECT = (datetime.today() + timedelta(days=1)).strftime("%d.%m.%Y")
    START_DATE_UNCORRECT = (datetime.today() + timedelta(days=1)).strftime("%d.%m.%Y")
    END_DATE_UNCORRECT = (datetime.today() + timedelta(days=2)).strftime("%d.%m.%Y")



    def should_be_all_correct_fields(self):
        self.should_be_administration_regulation_fields()
        table_head = "№ Код Наименование Период действия Инструменты\nс по"
        self.should_be_correct_title("Справочник видов экономической деятельности")
        table_text = self.return_text(*DirectoryVEDLocators.TABLE_HEAD_LOCATOR)
        assert table_head == table_text
        assert self.is_element_present(*DirectoryVEDLocators.ADD_REF_EA_TYPE_LINK_LOCATOR)

    def click_to_add_ea_type_button(self):
        self.click_to(*DirectoryVEDLocators.ADD_REF_EA_TYPE_LINK_LOCATOR)
    
    def enter_code_field(self, text):
        self.is_element_present(*DirectoryVEDLocators.CODE_NAME_LOCATOR)
        self.fill_field(*DirectoryVEDLocators.CODE_INPUT_LOCATOR, text)
    
    def enter_name_field(self, text):
        self.is_element_present(*DirectoryVEDLocators.NAME_NAME_LOCATOR)
        self.fill_field(*DirectoryVEDLocators.NAME_INPUT_LOCATOR, text)

    def enter_dates_field(self, date_1, date_2):
        self.is_element_present(*DirectoryVEDLocators.NAME_DATE_LOCATOR)
        self.fill_field(*DirectoryVEDLocators.START_DATE_INPUT_LOCATOR, date_1)
        self.fill_field(*DirectoryVEDLocators.END_DATE_INPUT_LOCATOR, date_2)
    
    def create_ea_fields(self, field_type):
        fields = {
            1: [self.CODE, self.NAME, self.START_DATE_CORRECT, self.END_DATE_CORRECT],
            2: [self.CODE, self.NAME, self.START_DATE_UNCORRECT, self.END_DATE_UNCORRECT],
            3: [self.CODE_EDIT, self.NAME_EDIT, "", ""]
        }

        if field_type > len(fields):
            field_type = 1

        return fields[field_type]

    def fill_ea_type_fields(self, field_type):
        fields = self.create_ea_fields(field_type)
        self.enter_code_field(fields[0])
        self.enter_name_field(fields[1])
        self.enter_dates_field(fields[2], fields[3])
        self.click_to(*DirectoryVEDLocators.SAVE_BUTTON_LOCATOR)
    
    def should_be_сreated_ea_type(self, field_type):
        created_elements = self.create_ea_fields(field_type) + ["редактировать", "удалить"]
        taken_elements = self.return_text(*DirectoryVEDLocators.find_created_ea_type(created_elements[0]))

        for i in created_elements:
            if i not in taken_elements:
                assert False
    
    def edit_created_ea_button(self, field_type):
        fields = self.create_ea_fields(field_type)
        self.click_to(*DirectoryVEDLocators.edit_created_ea_type(fields[0]))

    def ea_type_should_be_in_regulation_document(self, field_type, from_new_window):
        self.select_order_cm("851")
        self.select_type_request_cm("1. Заявка на размещение уведомления о подготовке проекта НПА")
        fields = self.create_ea_fields(field_type)

        if from_new_window == False:
            self.enter_text_ea_type("* Виды экономической деятельности", fields[1], False, True)
        else:
            self.enter_new_window_ea_type("* Виды экономической деятельности", fields[1], False, True)

    def delete_created_ea_type(self):
        field = None

        for i in range(3):
            field = self.create_ea_fields(i+1)[0]
            if self.is_not_element_present(*DirectoryVEDLocators.delete_created_ea_type(field)) == False:
                break


        self.click_to(*DirectoryVEDLocators.delete_created_ea_type(field))

        self.is_not_element_present(*DirectoryVEDLocators.find_created_ea_type(field))


class RegulationControlPage(RegulationDocumentPage, AdministrationRegulationPage):
    def should_be_all_correct_fields(self):
        self.should_be_administration_regulation_fields()

        self.should_be_correct_title("Контроль")

        elemets = [RegulationControlLocators.NPA_IDENTIFICATOR_NAME_LOCATOR, RegulationControlLocators.NPA_IDENTIFICATOR_FIELD_LOCATOR, RegulationControlLocators.DOCUMENT_IDENTIFICATOR_NAME_LOCATOR, RegulationControlLocators.DOCUMENT_IDENTIFICATOR_FIELD_LOCATOR, RegulationControlLocators.FIND_BUTTON_LOCATOR]
     
        for i in elemetns:
            assert self.is_element_present(*i)
    
    def enter_npa_identificator_field(self, chain_index):
        self.fill_field(*RegulationControlLocators.NPA_IDENTIFICATOR_FIELD_LOCATOR, self.regulation_npa_id(chain_index))
        self.click_to(*RegulationControlLocators.FIND_BUTTON_LOCATOR)
    
    def alert_accept(self, element):
        count = 0
        while self.alert_open() == False and count <= 5:
            self.click_to(*element)
        self.driver.switch_to.alert.accept()

        if count == 5:
            assert False
    
    def send_message_key_date(self, date, field_type):
        if field_type == 1:
            elements = [RegulationControlLocators.KEY_DATE_1_LOCATOR, RegulationControlLocators.SAVE_CHANGES_1_LOCATOR, RegulationControlLocators.SEND_NOTIFICATION_1_LOCATOR]
        elif field_type == 2:
            elements = [RegulationControlLocators.KEY_DATE_2_LOCATOR, RegulationControlLocators.SAVE_CHANGES_2_LOCATOR, RegulationControlLocators.SEND_NOTIFICATION_2_LOCATOR]

        self.fill_field(*elements[0], date)
        self.alert_accept(elements[1])
        self.alert_accept(elements[2])
        

class SystemNotificationPage(AllDocumentFieldPage):
    CURRENT_DATE = (datetime.today()).strftime("%d.%m.%Y")

    def click_to_save_button(self):
        self.click_to(*SystemNotificationLocators.SAVE_BUTTON_LOCATOR)

    def delete_notification_email(self):
        locator = SystemNotificationLocators.notification_email_locator(EMAIL)

        self.is_element_present(*locator)
        elements_need_to_delete = self.driver.find_elements(*locator)

        for i in range(len(elements_need_to_delete)):
            elements_need_to_delete[i].click()

        self.is_not_element_present(*locator)
        self.click_to_save_button()

    def should_be_notification_field(self, notification_type):
        locator = SystemNotificationLocators(notification_type)
        elemetns = [locator.notification_title_locator(), locator.notification_input_email_locator(), locator.notification_add_button_locator()]
        
        for i in elemetns:
            assert self.is_element_present(*i)

        return locator
    
    def enter_email_notification(self, notification_type):
        locator = self.should_be_notification_field(notification_type)
        email = MainFunc.config("email")

        self.fill_field(*locator.notification_input_email_locator(), email)
        self.click_to(*locator.notification_add_button_locator())
        assert self.is_element_present(*locator.notification_email_locator(email))
    
    def write_in_doc(self, chain_index, notification_type, message_type, date):
        locator = self.should_be_notification_field(notification_type)
        emails = [i.text for i in self.driver.find_elements(*locator.notification_all_emails_locator())]

        regulation = RegulationDocumentPage(self.driver, "")
        regulation_index = regulation.regulation_npa_id(chain_index)

        if message_type == 1:
            message_text = {
                1: f"Тема сообщения: «Закончился срок обсуждения уведомления о подготовке проекта НПА».\nТекст сообщения: {date} закончился срок общественного обсуждения уведомления о подготовке проекта НПА.\nID проекта на сайте regulation.gov.ru: {regulation_index}",
                2: f"Тема сообщения: «Закончился срок общественного обсуждения проекта НПА».\nТекст сообщения: {date} закончился срок общественного обсуждения проекта НПА.\nID проекта на сайте regulation.gov.ru: {regulation_index}",
                7: f"Тема сообщения: «Закончился срок публичного обсуждения проекта НПА и сводного отчета».\nТекст сообщения: {date} закончился срок публичного обсуждения проекта НПА и сводного отчета.\nID проекта правового акта: {regulation_index}",
                8: f"Тема сообщения: «Закончился срок публичного обсуждения проекта решения ЕЭК».\nТекст сообщения: {date} закончился срок публичного обсуждения проекта решения ЕЭК.\nID проекта на сайте regulation.gov.ru: {regulation_index}",
                13: f"Тема сообщения: «Закончился срок проведения антикоррупционной экспертизы по проекту НПА».\nТекст сообщения: {date} закончился срок проведения антикоррупционной экспертизы по проекту НПА.\nID проекта на сайте regulation.gov.ru:  {regulation_index}",
                14: f"Тема сообщения: «Закончился срок обсуждения НПА и отчета ОФВ».\nТекст сообщения: {date} закончился срок обсуждения НПА и отчета ОФВ.\nID проекта на сайте regulation.gov.ru: {regulation_index}",
            }
        elif message_type == 2:
            message_text = {
                1: f"Тема сообщения: «Не поступила заявка на размещение сводки предложений».\nТекст сообщения: В 21 департамент не поступила заявка на размещение сводки предложений по уведомлению о подготовке проекта НПА. Необходимо направить письмо для разработчика проекта. ID проекта на сайте regulation.gov.ru: {regulation_index}",
                6: f"Тема сообщения: «Не поступила заявка на размещение сводки предложений».\nТекст сообщения: В 21 департамент не поступила заявка на размещение сводки предложений по уведомлению о подготовке проекта НПА. Необходимо направить письмо для разработчика проекта. ID проекта на сайте regulation.gov.ru: {regulation_index}",
                2: f"Тема сообщения: «Не поступила заявка на размещение сводки предложений».\nТекст сообщения: В 21 департамент не поступила заявка на размещение сводки предложений по проекту НПА. Необходимо направить письмо для разработчика проекта. ID проекта на сайте regulation.gov.ru: {regulation_index}",
                7: f"Тема сообщения: «Не поступила заявка на размещение сводки предложений».\nТекст сообщения: В 21 департамент не поступила заявка на размещение сводки предложений по проекту НПА и сводному отчета. Необходимо направить письмо для разработчика проекта. ID проекта правового акта: {regulation_index}",
                8: f"Тема сообщения: «Не поступила заявка на размещение сводки предложений».\nТекст сообщения: В 21 департамент не поступила заявка на размещение сводки предложений по проекту решения ЕЭК. Необходимо направить письмо для разработчика проекта. ID проекта на сайте regulation.gov.ru: {regulation_index}",
                14: f"Тема сообщения: «Не поступила заявка на размещение сводки предложений».\nТекст сообщения: В 21 департамент не поступила заявка на размещение сводки предложений по отчету ОФВ. Необходимо направить письмо для разработчика отчета. ID проекта на сайте regulation.gov.ru: {regulation_index}",
            }
        
        text = f"Письмо отправлено на почту: {(', '.join(emails))}\n{message_text[chain_index]}\n\n"
        file_name = f"{SystemNotificationPage.CURRENT_DATE}-Notification.doc"

        PATH = os.path.join(os.path.dirname(os.path.abspath(
            __file__)), "files", file_name)
        with open(PATH, "a", encoding='utf8') as f:
            f.write(text)




