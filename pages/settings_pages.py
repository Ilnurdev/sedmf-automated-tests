from typing import Union
from .main_functions import MainFunc
from .urls import URLs
from .all_document_fields_page import AllDocumentFieldPage
from .regulation_document_page import RegulationDocumentPage
from .locators import DirectoryVEDLocators, SystemNotificationLocators, RegulationControlLocators, SettingsPageLocators, OSMFInformationSettingsLocators, AllDocumentFieldLocators
from .value_for_fields import DateValues, DirectoryVEDValues, RegulationFields, OSMFInformationValues, SettingsValues


EMAIL = MainFunc.config("email")


# Настройки системы
class SettingsPage(MainFunc):
    def should_be_correct_links(self):
        elements = [
            "Cправочник организаций и пользователей",
            "Структура моей организации",
            "Журналы регистраций",
            "Часто назначаемые исполнители",
            "Населенные пункты...",
            "Области РФ...",
            "Тематики",
            "Классификатор",
            "Доверенные лица",
            # "Материально-технические ресурсы",
            # "Программно-технические ресурсы",
            "Администрирование заявок regulation",
            # "Списки IP-адресов с доступом к служебной информации ограниченного распространения",
            "Списки рассылки документов",
            "Предустановленные тексты поручений",
            "Список исполнителей для МО",
            "Номенклатура дел",
            "Причины удаления карточек",
            "Списки отозванных сертификатов",
            "Особый контроль",
            "Настройка системных уведомлений",
            "Причины отказа",
            "Вид информации ОСМФ",
            "Состав информации, размещаемой на ОСМФ",
            "Организации МЭДО",
            "Производственный календарь",
            "Сопоставление организаций со справочником ССТУ",
            "Результаты запросов к КП ССТУ",
            "Распечатать список выбранных документов",
            # "Печать реестра",
            "Групповое создание резолюций",
            "Групповое исполнение",
            "Новые записи в справочнике организаций и пользователей",
            "Выгрузка документов",
            # "Сведения о количестве сеансов пользователей в системе",
            "Контроль взаимодействия с МЭДО",
            # "Журнал действий пользователей",
            "История справочников",
            "Список всех подключенных организаций",
            "Реестры документов из МЭДО",
            'Журнал результатов обработки запросов из системы "Бюджетное планирование"',
            "Отчет по загрузке данных из кадровой задачи",
            'Контроль взаимодействия с системой "Аудит"',
            "Контроль отправки ответов по электронной почте",
            "Проверить ЭП",
            "Изменить пароль",
            # "Мероприятия",
            "Отчеты для мобильного офиса",
            "Назначение пользователей для личных папок МО",
            "Перенос личных папок",
            "Перенаправление неисполненных документов",
            "Блокировка доступа к СЭД",
            "Права доступа для пользователей",
            "Управление новостями",
            "Система мониторинга информации",
            "Собственноручная подпись",
            "Списки исполнителей для мобильного офиса",
            "Инструменты оптимизации справочников организаций и пользователей",
        ]

        for i in elements:
            element = SettingsPageLocators(i).choose_setting()
            assert self.is_element_present(*element)

    def go_to_osmf_information(self):
        self.click_to(
            *AllDocumentFieldLocators.find_text_locator("Вид информации ОСМФ"))
        AllDocumentFieldPage(self.driver).should_be_correct_title(
            'Справочник "Вид информации"')

    def go_to_osmf_place_information(self):
        self.click_to(
            *AllDocumentFieldLocators.find_text_locator("Состав информации, размещаемой на ОСМФ"))
        AllDocumentFieldPage(self.driver).should_be_correct_title(
            'Справочник "Состав информации, размещаемой на ОСМФ"')


# Администрирование заявок regulation
class AdministrationRegulationPage:
    def should_be_administration_regulation_fields(self):
        main_link = [RegulationControlLocators.VERSON_LINK_LOCATOR, RegulationControlLocators.PROCESS_LINK_LOCATOR,
                     RegulationControlLocators.TYPE_LINK_LOCATOR, RegulationControlLocators.REF_EA_TYPE_LINK_LOCATOR, RegulationControlLocators.CONTROL_LINK_LOCATOR]

        for i in main_link:
            assert self.is_element_present(*i)


