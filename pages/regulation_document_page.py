from .all_document_fields_page import AllDocumentFieldPage
from .enter_documets_page import EnterDocumentsPage
from .main_page import SoglDocumentsBlock
from .main_functions import MainFunc
from .locators import AllDocumentFieldLocators, RegulationDocumentLocators, RegulationEATypeWindow, ChooseOrganisationFromNewWindow, ChooseUserFromNewWindow, AgreeSheetLocators, RegulationAnswerPageLocators, ChangeResponsibleInfoLocators
from selenium import webdriver
from datetime import timedelta, datetime
from random import randint
import json
import re
import os

import time

# Заголовки страниц
SOGL_TITLE = "Согласование внутреннего документа-заявки Regulation"
ENTER_TITLE = "Внутренний документ-заявка Regulation"
SOGL_ANSWER_TITLE = "Согласование внутреннего документа-ответа на заявку Regulation"
ENTER_ANSWER_TITLE = "Внутренний документ-ответ на заявку Regulation"

# Ответ
ANSWER_START_1 = "Дата начала обсуждения уведомления"
ANSWER_END_1 = "Дата окончания обсуждения уведомления"
ANSWER_START_2 = "Дата начала обсуждения проекта НПА"
ANSWER_END_2 = "Дата окончания обсуждения проекта НПА"
ANSWER_START_3 = "Дата окончания экспертизы"
ANSWER_END_3 = "Дата начала экспертизы"
ANSWER_START_4 = "Дата начала обсуждения отчета"
ANSWER_END_4 = "Дата окончания обсуждения отчета"

# Краткое содержание
SHORT_CONTENT_TEXT = "Заявка на размещение информации на официальном сайте regulation.gov.ru"
SHORT_CONTENT_ANSWER_TEXT = "Ответ на заявку на размещение информации на официальном сайте regulation.gov.ru"

# Поля Regulation
ORDER_FIELD = "* № постановления"
REQUEST_TYPE = "* Тип заявки"
NPA_TYPE = "* Вид НПА"
NPA_NAME_1 = "* Наименование проекта НПА"
NPA_NAME_2 = "* Наименование НПА"
ORG_INFO = "* Сведения об органах и организациях"
ORG_INFO_NAME = "* Сведения об органах и организациях, Наименование"
ORG_INFO_EMAIL = "* Сведения об органах и организациях, E-mail"
EA_TYPE = "* Виды экономической деятельности"
KEYWORD = "* Ключевые слова"
DISCUSS_PERIOD = "* Срок обсуждения"
RESPONSIBLE_REVIEW_1 = "* Ответственный за рассмотрение предложений"
RESPONSIBLE_REVIEW_2 = "* Ответственный за направление информации"
RESPONSIBLE_REVIEW_3 = "* Ответственный за направление НПА"
NOTIFY_NPA = "* Уведомление о подготовке проекта НПА"
PROJECT_NPA_ID = "* ID проекта НПА"
TOTAL_COMMENT = "* Общее кол-во замечаний"
NUMBER_COMMENT = "* Кол-во учтенных замечаний"
NUMBER_UNA_COMMENT = "* Кол-во неучтенных замечаний"
NUMBER_PTA_COMMENT = "* Кол-во частично учтенных замечаний"
DECISION_INFO = "* Информация о принятом решении"
DECISION_INFO_2 = "* Принятое решение по проекту НПА"
SUMMARY_INFO = "* Сводка предложений"
SHORT_CONTENT = "* Краткое содержание"
NPA_PROJECT = "* Проект НПА"
EXPLAIN_NOTE = "* Пояснительная записка"
MODIFIED_NPA = "* Доработанный проект НПА"
AC_EXPERTISE = "* Прием заключений антикоррупционной экспертизы"
EMAIL_AC_EXPERTISE = "* E-mail для заключений антикоррупционной экспертизы"
MAIL_AC_EXPERTISE = "* Почта для заключений антикоррупционной экспертизы"
CORRUPTION_FACTOR = "* Коррупциогенные факторы"
NUMBER_CONCLUSION = "* Кол-во заключений"
GC_AC = "* Общее заключение по итогам антикоррупционной экспертизы"
NPA_DRAFT = "* Нормативный правовой акт (проект)"
NPA_NUMBER = "* Номер принятого НПА"
APPROVED_NPA = "* Утвержденный НПА"
NPA_ADOPTION_DATE_1 = "* Дата принятия НПА"
NPA_ADOPTION_DATE_2 = "* Дата НПА"
PD_NPA = "* Обоснование отказа от общественного обсуждения проекта НПА"
CONSOL_REPORT = "* Сводный отчет"
DECISION_PERIOD = "* Срок принятия предложений"
DEGREE_EXPOSURE = "* Степень воздействия"
MSR = "* Доработанный сводный отчет"
EEC = "* Проект решения ЕЭК"
MDD = "* Доработанный проект решения ЕЭК"
ASSESSMENT_REPORT = "* Отчет об оценке фактического воздействия НПА"
RR_NPA = "* Доработанный отчет об оценке фактического воздействия НПА"
OFFERS_EMAIL = "* Е-mail для предложений"
REGULATORY_GILLIOTINE = "Регуляторная гильотина"
NOTICE_NPA_NOT_PLACED = "Уведомление о подготовке НПА не размещается"
CO_EXECTOR = "Органы гос. власти – соисполнители"
ADD_OFFER_EMAIL = "Доп. e-mail для предложений"
REASON_CREATE_NPA = "Основание для разработки НПА"
LINK_ID = "ID связанных НПА"
ADDITIONAL_MATERIAL = "Дополнительные материалы"
STATE_NUMBER = "Номер государственной регистрации НПА"
ISSUE_TYPE = "Тип затрагиваемых вопросов"


# Заполнение/Заполненные поля Regulation
FILL_FIELD = "Автотест - ЗАПОЛНЕНИЕ поля: "

FILL_NPA_TYPE = "Иное"
FILL_NPA_NAME_1 = FILL_FIELD + NPA_NAME_1
FILL_NPA_NAME_2 = FILL_FIELD + NPA_NAME_2
FILL_ORG_INFO_NAME = FILL_FIELD + ORG_INFO_NAME
FILL_ORG_INFO_EMAIL = FILL_FIELD + ORG_INFO_EMAIL
FILL_EA_TYPE = "Внешнеэкономическая деятельность"
FILL_KEYWORD = FILL_FIELD + KEYWORD
FILL_DISCUSS_PERIOD = "20"
FILL_RESPONSIBLE_REVIEW_NAME = "администратор"
FILL_RESPONSIBLE_REVIEW_PHONE = "88005553535"
FILL_RESPONSIBLE_REVIEW_EMAIL = "in9334459@gmail.com"
FILL_NOTIFY_NPA = FILL_FIELD + NOTIFY_NPA
FILL_EMAIL = "autotest@autotest.autotest"
FILL_NUMBER_COMMENT = 2
FILL_NUMBER_UNA_COMMENT = 3
FILL_NUMBER_PTA_COMMENT = 4
FILL_TOTAL_COMMENT = FILL_NUMBER_COMMENT + FILL_NUMBER_UNA_COMMENT + FILL_NUMBER_PTA_COMMENT
FILL_DECISION_INFO = "Отказ от разработки проекта нормативного правового акта"
FILL_DECISION_INFO_2 = "Отказ от разработки (принятия) проекта нормативного правового акта"
FILL_SUMMARY_INFO = FILL_FIELD + SUMMARY_INFO
FILL_NPA_PROJECT = FILL_FIELD + NPA_PROJECT
FILL_EXPLAIN_NOTE = FILL_FIELD + EXPLAIN_NOTE
FILL_MODIFIED_NPA = FILL_FIELD + MODIFIED_NPA
FILL_AC_EXPERTISE = "20"
FILL_EMAIL_AC_EXPERTISE = "autotestemailacex@autotestemailacex.autotestemailacex"
FILL_MAIL_AC_EXPERTISE = FILL_FIELD + MAIL_AC_EXPERTISE
FILL_CORRUPTION_FACTOR = "Выявлены"
FILL_NUMBER_CONCLUSION = "5"
FILL_GC_AC = FILL_FIELD + GC_AC
FILL_NPA_DRAFT = FILL_FIELD + NPA_DRAFT
FILL_NPA_NUMBER = FILL_FIELD + NPA_NUMBER
FILL_APPROVED_NPA = FILL_FIELD + APPROVED_NPA
FILL_NOTICE_NPA_NAME = "администратор"
FILL_PD_NPA = FILL_FIELD + PD_NPA
FILL_CONSOL_REPORT = FILL_FIELD + CONSOL_REPORT
FILL_DECISION_PERIOD = "6"
FILL_DEGREE_EXPOSURE = "Высокая"
FILL_MSR = FILL_FIELD + MSR
FILL_EEC = FILL_FIELD + EEC
FILL_MDD = FILL_FIELD + MDD
FILL_ASSESSMENT_REPORT = FILL_FIELD + ASSESSMENT_REPORT
FILL_RR_NPA = FILL_FIELD + RR_NPA

NO_FIELD = "Нет"
NON_REQUIRED_FIELD = "-"

# Поля после редактирования
EDIT_FIELD = "Автотест - РЕДАКТИРОВАНИЕ поля: "

FILL_NPA_TYPE_EDIT = "Постановление Правительства Российской Федерации"
FILL_NPA_NAME_1_EDIT = EDIT_FIELD + NPA_NAME_1
FILL_NPA_NAME_2_EDIT = EDIT_FIELD + NPA_NAME_2
FILL_ORG_INFO_NAME_EDIT = EDIT_FIELD + ORG_INFO_NAME
FILL_ORG_INFO_EMAIL_EDIT = EDIT_FIELD + ORG_INFO_EMAIL
FILL_EA_TYPE_EDIT = "Налоговое администрирование"
FILL_KEYWORD_EDIT = EDIT_FIELD + KEYWORD
FILL_DISCUSS_PERIOD_EDIT = "30"
FILL_RESPONSIBLE_REVIEW_NAME_EDIT = "пользователь"
FILL_RESPONSIBLE_REVIEW_PHONE_EDIT = "89600540342"
FILL_RESPONSIBLE_REVIEW_EMAIL_EDIT = "resprev@resprev.resprev"
FILL_NOTIFY_NPA_EDIT = EDIT_FIELD + NOTIFY_NPA
FILL_CO_EXECTOR_EDIT = "Testovaya organizaciya"
FILL_EMAIL_EDIT = "autotestred@autotestred.autotestred"
FILL_REASON_CREATE_NPA_EDIT = EDIT_FIELD + REASON_CREATE_NPA
FILL_LINK_ID_EDIT = EDIT_FIELD + LINK_ID
FILL_ADDITIONAL_MATERIAL_EDIT = EDIT_FIELD + ADDITIONAL_MATERIAL
FILL_NUMBER_COMMENT_EDIT = 6
FILL_NUMBER_UNA_COMMENT_EDIT = 7
FILL_NUMBER_PTA_COMMENT_EDIT = 8
FILL_TOTAL_COMMENT_EDIT = FILL_NUMBER_COMMENT_EDIT + FILL_NUMBER_UNA_COMMENT_EDIT + FILL_NUMBER_PTA_COMMENT_EDIT
FILL_DECISION_INFO_EDIT = "Разработка проекта нормативного правового акта"
FILL_DECISION_INFO_2_EDIT = "Проект нормативного правового акта направлен в Правительство Российской Федерации"
FILL_DECISION_INFO_3_EDIT = "Направление проекта нормативного правового акта и сводного отчета на согласование, оценку"
FILL_SUMMARY_INFO_EDIT = EDIT_FIELD + SUMMARY_INFO
FILL_NPA_PROJECT_EDIT = EDIT_FIELD + NPA_PROJECT
FILL_EXPLAIN_NOTE_EDIT = EDIT_FIELD + EXPLAIN_NOTE
FILL_REGULATORY_GILLIOTINE_EDIT = "Да"
FILL_MODIFIED_NPA_EDIT = EDIT_FIELD + MODIFIED_NPA
FILL_AC_EXPERTISE_EDIT = "35"
FILL_EMAIL_AC_EXPERTISE_EDIT = "autotestemailacexred@autotestemailacexred.autotestemailacexred"
FILL_MAIL_AC_EXPERTISE_EDIT = EDIT_FIELD + MAIL_AC_EXPERTISE
FILL_CORRUPTION_FACTOR_EDIT = "Не выявлены"
FILL_NUMBER_CONCLUSION_EDIT = "9"
FILL_GC_AC_EDIT = EDIT_FIELD + GC_AC
FILL_NPA_DRAFT_EDIT = EDIT_FIELD + NPA_DRAFT
FILL_NPA_NUMBER_EDIT = EDIT_FIELD + NPA_NUMBER
FILL_STATE_NUMBER_EDIT = EDIT_FIELD + STATE_NUMBER
FILL_APPROVED_NPA_EDIT = EDIT_FIELD + APPROVED_NPA
FILL_NOTICE_NPA_NAME_EDIT = "суперадмин"
FILL_PD_NPA_EDIT = EDIT_FIELD + PD_NPA
FILL_CONSOL_REPORT_EDIT = EDIT_FIELD + CONSOL_REPORT
FILL_DECISION_PERIOD_EDIT = "25"
FILL_DEGREE_EXPOSURE_EDIT = "Средняя"
FILL_ISSUE_TYPE_EDIT = "Контрольно-надзорная деятельность"
FILL_MSR_EDIT = EDIT_FIELD + MSR
FILL_EEC_EDIT = EDIT_FIELD + EEC
FILL_MDD_EDIT = EDIT_FIELD + MDD
FILL_ASSESSMENT_REPORT_EDIT = EDIT_FIELD + ASSESSMENT_REPORT
FILL_RR_NPA_EDIT = EDIT_FIELD + RR_NPA

# Дата
DATE = datetime.today().strftime("%d.%m.%Y")
DATE_EDIT = (datetime.today() - timedelta(days=1)).strftime("%d.%m.%Y")

# 35 тип
REQUEST_TYPE_35 = "Тип заявки"
NPA_NAME_35 = "* Наименование проекта НПА (отчета ОФВ)"
PROJECT_NPA_ID_35 = PROJECT_NPA_ID
ACTUAL_RR_35 = "* Текущий ответственный сотрудник"
NEW_RR_35 = "* Новый ответственный сотрудник"
FILL_NPA_NAME_3 = FILL_FIELD + NPA_NAME_35
EDIT_NPA_NAME_3 = EDIT_FIELD + NPA_NAME_35


class RegulationDocumentPage(AllDocumentFieldPage, SoglDocumentsBlock, EnterDocumentsPage):

    def should_be_correct_field_name(self, correct_name, *locator):
        text = self.return_text(*locator[0])
        return text == correct_name + ":"

    """

    * № постановления

    """

    def should_be_order_field(self):
        assert self.is_element_present(
            *RegulationDocumentLocators.SELECT_ORDER_NAME_LOCATOR), f"Не отображается или не является обязательным поле '{ORDER_FIELD}'"

    def should_be_order_fields(self):
        self.should_be_order_field()
        assert self.is_element_present(
            *RegulationDocumentLocators.SELECT_ORDER_FIELD_CM_LOCATOR), f"Не отображается селектор поля '{ORDER_FIELD}'"

    def should_not_be_order_enter_fields(self, npa_order):
        self.should_be_order_field()
        assert self.is_not_element_present(
            *RegulationDocumentLocators.SELECT_ORDER_FIELD_CM_LOCATOR)
        assert npa_order == self.return_text(
            *RegulationDocumentLocators.ORDER_FIELD_VIEW_MODE_LOCATOR)

    def select_order_cm(self, value):
        self.work_with_selector(
            *RegulationDocumentLocators.SELECT_ORDER_FIELD_CM_LOCATOR, visible_text=str(value))

    """

    * Тип заявки

    """

    def should_be_request_type_field(self):
        assert self.is_element_present(
            *RegulationDocumentLocators.SELECT_REQUEST_TYPE_NAME_LOCATOR), f"Не отображается или не является обязательным поле '{REQUEST_TYPE}'"

    def should_be_request_type_fields(self):
        self.should_be_request_type_field()
        assert self.is_element_present(
            *RegulationDocumentLocators.SELECT_REQUEST_TYPE_FIELD_LOCATOR), f"Не отображается селектор поля '{REQUEST_TYPE}'"

    def should_not_be_request_type_enter_fields(self, request_type):
        self.should_be_request_type_field()
        assert self.is_not_element_present(
            *RegulationDocumentLocators.SELECT_REQUEST_TYPE_FIELD_LOCATOR)
        assert request_type == self.return_text(
            *RegulationDocumentLocators.REQUEST_TYPE_FIELD_VIEW_MODE_LOCATOR)

    def select_type_request_cm(self, value):
        self.work_with_selector(
            *RegulationDocumentLocators.SELECT_REQUEST_TYPE_FIELD_LOCATOR, visible_text=str(value))

    """

    * Вид НПА

    """

    def should_be_npa_type_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.SELECT_NPA_TYPE_NAME_LOCATOR)

    def should_be_npa_type_fields(self, name, text):
        self.should_be_npa_type_field(name)
        assert text == self.return_text(
            *RegulationDocumentLocators.NPA_TYPE_FIELD_VIEW_MODE_LOCATOR)

    def select_npa_type_field(self, name, text, edit):
        self.should_be_npa_type_field(name)
        assert self.is_element_present(
                *RegulationDocumentLocators.SELECT_NPA_TYPE_FIELD_LOCATOR), f"Не отображается селектор поля '{name}'"
        self.work_with_selector(
            *RegulationDocumentLocators.SELECT_NPA_TYPE_FIELD_LOCATOR, visible_text=str(text))

    """

    * Наименование проекта НПА & Наименование НПА

    """

    def should_be_npa_name_field(self, name):
        if name == NPA_NAME_1:
            locator = [RegulationDocumentLocators.NPA_NAME_1_FIELD_LOCATOR, RegulationDocumentLocators.NPA_NAME_1_FIELD_VIEW_MODE_LOCATOR]
        elif name == NPA_NAME_2:
            locator = [RegulationDocumentLocators.NPA_NAME_2_FIELD_LOCATOR, RegulationDocumentLocators.NPA_NAME_2_FIELD_VIEW_MODE_LOCATOR]
        assert self.should_be_correct_field_name(name, locator[0])

        return locator
    
    def should_be_npa_name_fields(self, field_name, text):
        field = self.should_be_npa_name_field(field_name)
        assert text == self.return_text(*field[1])

    def enter_npa_name_field(self, field_name, text, edit):
        self.should_be_npa_name_field(field_name)

        self.fill_field(*RegulationDocumentLocators.NPA_NAME_FIELD_LOCATOR, text)


    """

    * Сведения об органах и организациях

    """

    def should_be_org_info_field(self, name, edit):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.ORG_INFO_NAME_LOCATOR)
        if edit == False:
            return [FILL_ORG_INFO_NAME, FILL_ORG_INFO_EMAIL]
        elif edit == True:
            return [FILL_ORG_INFO_NAME_EDIT, FILL_ORG_INFO_EMAIL_EDIT]

    def should_be_org_info_fields(self, field_name, edit):
        field = self.should_be_org_info_field(field_name, edit)
        text = self.return_text(
            *RegulationDocumentLocators.ORG_INFO_FIELD_VIEW_MODE_LOCATOR)
        assert field[0] in text
        assert field[1] in text

    def count_org_info_elments(self):
        count = self.count_all_elements(
            *RegulationDocumentLocators.FOR_COUNT_ELEMENTS_IN_ORG_INFO_FIELD_LOCATOR)
        if count == 1:
            assert self.is_not_element_present(
                *RegulationDocumentLocators.LAST_REMOVE_BUTTON_IN_ORG_INFO_LOCATOR)
        else:
            assert self.is_element_present(
                *RegulationDocumentLocators.LAST_REMOVE_BUTTON_IN_ORG_INFO_LOCATOR), f"Нет кнопки удаления в '{ORG_INFO}'"
        return count

    def click_to_add_button_org_info(self):
        count_org_info_opened = self.count_org_info_elments()
        add_button = self.driver.find_element(
            *RegulationDocumentLocators.ADD_NEW_ELEMENT_IN_ORG_INFO_LOCATOR)
        add_button.click()
        count_org_info = self.count_org_info_elments()
        assert count_org_info == count_org_info_opened + \
            1, f"Не добавился новый элемент в поле '{ORG_INFO}'"

    def click_to_delete_button_org_info(self):
        count_org_info_opened = self.count_org_info_elments()
        delete_button = self.driver.find_element(
            *RegulationDocumentLocators.LAST_REMOVE_BUTTON_IN_ORG_INFO_LOCATOR)
        delete_button.click()
        count_org_info = self.count_org_info_elments()
        assert count_org_info == count_org_info_opened - \
            1, f"Не удалился элемент в поле '{ORG_INFO}'"

    def enter_org_info_name_field(self, text):
        self.fill_field(
            *RegulationDocumentLocators.ORG_INFO_NAME_FIELD_LOCATOR, text)

    def enter_org_info_email_field(self, text):
        self.fill_field(
            *RegulationDocumentLocators.ORG_INFO_EMAIL_FIELD_LOCATOR, text)
    
    def enter_org_info_field(self, field_name, edit, requered):
        field = self.should_be_org_info_field(field_name, edit)
        assert self.is_element_present(
            *RegulationDocumentLocators.ORG_INFO_NAME_FIELD_LOCATOR), f"Нет поля 'Наименование' в '{ORG_INFO}'"
        assert self.is_element_present(
            *RegulationDocumentLocators.ORG_INFO_EMAIL_FIELD_LOCATOR), f"Нет поля 'E-mail' в '{ORG_INFO}'"
        assert self.is_element_present(
            *RegulationDocumentLocators.CHOOSE_ORG_FROM_NEW_WINDOW), f"Нет кнопки 'Выбрать' в '{ORG_INFO}'"
        assert self.is_element_present(
            *RegulationDocumentLocators.ADD_NEW_ELEMENT_IN_ORG_INFO_LOCATOR), f"Нет кнопки 'Добавить' в '{ORG_INFO}'"
        
        self.fill_field(
            *RegulationDocumentLocators.ORG_INFO_NAME_FIELD_LOCATOR, field[0])
        self.fill_field(
            *RegulationDocumentLocators.ORG_INFO_EMAIL_FIELD_LOCATOR, field[1])

    """

    * Виды экономической деятельности

    """

    def should_be_ea_type_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.EA_TYPE_NAME_LOCATOR)

    def should_be_ea_type_fields(self, name, text):
        self.should_be_ea_type_field(name)

        assert text in self.return_text(
            *RegulationDocumentLocators.EA_TYPE_FIELD_VIEW_MODE_LOCATOR)

    def enter_text_ea_type(self, name, text, edit, ved=False):
        self.should_be_ea_type_field(name)
        self.fill_field(
            *RegulationDocumentLocators.ENTER_NEW_ELEMENT_IN_EA_TYPE_LOCATOR, text)
        self.click_to(*RegulationDocumentLocators.CHOOSE_EA_TYPE_DROP_LIST, 10 if ved == True else 30)

    def enter_new_window_ea_type(self, name, text, edit, ved=False):
        self.should_be_ea_type_field(name)

        assert self.is_element_present(
            *RegulationDocumentLocators.ENTER_NEW_ELEMENT_IN_EA_TYPE_LOCATOR), f"Не отображается поле '{EA_TYPE}'"
        assert self.is_element_present(
            *RegulationDocumentLocators.CHOOSE_EA_TYPE_FROM_NEW_WINDOW), f"Нет кнопки 'Выбрать' в '{EA_TYPE}'"

        self.click_to(*RegulationDocumentLocators.CHOOSE_EA_TYPE_FROM_NEW_WINDOW)
        self.work_with_windows(1)
        self.fill_field(*RegulationEATypeWindow.FILTER_LICATOR, text)
        self.click_to(*RegulationEATypeWindow.find_element_in_ea_window(text), 10 if ved == True else 30)
        self.click_to(*RegulationEATypeWindow.ADD_BUTTON_LOCATOR)
        self.work_with_windows()

    def delete_ea_type_last_field(self):
        self.click_to(*RegulationDocumentLocators.LAST_REMOVE_BUTTON_IN_EA_TYPE_LOCATOR)

    """

    * Ключевые слова

    """

    def should_be_keyword_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.KEYWORD_NAME_LOCATOR)

    def should_be_keyword_fields(self, field_name, text):
        self.should_be_keyword_field(field_name)
        assert text in self.return_text(
            *RegulationDocumentLocators.KEYWORD_FIELD_VIEW_MODE_LOCATOR)

    def enter_keyword_field(self, field_name, text, edit):
        self.should_be_keyword_field(field_name)
        assert self.is_element_present(
                *RegulationDocumentLocators.KEYWORD_INPUT_FILELD_LOCATOR), f"Не отображается поле '{KEYWORD}'"
        self.fill_field(
            *RegulationDocumentLocators.KEYWORD_INPUT_FILELD_LOCATOR, text)

    """

    * Срок обсуждения

    """

    def should_be_discuss_period_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.DISCUSS_PERIOD_NAME_LOCATOR)

    def should_be_discuss_period_fields(self, field_name, text):
        self.should_be_discuss_period_field(field_name)

        assert text in self.return_text(
            *RegulationDocumentLocators.DISCUSS_PERIOD_FIELD_VIEW_MODE_LOCATOR)

    def enter_discuss_period_field(self, field_name, text, edit):
        self.should_be_discuss_period_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.DISCUSS_PERIOD_FIELD_LOCATOR, text)

    """

    * Ответственный за рассмотрение предложений & * Ответственный за направление информации & * Ответственный за направление НПА

    """

    def should_be_resp_review_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.RESPONSIBLE_REVIEW_NAME_LOCATOR)

    def should_be_resp_review_fields(self, name, phone, email, field_name):
        self.should_be_resp_review_field(field_name)
        text = self.return_text(*RegulationDocumentLocators.RESPONSIBLE_REVIEW_FIELD_VIEW_LOCATOR)
        assert name in text
        assert phone in text
        assert email in text

    def click_to_responsible_review_delete_button(self):
        self.click_to(*RegulationDocumentLocators.RESPONSIBLE_REVIEW_DELETE_BUTTON_LOCATOR)
        if self.is_active(*RegulationDocumentLocators.RESPONSIBLE_REVIEW_DELETE_BUTTON_LOCATOR, timeout=0) == True:
            self.click_to(*RegulationDocumentLocators.RESPONSIBLE_REVIEW_DELETE_BUTTON_LOCATOR)

    def enter_responsible_review_from_new_window(self, text, r_type=RESPONSIBLE_REVIEW_1):
        assert self.is_element_present(
            *RegulationDocumentLocators.RESPONSIBLE_REVIEW_FIO_FIELD_LOCATOR), f"Не отображается 'ФИО' '{r_type}'"
        assert self.is_element_present(
            *RegulationDocumentLocators.RESPONSIBLE_REVIEW_PHONE_FIELD_LOCATOR), f"Не отображается 'Телефон' '{r_type}'"
        assert self.is_element_present(
            *RegulationDocumentLocators.RESPONSIBLE_REVIEW_EMAIL_FIELD_LOCATOR), f"Не отображается 'E-mail' '{r_type}'"
        assert self.is_element_present(
            *RegulationDocumentLocators.CHOOSE_RESPONSIBLE_REVIEW_FROM_NEW_WINDOW), f"Не отображается ссылка выбора автора из нового окна '{r_type}'"

        self.click_to(*RegulationDocumentLocators.CHOOSE_RESPONSIBLE_REVIEW_FROM_NEW_WINDOW)
        self.work_with_windows(1)
        self.fill_field(*ChooseUserFromNewWindow.USER_FIND_LOCATOR, text)
        self.click_to(*AllDocumentFieldLocators.find_text_locator(text))
        self.work_with_windows()

    def enter_responsible_review_phone_field(self, text):
        self.fill_field(
            *RegulationDocumentLocators.RESPONSIBLE_REVIEW_PHONE_FIELD_LOCATOR, text)

    def enter_responsible_review_email_field(self, text):
        self.fill_field(
            *RegulationDocumentLocators.RESPONSIBLE_REVIEW_EMAIL_FIELD_LOCATOR, text)

    def enter_responsilble_review(self, text):
        self.fill_field(
            *RegulationDocumentLocators.RESPONSIBLE_REVIEW_FIO_FIELD_LOCATOR, text)
        self.choose_user_from_drop_list()

    def enter_resp_review_field(self, name, phone, email, field_name):
        self.should_be_resp_review_field(field_name)
        self.enter_responsible_review_from_new_window(name)
        self.enter_responsible_review_phone_field(phone)
        self.enter_responsible_review_email_field(email)

    """

    * Уведомление о подготовке проекта НПА

    """

    def should_be_notify_npa_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.NOTIFY_NPA_NAME_LOCATOR)

    def should_be_notify_npa_fields(self, field_name, text):
        self.should_be_notify_npa_field(field_name)

        field_text = self.return_text(*RegulationDocumentLocators.NOTIFY_NPA_FIELD_VIEW_MODE_LOCATOR)
        assert text == field_text

    def enter_notify_npa_field(self, field_name, text, edit):
        self.should_be_notify_npa_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.NOTIFY_NPA_FIELD_LOCATOR), f"Не отображается поле '{NOTIFY_NPA}'"
        assert self.is_element_present(
            *RegulationDocumentLocators.NOTIFY_NPA_CHOOSE_FILE_LOCATOR), f"Не отображается кнопка добавления файла в '{NOTIFY_NPA}'"

        self.fill_field(
            *RegulationDocumentLocators.NOTIFY_NPA_CHOOSE_FILE_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.NOTIFY_NPA_FIELD_LOCATOR, text)

    """

    * Проект НПА

    """

    def should_be_npa_project_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.NPA_PROJECT_NAME_LOCATOR)

    def should_be_npa_project_fields(self, field_name, text):
        self.should_be_npa_project_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.NPA_PROJECT_FIELD_VIEW_MODE_LOCATOR)

    def enter_npa_project_field(self, field_name, text, edit):
        self.should_be_npa_project_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.NPA_PROJECT_FIELD_LOCATOR)
        assert self.is_element_present(
            *RegulationDocumentLocators.NPA_PROJECT_ADD_FILE_BUTTON_LOCATOR)

        self.fill_field(
            *RegulationDocumentLocators.NPA_PROJECT_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.NPA_PROJECT_FIELD_LOCATOR, text)

    """

    * Пояснительная записка

    """

    def should_be_explain_note_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.EXPLAIN_NOTE_NAME_LOCATOR)

    def should_be_explain_note_fields(self, field_name, text):
        self.should_be_explain_note_field(field_name)
        assert text == self.return_text(
            *RegulationDocumentLocators.EXPLAIN_NOTE_FIELD_VIEW_MODE_LOCATOR)

    def enter_explain_note_field(self, field_name, text, edit):
        self.should_be_explain_note_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.EXPLAIN_NOTE_FIELD_LOCATOR)
        assert self.is_element_present(
            *RegulationDocumentLocators.EXPLAIN_NOTE_ADD_FILE_BUTTON_LOCATOR)
        
        self.fill_field(
            *RegulationDocumentLocators.EXPLAIN_NOTE_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.EXPLAIN_NOTE_FIELD_LOCATOR, text)

    """

    * ID проекта НПА

    """

    def should_be_project_npa_id_field(self, type):
        if type == 1:
            assert self.is_element_present(
                *RegulationDocumentLocators.ID_NPA_PROJECT_NAME_LOCATOR)
        elif type == 2:
            assert self.is_element_present(
                *RegulationDocumentLocators.ID_NPA_PROJECT_NAME_LOCATOR_2)
    
    def should_be_closed_project_npa_id_field(self, type, first, index):
        if type == 1:
            id_field = self.return_text(*RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_VIEW_MODE_LOCATOR)
        elif type == 2:
            id_field = self.return_text(*RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_VIEW_MODE_LOCATOR_2)

        if first == True:
            assert NON_REQUIRED_FIELD == id_field
        else:
            assert self.regulation_npa_id(index) in id_field

    def should_be_project_npa_id_fields(self, type, first, edit_mode, index):
        self.should_be_project_npa_id_field(type)

        if edit_mode == True:
            if first == True:
                assert self.is_element_present(*RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_LOCATOR)
            elif first == False:
                element = self.driver.find_element(*RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_LOCATOR)
                assert element.get_attribute("type") == "hidden"
                self.should_be_closed_project_npa_id_field(type, first, index)
        else:
            assert self.is_not_element_present(*RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_LOCATOR), f"Поле '{PROJECT_NPA_ID}' доступно для редактирования"
            self.should_be_closed_project_npa_id_field(type, first, index)

    def enter_project_npa_id_field(self, type, first, index):
        self.should_be_project_npa_id_field(type)
        assert self.is_element_present(*RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_LOCATOR)

        if first == False:
            self.fill_field(*RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_LOCATOR, self.regulation_npa_id(index))

    def regulation_correct_npa_id_fields(self, index, npa_index, first, mode):
        mods = {
            1: [True],
            2: [False, True],
            3: [False, False],
        }

        if index not in [1, 2, 3, 32]:
            id_type = 2 if index in [33, 34] else 1
            if (mods[mode][0] == True):
                self.enter_project_npa_id_field(id_type, first, npa_index)
            else:
                self.should_be_project_npa_id_fields(id_type, first, mods[mode][1], npa_index)

    """

    * Общее кол-во замечаний

    """

    def count_comment_fields(self, name, fill):
        if name == TOTAL_COMMENT:
            tc = [(RegulationDocumentLocators.TOTAL_COMMENT_FIELD_VIEW_MODE_LOCATOR, RegulationDocumentLocators.TOTAL_COMMENT_FIELD_2_VIEW_MODE_LOCATOR),
                  (RegulationDocumentLocators.TOTAL_COMMENT_FIELD_LOCATOR, RegulationDocumentLocators.TOTAL_COMMENT_FIELD_2_LOCATOR)]
            elements = self.count_all_elements(*RegulationDocumentLocators.TOTAL_COMMENT_NAME_LOCATOR)
            arr_elements = tc
        elif name == NUMBER_COMMENT:
            nc = [[RegulationDocumentLocators.NUMBER_COMMENT_FIELD_VIEW_MODE_LOCATOR, RegulationDocumentLocators.NUMBER_COMMENT_FIELD_2_VIEW_MODE_LOCATOR],
                  [RegulationDocumentLocators.NUMBER_COMMENT_FIELD_LOCATOR, RegulationDocumentLocators.NUMBER_COMMENT_FIELD_2_LOCATOR]]
            elements = self.count_all_elements(*RegulationDocumentLocators.NUMBER_COMMENT_NAME_LOCATOR)
            arr_elements = nc
        elif name == NUMBER_UNA_COMMENT:
            nuc = [[RegulationDocumentLocators.NUMBER_UNA_COMMENT_FIELD_VIEW_MODE_LOCATOR, RegulationDocumentLocators.NUMBER_UNA_COMMENT_FIELD_2_VIEW_MODE_LOCATOR],
                   [RegulationDocumentLocators.NUMBER_UNA_COMMENT_FIELD_LOCATOR, RegulationDocumentLocators.NUMBER_UNA_COMMENT_FIELD_2_LOCATOR]]
            elements = self.count_all_elements(*RegulationDocumentLocators.NUMBER_UNA_COMMENT_NAME_LOCATOR)
            arr_elements = nuc
        elif name == NUMBER_PTA_COMMENT:
            npc = [[RegulationDocumentLocators.NUMBER_PTA_COMMENT_FIELD_VIEW_MODE_LOCATOR, RegulationDocumentLocators.NUMBER_PTA_COMMENT_FIELD_2_VIEW_MODE_LOCATOR],
                  [RegulationDocumentLocators.NUMBER_PTA_COMMENT_FIELD_LOCATOR, RegulationDocumentLocators.NUMBER_PTA_COMMENT_FIELD_2_LOCATOR]]
            elements = self.count_all_elements(*RegulationDocumentLocators.NUMBER_PTA_COMMENT_NAME_LOCATOR)
            arr_elements = npc
        
        if elements == 1:
            if fill == False:
                return [arr_elements[0][0]]
            elif fill == True:
                return [arr_elements[1][0]]
        elif elements == 2:
            if fill == False:
                return arr_elements[0]
            elif fill == True:
                return arr_elements[1]

    def should_be_total_comment_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.TOTAL_COMMENT_NAME_LOCATOR)

    def should_be_total_comment_fields(self, name, text):
        self.should_be_total_comment_field(name)
        for i in self.count_comment_fields(name, False):
            assert str(text) == self.return_text(*i)

    def enter_total_comment_field(self, name, text, edit):
        self.should_be_total_comment_field(name)
        for i in self.count_comment_fields(name, True):
            self.fill_field(*i, text)

    """

    * Кол-во учтенных замечаний

    """

    def should_be_number_comment_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.NUMBER_COMMENT_NAME_LOCATOR)

    def should_be_number_comment_fields(self, name, text):
        self.should_be_number_comment_field(name)
        for i in self.count_comment_fields(name, False):
            assert str(text) == self.return_text(*i)

    def enter_number_comment_field(self, name, text, edit):
        self.should_be_number_comment_field(name)
        for i in self.count_comment_fields(name, True):
            self.fill_field(*i, text)

    """

    * Кол-во неучтенных замечаний

    """

    def should_be_number_una_comment_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.NUMBER_UNA_COMMENT_NAME_LOCATOR)

    def should_be_number_una_comment_fields(self, name, text):
        self.should_be_number_una_comment_field(name)
        for i in self.count_comment_fields(name, False):
            assert str(text) == self.return_text(*i)

    def enter_number_una_comment_field(self, name, text, edit):
        self.should_be_number_una_comment_field(name)
        for i in self.count_comment_fields(name, True):
            self.fill_field(*i, text)

    """

    * Кол-во частично учтенных замечаний

    """

    def should_be_number_pta_comment_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.NUMBER_PTA_COMMENT_NAME_LOCATOR)

    def should_be_number_pta_comment_fields(self, name, text):
        self.should_be_number_pta_comment_field(name)
        for i in self.count_comment_fields(name, False):
            assert str(text) == self.return_text(*i)

    def enter_number_pta_comment_field(self, name, text, edit):
        self.should_be_number_pta_comment_field(name)
        for i in self.count_comment_fields(name, True):
            self.fill_field(*i, text)

    """

    * Информация о принятом решении & * Принятое решение по проекту НПА

    """
    def decision_info_type(self, name, text):
        if name == DECISION_INFO:
            if text != FILL_DECISION_INFO:
                if self.count_all_elements(*AllDocumentFieldLocators.find_text_locator(FILL_DECISION_INFO_EDIT)) > 0:
                    return [RegulationDocumentLocators.DECISION_INFO_NAME_LOCATOR, RegulationDocumentLocators.DECISION_INFO_SELECT_LOCATOR, RegulationDocumentLocators.DECISION_INFO_FIELD_VIEW_MODE_LOCATOR, FILL_DECISION_INFO_EDIT]
                elif self.count_all_elements(*AllDocumentFieldLocators.find_text_locator(FILL_DECISION_INFO_3_EDIT)) > 0:
                    return [RegulationDocumentLocators.DECISION_INFO_NAME_LOCATOR, RegulationDocumentLocators.DECISION_INFO_SELECT_LOCATOR, RegulationDocumentLocators.DECISION_INFO_FIELD_VIEW_MODE_LOCATOR, FILL_DECISION_INFO_3_EDIT]
            return [RegulationDocumentLocators.DECISION_INFO_NAME_LOCATOR, RegulationDocumentLocators.DECISION_INFO_SELECT_LOCATOR, RegulationDocumentLocators.DECISION_INFO_FIELD_VIEW_MODE_LOCATOR, FILL_DECISION_INFO]
        elif name == DECISION_INFO_2:
            if text != FILL_DECISION_INFO_2:
                return [RegulationDocumentLocators.DECISION_INFO_2_NAME_LOCATOR, RegulationDocumentLocators.DECISION_INFO_2_SELECT_LOCATOR, RegulationDocumentLocators.DECISION_INFO_2_FIELD_VIEW_MODE_LOCATOR, FILL_DECISION_INFO_2_EDIT]
            return [RegulationDocumentLocators.DECISION_INFO_2_NAME_LOCATOR, RegulationDocumentLocators.DECISION_INFO_2_SELECT_LOCATOR, RegulationDocumentLocators.DECISION_INFO_2_FIELD_VIEW_MODE_LOCATOR, FILL_DECISION_INFO_2]

    def should_be_decision_info_field(self, name, text):
        dec_type = self.decision_info_type(name, text)

        assert self.should_be_correct_field_name(name, dec_type[0])
        return dec_type

    def should_be_decision_info_fields(self, field_name, text):
        dec_type = self.should_be_decision_info_field(field_name, text)
        field_text = self.return_text(*dec_type[2])
        assert dec_type[-1] == field_text

    def select_decision_info_field(self, field_name, text, edit):
        dec_type = self.should_be_decision_info_field(field_name, text)
        assert self.is_element_present(*dec_type[1])
        self.work_with_selector(*dec_type[1], visible_text=str(dec_type[-1]))

    """

    * Сводка предложений

    """

    def should_be_summary_info_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.SUMMARY_INFO_NAME_LOCATOR)

    def should_be_summary_info_fields(self, field_name, text):
        self.should_be_summary_info_field(field_name)
        assert text == self.return_text(
            *RegulationDocumentLocators.SUMMARY_INFO_FIELD_VIEW_MODE_LOCATOR)

    def enter_summary_info_field(self, field_name, text, edit):
        self.should_be_summary_info_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.SUMMARY_INFO_FIELD_LOCATOR)
        assert self.is_element_present(
            *RegulationDocumentLocators.SUMMARY_INFO_ADD_FILE_BUTTON_LOCATOR)

        self.fill_field(
            *RegulationDocumentLocators.SUMMARY_INFO_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.SUMMARY_INFO_FIELD_LOCATOR, text)

    """

    * Доработанный проект НПА

    """

    def should_be_modified_npa_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.MODIFIED_NPA_NAME_LOCATOR)

    def should_be_modified_npa_fields(self, field_name, text):
        self.should_be_modified_npa_field(field_name)
        assert text == self.return_text(
            *RegulationDocumentLocators.MODIFIED_NPA_FIELD_VIEW_MODE_LOCATOR)

    def enter_modified_npa_field(self, field_name, text, edit):
        self.should_be_modified_npa_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.MODIFIED_NPA_FIELD_LOCATOR)
        assert self.is_element_present(
            *RegulationDocumentLocators.MODIFIED_NPA_ADD_FILE_BUTTON_LOCATOR)

        self.fill_field(
            *RegulationDocumentLocators.MODIFIED_NPA_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.MODIFIED_NPA_FIELD_LOCATOR, text)

    """

    * Прием заключений антикоррупционной экспертизы

    """

    def should_be_ac_expertise_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.AC_EXPERTISE_NAME_LOCATOR)

    def should_be_ac_expertise_fields(self, field_name, text):
        self.should_be_ac_expertise_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.AC_EXPERTISE_FIELD_VIEW_MODE_LOCATOR)

    def enter_ac_expertise_field(self, field_name, text, edit):
        self.should_be_ac_expertise_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.AC_EXPERTISE_FIELD_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.AC_EXPERTISE_FIELD_LOCATOR, text)

    """

    * E-mail для заключений антикоррупционной экспертизы

    """

    def should_be_email_ac_expertise_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.EMAIL_AC_EXPERTISE_NAME_LOCATOR)

    def should_be_email_ac_expertise_fields(self, field_name, text):
        self.should_be_email_ac_expertise_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.EMAIL_AC_EXPERTISE_FIELD_VIEW_MODE_LOCATOR)

    def enter_email_ac_expertise_field(self, field_name, text, edit):
        self.should_be_email_ac_expertise_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.EMAIL_AC_EXPERTISE_FIELD_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.EMAIL_AC_EXPERTISE_FIELD_LOCATOR, text)

    """

    * Почта для заключений антикоррупционной экспертизы

    """

    def should_be_mail_ac_expertise_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.MAIL_AC_EXPERTISE_NAME_LOCATOR)

    def should_be_mail_ac_expertise_fields(self, field_name, text):
        self.should_be_mail_ac_expertise_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.MAIL_AC_EXPERTISE_FIELD_VIEW_MODE_LOCATOR)

    def enter_mail_ac_expertise_field(self, field_name, text, edit):
        self.should_be_mail_ac_expertise_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.MAIL_AC_EXPERTISE_FIELD_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.MAIL_AC_EXPERTISE_FIELD_LOCATOR, text)

    """

    * Коррупциогенные факторы

    """

    def should_be_corruption_factor_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.CORRUPTION_FACTOR_NAME_LOCATOR)

    def should_be_corruption_factor_fields(self, field_name, text):
        self.should_be_corruption_factor_field(field_name)
        assert text == self.return_text(
            *RegulationDocumentLocators.CORRUPTION_FACTOR_FIELD_VIEW_MODE_LOCATOR)

    def select_corruption_factor_field(self, field_name, text, edit):
        self.should_be_corruption_factor_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.CORRUPTION_FACTOR_FIELD_LOCATOR)
        self.work_with_selector(
            *RegulationDocumentLocators.CORRUPTION_FACTOR_FIELD_LOCATOR, visible_text=text)

    """

    * Кол-во заключений

    """

    def should_be_number_conclusion_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.NUMBER_CONCLUSION_NAME_LOCATOR)

    def should_be_number_conclusion_fields(self, field_name, text):
        self.should_be_number_conclusion_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.NUMBER_CONCLUSION_FIELD_VIEW_MODE_LOCATOR)

    def enter_number_conclusion_field(self, field_name, text, edit):
        self.should_be_number_conclusion_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.NUMBER_CONCLUSION_FIELD_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.NUMBER_CONCLUSION_FIELD_LOCATOR, text)

    """

    * Общее заключение по итогам антикоррупционной экспертизы

    """

    def should_be_gc_ac_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.GC_AC_NAME_LOCATOR)

    def should_be_gc_ac_fields(self, field_name, text):
        self.should_be_gc_ac_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.GC_AC_FIELD_VIEW_MODE_LOCATOR)

    def enter_gc_ac_field(self, field_name, text, edit):
        self.should_be_gc_ac_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.GC_AC_FIELD_LOCATOR)
        assert self.is_element_present(
            *RegulationDocumentLocators.GC_AC_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.GC_AC_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.GC_AC_FIELD_LOCATOR, text)

    """

    * Нормативный правовой акт (проект)

    """

    def should_be_npa_draft_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.NPA_DRAFT_NAME_LOCATOR)

    def should_be_npa_draft_fields(self, field_name, text):
        self.should_be_npa_draft_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.NPA_DRAFT_FIELD_VIEW_MODE_LOCATOR)

    def enter_npa_draft_field(self, field_name, text, edit):
        self.should_be_npa_draft_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.NPA_DRAFT_FIELD_LOCATOR)
        assert self.is_element_present(
            *RegulationDocumentLocators.NPA_DRAFT_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.NPA_DRAFT_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.NPA_DRAFT_FIELD_LOCATOR, text)

    """

    * Номер принятого НПА & Номер НПА

    """

    def should_be_npa_number_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.NPA_NUMBER_NAME_LOCATOR)

    def should_be_npa_number_fields(self, field_name, text):
        self.should_be_npa_number_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.NPA_NUMBER_FIELD_VIEW_MODE_LOCATOR)

    def enter_npa_number_field(self, field_name, text, edit):
        self.should_be_npa_number_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.NPA_NUMBER_FIELD_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.NPA_NUMBER_FIELD_LOCATOR, text)

    """

    * Утвержденный НПА

    """

    def should_be_approved_npa_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.APPROVED_NPA_NAME_LOCATOR)

    def should_be_approved_npa_fields(self, field_name, text):
        self.should_be_approved_npa_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.APPROVED_NPA_FIELD_VIEW_MODE_LOCATOR)

    def enter_approved_npa_field(self, field_name, text, edit):
        self.should_be_approved_npa_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.APPROVED_NPA_FIELD_LOCATOR)
        assert self.is_element_present(
            *RegulationDocumentLocators.APPROVED_NPA_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.APPROVED_NPA_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.APPROVED_NPA_FIELD_LOCATOR, text)

    """

    * Дата принятия НПА & Дата НПА

    """

    def should_be_npa_adoption_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.NPA_ADOPTION_NAME_LOCATOR)
        if name == NPA_ADOPTION_DATE_1:
            return [RegulationDocumentLocators.NPA_ADOPTION_FIELD_LOCATOR]
        elif name == NPA_ADOPTION_DATE_2:
            return [RegulationDocumentLocators.NPA_DATE_FIELD_LOCATOR]

    def should_be_npa_adoption_fields(self, field_name, text):
        self.should_be_npa_adoption_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.NPA_ADOPTION_FIELD_VIEW_MODE_LOCATOR)

    def enter_npa_adoption_field(self, field_name, text, edit):
        field = self.should_be_npa_adoption_field(field_name)

        assert self.is_element_present(*field[0])
        self.fill_field(*field[0], text)

    """

    * Обоснование отказа от общественного обсуждения проекта НПА

    """

    def should_be_pd_npa_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.PD_NPA_NAME_LOCATOR)

    def should_be_pd_npa_fields(self, field_name, text):
        self.should_be_pd_npa_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.PD_NPA_FIELD_VIEW_MODE_LOCATOR)

    def enter_pd_npa_field(self, field_name, text, edit):
        self.should_be_pd_npa_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.PD_NPA_FIELD_LOCATOR)
        assert self.is_element_present(
            *RegulationDocumentLocators.PD_NPA_ADD_FILE_BUTTON_LOCATOR)

        self.fill_field(
            *RegulationDocumentLocators.PD_NPA_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.PD_NPA_FIELD_LOCATOR, text)

    """

    * Сводный отчет

    """

    def should_be_consol_report_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.CONSOL_REPORT_NAME_LOCATOR)

    def should_be_consol_report_fields(self, field_name, text):
        self.should_be_consol_report_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.CONSOL_REPORT_FIELD_VIEW_MODE_LOCATOR)

    def enter_consol_report_field(self, field_name, text, edit):
        self.should_be_consol_report_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.CONSOL_REPORT_FIELD_LOCATOR)
        assert self.is_element_present(
            *RegulationDocumentLocators.CONSOL_REPORT_ADD_FILE_BUTTON_LOCATOR)

        self.fill_field(
            *RegulationDocumentLocators.CONSOL_REPORT_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.CONSOL_REPORT_FIELD_LOCATOR, text)

    """

    * Срок принятия предложений

    """

    def should_be_decision_period_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.DECISION_PERIOD_NAME_LOCATOR)

    def should_be_decision_period_fields(self, field_name, text):
        self.should_be_decision_period_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.DECISION_PERIOD_FIELD_VIEW_MODE_LOCATOR)

    def enter_decision_period_field(self, field_name, text, edit):
        self.should_be_decision_period_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.DECISION_PERIOD_FIELD_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.DECISION_PERIOD_FIELD_LOCATOR, text)

    """

    * Степень воздействия

    """

    def should_be_degree_exposure_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.DEGREE_EXPOSURE_NAME_LOCATOR)

    def should_be_degree_exposure_fields(self, field_name, text):
        self.should_be_degree_exposure_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.DEGREE_EXPOSURE_FIELD_VIEW_MODE_LOCATOR)

    def select_degree_exposure_field(self, field_name, text, edit):
        self.should_be_degree_exposure_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.DEGREE_EXPOSURE_FIELD_LOCATOR), f"Не отображается селектор поля '{NPA_TYPE}'"
        self.work_with_selector(
            *RegulationDocumentLocators.DEGREE_EXPOSURE_FIELD_LOCATOR, visible_text=str(text))

    """

    * Краткое содержание

    """

    def should_be_closed_short_content_fields(self, field_type=1):
        field = {
            1: SHORT_CONTENT_TEXT,
            2: SHORT_CONTENT_ANSWER_TEXT,
            3: "Отказ на заявку на размещение информации на официальном сайте regulation.gov.ru"
        }

        assert self.is_element_present(
            *RegulationDocumentLocators.SHORT_CONTENT_NAME_LOCATOR), f"Не отображается или не является обязательным поле '{SHORT_CONTENT}'"
        assert self.is_element_present(
            *RegulationDocumentLocators.SHORT_CONTENT_FIELD_LOCATOR), f"Не отображается или доступно для редактирования поле '{SHORT_CONTENT}'"
        short_content_field = self.driver.find_element(
            *RegulationDocumentLocators.SHORT_CONTENT_FIELD_LOCATOR)
        assert short_content_field.text == field[field_type], f"Поле '{SHORT_CONTENT}' должно быть заполнено тектом {field[field_type]}"

    """

    * Доработанный сводный отчет

    """

    def should_be_msr_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.MSR_NAME_LOCATOR)

    def should_be_msr_fields(self, field_name, text):
        self.should_be_msr_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.MSR_FIELD_VIEW_MODE_LOCATOR)

    def enter_msr_field(self, field_name, text, edit):
        self.should_be_msr_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.MSR_FIELD_LOCATOR)
        assert self.is_element_present(
            *RegulationDocumentLocators.MSR_ADD_FILE_BUTTON_LOCATOR)

        self.fill_field(
            *RegulationDocumentLocators.MSR_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.MSR_FIELD_LOCATOR, text)

    """

    * Проект решения ЕЭК

    """

    def should_be_eec_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.EEC_NAME_LOCATOR)

    def should_be_eec_fields(self, field_name, text):
        self.should_be_eec_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.EEC_FIELD_VIEW_MODE_LOCATOR)

    def enter_eec_field(self, field_name, text, edit):
        self.should_be_eec_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.EEC_FIELD_LOCATOR)
        assert self.is_element_present(
            *RegulationDocumentLocators.EEC_ADD_FILE_BUTTON_LOCATOR)

        self.fill_field(
            *RegulationDocumentLocators.EEC_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.EEC_FIELD_LOCATOR, text)

    """

    * Доработанный проект решения ЕЭК

    """

    def should_be_mdd_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.MDD_NAME_LOCATOR)

    def should_be_mdd_fields(self, field_name, text):
        self.should_be_mdd_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.MDD_FIELD_VIEW_MODE_LOCATOR)

    def enter_mdd_field(self, field_name, text, edit):
        self.should_be_mdd_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.MDD_FIELD_LOCATOR)
        assert self.is_element_present(
            *RegulationDocumentLocators.MDD_ADD_FILE_BUTTON_LOCATOR)

        self.fill_field(
            *RegulationDocumentLocators.MDD_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.MDD_FIELD_LOCATOR, text)

    """

    * Отчет об оценке фактического воздействия НПА

    """

    def should_be_assessment_report_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.ASSESSMENT_REPORT_NAME_LOCATOR)

    def should_be_assessment_report_fields(self, field_name, text):
        self.should_be_assessment_report_field(field_name)
        
        assert text == self.return_text(*RegulationDocumentLocators.ASSESSMENT_REPORT_FIELD_VIEW_MODE_LOCATOR)
    
    def enter_assessment_report_field(self, field_name, text, edit):
        self.should_be_assessment_report_field(field_name)

        assert self.is_element_present(*RegulationDocumentLocators.ASSESSMENT_REPORT_FIELD_LOCATOR)
        assert self.is_element_present(*RegulationDocumentLocators.ASSESSMENT_REPORT_ADD_FILE_BUTTON_LOCATOR)

        self.fill_field(*RegulationDocumentLocators.ASSESSMENT_REPORT_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.ASSESSMENT_REPORT_FIELD_LOCATOR, text)  

    """

    * Доработанный отчет об оценке фактического воздействия НПА

    """ 

    def should_be_rr_npa_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.RR_NPA_NAME_LOCATOR)

    def should_be_rr_npa_fields(self, field_name, text):
        self.should_be_rr_npa_field(field_name)

        assert text == self.return_text(*RegulationDocumentLocators.RR_NPA_FIELD_VIEW_MODE_LOCATOR)
    
    def enter_rr_npa_field(self, field_name, text, edit):
        self.should_be_rr_npa_field(field_name)

        assert self.is_element_present(*RegulationDocumentLocators.RR_NPA_FIELD_LOCATOR)
        assert self.is_element_present(*RegulationDocumentLocators.RR_NPA_ADD_FILE_BUTTON_LOCATOR)

        self.fill_field(*RegulationDocumentLocators.RR_NPA_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.RR_NPA_FIELD_LOCATOR, text)

    """

    * Е-mail для предложений

    """

    def should_be_offers_email_field(self, name):
        self.should_be_correct_field_name(name, RegulationDocumentLocators.OFFERS_EMAIL_NAME_LOCATOR)

    def should_be_offers_email_fields(self, field_name, text):
        self.should_be_offers_email_field(field_name)

        assert text == self.return_text(*RegulationDocumentLocators.OFFERS_EMAIL_FIELD_VIEW_MODE_LOCATOR)
    
    def enter_offers_email_field(self, field_name, text, edit):
        self.should_be_offers_email_field(field_name)

        assert self.is_element_present(*RegulationDocumentLocators.OFFERS_EMAIL_FIELD_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.OFFERS_EMAIL_FIELD_LOCATOR, text)

    """

    Органы гос. власти – соисполнители

    """

    def should_be_co_exector_field(self, name):
        assert self.is_element_present(
            *RegulationDocumentLocators.CO_EXECTOR_NAME_LOCATOR),  f"Не отображается или является обязательным поле '{CO_EXECTOR}'"

    def should_be_co_exector_fields(self, field_name, text):
        self.should_be_co_exector_field(field_name)
        assert text == self.return_text(
            *RegulationDocumentLocators.CO_EXECTOR_FIELD_VIEW_MODE_LOCATOR)

    def count_co_exector_elements(self):
        return self.count_all_elements(*RegulationDocumentLocators.FOR_COUNT_ELEMENTS_IN_CO_EXECTOR_FIELD_CEM_LOCATOR)

    def select_text_co_exector(self, text):
        count_elements = self.count_co_exector_elements()
        self.fill_field(
            *RegulationDocumentLocators.CO_EXECTOR_FIELD_LOCATOR, text)
        self.choose_user_from_drop_list()
        assert self.count_co_exector_elements() == count_elements+1

    def enter_new_window_co_exector(self, field_name, text, edit):
        self.should_be_co_exector_field(field_name)
        assert self.is_element_present(
            *RegulationDocumentLocators.CO_EXECTOR_FIELD_LOCATOR), f"Не отображается поле '{CO_EXECTOR}'"
        assert self.is_element_present(
            *RegulationDocumentLocators.CHOOSE_CO_EXECTOR_FROM_NEW_WINDOW), f"Не отображается кнопка '{CO_EXECTOR}'"
        if edit == True:
            count_elements = self.count_co_exector_elements()
            self.driver.find_element(
                *RegulationDocumentLocators.CHOOSE_CO_EXECTOR_FROM_NEW_WINDOW).click()
            self.work_with_windows(1)
            self.driver.find_element(
                *ChooseOrganisationFromNewWindow.ORG_FIND_LOCATOR).send_keys(text)
            self.driver.find_element(
                *ChooseOrganisationFromNewWindow.FIND_BUTTON_LOCATOR).click()
            self.driver.find_element(
                *AllDocumentFieldLocators.find_text_locator(text)).click()
            self.work_with_windows()

            assert self.count_co_exector_elements() == count_elements+1

    """

    Доп. e-mail для предложений

    """

    def should_be_add_offer_email_field(self, name):
        text = self.return_text(*RegulationDocumentLocators.ADD_OFFER_EMAIL_NAME_LOCATOR)
        assert text == name + ":"

    def should_be_add_offer_email_fields(self, field_name, text):
        self.should_be_add_offer_email_field(field_name)
        assert text == self.return_text(
            *RegulationDocumentLocators.ADD_OFFER_EMAIL_FIELD_VIEW_MODE_LOCATOR)

    def enter_add_offer_email_field(self, field_name, text, edit):
        self.should_be_add_offer_email_field(field_name)
        assert self.is_element_present(
            *RegulationDocumentLocators.ADD_OFFER_EMAIL_FIELD_LOCATOR), f"Не отображается поле '{ADD_OFFER_EMAIL}'"
        if edit == True:
            self.fill_field(
                *RegulationDocumentLocators.ADD_OFFER_EMAIL_FIELD_LOCATOR, text)

    """

    Основание для разработки НПА

    """

    def should_be_reason_create_npa_field(self, name):
        text = self.return_text(*RegulationDocumentLocators.REASON_CREATE_NPA_NAME_LOCATOR)
        assert text == name + ":"

    def should_be_reason_create_npa_fields(self, field_name, text):
        self.should_be_reason_create_npa_field(field_name)
        assert text == self.return_text(
            *RegulationDocumentLocators.REASON_CREATE_NPA_FIELD_VIEW_MODE_LOCATOR)

    def enter_reason_create_npa_field(self, field_name, text, edit):
        self.should_be_reason_create_npa_field(field_name)
        assert self.is_element_present(
                *RegulationDocumentLocators.REASON_CREATE_NPA_FIELD_LOCATOR), f"Не отображается поле '{REASON_CREATE_NPA}'"
        if edit == True:    
            self.fill_field(
                *RegulationDocumentLocators.REASON_CREATE_NPA_FIELD_LOCATOR, text)

    """

    ID связанных НПА

    """

    def should_be_link_id_field(self, name):
        text = self.return_text(*RegulationDocumentLocators.NPA_LINK_ID_NAME_LOCATOR)
        assert text == name + ":"

    def should_be_link_id_fields(self, field_name, text):
        self.should_be_link_id_field(field_name)
        assert text == self.return_text(
            *RegulationDocumentLocators.NPA_LINK_ID_FIELD_VIEW_MODE_LOCATOR)

    def enter_link_id_field(self, field_name, text, edit):
        self.should_be_link_id_field(field_name)
        assert self.is_element_present(
                *RegulationDocumentLocators.NPA_LINK_ID_FIELD_LOCATOR), f"Не отображается поле '{LINK_ID}'"
        if edit == True:
            self.fill_field(
                *RegulationDocumentLocators.NPA_LINK_ID_FIELD_LOCATOR, text)

    """

    Дополнительные материалы

    """

    def should_be_additional_materials_field(self, name):
        text = self.return_text(*RegulationDocumentLocators.ADDITIONAL_MATERIALS_NAME_LOCATOR)
        assert text == name + ":"

    def should_be_additional_materials_fields(self, field_name, text):
        self.should_be_additional_materials_field(field_name)
        assert text in self.return_text(
            *RegulationDocumentLocators.ADDITIONAL_MATERIALS_FIELD_VIEW_MODE_LOCATOR)

    def count_additonal_material_elments(self):
        return self.count_all_elements(*RegulationDocumentLocators.FOR_COUNT_ELEMENTS_IN_ADDITIONAL_MATERIALS_FIELD_CEM_LOCATOR)

    def click_to_additonal_material_add_button(self):
        additional_material_count_opened = self.count_additonal_material_elments()
        self.driver.find_element(
            *RegulationDocumentLocators.ADDITIONAL_MATERIALS_ADD_BUTTON_LOCATOR).click()
        assert self.count_additonal_material_elments(
        ) == additional_material_count_opened + 1

    def click_to_additonal_material_delete_button(self):
        additional_material_count = self.count_additonal_material_elments()
        self.driver.find_element(
            *RegulationDocumentLocators.REMOVE_LAST_ELEMENT_IN_ADDITIONAL_MATERIALS_LOCATOR).click()
        assert self.count_additonal_material_elments() == additional_material_count - 1

    def enter_additional_materials_field(self, field_name, text, edit):
        self.should_be_additional_materials_field(field_name)
        assert self.is_element_present(
                *RegulationDocumentLocators.ADDITIONAL_MATERIALS_ADD_BUTTON_LOCATOR), f"Не отображается кнопка '{ADDITIONAL_MATERIAL}'"
        if edit == True:
            self.click_to_additonal_material_add_button()
            self.fill_field(
                *RegulationDocumentLocators.ADD_FILE_LAST_ELEMENT_IN_ADDITIONAL_MATERIALS_LOCATOR)
            self.fill_field(
                *RegulationDocumentLocators.ENTER_LAST_ELEMENT_IN_ADDITIONAL_MATERIALS_LOCATOR, text)

    """

    Регуляторная гильотина

    """

    def should_be_regulatory_gilliotine_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.REGULATORY_GILLIOTINE_NAME_LOCATOR)

    def should_be_regulatory_gilliotine_fields(self, field_name, text):
        self.should_be_regulatory_gilliotine_field(field_name)
        assert text == self.return_text(
            *RegulationDocumentLocators.REGULATORY_GILLIOTINE_FIELD_VIEW_MODE_LOCATOR)

    def activate_regulatory_gilliotine_checkbox(self, field_name, text, edit):
        self.should_be_regulatory_gilliotine_field(field_name)
        assert self.is_element_present(*RegulationDocumentLocators.REGULATORY_GILLIOTINE_CHECKBOX_LOCATOR)
        if edit == True:
            self.driver.find_element(
                *RegulationDocumentLocators.REGULATORY_GILLIOTINE_CHECKBOX_LOCATOR).click()

    """

    Уведомление о подготовке НПА не размещается

    """

    def should_be_notice_npa_not_placed_field(self, name, edit):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.NOTICE_NPA_NOT_PLACED_NAME_LOCATOR)
        if edit == None:
            return [NO_FIELD]
        elif edit == False:
            return [FILL_NOTICE_NPA_NAME, DATE]
        elif edit == True:
            return [FILL_NOTICE_NPA_NAME_EDIT, DATE_EDIT]

    def should_be_notice_npa_not_placed_fields(self, field_name, edit):
        field = self.should_be_notice_npa_not_placed_field(field_name, edit)
        text = self.return_text(
            *RegulationDocumentLocators.NOTICE_NPA_NOT_PLACED_FIELD_VIEW_MODE_LOCATOR)

        for i in field:
            assert i in text

    def enter_notice_npa_not_placed_field(self, field_name, edit):
        field = self.should_be_notice_npa_not_placed_field(field_name, edit)
        assert self.is_element_present(
                *RegulationDocumentLocators.NOTICE_NPA_NOT_PLACED_CHECKBOX_LOCATOR)
        if edit != None:
            if edit == False:
                self.driver.find_element(
                    *RegulationDocumentLocators.NOTICE_NPA_NOT_PLACED_CHECKBOX_LOCATOR).click()
            else:
                self.driver.find_element(
                    *RegulationDocumentLocators.NOTICE_NPA_NOT_PLASED_DELETE_BUTTON_LOCATOR).click()
            self.driver.find_element(
                *RegulationDocumentLocators.NOTICE_NPA_NOT_PLACED_NEW_WINDOW_LOCATOR).click()
            self.work_with_windows(1)
            self.fill_field(
                *ChooseUserFromNewWindow.USER_FIND_LOCATOR, field[0])
            self.driver.find_element(
                *AllDocumentFieldLocators.find_text_locator(field[0])).click()
            self.work_with_windows()
            self.fill_field(
                *RegulationDocumentLocators.NOTICE_NPA_NOT_PLACED_DATE_LOCATOR, field[1])
    
    def regulation_correct_notice_npa_not_placed_fields(self, index, first, mode):
        mods = {
            1: (True, False),
            2: (True, True),
            3: (False, True),
            4: (False, False),
        }
        
        if index in [7, 8, 10, 12, 13]:
            if mods[mode][0] == True:
                L = self.enter_notice_npa_not_placed_field
                L(NOTICE_NPA_NOT_PLACED, mods[mode][1]) if first == True else L(NOTICE_NPA_NOT_PLACED, None)
            else:
                L = self.should_be_notice_npa_not_placed_fields
                L(NOTICE_NPA_NOT_PLACED, mods[mode][1]) if first == True else L(NOTICE_NPA_NOT_PLACED, None)

    """

    Номер государственной регистрации НПА

    """

    def should_be_state_number_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.STATE_NUMBER_NAME_LOCATOR)

    def should_be_state_number_fields(self, field_name, text):
        self.should_be_state_number_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.STATE_NUMBER_FIELD_VIEW_MODE_LOCATOR)

    def enter_state_number_field(self, field_name, text, edit):
        self.should_be_state_number_field(field_name)
        assert self.is_element_present(
            *RegulationDocumentLocators.STATE_NUMBER_FIELD_LOCATOR)
        if edit == True:
            self.fill_field(
                *RegulationDocumentLocators.STATE_NUMBER_FIELD_LOCATOR, text)

    """

    Тип затрагиваемых вопросов

    """

    def should_be_issue_type_field(self, name):
        assert self.should_be_correct_field_name(name, RegulationDocumentLocators.ISSUE_TYPE_NAME_LOCATOR)

        for i in [RegulationDocumentLocators.ISSUE_TYPE_FIELD_LOCATOR, RegulationDocumentLocators.ISSUE_TYPE_FIELD_2_LOCATOR]:
            if self.count_all_elements(*i) != 0:
                return i

    def should_be_issue_type_fields(self, field_name, text):
        self.should_be_issue_type_field(field_name)
        
        field_text = self.return_text(*RegulationDocumentLocators.ISSUE_TYPE_FIELD_VIEW_MODE_LOCATOR)
        field_text = (text == field_text) or (field_text == NON_REQUIRED_FIELD)
        assert field_text

    def enter_issue_type_field(self, field_name, text, edit):
        field = self.should_be_issue_type_field(field_name)
        assert self.is_element_present(*field)
        if edit == True:
            self.work_with_selector(*field, visible_text=text)

    """

    Сообщение о повтороной Заявке

    """
    
    def should_be_repeat_message(self):
        self.is_element_present(*RegulationDocumentLocators.REPEAT_MESSAGE_LOCATOR)
        text_in_message = self.return_text(*RegulationDocumentLocators.REPEAT_MESSAGE_LOCATOR)

        assert text_in_message == "Обращаем внимание!\nДанный НПА размещается повторно."


    """

    Ответ

    """

    # * ID проекта НПА
    def should_be_npa_id_fields(self, type=1):
        if type == 4:
            assert self.is_element_present(
                *RegulationAnswerPageLocators.NPA_ID_NAME_LOCATOR_2)
        else:
            assert self.is_element_present(
                *RegulationAnswerPageLocators.NPA_ID_NAME_LOCATOR)

    def enter_npa_id_fields(self, id, create=False):
        if create == True:
            self.fill_field(*RegulationAnswerPageLocators.NPA_ID_FIELD_LOCATOR, str(id))
        else:
            self.driver.find_element(
                *AllDocumentFieldLocators.find_text_locator(id))

    # * Дата начала обсуждения уведомления
    def should_be_start_date_name_field(self):
        assert self.is_element_present(
            *RegulationAnswerPageLocators.DATE_START_NAME_LOCATOR)

    def should_be_start_date_fields(self, a_type):
        self.should_be_start_date_name_field()
        assert self.is_element_present(
            *RegulationAnswerPageLocators.DATE_START_FIELD_LOCATOR)

        text = self.driver.find_element(
            *RegulationAnswerPageLocators.DATE_START_FIELD_LOCATOR).text
        if a_type == 1:
            text == ANSWER_START_1
        elif a_type == 2:
            text == ANSWER_START_2
        elif a_type == 3:
            text == ANSWER_START_3
        elif a_type == 4:
            text == ANSWER_START_4

    def enter_start_date(self):
        self.driver.find_element(
            *RegulationAnswerPageLocators.DATE_START_FIELD_LOCATOR).send_keys(self.date_return())

    # * Дата окончания обсуждения уведомления
    def should_be_end_date_name_field(self):
        assert self.is_element_present(
            *RegulationAnswerPageLocators.DATE_END_NAME_LOCATOR)

    def should_be_end_date_fields(self, a_type):
        self.should_be_start_date_name_field()
        assert self.is_element_present(
            *RegulationAnswerPageLocators.DATE_END_FIELD_LOCATOR)

        text = self.driver.find_element(
            *RegulationAnswerPageLocators.DATE_END_FIELD_LOCATOR).text
        if a_type == 1:
            text == ANSWER_END_1
        elif a_type == 2:
            text == ANSWER_END_2
        elif a_type == 3:
            text == ANSWER_END_3
        elif a_type == 4:
            text == ANSWER_END_4

    def enter_end_date(self):
        self.driver.find_element(
            *RegulationAnswerPageLocators.DATE_END_FIELD_LOCATOR).send_keys(self.date_return())

    # Добавить файлы
    def should_be_add_file_button(self):
        assert self.is_element_present(
            *RegulationAnswerPageLocators.ADD_DOCUMENT_LOCATOR)

    """

    Остальное связанное с Regulation

    """

    def save_regulation_rcd(self, edit, index):
        save_button = AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR
        assert self.is_active(*save_button)
        self.click_to(*save_button)

        url = self.driver.current_url
        count = 0

        # try:
        #     none_attribute = self.driver.find_element(*save_button).get_attribute("style")
        # except:
        #     none_attribute = "none"

        while self.url_change(url, timeout=20) == False and count < 3:
            if int(index) not in [4, 5, 6, 20, 21, 28, 33, 34]:
                if self.is_not_element_present(*RegulationDocumentLocators.REGULATION_ERROR_MESSAGE_PHONE_EMAIL_LOCATOR, timeout=5) == False:
                    self.enter_responsible_review_phone_field(FILL_RESPONSIBLE_REVIEW_PHONE_EDIT if edit == True else FILL_RESPONSIBLE_REVIEW_PHONE)
                    self.enter_responsible_review_email_field(FILL_RESPONSIBLE_REVIEW_EMAIL_EDIT if edit == True else FILL_RESPONSIBLE_REVIEW_EMAIL)
                self.click_to(*save_button)
            count += 1
        
        if count == 3:
            assert False, "Не удалось сохранить документ"

        # if "none" not in none_attribute:
        #     try:
        #         self.click_to(*save_button)
        #     except:
        #         pass
        # if self.url_change(url) == True:
        #     pass
        # else:
        #     try:
        #         self.click_to(*save_button)
        #     except:
        #         pass
        #     assert self.url_change(url) == True

    def should_be_correct_error_message(self, error_message):
        err_type = "Не найдена связанная цепочка заявок"
        locator = RegulationDocumentLocators.REGULATION_ERROR_MESSAGE_ID_LOCATOR if error_message == err_type else RegulationDocumentLocators.REGULATION_ERROR_MESSAGE_LOCATOR

        self.is_appeared(*locator)
        text = self.return_text(*locator)
        count = 0

        while text == "":
            self.click_to(*AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR)
            text = self.return_text(*locator)
            if count >= 10:
                assert False

        return text == error_message

    def create_npa_regulation_id(self, index):
        npa_body = datetime.today().strftime("%Y%m%d%H%M%S")
        return f"autotest-{npa_body}-{index}"

    def regulation_npa_id(self, chain_index, save=False):
        PATH = os.path.join(os.path.dirname(os.path.abspath(
            __file__)), "files", "regulation-npa-id.json")
        with open(PATH, "r") as read:
            data = json.load(read)
            chain_index = str(chain_index)

            if save == True:
                data[chain_index] = self.create_npa_regulation_id(chain_index)

                with open(PATH, "w") as write:
                    json.dump(data, write, indent=4)
                return data[chain_index]
            else:
                return data[chain_index]

    def modify_npa_type(self, npa_type, group=2):
        npa = (re.search(r"(\d+)\. (.+)", npa_type)[group])
        return (npa if group == 2 else int(npa))

    def register_and_send_enter_regulation_document(self, *func, answer=False):
        self.click_to_register_pictogram()

        if answer == False:
            self.should_be_required_fields(ENTER_TITLE)
        else:
            self.should_be_required_fields(ENTER_ANSWER_TITLE)

        if len(func) == 4:
            func[0](func[1], func[2], func[3])
                
        self.save_rcd()
    
    def have_answer(self, index):
        answer_type = 0
        answer_types = {
            1: [1, 2, 3],
            2: [7, 8, 10, 11, 12, 13],
            3: [9, 22],
            4: [32]
        }

        for i in answer_types:
            if index in answer_types[i]:
                answer_type = i; break

        return answer_type
    
    def create_and_send_answer(self, index, chain_index, create_id=False):
        answer_type = self.have_answer(index)
        if answer_type != 0:
            self.create_answer(answer_type, create_id, chain_index)
            self.create_and_send_agree_sheet()
            self.register_and_send_enter_regulation_document(answer=True)
            
            self.send_medo()

    def create_answer(self, answer_type, create_id, chain_index):
        self.click_to_answer_pictogram()

        self.should_be_required_fields(SOGL_ANSWER_TITLE)
        self.fill_in_all_document_required_fields(
            "администратор", "суперадмин")

        self.should_be_npa_id_fields(answer_type)
        self.should_be_start_date_fields(answer_type)
        self.should_be_end_date_fields(answer_type)
        self.should_be_add_file_button()

        self.enter_npa_id_fields(
            self.regulation_npa_id(chain_index, create_id), create_id)
        self.fill_field(
            *RegulationAnswerPageLocators.ADD_DOCUMENT_LOCATOR, None)
        self.enter_start_date()
        self.enter_end_date()

        self.save_rcd()

    def fields(self, args, fill=False, edit=False):
        arr_fields = [
            (NPA_TYPE, self.should_be_npa_type_fields, self.select_npa_type_field, FILL_NPA_TYPE, FILL_NPA_TYPE_EDIT),
            (NPA_NAME_1, self.should_be_npa_name_fields, self.enter_npa_name_field, FILL_NPA_NAME_1, FILL_NPA_NAME_1_EDIT),
            (NPA_NAME_2, self.should_be_npa_name_fields, self.enter_npa_name_field, FILL_NPA_NAME_2, FILL_NPA_NAME_2_EDIT),
            (NPA_PROJECT, self.should_be_npa_project_fields, self.enter_npa_project_field, FILL_NPA_PROJECT, FILL_NPA_PROJECT_EDIT),
            (DISCUSS_PERIOD, self.should_be_discuss_period_fields, self.enter_discuss_period_field, FILL_DISCUSS_PERIOD, FILL_DISCUSS_PERIOD_EDIT),
            (EA_TYPE, self.should_be_ea_type_fields, self.enter_new_window_ea_type, FILL_EA_TYPE, FILL_EA_TYPE_EDIT),
            (KEYWORD, self.should_be_keyword_fields, self.enter_keyword_field, FILL_KEYWORD, FILL_KEYWORD_EDIT),
            (NOTIFY_NPA, self.should_be_notify_npa_fields, self.enter_notify_npa_field, FILL_NOTIFY_NPA, FILL_NOTIFY_NPA_EDIT),
            (SUMMARY_INFO, self.should_be_summary_info_fields, self.enter_summary_info_field, FILL_SUMMARY_INFO, FILL_SUMMARY_INFO_EDIT),
            (TOTAL_COMMENT, self.should_be_total_comment_fields, self.enter_total_comment_field, FILL_TOTAL_COMMENT, FILL_TOTAL_COMMENT_EDIT),
            (NUMBER_UNA_COMMENT, self.should_be_number_una_comment_fields, self.enter_number_una_comment_field, FILL_NUMBER_UNA_COMMENT, FILL_NUMBER_UNA_COMMENT_EDIT),
            (NUMBER_COMMENT, self.should_be_number_comment_fields, self.enter_number_comment_field, FILL_NUMBER_COMMENT, FILL_NUMBER_COMMENT_EDIT),
            (NUMBER_PTA_COMMENT, self.should_be_number_pta_comment_fields, self.enter_number_pta_comment_field, FILL_NUMBER_PTA_COMMENT, FILL_NUMBER_PTA_COMMENT_EDIT),
            (DECISION_INFO, self.should_be_decision_info_fields, self.select_decision_info_field, FILL_DECISION_INFO, FILL_DECISION_INFO_EDIT),
            (DECISION_INFO_2, self.should_be_decision_info_fields, self.select_decision_info_field, FILL_DECISION_INFO_2, FILL_DECISION_INFO_2_EDIT),
            (ORG_INFO, self.should_be_org_info_fields, self.enter_org_info_field, False, True),
            (EXPLAIN_NOTE, self.should_be_explain_note_fields, self.enter_explain_note_field, FILL_EXPLAIN_NOTE, FILL_EXPLAIN_NOTE_EDIT),
            (MODIFIED_NPA, self.should_be_modified_npa_fields, self.enter_modified_npa_field, FILL_MODIFIED_NPA, FILL_MODIFIED_NPA_EDIT),
            (AC_EXPERTISE, self.should_be_ac_expertise_fields, self.enter_ac_expertise_field, FILL_AC_EXPERTISE, FILL_AC_EXPERTISE_EDIT),
            (EMAIL_AC_EXPERTISE, self.should_be_email_ac_expertise_fields, self.enter_email_ac_expertise_field, FILL_EMAIL_AC_EXPERTISE, FILL_EMAIL_AC_EXPERTISE_EDIT),
            (MAIL_AC_EXPERTISE, self.should_be_mail_ac_expertise_fields, self.enter_mail_ac_expertise_field, FILL_MAIL_AC_EXPERTISE, FILL_MAIL_AC_EXPERTISE_EDIT),
            (CORRUPTION_FACTOR, self.should_be_corruption_factor_fields, self.select_corruption_factor_field, FILL_CORRUPTION_FACTOR, FILL_CORRUPTION_FACTOR_EDIT),
            (NUMBER_CONCLUSION, self.should_be_number_conclusion_fields, self.enter_number_conclusion_field, FILL_NUMBER_CONCLUSION, FILL_NUMBER_CONCLUSION_EDIT),
            (GC_AC, self.should_be_gc_ac_fields, self.enter_gc_ac_field, FILL_GC_AC, FILL_GC_AC_EDIT),
            (NPA_DRAFT, self.should_be_npa_draft_fields, self.enter_npa_draft_field, FILL_NPA_DRAFT, FILL_NPA_DRAFT_EDIT),
            (APPROVED_NPA, self.should_be_approved_npa_fields, self.enter_approved_npa_field, FILL_APPROVED_NPA, FILL_APPROVED_NPA_EDIT),
            (NPA_NUMBER, self.should_be_npa_number_fields, self.enter_npa_number_field, FILL_NPA_NUMBER, FILL_NPA_NUMBER_EDIT),
            (NPA_ADOPTION_DATE_1, self.should_be_npa_adoption_fields, self.enter_npa_adoption_field, DATE, DATE_EDIT),
            (NPA_ADOPTION_DATE_2, self.should_be_npa_adoption_fields, self.enter_npa_adoption_field, DATE, DATE_EDIT),
            (PD_NPA, self.should_be_pd_npa_fields, self.enter_pd_npa_field, FILL_PD_NPA, FILL_PD_NPA_EDIT),
            (CONSOL_REPORT, self.should_be_consol_report_fields, self.enter_consol_report_field, FILL_CONSOL_REPORT, FILL_CONSOL_REPORT_EDIT),
            (DECISION_PERIOD, self.should_be_decision_period_fields, self.enter_decision_period_field, FILL_DECISION_PERIOD, FILL_DECISION_PERIOD_EDIT),
            (DEGREE_EXPOSURE, self.should_be_degree_exposure_fields, self.select_degree_exposure_field, FILL_DEGREE_EXPOSURE, FILL_DEGREE_EXPOSURE_EDIT),
            (MSR, self.should_be_msr_fields, self.enter_msr_field, FILL_MSR, FILL_MSR_EDIT),
            (EEC, self.should_be_eec_fields, self.enter_eec_field, FILL_EEC, FILL_EEC_EDIT),
            (MDD, self.should_be_mdd_fields, self.enter_mdd_field, FILL_MDD, FILL_MDD_EDIT),
            (ASSESSMENT_REPORT, self.should_be_assessment_report_fields, self.enter_assessment_report_field, FILL_ASSESSMENT_REPORT, FILL_ASSESSMENT_REPORT_EDIT),
            (RR_NPA, self.should_be_rr_npa_fields, self.enter_rr_npa_field, FILL_RR_NPA, FILL_RR_NPA_EDIT),
            (OFFERS_EMAIL, self.should_be_offers_email_fields, self.enter_offers_email_field, DATE, DATE_EDIT),

            (STATE_NUMBER, self.should_be_state_number_fields, self.enter_state_number_field, NON_REQUIRED_FIELD, FILL_STATE_NUMBER_EDIT),
            (REASON_CREATE_NPA, self.should_be_reason_create_npa_fields, self.enter_reason_create_npa_field, NON_REQUIRED_FIELD, FILL_REASON_CREATE_NPA_EDIT),
            (ADD_OFFER_EMAIL, self.should_be_add_offer_email_fields, self.enter_add_offer_email_field, NON_REQUIRED_FIELD, FILL_EMAIL),
            (LINK_ID, self.should_be_link_id_fields, self.enter_link_id_field, NON_REQUIRED_FIELD, FILL_LINK_ID_EDIT),
            (CO_EXECTOR, self.should_be_co_exector_fields, self.enter_new_window_co_exector, NON_REQUIRED_FIELD, FILL_CO_EXECTOR_EDIT),
            (ADDITIONAL_MATERIAL, self.should_be_additional_materials_fields, self.enter_additional_materials_field, NON_REQUIRED_FIELD, FILL_ADDITIONAL_MATERIAL_EDIT),
            (REGULATORY_GILLIOTINE, self.should_be_regulatory_gilliotine_fields, self.activate_regulatory_gilliotine_checkbox, NO_FIELD, FILL_REGULATORY_GILLIOTINE_EDIT),
            (ISSUE_TYPE, self.should_be_issue_type_fields, self.enter_issue_type_field, "", FILL_ISSUE_TYPE_EDIT)
                      ]

        for i in range(len(args)):
            if (RESPONSIBLE_REVIEW_1 == args[i]) or (RESPONSIBLE_REVIEW_2 == args[i]) or (RESPONSIBLE_REVIEW_3 == args[i]):
                if fill == False and edit == False:
                    self.should_be_resp_review_fields(FILL_RESPONSIBLE_REVIEW_NAME, FILL_RESPONSIBLE_REVIEW_PHONE, FILL_RESPONSIBLE_REVIEW_EMAIL, args[i])
                elif fill == False and edit == True:
                    self.should_be_resp_review_fields(FILL_RESPONSIBLE_REVIEW_NAME_EDIT, FILL_RESPONSIBLE_REVIEW_PHONE_EDIT, FILL_RESPONSIBLE_REVIEW_EMAIL_EDIT, args[i])
                elif fill == True and edit == False:
                    self.enter_resp_review_field(FILL_RESPONSIBLE_REVIEW_NAME, FILL_RESPONSIBLE_REVIEW_PHONE, FILL_RESPONSIBLE_REVIEW_EMAIL, args[i])
                elif fill == True and edit == True:
                    self.enter_resp_review_field(FILL_RESPONSIBLE_REVIEW_NAME_EDIT, FILL_RESPONSIBLE_REVIEW_PHONE_EDIT, FILL_RESPONSIBLE_REVIEW_EMAIL_EDIT, args[i])
                continue
            else:
                for q in range(len(arr_fields)):
                    if args[i] == arr_fields[q][0]:
                        L = arr_fields[q]
                        if fill == False:
                            if edit == False:
                                L[1](L[0], L[3]); break
                            else:
                                L[1](L[0], L[4]); break
                        else:
                            if edit == True:
                                L[2](L[0], L[4], edit); break
                            else:
                                L[2](L[0], L[3], edit); break
    
    def main_regulation_fields(self, order, request_type, edit=False, from_rcsi=False):
        if edit == False:
            self.should_be_required_fields(SOGL_TITLE)
            self.fill_in_all_document_required_fields(
                "суперадмин", "администратор")
            if from_rcsi == True:
                self.should_not_be_order_enter_fields(order)
                self.should_not_be_request_type_enter_fields(self.modify_npa_type(request_type))
            else:
                self.should_be_order_fields()
                self.should_be_request_type_fields()
                self.select_order_cm(order)
                self.select_type_request_cm(request_type)
        elif edit == True:
            self.should_not_be_order_enter_fields(order)
            self.should_not_be_request_type_enter_fields(self.modify_npa_type(request_type))
    
    def regulation_delete_all_added_files(self, fields):
        self.delete_all_added_files()

        rr_fields = [RESPONSIBLE_REVIEW_1, RESPONSIBLE_REVIEW_2, RESPONSIBLE_REVIEW_3]
        for i in rr_fields:
            if (i in fields) == True:
                self.click_to_responsible_review_delete_button(); break

    def regulation_index_fields(self, index):
        fields = {
            1: [NOTIFY_NPA, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, DISCUSS_PERIOD, EA_TYPE, KEYWORD, ORG_INFO, REASON_CREATE_NPA, ADD_OFFER_EMAIL, LINK_ID, CO_EXECTOR],
            4: [SUMMARY_INFO, NPA_TYPE, NPA_NAME_1, TOTAL_COMMENT, NUMBER_UNA_COMMENT, NUMBER_COMMENT, NUMBER_PTA_COMMENT, DECISION_INFO],
            7: [NPA_PROJECT, EXPLAIN_NOTE, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, DISCUSS_PERIOD, EA_TYPE, KEYWORD, ORG_INFO, ADDITIONAL_MATERIAL, REGULATORY_GILLIOTINE, REASON_CREATE_NPA, ADD_OFFER_EMAIL, LINK_ID, CO_EXECTOR],
            8: [NPA_PROJECT, EXPLAIN_NOTE, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, DISCUSS_PERIOD, EA_TYPE, KEYWORD, ORG_INFO, AC_EXPERTISE, EMAIL_AC_EXPERTISE, MAIL_AC_EXPERTISE, REGULATORY_GILLIOTINE, REASON_CREATE_NPA, ADD_OFFER_EMAIL, LINK_ID, CO_EXECTOR],
            9: [NPA_PROJECT, PD_NPA, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, AC_EXPERTISE, EMAIL_AC_EXPERTISE, MAIL_AC_EXPERTISE, EA_TYPE, KEYWORD, ORG_INFO, LINK_ID, REASON_CREATE_NPA, CO_EXECTOR],
            10: [NPA_PROJECT, CONSOL_REPORT, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, EA_TYPE, KEYWORD, ORG_INFO, DEGREE_EXPOSURE, ISSUE_TYPE, REASON_CREATE_NPA, ADD_OFFER_EMAIL, LINK_ID, CO_EXECTOR, AC_EXPERTISE, EMAIL_AC_EXPERTISE, MAIL_AC_EXPERTISE, DECISION_PERIOD],
            11: [EEC, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, DECISION_PERIOD, EA_TYPE, KEYWORD, ORG_INFO, ISSUE_TYPE, REASON_CREATE_NPA, ADD_OFFER_EMAIL, LINK_ID, CO_EXECTOR],
            12: [EXPLAIN_NOTE, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_1, NPA_PROJECT, RESPONSIBLE_REVIEW_1, DISCUSS_PERIOD, EA_TYPE, KEYWORD, ORG_INFO, FILL_REASON_CREATE_NPA_EDIT, ADD_OFFER_EMAIL, LINK_ID, CO_EXECTOR],
            13: [NPA_PROJECT, EXPLAIN_NOTE, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, DISCUSS_PERIOD, EA_TYPE, KEYWORD, ORG_INFO, AC_EXPERTISE, EMAIL_AC_EXPERTISE, MAIL_AC_EXPERTISE, REGULATORY_GILLIOTINE, REASON_CREATE_NPA, ADD_OFFER_EMAIL, LINK_ID, CO_EXECTOR],
            14: [SUMMARY_INFO, MODIFIED_NPA, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, TOTAL_COMMENT, NUMBER_UNA_COMMENT, NUMBER_COMMENT, NUMBER_PTA_COMMENT, DECISION_INFO],
            15: [SUMMARY_INFO, MODIFIED_NPA, GC_AC, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, TOTAL_COMMENT, NUMBER_UNA_COMMENT, NUMBER_COMMENT, NUMBER_PTA_COMMENT, DECISION_INFO, CORRUPTION_FACTOR, NUMBER_CONCLUSION],
            16: [SUMMARY_INFO, GC_AC, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, TOTAL_COMMENT, NUMBER_UNA_COMMENT, NUMBER_COMMENT, NUMBER_PTA_COMMENT, CORRUPTION_FACTOR, NUMBER_CONCLUSION],
            17: [SUMMARY_INFO, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, TOTAL_COMMENT, NUMBER_UNA_COMMENT, NUMBER_COMMENT, NUMBER_PTA_COMMENT],
            20: [MODIFIED_NPA, MSR, NPA_TYPE, NPA_NAME_1, DECISION_INFO],
            21: [NPA_TYPE, NPA_NAME_1, DECISION_INFO, MDD],
            22: [NPA_PROJECT, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, AC_EXPERTISE, EMAIL_AC_EXPERTISE, MAIL_AC_EXPERTISE, EA_TYPE, KEYWORD, REGULATORY_GILLIOTINE, LINK_ID, REASON_CREATE_NPA, CO_EXECTOR],
            23: [GC_AC, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_1, CORRUPTION_FACTOR, NUMBER_CONCLUSION, TOTAL_COMMENT, NUMBER_COMMENT, NUMBER_UNA_COMMENT, NUMBER_PTA_COMMENT, DECISION_INFO],
            24: [NPA_DRAFT, NPA_TYPE, NPA_NAME_1, RESPONSIBLE_REVIEW_2, DECISION_INFO_2],
            28: [APPROVED_NPA, NPA_TYPE, NPA_NAME_2, NPA_NUMBER, NPA_ADOPTION_DATE_1, RESPONSIBLE_REVIEW_3, STATE_NUMBER],
            32: [APPROVED_NPA, ASSESSMENT_REPORT, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NAME_2, NPA_NUMBER, NPA_ADOPTION_DATE_2, RESPONSIBLE_REVIEW_1, DISCUSS_PERIOD, OFFERS_EMAIL, EA_TYPE, KEYWORD, LINK_ID, CO_EXECTOR],
            33: [SUMMARY_INFO, ADDITIONAL_MATERIAL, NPA_TYPE, NPA_NUMBER, NPA_NAME_2, NPA_ADOPTION_DATE_2, TOTAL_COMMENT, NUMBER_COMMENT, NUMBER_UNA_COMMENT, NUMBER_PTA_COMMENT],
            34: [NPA_TYPE, NPA_NUMBER, NPA_NAME_2, NPA_ADOPTION_DATE_2, RR_NPA],
        }

        indexes = {
            1: [1, 2, 3],
            4: [4, 5, 6],
            14: [14, 18],
            15: [15, 19],
            24: [24, 25, 26, 27],
            28: [28, 29, 30, 31],
        }

        for i in indexes:
            if index in indexes[i]:
                index = i; break

        return fields[int(index)]

    def check_regulation_doc(self, index, chain_index, first=False, edit=True):
        self.regulation_correct_npa_id_fields(index, chain_index, first, 3)
        self.regulation_correct_notice_npa_not_placed_fields(index, first, (3 if edit == True else 4))

        fields = self.regulation_index_fields(index)
        self.fields(fields, edit=edit)

    def regulation_doc(self, order, request_type, chain_index, edit=False, first=False, from_rcsi=False, error=False):
        if edit == True:
            self.click_to_edit_pictogram()

        edit_bool = True if edit == True else False
        edit_status = (2 if edit == True else 1) if from_rcsi == False else 2

        self.main_regulation_fields(order, request_type, edit_bool, from_rcsi)

        index = self.modify_npa_type(request_type, 1)
        fields = self.regulation_index_fields(index)

        if edit == True:
            self.regulation_delete_all_added_files(fields)
        
        self.regulation_correct_npa_id_fields(index, chain_index, first, edit_status)
        self.regulation_correct_notice_npa_not_placed_fields(index, first, edit_status)

        self.fields(fields, fill=True, edit=edit_bool)
        
        if error == False:
            self.save_regulation_rcd(edit, index)
            self.check_regulation_doc(index, chain_index, first, edit_bool)
        else:
            self.click_to(*AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR)
            assert self.should_be_correct_error_message(error)