# Администрирование заявок regulation / Справочник видов экономической деятельности
class DirectoryVEDPage(RegulationDocumentPage, AdministrationRegulationPage):
    def should_be_all_correct_fields(self):
        table_head = "№ Код Наименование Период действия Инструменты\nс по"

        self.should_be_administration_regulation_fields()
        self.should_be_correct_title(
            "Справочник видов экономической деятельности")
        table_text = self.return_text(*DirectoryVEDLocators.TABLE_HEAD_LOCATOR)
        
        assert table_head == table_text
        assert self.is_element_present(
            *DirectoryVEDLocators.ADD_REF_EA_TYPE_LINK_LOCATOR)

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
            1: [DirectoryVEDValues.CODE, DirectoryVEDValues.NAME, DateValues.DATE_YESTERDAY, DateValues.DATE_TOMORROW],
            2: [DirectoryVEDValues.CODE, DirectoryVEDValues.NAME, DateValues.DATE_TOMORROW, DateValues.DATE_TOMORROW_2],
            3: [DirectoryVEDValues.CODE_EDIT, DirectoryVEDValues.NAME_EDIT, "", ""]
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
        created_elements = self.create_ea_fields(
            field_type) + ["редактировать", "удалить"]
        taken_elements = self.return_text(
            *DirectoryVEDLocators.find_created_ea_type(created_elements[0]))

        for i in created_elements:
            if i not in taken_elements:
                assert False

    def edit_created_ea_button(self, field_type):
        fields = self.create_ea_fields(field_type)
        self.click_to(*DirectoryVEDLocators.edit_created_ea_type(fields[0]))

    def ea_type_should_be_in_regulation_document(self, field_type, from_new_window):
        self.select_order_cm(RegulationFields.NPA_851)
        self.select_type_request_cm(RegulationFields.REGULATION_TYPE_851_1)

        func = self.enter_text_ea_type if from_new_window == False else self.enter_new_window_ea_type
        func("* Виды экономической деятельности", self.create_ea_fields(field_type)[1])

    def delete_created_ea_type(self):
        field = None

        for i in range(3):
            field = self.create_ea_fields(i+1)[0]
            if self.is_not_element_present(*DirectoryVEDLocators.delete_created_ea_type(field)) == False:
                break

        self.click_to(*DirectoryVEDLocators.delete_created_ea_type(field))
        self.is_not_element_present(
            *DirectoryVEDLocators.find_created_ea_type(field))


# Администрирование заявок regulation / Контроль
class RegulationControlPage(RegulationDocumentPage, AdministrationRegulationPage):
    def should_be_all_correct_fields(self):
        self.should_be_administration_regulation_fields()

        self.should_be_correct_title("Контроль")

        elements = [RegulationControlLocators.NPA_IDENTIFICATOR_NAME_LOCATOR, RegulationControlLocators.NPA_IDENTIFICATOR_FIELD_LOCATOR,
                    RegulationControlLocators.DOCUMENT_IDENTIFICATOR_NAME_LOCATOR, RegulationControlLocators.DOCUMENT_IDENTIFICATOR_FIELD_LOCATOR, RegulationControlLocators.FIND_BUTTON_LOCATOR]

        for i in elements:
            assert self.is_element_present(*i)

    def enter_npa_identificator_field(self, npa_id):
        self.fill_field(
            *RegulationControlLocators.NPA_IDENTIFICATOR_FIELD_LOCATOR, npa_id)
        self.click_to(*RegulationControlLocators.FIND_BUTTON_LOCATOR)

    def alert_accept(self, element):
        count = 0
        while self.alert_open() == False and count <= 5:
            self.click_to(*element)
        self.driver.switch_to.alert.accept()

        if count == 5:
            assert False

    def send_message_key_date(self, date: str, field_name: str):
        """Изменяет дату, отправляет сообщения"""
        elements = [[RegulationControlLocators.KEY_DATE_1_LOCATOR, RegulationControlLocators.SAVE_CHANGES_1_LOCATOR, RegulationControlLocators.SEND_NOTIFICATION_1_LOCATOR], [
            RegulationControlLocators.KEY_DATE_2_LOCATOR, RegulationControlLocators.SAVE_CHANGES_2_LOCATOR, RegulationControlLocators.SEND_NOTIFICATION_2_LOCATOR]]

        field_type = 0 if field_name == SettingsValues.SystemNotification.REGULATION_DISCUSS_NPA else 1
        self.fill_field(*elements[field_type][0], date)
        self.alert_accept(elements[field_type][1])
        self.alert_accept(elements[field_type][2])