class ChangeResponsibleInfo(RegulationDocumentPage):
    # Тип заявки
    def should_be_request_type_35_fields(self, text, field_name):
        self.should_be_correct_field_name(field_name, ChangeResponsibleInfoLocators.REQUEST_TYPE_NAME_35_LOCATOR)
        field_text = self.return_text(*ChangeResponsibleInfoLocators.REQUEST_TYPE_FIELD_VIEW_MODE_35_LOCATOR)
        assert field_text == text
    
    # Наименование проекта НПА (отчета ОФВ)
    def enter_npa_name_35_fields(self, text, field_name):
        self.should_be_correct_field_name(field_name, ChangeResponsibleInfoLocators.NPA_NAME_NAME_FIELD_35_LOCATOR)
        
        self.fill_field(*ChangeResponsibleInfoLocators.NPA_NAME_FIELD_35_LOCATOR, text)
    
    def should_be_npa_name_35_fields(self, text, field_name):
        self.should_be_correct_field_name(ACTUAL_RR_35, ChangeResponsibleInfoLocators.NPA_NAME_NAME_FIELD_35_LOCATOR)

        assert text == self.return_text(
            *ChangeResponsibleInfoLocators.NPA_NAME_VIEW_MODE_35_LOCATOR)
    
    # Текущий ответственный сотрудник
    def should_be_actual_rr_field(self, name):
        assert self.should_be_correct_field_name(name, ChangeResponsibleInfoLocators.CURRENT_RESPONSIBLE_USER_NAME_LOCATOR)

    def should_be_actual_rr_fields(self, name, field_name):
        self.should_be_actual_rr_field(field_name)
        text = self.return_text(*ChangeResponsibleInfoLocators.CURRENT_RESPONSIBLE_USER_VIEW_MODE_LOCATOR)
        assert name in text

    def enter_actual_rr_fields(self, text, field_name):
        self.should_be_actual_rr_field(field_name)
        assert self.is_element_present(*ChangeResponsibleInfoLocators.CURRENT_RESPONSIBLE_USER_FIELD_LOCATOR)
        assert self.is_element_present(*ChangeResponsibleInfoLocators.CURRENT_RESPONSIBLE_USER_NEW_WINDOW_LOCATOR)

        self.click_to(*ChangeResponsibleInfoLocators.CURRENT_RESPONSIBLE_USER_NEW_WINDOW_LOCATOR)
        self.work_with_windows(1)
        self.fill_field(*ChooseUserFromNewWindow.USER_FIND_LOCATOR, text)
        self.click_to(*AllDocumentFieldLocators.find_text_locator(text))
        self.work_with_windows()

    # Новый ответственный сотрудник
    def should_be_new_rr_field(self, name, edit_mode):
        assert self.should_be_correct_field_name(name, ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_NAME_LOCATOR)
        return [FILL_RESPONSIBLE_REVIEW_NAME_EDIT, FILL_RESPONSIBLE_REVIEW_PHONE_EDIT, FILL_RESPONSIBLE_REVIEW_EMAIL_EDIT] if edit_mode == False else [FILL_RESPONSIBLE_REVIEW_NAME, FILL_RESPONSIBLE_REVIEW_PHONE, FILL_RESPONSIBLE_REVIEW_EMAIL]
        
    def should_be_new_rr_fields(self, edit_mode, field_name):
        rr_fill_field = self.should_be_new_rr_field(field_name, edit_mode)
        text = self.return_text(*ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_VIEW_MODE_LOCATOR)
        for i in rr_fill_field:
            assert i in text
    
    def enter_new_rr_fields(self, edit_mode, field_name):
        rr_fill_field = self.should_be_new_rr_field(field_name, edit_mode)
        assert self.is_element_present(*ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_FIELD_LOCATOR)
        assert self.is_element_present(*ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_EMAIL_FIELD_LOCATOR)
        assert self.is_element_present(*ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_PHONE_FIELD_LOCATOR)
        assert self.is_element_present(*ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_NEW_WINDOW_LOCATOR)

        self.click_to(*ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_NEW_WINDOW_LOCATOR)
        self.work_with_windows(1)
        self.fill_field(*ChooseUserFromNewWindow.USER_FIND_LOCATOR, rr_fill_field[0])
        self.click_to(*AllDocumentFieldLocators.find_text_locator(rr_fill_field[0]))
        self.work_with_windows()

        self.fill_field(*ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_PHONE_FIELD_LOCATOR, rr_fill_field[1])
        self.fill_field(*ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_EMAIL_FIELD_LOCATOR, rr_fill_field[2])
    
    def click_to_save_with_error(self, text):
        assert self.is_active(*AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR)
        self.click_to(*AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR)

        self.is_active(*ChangeResponsibleInfoLocators.ERROR_ID_NOT_FOUND)
        error_text = self.return_text(*ChangeResponsibleInfoLocators.ERROR_ID_NOT_FOUND)
        assert error_text == text

    def choose_chain(self):
        chain_index = randint(1, 14)
        chain_open = self.regulation_npa_id(chain_index)

        while chain_open == "":
            chain_index = randint(1, 14)
            chain_open = self.regulation_npa_id(chain_index)

        return chain_index
    
    def main_regulation_35_fields(self, edit=False):
        if edit == False:
            self.should_be_required_fields(SOGL_TITLE)
            self.fill_in_all_document_required_fields(
                "суперадмин", "администратор")
        else:
            self.should_be_correct_title(SOGL_TITLE)
    
    def fields_35(self, fill, edit):
        text = "Заявка на изменение информации о работнике, ответственном за размещение информации на regulation.gov.ru"
        work_with_fields = [
            (REQUEST_TYPE, self.should_be_request_type_35_fields, self.should_be_request_type_35_fields, text, text),
            (NPA_NAME_35, self.should_be_npa_name_35_fields, self.enter_npa_name_35_fields, FILL_NPA_NAME_3, EDIT_NPA_NAME_3),
            (ACTUAL_RR_35, self.should_be_actual_rr_fields, self.enter_actual_rr_fields, FILL_RESPONSIBLE_REVIEW_NAME, FILL_RESPONSIBLE_REVIEW_NAME_EDIT),
            (NEW_RR_35, self.should_be_new_rr_fields, self.enter_new_rr_fields, False, True)
        ]

        for i in work_with_fields:
            if fill == True:
                i[2](i[3 if edit == False else 4], i[0])
            elif fill == False:
                i[1](i[3 if edit == False else 4], i[0])

    def change_responsible_info_doc(self, edit=False, chain_index=None):
        if edit == True:
            self.click_to_edit_pictogram()
            self.click_to(*ChangeResponsibleInfoLocators.CURRENT_RESPONSIBLE_USER_DELETE_BUTTON)
            self.click_to(*ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_DELETE_BUTTON)

        self.main_regulation_35_fields(edit)

        if edit == False:
            self.enter_npa_id_fields("uncorrect-9999999999999999-id", True)
        self.fields_35(fill=True, edit=edit)
        if edit == False:
            self.click_to_save_with_error("Не найдена связанная цепочка заявок")

        if edit == False:
            self.enter_project_npa_id_field(1, False, chain_index)
        else:
            self.should_be_project_npa_id_fields(1, False, True, chain_index)

        self.save_rcd()

        self.fields_35(fill=False, edit=edit)

    def register_and_send_enter_change_info_document(self, chain_index):
        self.click_to_register_pictogram()

        self.should_be_correct_title(ENTER_TITLE)
        self.should_be_project_npa_id_fields(1, False, False, chain_index)
        self.fields_35(fill=False, edit=True)

        self.save_rcd()

        self.send_medo()


class RegulationRefuseDocument(RegulationDocumentPage):
    def create_refuse_document(self, have_answer, doc_link):
        if have_answer == False:
            self.should_not_be_answer_pictogram()
        else:
            self.should_be_answer_pictogram()
        self.should_be_refuse_pictogram()

        url = self.driver.current_url
        self.click_to_refuse_pictogram()
        self.url_change(url)

        self.should_be_required_fields("Согласование внутреннего документа-отказа на заявку Regulation")
        self.fill_in_all_document_required_fields(
            "администратор", "суперадмин")
        
        self.fill_field(*AllDocumentFieldLocators.ADD_FILE_BUTTON_LOCATOR)
        self.should_be_closed_short_content_fields(3)

        # self.is_element_present(*AllDocumentFieldLocators.link_document(MainFunc.create_doc_link("")[1:]))
        self.is_element_present(*AllDocumentFieldLocators.link_document("id=" + doc_link))

        self.save_rcd()

    def register_and_send_refuse_document(self, doc_link, from_rcsi=False):
        self.click_to_register_pictogram()
        self.should_be_required_fields("Внутренний документ-отказ на заявку Regulation")
        self.save_rcd()
        self.send_medo()

        if from_rcsi == False:
            # self.is_element_present(*AllDocumentFieldLocators.link_document(MainFunc.create_doc_link("")[1:]))
            # self.click_to(*AllDocumentFieldLocators.link_document(MainFunc.create_doc_link("")[1:]))

            self.is_element_present(*AllDocumentFieldLocators.link_document("id=" + doc_link))
            self.click_to(*AllDocumentFieldLocators.link_document("id=" + doc_link))

            self.work_with_windows(1)
            self.should_be_correct_title("Внутренний документ-заявка Regulation")
            self.should_not_be_answer_pictogram()
            self.should_not_be_refuse_pictogram()
        