# Настройка системных уведомлений
class SystemNotificationPage(MainFunc):
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
        elemetns = [locator.notification_title_locator(
        ), locator.notification_input_email_locator(), locator.notification_add_button_locator()]

        for i in elemetns:
            assert self.is_element_present(*i)

        return locator

    def enter_email_notification(self, notification_type: str):
        locator = self.should_be_notification_field(notification_type)

        self.fill_field(*locator.notification_input_email_locator(), EMAIL)
        self.click_to(*locator.notification_add_button_locator())
        
        assert self.is_element_present(
            *locator.notification_email_locator(EMAIL))

    def write_in_doc(self, npa_id: Union[int, str], field_name: str, regulation_type: str, date: str):
        """"Создает и/или записывает отправленные уведомления в файл"""
        locator = self.should_be_notification_field(field_name)
        emails = [i.text for i in self.driver.find_elements(
            *locator.notification_all_emails_locator())]

        if field_name == SettingsValues.SystemNotification.REGULATION_DISCUSS_NPA:
            message_text = {
                RegulationFields.REGULATION_TYPE_851_1: f"Тема сообщения: «Закончился срок обсуждения уведомления о подготовке проекта НПА».\nТекст сообщения: {date} закончился срок общественного обсуждения уведомления о подготовке проекта НПА.\nID проекта на сайте regulation.gov.ru: {npa_id}",
                RegulationFields.REGULATION_TYPE_851_7: f"Тема сообщения: «Закончился срок общественного обсуждения проекта НПА».\nТекст сообщения: {date} закончился срок общественного обсуждения проекта НПА.\nID проекта на сайте regulation.gov.ru: {npa_id}",
                RegulationFields.REGULATION_TYPE_1318_10: f"Тема сообщения: «Закончился срок публичного обсуждения проекта НПА и сводного отчета».\nТекст сообщения: {date} закончился срок публичного обсуждения проекта НПА и сводного отчета.\nID проекта правового акта: {npa_id}",
                RegulationFields.REGULATION_TYPE_1318_11: f"Тема сообщения: «Закончился срок публичного обсуждения проекта решения ЕЭК».\nТекст сообщения: {date} закончился срок публичного обсуждения проекта решения ЕЭК.\nID проекта на сайте regulation.gov.ru: {npa_id}",
                RegulationFields.REGULATION_TYPE_96_22: f"Тема сообщения: «Закончился срок проведения антикоррупционной экспертизы по проекту НПА».\nТекст сообщения: {date} закончился срок проведения антикоррупционной экспертизы по проекту НПА.\nID проекта на сайте regulation.gov.ru:  {npa_id}",
                RegulationFields.REGULATION_TYPE_83_32: f"Тема сообщения: «Закончился срок обсуждения НПА и отчета ОФВ».\nТекст сообщения: {date} закончился срок обсуждения НПА и отчета ОФВ.\nID проекта на сайте regulation.gov.ru: {npa_id}",
            }
        else:
            message_text = {
                RegulationFields.REGULATION_TYPE_851_1: f"Тема сообщения: «Не поступила заявка на размещение сводки предложений».\nТекст сообщения: В 21 департамент не поступила заявка на размещение сводки предложений по уведомлению о подготовке проекта НПА. Необходимо направить письмо для разработчика проекта. ID проекта на сайте regulation.gov.ru: {npa_id}",
                RegulationFields.REGULATION_TYPE_1318_2: f"Тема сообщения: «Не поступила заявка на размещение сводки предложений».\nТекст сообщения: В 21 департамент не поступила заявка на размещение сводки предложений по уведомлению о подготовке проекта НПА. Необходимо направить письмо для разработчика проекта. ID проекта на сайте regulation.gov.ru: {npa_id}",
                RegulationFields.REGULATION_TYPE_851_7: f"Тема сообщения: «Не поступила заявка на размещение сводки предложений».\nТекст сообщения: В 21 департамент не поступила заявка на размещение сводки предложений по проекту НПА. Необходимо направить письмо для разработчика проекта. ID проекта на сайте regulation.gov.ru: {npa_id}",
                RegulationFields.REGULATION_TYPE_1318_10: f"Тема сообщения: «Не поступила заявка на размещение сводки предложений».\nТекст сообщения: В 21 департамент не поступила заявка на размещение сводки предложений по проекту НПА и сводному отчета. Необходимо направить письмо для разработчика проекта. ID проекта правового акта: {npa_id}",
                RegulationFields.REGULATION_TYPE_1318_11: f"Тема сообщения: «Не поступила заявка на размещение сводки предложений».\nТекст сообщения: В 21 департамент не поступила заявка на размещение сводки предложений по проекту решения ЕЭК. Необходимо направить письмо для разработчика проекта. ID проекта на сайте regulation.gov.ru: {npa_id}",
                RegulationFields.REGULATION_TYPE_83_32: f"Тема сообщения: «Не поступила заявка на размещение сводки предложений».\nТекст сообщения: В 21 департамент не поступила заявка на размещение сводки предложений по отчету ОФВ. Необходимо направить письмо для разработчика отчета. ID проекта на сайте regulation.gov.ru: {npa_id}",
            }

        text = f"Письмо отправлено на почту: {(', '.join(emails))}\n{message_text[regulation_type]}\n\n"
        file_name = f"{DateValues.DATE_TODAY}-Notification.doc"
        document_path = self.folder_path + "//" + file_name

        with open(document_path, "a", encoding='UTF-8') as f:
            f.write(text)