class RegulationChainShowInstrument(RegulationRefuseDocument):
    def click_to_rcsi_repeat(self):
        self.click_to_rcsi_pictogram()
        self.is_element_present(*RegulationDocumentLocators.RCSI_REPEAT_LINK_LOCATOR)
        url = self.driver.current_url
        self.click_to(*RegulationDocumentLocators.RCSI_REPEAT_LINK_LOCATOR)
        self.url_change(url)
    
    def click_to_rcsi_next_doc(self, request_type):
        request_type = self.modify_npa_type(request_type)
        self.click_to_rcsi_pictogram()
        self.is_element_present(*RegulationDocumentLocators.rsci_next_request_link_locator(request_type))
        url = self.driver.current_url
        self.click_to(*RegulationDocumentLocators.rsci_next_request_link_locator(request_type))
        self.url_change(url)

    def check_rcsi_name(self, have_id):
        text = ""
        count = 0

        while text == "" and count < 10:
            self.is_active(*RegulationDocumentLocators.RCSI_NAME_LOCATOR)
            text = self.return_text(*RegulationDocumentLocators.RCSI_NAME_LOCATOR)
            count += 1

        arr = ["Заявки по проекту НПА (отчету ОФВ)"]

        if have_id == True:
            arr += ["ID", self.regulation_npa_id(13)]

        for i in arr:
            assert i in text

    def check_rcsi_status(self, status, next_type):
        self.is_element_present(*RegulationDocumentLocators.RCSI_STATUS_LOCATOR)
        text = self.return_text(*RegulationDocumentLocators.RCSI_STATUS_LOCATOR)
        statuses = {
            1: "Ожидается отправка на согласование документа заявки",
            2: "Ожидается подписание документа заявки",
            3: "Ожидается регистрация документа заявки",
            4: "Ожидается создание ответа",
            5: "Ожидается отправка на согласование документа ответа",
            6: "Ожидается подписание документа ответа",
            7: "Ожидается регистрация документа ответа",
            8: "Создать заявку...",
            9: "Ожидается отправка на согласование документа отказа",
            10: "Ожидается подписание документа отказа",
            11: "Ожидается регистрация документа отказа",
            12: "Разработка проекта НПА завершена",
        }

        elements = [statuses[status]] + next_type

        for i in elements:
            assert i in text
    
    def check_rcsi_number(self, number, name, status):
        if status == 5:
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*RegulationDocumentLocators.RCSI_OPEN_CHAIN_AFTER_REFUSE))

        self.is_element_present(*RegulationDocumentLocators.find_rcsi_elements(number))
        # text = ""

        rcsi_elements = {
            1: [RegulationDocumentLocators.find_rcsi_number, RegulationDocumentLocators.find_rcsi_name, RegulationDocumentLocators.find_rcsi_project, RegulationDocumentLocators.find_rcsi_request, RegulationDocumentLocators.find_rcsi_answer],
            2: [RegulationDocumentLocators.find_rcsi_project, RegulationDocumentLocators.find_rcsi_request, RegulationDocumentLocators.find_rcsi_number, RegulationDocumentLocators.find_rcsi_name],
            3: [RegulationDocumentLocators.find_rcsi_project, RegulationDocumentLocators.find_rcsi_request, RegulationDocumentLocators.find_rcsi_refuse, RegulationDocumentLocators.find_rcsi_number, RegulationDocumentLocators.find_rcsi_name],
            4: [RegulationDocumentLocators.find_rcsi_dots, RegulationDocumentLocators.find_rcsi_project, RegulationDocumentLocators.find_rcsi_request, RegulationDocumentLocators.find_rcsi_number, RegulationDocumentLocators.find_rcsi_name],
            5: [RegulationDocumentLocators.find_rcsi_project, RegulationDocumentLocators.find_rcsi_request, RegulationDocumentLocators.find_rcsi_refuse, RegulationDocumentLocators.find_rcsi_number, RegulationDocumentLocators.find_rcsi_name],
        }

        for i in rcsi_elements[status]:
            # self.is_appeared(*i(number))
            self.is_element_present(*i(number))
            if status == 5 and (i == RegulationDocumentLocators.find_rcsi_project or i == RegulationDocumentLocators.find_rcsi_request):
                assert self.count_all_elements(*i(number)) == 2
            elif i == RegulationDocumentLocators.find_rcsi_name:
                assert self.return_text(*i(number)) == self.modify_npa_type(name)

            # text += self.return_text(*i(number))*self.count_all_elements(*i(number))

        # name = self.modify_npa_type(name)
        # number = str(number)

        # elements = {
        #     1: ["Проект", "Заявка", "Ответ", number, name],
        #     2: ["Проект", "Заявка", number, name],
        #     3: ["Проект", "Заявка", "Отказ", number, name],
        #     4: ["...", "Проект", "Заявка", number, name],
        #     5: ["Проект", "Заявка", "Отказ", "Проект", "Заявка", number, name],
        # }

        # self.correct_text_check(elements[status], text)
    
    def check_rcsi(self, have_id, doc_status, number, name, wait, repeat, num_satus, *next_type):
        if wait == True:
            self.should_be_status_on_agree()

        self.click_to_rcsi_pictogram()

        if repeat == True:
            self.is_element_present(*RegulationDocumentLocators.RCSI_ACTUAL_VERSION_LOCATOR)
        self.check_rcsi_name(have_id)
        self.check_rcsi_status(doc_status, [self.modify_npa_type(next_type[i]) for i in range(len(next_type))])
        self.check_rcsi_number(number, name, num_satus)

        self.click_to_rcsi_pictogram()
    
    def check_rcsi_previous_version(self, version):
        self.click_to_rcsi_pictogram()
        self.is_element_present(*RegulationDocumentLocators.RCSI_ACTUAL_VERSION_LOCATOR)
        self.click_to(*RegulationDocumentLocators.go_to_rcsi_version(version))
        self.is_not_element_present(*RegulationDocumentLocators.RCSI_STATUS_LOCATOR)
        self.click_to_rcsi_pictogram()