# Вид информации ОСМФ | Состав информации, размещаемой на ОСМФ
class OSMFInformationSettings(MainFunc):
    def should_be_osmf_information_correct_fields(self, osmf_type):
        AllDocumentFieldPage(self.driver).should_be_correct_title(osmf_type)
        
        assert self.is_element_present(
            *OSMFInformationSettingsLocators.ADD_BUTTON_LOCATOR)
        assert self.is_element_present(
            *OSMFInformationSettingsLocators.BACK_BUTTON_LOCATOR)
        self.create_information_type(OSMFInformationValues.INFORMATION_TYPE)
        
        assert self.is_element_present(
            *OSMFInformationSettingsLocators(OSMFInformationValues.INFORMATION_TYPE).delete_osmf())
        assert self.is_element_present(
            *OSMFInformationSettingsLocators(OSMFInformationValues.INFORMATION_TYPE).edit_osmf())
        self.delete_information_type(OSMFInformationValues.INFORMATION_TYPE)

    def create_information_type(self, text):
        self.click_to(*OSMFInformationSettingsLocators.ADD_BUTTON_LOCATOR)
        
        assert self.is_element_present(
            *OSMFInformationSettingsLocators.ENTER_NEW_OSMF_LOCATOR)
        self.fill_field(
            *OSMFInformationSettingsLocators.ENTER_NEW_OSMF_LOCATOR, text)
        self.click_to(*OSMFInformationSettingsLocators.SAVE_BUTTON_LOCATOR)
        
        assert self.is_element_present(
            *OSMFInformationSettingsLocators(text).osmf_type())

    def edit_information_type(self, text, new_text):
        assert self.is_element_present(
            *OSMFInformationSettingsLocators(text).osmf_type())
        self.click_to(*OSMFInformationSettingsLocators(text).edit_osmf())
        self.fill_field(
            *OSMFInformationSettingsLocators(text).input_edit_osmf(), new_text)
        self.click_to(*OSMFInformationSettingsLocators.SAVE_BUTTON_LOCATOR)
        
        assert self.is_element_present(
            *OSMFInformationSettingsLocators(new_text).osmf_type())

    def delete_information_type(self, text: str):
        element_deleted = False
        osmf_locator = OSMFInformationSettingsLocators(text).osmf_type()
        
        assert self.is_element_present(*osmf_locator)
        self.click_to(*OSMFInformationSettingsLocators(text).delete_osmf())
        
        count = 0
        while element_deleted == False:
            if count == 10:
                assert False

            self.driver.refresh()
            element_deleted = self.is_not_element_present(*osmf_locator)
            count += 1
        assert element_deleted

    def back_osmf_information_button(self):
        self.click_to(*OSMFInformationSettingsLocators.BACK_BUTTON_LOCATOR)
        
        assert URLs.SETTINGS_LINK in self.driver.current_url
