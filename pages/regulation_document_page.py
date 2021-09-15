from .value_for_fields import RegulationFields
from .all_document_fields_page import AllDocumentFieldPage
from .enter_documets_page import EnterDocumentsPage
from .main_page import SoglDocumentsBlock
from .locators import AllDocumentFieldLocators, RegulationDocumentLocators, RegulationEATypeWindow, ChooseOrganisationFromNewWindow, ChooseUserFromNewWindow, RegulationAnswerPageLocators, ChangeResponsibleInfoLocators, OpenDocumentPictagramsLocators
from datetime import datetime
from re import search


class RegulationDocumentPage(AllDocumentFieldPage, SoglDocumentsBlock, EnterDocumentsPage):

    def should_be_correct_field_name(self, correct_name, *locator):
        text = self.return_text(*locator[0])

        return text == correct_name + ":"

    """

    * № постановления

    """

    def should_be_order_field(self):
        assert self.is_element_present(
            *RegulationDocumentLocators.SELECT_ORDER_NAME_LOCATOR), f"Не отображается или не является обязательным поле '{RegulationFields.ORDER_FIELD}'"

    def should_be_order_fields(self):
        self.should_be_order_field()
        assert self.is_element_present(
            *RegulationDocumentLocators.SELECT_ORDER_FIELD_CM_LOCATOR), f"Не отображается селектор поля '{RegulationFields.ORDER_FIELD}'"

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
            *RegulationDocumentLocators.SELECT_REQUEST_TYPE_NAME_LOCATOR), f"Не отображается или не является обязательным поле '{RegulationFields.REQUEST_TYPE}'"

    def should_be_request_type_fields(self):
        self.should_be_request_type_field()
        assert self.is_element_present(
            *RegulationDocumentLocators.SELECT_REQUEST_TYPE_FIELD_LOCATOR), f"Не отображается селектор поля '{RegulationFields.REQUEST_TYPE}'"

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
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.SELECT_NPA_TYPE_NAME_LOCATOR)

    def should_be_npa_type_fields(self, name, text):
        self.should_be_npa_type_field(name)
        assert text == self.return_text(
            *RegulationDocumentLocators.NPA_TYPE_FIELD_VIEW_MODE_LOCATOR)

    def select_npa_type_field(self, name, text):
        self.should_be_npa_type_field(name)

        self.work_with_selector(
            *RegulationDocumentLocators.SELECT_NPA_TYPE_FIELD_LOCATOR, visible_text=str(text))

    """

    * Наименование проекта НПА & Наименование НПА

    """

    def should_be_npa_name_field(self, name):
        if name == RegulationFields.NPA_NAME_1:
            locator = [RegulationDocumentLocators.NPA_NAME_1_FIELD_LOCATOR,
                       RegulationDocumentLocators.NPA_NAME_1_FIELD_VIEW_MODE_LOCATOR]
        elif name == RegulationFields.NPA_NAME_2:
            locator = [RegulationDocumentLocators.NPA_NAME_2_FIELD_LOCATOR,
                       RegulationDocumentLocators.NPA_NAME_2_FIELD_VIEW_MODE_LOCATOR]
        assert self.should_be_correct_field_name(name, locator[0])

        return locator

    def should_be_npa_name_fields(self, field_name, text):
        field = self.should_be_npa_name_field(field_name)
        assert text == self.return_text(*field[1])

    def enter_npa_name_field(self, field_name, text):
        self.should_be_npa_name_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.NPA_NAME_FIELD_LOCATOR, text)

    """

    * Сведения об органах и организациях

    """

    def should_be_org_info_field(self, name, edit):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.ORG_INFO_NAME_LOCATOR)

        if edit == False:
            return [RegulationFields.FILL_ORG_INFO_NAME, RegulationFields.FILL_ORG_INFO_EMAIL]
        else:
            return [RegulationFields.FILL_ORG_INFO_NAME_EDIT, RegulationFields.FILL_ORG_INFO_EMAIL_EDIT]

    def should_be_org_info_fields(self, field_name, edit):
        field = self.should_be_org_info_field(field_name, edit)
        text = self.return_text(
            *RegulationDocumentLocators.ORG_INFO_FIELD_VIEW_MODE_LOCATOR)

        for i in field:
            assert i in text

    def count_org_info_elments(self):
        count = self.count_all_elements(
            *RegulationDocumentLocators.FOR_COUNT_ELEMENTS_IN_ORG_INFO_FIELD_LOCATOR)
        if count == 1:
            assert self.is_not_element_present(
                *RegulationDocumentLocators.LAST_REMOVE_BUTTON_IN_ORG_INFO_LOCATOR)
        else:
            assert self.is_element_present(
                *RegulationDocumentLocators.LAST_REMOVE_BUTTON_IN_ORG_INFO_LOCATOR), f"Нет кнопки удаления в '{RegulationFields.ORG_INFO}'"
        return count

    def org_info_button(self, action: str):
        actions = {
            "del": RegulationDocumentLocators.LAST_REMOVE_BUTTON_IN_ORG_INFO_LOCATOR,
            "add": RegulationDocumentLocators.ADD_NEW_ELEMENT_IN_ORG_INFO_LOCATOR
        }

        initial_elements = self.count_org_info_elments()
        count_org_info_opened = lambda action, elements: elements + 1 if action == "add" else elements - 1

        self.click_to(*actions[action])
        count_org_info = self.count_org_info_elments()

        assert count_org_info == count_org_info_opened(
            action, initial_elements), f"Не добавился новый элемент в поле '{RegulationFields.ORG_INFO}'"

    def enter_org_info_name_field(self, text):
        self.fill_field(
            *RegulationDocumentLocators.ORG_INFO_NAME_FIELD_LOCATOR, text)

    def enter_org_info_email_field(self, text):
        self.fill_field(
            *RegulationDocumentLocators.ORG_INFO_EMAIL_FIELD_LOCATOR, text)

    def enter_org_info_field(self, field_name, edit):
        field = self.should_be_org_info_field(field_name, edit)

        elements = (RegulationDocumentLocators.ORG_INFO_NAME_FIELD_LOCATOR, RegulationDocumentLocators.ORG_INFO_EMAIL_FIELD_LOCATOR,
                    RegulationDocumentLocators.CHOOSE_ORG_FROM_NEW_WINDOW, RegulationDocumentLocators.ADD_NEW_ELEMENT_IN_ORG_INFO_LOCATOR)
        fill_elements = (RegulationDocumentLocators.ORG_INFO_NAME_FIELD_LOCATOR,
                         RegulationDocumentLocators.ORG_INFO_EMAIL_FIELD_LOCATOR)

        for i in elements:
            assert self.is_element_present(*i)
            if i in fill_elements:
                self.fill_field(*i, field[fill_elements.index(i)])

    """

    * Виды экономической деятельности

    """

    def should_be_ea_type_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.EA_TYPE_NAME_LOCATOR)

    def should_be_ea_type_fields(self, name, text):
        self.should_be_ea_type_field(name)

        assert text in self.return_text(
            *RegulationDocumentLocators.EA_TYPE_FIELD_VIEW_MODE_LOCATOR)

    def enter_text_ea_type(self, name, text):
        self.should_be_ea_type_field(name)
        self.fill_field(
            *RegulationDocumentLocators.ENTER_NEW_ELEMENT_IN_EA_TYPE_LOCATOR, text)
        self.click_to(
            *RegulationDocumentLocators.CHOOSE_EA_TYPE_DROP_LIST)

    def enter_new_window_ea_type(self, name, text):
        self.should_be_ea_type_field(name)

        assert self.is_element_present(
            *RegulationDocumentLocators.ENTER_NEW_ELEMENT_IN_EA_TYPE_LOCATOR), f"Не отображается поле '{RegulationFields.EA_TYPE}'"
        assert self.is_element_present(
            *RegulationDocumentLocators.CHOOSE_EA_TYPE_FROM_NEW_WINDOW), f"Нет кнопки 'Выбрать' в '{RegulationFields.EA_TYPE}'"

        self.click_to(
            *RegulationDocumentLocators.CHOOSE_EA_TYPE_FROM_NEW_WINDOW)
        self.work_with_windows(1)
        self.fill_field(*RegulationEATypeWindow.FILTER_LICATOR, text)
        self.click_to(
            *RegulationEATypeWindow.find_element_in_ea_window(text))
        self.click_to(*RegulationEATypeWindow.ADD_BUTTON_LOCATOR)
        self.work_with_windows()

    def delete_ea_type_last_field(self):
        self.click_to(
            *RegulationDocumentLocators.LAST_REMOVE_BUTTON_IN_EA_TYPE_LOCATOR)

    """

    * Ключевые слова

    """

    def should_be_keyword_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.KEYWORD_NAME_LOCATOR)

    def should_be_keyword_fields(self, field_name, text):
        self.should_be_keyword_field(field_name)
        assert text in self.return_text(
            *RegulationDocumentLocators.KEYWORD_FIELD_VIEW_MODE_LOCATOR)

    def enter_keyword_field(self, field_name, text):
        self.should_be_keyword_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.KEYWORD_INPUT_FILELD_LOCATOR, text)

    """

    * Срок обсуждения

    """

    def should_be_discuss_period_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.DISCUSS_PERIOD_NAME_LOCATOR)

    def should_be_discuss_period_fields(self, field_name, text):
        self.should_be_discuss_period_field(field_name)

        assert text in self.return_text(
            *RegulationDocumentLocators.DISCUSS_PERIOD_FIELD_VIEW_MODE_LOCATOR)

    def enter_discuss_period_field(self, field_name, text):
        self.should_be_discuss_period_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.DISCUSS_PERIOD_FIELD_LOCATOR, text)

    """

    * Ответственный за рассмотрение предложений & * Ответственный за направление информации & * Ответственный за направление НПА

    """

    def should_be_resp_review_field(self, edit: bool, name: str) -> list:
        """Проверяет наличие основного поля и возвращает данные для заполнения/проверки, True = Данные без изменений, False = Данные с изменениями."""
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.RESPONSIBLE_REVIEW_NAME_LOCATOR)

        if edit == False:
            return [RegulationFields.FILL_RESPONSIBLE_REVIEW_NAME, RegulationFields.FILL_RESPONSIBLE_REVIEW_PHONE, RegulationFields.FILL_RESPONSIBLE_REVIEW_EMAIL]
        return [RegulationFields.FILL_RESPONSIBLE_REVIEW_NAME_EDIT, RegulationFields.FILL_RESPONSIBLE_REVIEW_PHONE_EDIT, RegulationFields.FILL_RESPONSIBLE_REVIEW_EMAIL_EDIT]

    def should_be_resp_review_fields(self, field_name: str, edit: bool) -> None:
        """Проверяет наличие введеного текта в полученном."""
        values = self.should_be_resp_review_field(edit, field_name)

        text = self.return_text(
            *RegulationDocumentLocators.RESPONSIBLE_REVIEW_FIELD_VIEW_LOCATOR)
        for i in values:
            assert i in text

    def enter_resp_review_field(self, field_name: str, edit: bool) -> None:
        values = self.should_be_resp_review_field(edit, field_name)

        self.enter_responsible_review_from_new_window(values[0])
        self.enter_responsible_review_phone_field(values[1])
        self.enter_responsible_review_email_field(values[2])

    def click_to_responsible_review_delete_button(self):
        self.click_to(
            *RegulationDocumentLocators.RESPONSIBLE_REVIEW_DELETE_BUTTON_LOCATOR)
        if self.is_active(*RegulationDocumentLocators.RESPONSIBLE_REVIEW_DELETE_BUTTON_LOCATOR, timeout=0) == True:
            self.click_to(
                *RegulationDocumentLocators.RESPONSIBLE_REVIEW_DELETE_BUTTON_LOCATOR)

    def enter_responsible_review_from_new_window(self, text):
        fields = [RegulationDocumentLocators.RESPONSIBLE_REVIEW_FIO_FIELD_LOCATOR, RegulationDocumentLocators.RESPONSIBLE_REVIEW_PHONE_FIELD_LOCATOR,
                  RegulationDocumentLocators.RESPONSIBLE_REVIEW_EMAIL_FIELD_LOCATOR, RegulationDocumentLocators.CHOOSE_RESPONSIBLE_REVIEW_FROM_NEW_WINDOW]

        for i in fields:
            assert self.is_element_present(*i)

        self.click_to(*fields[-1])
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

    """

    * Уведомление о подготовке проекта НПА

    """

    def should_be_notify_npa_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.NOTIFY_NPA_NAME_LOCATOR)

    def should_be_notify_npa_fields(self, field_name, text):
        self.should_be_notify_npa_field(field_name)

        field_text = self.return_text(
            *RegulationDocumentLocators.NOTIFY_NPA_FIELD_VIEW_MODE_LOCATOR)
        assert text == field_text

    def enter_notify_npa_field(self, field_name, text):
        self.should_be_notify_npa_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.NOTIFY_NPA_CHOOSE_FILE_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.NOTIFY_NPA_FIELD_LOCATOR, text)

    """

    * Проект НПА

    """

    def should_be_npa_project_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.NPA_PROJECT_NAME_LOCATOR)

    def should_be_npa_project_fields(self, field_name, text):
        self.should_be_npa_project_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.NPA_PROJECT_FIELD_VIEW_MODE_LOCATOR)

    def enter_npa_project_field(self, field_name, text):
        self.should_be_npa_project_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.NPA_PROJECT_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.NPA_PROJECT_FIELD_LOCATOR, text)

    """

    * Пояснительная записка

    """

    def should_be_explain_note_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.EXPLAIN_NOTE_NAME_LOCATOR)

    def should_be_explain_note_fields(self, field_name, text):
        self.should_be_explain_note_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.EXPLAIN_NOTE_FIELD_VIEW_MODE_LOCATOR)

    def enter_explain_note_field(self, field_name, text):
        self.should_be_explain_note_field(field_name)

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
            id_field = self.return_text(
                *RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_VIEW_MODE_LOCATOR)
        elif type == 2:
            id_field = self.return_text(
                *RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_VIEW_MODE_LOCATOR_2)

        if first == True:
            assert RegulationFields.NON_REQUIRED_FIELD == id_field
        else:
            assert index in id_field

    def should_be_project_npa_id_fields(self, type, first, edit_mode, index):
        self.should_be_project_npa_id_field(type)

        if edit_mode == True:
            if first == True:
                assert self.is_element_present(
                    *RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_LOCATOR)
            elif first == False:
                element = self.driver.find_element(
                    *RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_LOCATOR)
                assert element.get_attribute("type") == "hidden"
                
                self.should_be_closed_project_npa_id_field(type, first, index)
        else:
            assert self.is_not_element_present(
                *RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_LOCATOR), f"Поле '{RegulationFields.PROJECT_NPA_ID}' доступно для редактирования"
            self.should_be_closed_project_npa_id_field(type, first, index)

    def enter_project_npa_id_field(self, type, first, npa_id):
        self.should_be_project_npa_id_field(type)
        assert self.is_element_present(
            *RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_LOCATOR)

        if first == False:
            self.fill_field(
                *RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_LOCATOR, npa_id)

    def regulation_correct_npa_id_fields(self, index, npa_id, first, mode):
        mods = {
            1: [True],
            2: [False, True],
            3: [False, False],
        }

        if index not in (1, 2, 3, 32):
            id_type = 2 if index in (33, 34) else 1
            if (mods[mode][0] == True):
                self.enter_project_npa_id_field(id_type, first, npa_id)
            else:
                self.should_be_project_npa_id_fields(
                    id_type, first, mods[mode][1], npa_id)

    """

    * Общее кол-во замечаний

    """

    def count_comment_fields(self, name, fill):
        types = {
            RegulationFields.TOTAL_COMMENT: [(RegulationDocumentLocators.TOTAL_COMMENT_FIELD_VIEW_MODE_LOCATOR, RegulationDocumentLocators.TOTAL_COMMENT_FIELD_2_VIEW_MODE_LOCATOR), (RegulationDocumentLocators.TOTAL_COMMENT_FIELD_LOCATOR, RegulationDocumentLocators.TOTAL_COMMENT_FIELD_2_LOCATOR), RegulationDocumentLocators.TOTAL_COMMENT_NAME_LOCATOR],
            RegulationFields.NUMBER_COMMENT: [(RegulationDocumentLocators.NUMBER_COMMENT_FIELD_VIEW_MODE_LOCATOR, RegulationDocumentLocators.NUMBER_COMMENT_FIELD_2_VIEW_MODE_LOCATOR), (RegulationDocumentLocators.NUMBER_COMMENT_FIELD_LOCATOR, RegulationDocumentLocators.NUMBER_COMMENT_FIELD_2_LOCATOR), RegulationDocumentLocators.NUMBER_COMMENT_NAME_LOCATOR],
            RegulationFields.NUMBER_UNA_COMMENT: [(RegulationDocumentLocators.NUMBER_UNA_COMMENT_FIELD_VIEW_MODE_LOCATOR, RegulationDocumentLocators.NUMBER_UNA_COMMENT_FIELD_2_VIEW_MODE_LOCATOR), (RegulationDocumentLocators.NUMBER_UNA_COMMENT_FIELD_LOCATOR, RegulationDocumentLocators.NUMBER_UNA_COMMENT_FIELD_2_LOCATOR), RegulationDocumentLocators.NUMBER_COMMENT_NAME_LOCATOR],
            RegulationFields.NUMBER_PTA_COMMENT: [(RegulationDocumentLocators.NUMBER_PTA_COMMENT_FIELD_VIEW_MODE_LOCATOR, RegulationDocumentLocators.NUMBER_PTA_COMMENT_FIELD_2_VIEW_MODE_LOCATOR), (RegulationDocumentLocators.NUMBER_PTA_COMMENT_FIELD_LOCATOR, RegulationDocumentLocators.NUMBER_PTA_COMMENT_FIELD_2_LOCATOR), RegulationDocumentLocators.NUMBER_PTA_COMMENT_NAME_LOCATOR],
        }

        L = types[name]
        elements = self.count_all_elements(*L[2])
        arr_elements = [L[0], L[1]]
        fill = 0 if fill == False else 1

        if elements == 1:
            return [arr_elements[fill][0]]
        elif elements == 2:
            return arr_elements[fill]

    def should_be_total_comment_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.TOTAL_COMMENT_NAME_LOCATOR)

    def should_be_total_comment_fields(self, name, text):
        self.should_be_total_comment_field(name)

        for i in self.count_comment_fields(name, False):
            assert str(text) == self.return_text(*i)

    def enter_total_comment_field(self, name, text):
        self.should_be_total_comment_field(name)

        for i in self.count_comment_fields(name, True):
            self.fill_field(*i, text)

    """

    * Кол-во учтенных замечаний

    """

    def should_be_number_comment_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.NUMBER_COMMENT_NAME_LOCATOR)

    def should_be_number_comment_fields(self, name, text):
        self.should_be_number_comment_field(name)

        for i in self.count_comment_fields(name, False):
            assert str(text) == self.return_text(*i)

    def enter_number_comment_field(self, name, text):
        self.should_be_number_comment_field(name)

        for i in self.count_comment_fields(name, True):
            self.fill_field(*i, text)

    """

    * Кол-во неучтенных замечаний

    """

    def should_be_number_una_comment_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.NUMBER_UNA_COMMENT_NAME_LOCATOR)

    def should_be_number_una_comment_fields(self, name, text):
        self.should_be_number_una_comment_field(name)

        for i in self.count_comment_fields(name, False):
            assert str(text) == self.return_text(*i)

    def enter_number_una_comment_field(self, name, text):
        self.should_be_number_una_comment_field(name)

        for i in self.count_comment_fields(name, True):
            self.fill_field(*i, text)

    """

    * Кол-во частично учтенных замечаний

    """

    def should_be_number_pta_comment_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.NUMBER_PTA_COMMENT_NAME_LOCATOR)

    def should_be_number_pta_comment_fields(self, name, text):
        self.should_be_number_pta_comment_field(name)

        for i in self.count_comment_fields(name, False):
            assert str(text) == self.return_text(*i)

    def enter_number_pta_comment_field(self, name, text):
        self.should_be_number_pta_comment_field(name)

        for i in self.count_comment_fields(name, True):
            self.fill_field(*i, text)

    """

    * Информация о принятом решении & * Принятое решение по проекту НПА

    """

    def decision_info_type(self, name, text):
        if name == RegulationFields.DECISION_INFO:
            elements = [RegulationDocumentLocators.DECISION_INFO_NAME_LOCATOR, RegulationDocumentLocators.DECISION_INFO_SELECT_LOCATOR,
                        RegulationDocumentLocators.DECISION_INFO_FIELD_VIEW_MODE_LOCATOR]

            if text != RegulationFields.FILL_DECISION_INFO:
                for i in (RegulationFields.FILL_DECISION_INFO_EDIT, RegulationFields.FILL_DECISION_INFO_3_EDIT):
                    if self.count_all_elements(*AllDocumentFieldLocators.find_text_locator(i)) > 0:
                        return elements + [i]
            return elements + [RegulationFields.FILL_DECISION_INFO]
        elif name == RegulationFields.DECISION_INFO_2:
            elements = [RegulationDocumentLocators.DECISION_INFO_2_NAME_LOCATOR, RegulationDocumentLocators.DECISION_INFO_2_SELECT_LOCATOR,
                        RegulationDocumentLocators.DECISION_INFO_2_FIELD_VIEW_MODE_LOCATOR]

            if text != RegulationFields.FILL_DECISION_INFO_2:
                return elements + [RegulationFields.FILL_DECISION_INFO_2_EDIT]
            return elements + [RegulationFields.FILL_DECISION_INFO_2]

    def should_be_decision_info_field(self, name, text):
        decision_type = self.decision_info_type(name, text)

        assert self.should_be_correct_field_name(name, decision_type[0])
        return decision_type

    def should_be_decision_info_fields(self, field_name, text):
        dec_type = self.should_be_decision_info_field(field_name, text)
        field_text = self.return_text(*dec_type[2])

        assert dec_type[-1] == field_text

    def select_decision_info_field(self, field_name, text):
        dec_type = self.should_be_decision_info_field(field_name, text)

        self.work_with_selector(*dec_type[1], visible_text=str(dec_type[-1]))

    """

    * Сводка предложений

    """

    def should_be_summary_info_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.SUMMARY_INFO_NAME_LOCATOR)

    def should_be_summary_info_fields(self, field_name, text):
        self.should_be_summary_info_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.SUMMARY_INFO_FIELD_VIEW_MODE_LOCATOR)

    def enter_summary_info_field(self, field_name, text):
        self.should_be_summary_info_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.SUMMARY_INFO_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.SUMMARY_INFO_FIELD_LOCATOR, text)

    """

    * Доработанный проект НПА

    """

    def should_be_modified_npa_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.MODIFIED_NPA_NAME_LOCATOR)

    def should_be_modified_npa_fields(self, field_name, text):
        self.should_be_modified_npa_field(field_name)
        
        assert text == self.return_text(
            *RegulationDocumentLocators.MODIFIED_NPA_FIELD_VIEW_MODE_LOCATOR)

    def enter_modified_npa_field(self, field_name, text):
        self.should_be_modified_npa_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.MODIFIED_NPA_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.MODIFIED_NPA_FIELD_LOCATOR, text)

    """

    * Прием заключений антикоррупционной экспертизы

    """

    def should_be_ac_expertise_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.AC_EXPERTISE_NAME_LOCATOR)

    def should_be_ac_expertise_fields(self, field_name, text):
        self.should_be_ac_expertise_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.AC_EXPERTISE_FIELD_VIEW_MODE_LOCATOR)

    def enter_ac_expertise_field(self, field_name, text):
        self.should_be_ac_expertise_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.AC_EXPERTISE_FIELD_LOCATOR, text)

    """

    * E-mail для заключений антикоррупционной экспертизы

    """

    def should_be_email_ac_expertise_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.EMAIL_AC_EXPERTISE_NAME_LOCATOR)

    def should_be_email_ac_expertise_fields(self, field_name, text):
        self.should_be_email_ac_expertise_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.EMAIL_AC_EXPERTISE_FIELD_VIEW_MODE_LOCATOR)

    def enter_email_ac_expertise_field(self, field_name, text):
        self.should_be_email_ac_expertise_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.EMAIL_AC_EXPERTISE_FIELD_LOCATOR, text)

    """

    * Почта для заключений антикоррупционной экспертизы

    """

    def should_be_mail_ac_expertise_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.MAIL_AC_EXPERTISE_NAME_LOCATOR)

    def should_be_mail_ac_expertise_fields(self, field_name, text):
        self.should_be_mail_ac_expertise_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.MAIL_AC_EXPERTISE_FIELD_VIEW_MODE_LOCATOR)

    def enter_mail_ac_expertise_field(self, field_name, text):
        self.should_be_mail_ac_expertise_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.MAIL_AC_EXPERTISE_FIELD_LOCATOR, text)

    """

    * Коррупциогенные факторы

    """

    def should_be_corruption_factor_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.CORRUPTION_FACTOR_NAME_LOCATOR)

    def should_be_corruption_factor_fields(self, field_name, text):
        self.should_be_corruption_factor_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.CORRUPTION_FACTOR_FIELD_VIEW_MODE_LOCATOR)

    def select_corruption_factor_field(self, field_name, text):
        self.should_be_corruption_factor_field(field_name)

        self.work_with_selector(
            *RegulationDocumentLocators.CORRUPTION_FACTOR_FIELD_LOCATOR, visible_text=text)

    """

    * Кол-во заключений

    """

    def should_be_number_conclusion_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.NUMBER_CONCLUSION_NAME_LOCATOR)

    def should_be_number_conclusion_fields(self, field_name, text):
        self.should_be_number_conclusion_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.NUMBER_CONCLUSION_FIELD_VIEW_MODE_LOCATOR)

    def enter_number_conclusion_field(self, field_name, text):
        self.should_be_number_conclusion_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.NUMBER_CONCLUSION_FIELD_LOCATOR, text)

    """

    * Общее заключение по итогам антикоррупционной экспертизы

    """

    def should_be_gc_ac_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.GC_AC_NAME_LOCATOR)

    def should_be_gc_ac_fields(self, field_name, text):
        self.should_be_gc_ac_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.GC_AC_FIELD_VIEW_MODE_LOCATOR)

    def enter_gc_ac_field(self, field_name, text):
        self.should_be_gc_ac_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.GC_AC_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.GC_AC_FIELD_LOCATOR, text)

    """

    * Нормативный правовой акт (проект)

    """

    def should_be_npa_draft_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.NPA_DRAFT_NAME_LOCATOR)

    def should_be_npa_draft_fields(self, field_name, text):
        self.should_be_npa_draft_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.NPA_DRAFT_FIELD_VIEW_MODE_LOCATOR)

    def enter_npa_draft_field(self, field_name, text):
        self.should_be_npa_draft_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.NPA_DRAFT_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.NPA_DRAFT_FIELD_LOCATOR, text)

    """

    * Номер принятого НПА & Номер НПА

    """

    def should_be_npa_number_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.NPA_NUMBER_NAME_LOCATOR)

    def should_be_npa_number_fields(self, field_name, text):
        self.should_be_npa_number_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.NPA_NUMBER_FIELD_VIEW_MODE_LOCATOR)

    def enter_npa_number_field(self, field_name, text):
        self.should_be_npa_number_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.NPA_NUMBER_FIELD_LOCATOR, text)

    """

    * Утвержденный НПА

    """

    def should_be_approved_npa_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.APPROVED_NPA_NAME_LOCATOR)

    def should_be_approved_npa_fields(self, field_name, text):
        self.should_be_approved_npa_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.APPROVED_NPA_FIELD_VIEW_MODE_LOCATOR)

    def enter_approved_npa_field(self, field_name, text):
        self.should_be_approved_npa_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.APPROVED_NPA_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.APPROVED_NPA_FIELD_LOCATOR, text)

    """

    * Дата принятия НПА & Дата НПА

    """

    def should_be_npa_adoption_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.NPA_ADOPTION_NAME_LOCATOR)

        types = {
            RegulationFields.NPA_ADOPTION_DATE_1: RegulationDocumentLocators.NPA_ADOPTION_FIELD_LOCATOR,
            RegulationFields.NPA_ADOPTION_DATE_2: RegulationDocumentLocators.NPA_DATE_FIELD_LOCATOR
        }

        return types[name]

    def should_be_npa_adoption_fields(self, field_name, text):
        self.should_be_npa_adoption_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.NPA_ADOPTION_FIELD_VIEW_MODE_LOCATOR)

    def enter_npa_adoption_field(self, field_name, text):
        field = self.should_be_npa_adoption_field(field_name)

        self.fill_field(*field, text)

    """

    * Обоснование отказа от общественного обсуждения проекта НПА

    """

    def should_be_pd_npa_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.PD_NPA_NAME_LOCATOR)

    def should_be_pd_npa_fields(self, field_name, text):
        self.should_be_pd_npa_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.PD_NPA_FIELD_VIEW_MODE_LOCATOR)

    def enter_pd_npa_field(self, field_name, text):
        self.should_be_pd_npa_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.PD_NPA_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.PD_NPA_FIELD_LOCATOR, text)

    """

    * Сводный отчет

    """

    def should_be_consol_report_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.CONSOL_REPORT_NAME_LOCATOR)

    def should_be_consol_report_fields(self, field_name, text):
        self.should_be_consol_report_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.CONSOL_REPORT_FIELD_VIEW_MODE_LOCATOR)

    def enter_consol_report_field(self, field_name, text):
        self.should_be_consol_report_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.CONSOL_REPORT_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.CONSOL_REPORT_FIELD_LOCATOR, text)

    """

    * Срок принятия предложений

    """

    def should_be_decision_period_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.DECISION_PERIOD_NAME_LOCATOR)

    def should_be_decision_period_fields(self, field_name, text):
        self.should_be_decision_period_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.DECISION_PERIOD_FIELD_VIEW_MODE_LOCATOR)

    def enter_decision_period_field(self, field_name, text):
        self.should_be_decision_period_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.DECISION_PERIOD_FIELD_LOCATOR, text)

    """

    * Степень воздействия

    """

    def should_be_degree_exposure_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.DEGREE_EXPOSURE_NAME_LOCATOR)

    def should_be_degree_exposure_fields(self, field_name, text):
        self.should_be_degree_exposure_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.DEGREE_EXPOSURE_FIELD_VIEW_MODE_LOCATOR)

    def select_degree_exposure_field(self, field_name, text):
        self.should_be_degree_exposure_field(field_name)

        self.work_with_selector(
            *RegulationDocumentLocators.DEGREE_EXPOSURE_FIELD_LOCATOR, visible_text=str(text))

    """

    * Краткое содержание

    """

    def should_be_closed_short_content_fields(self, field_type=1):
        field = {
            1: RegulationFields.SHORT_CONTENT_TEXT,
            2: RegulationFields.SHORT_CONTENT_ANSWER_TEXT,
            3: RegulationFields.SHORT_CONTENT_REFUSE_TEXT,
        }

        assert self.is_element_present(
            *RegulationDocumentLocators.SHORT_CONTENT_NAME_LOCATOR), f"Не отображается или не является обязательным поле '{RegulationFields.SHORT_CONTENT}'"
        assert self.is_element_present(
            *RegulationDocumentLocators.SHORT_CONTENT_FIELD_LOCATOR), f"Не отображается или доступно для редактирования поле '{RegulationFields.SHORT_CONTENT}'"

        short_content_field = self.return_text(
            *RegulationDocumentLocators.SHORT_CONTENT_FIELD_LOCATOR)

        assert short_content_field == field[
            field_type], f"Поле '{RegulationFields.SHORT_CONTENT}' должно быть заполнено тектом {field[field_type]}"

    """

    * Доработанный сводный отчет

    """

    def should_be_msr_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.MSR_NAME_LOCATOR)

    def should_be_msr_fields(self, field_name, text):
        self.should_be_msr_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.MSR_FIELD_VIEW_MODE_LOCATOR)

    def enter_msr_field(self, field_name, text):
        self.should_be_msr_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.MSR_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.MSR_FIELD_LOCATOR, text)

    """

    * Проект решения ЕЭК

    """

    def should_be_eec_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.EEC_NAME_LOCATOR)

    def should_be_eec_fields(self, field_name, text):
        self.should_be_eec_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.EEC_FIELD_VIEW_MODE_LOCATOR)

    def enter_eec_field(self, field_name, text):
        self.should_be_eec_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.EEC_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.EEC_FIELD_LOCATOR, text)

    """

    * Доработанный проект решения ЕЭК

    """

    def should_be_mdd_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.MDD_NAME_LOCATOR)

    def should_be_mdd_fields(self, field_name, text):
        self.should_be_mdd_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.MDD_FIELD_VIEW_MODE_LOCATOR)

    def enter_mdd_field(self, field_name, text):
        self.should_be_mdd_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.MDD_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.MDD_FIELD_LOCATOR, text)

    """

    * Отчет об оценке фактического воздействия НПА

    """

    def should_be_assessment_report_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.ASSESSMENT_REPORT_NAME_LOCATOR)

    def should_be_assessment_report_fields(self, field_name, text):
        self.should_be_assessment_report_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.ASSESSMENT_REPORT_FIELD_VIEW_MODE_LOCATOR)

    def enter_assessment_report_field(self, field_name, text):
        self.should_be_assessment_report_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.ASSESSMENT_REPORT_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(
            *RegulationDocumentLocators.ASSESSMENT_REPORT_FIELD_LOCATOR, text)

    """

    * Доработанный отчет об оценке фактического воздействия НПА

    """

    def should_be_rr_npa_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.RR_NPA_NAME_LOCATOR)

    def should_be_rr_npa_fields(self, field_name, text):
        self.should_be_rr_npa_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.RR_NPA_FIELD_VIEW_MODE_LOCATOR)

    def enter_rr_npa_field(self, field_name, text):
        self.should_be_rr_npa_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.RR_NPA_ADD_FILE_BUTTON_LOCATOR)
        self.fill_field(*RegulationDocumentLocators.RR_NPA_FIELD_LOCATOR, text)

    """

    * Е-mail для предложений

    """

    def should_be_offers_email_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.OFFERS_EMAIL_NAME_LOCATOR)

    def should_be_offers_email_fields(self, field_name, text):
        self.should_be_offers_email_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.OFFERS_EMAIL_FIELD_VIEW_MODE_LOCATOR)

    def enter_offers_email_field(self, field_name, text):
        self.should_be_offers_email_field(field_name)

        self.fill_field(
            *RegulationDocumentLocators.OFFERS_EMAIL_FIELD_LOCATOR, text)

    """

    Органы гос. власти – соисполнители

    """

    def should_be_co_exector_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.CO_EXECTOR_NAME_LOCATOR)

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

    def enter_new_window_co_exector(self, field_name, text):
        self.should_be_co_exector_field(field_name)

        for i in (RegulationDocumentLocators.CO_EXECTOR_FIELD_LOCATOR, RegulationDocumentLocators.CHOOSE_CO_EXECTOR_FROM_NEW_WINDOW):
            assert self.is_element_present(*i)

        if text != RegulationFields.NON_REQUIRED_FIELD:
            count_elements = self.count_co_exector_elements()
            self.click_to(
                *RegulationDocumentLocators.CHOOSE_CO_EXECTOR_FROM_NEW_WINDOW)
            self.work_with_windows(1)
            self.fill_field(
                *ChooseOrganisationFromNewWindow.ORG_FIND_LOCATOR, text)
            self.click_to(*ChooseOrganisationFromNewWindow.FIND_BUTTON_LOCATOR)
            self.click_to(*AllDocumentFieldLocators.find_text_locator(text))
            self.work_with_windows()

            assert self.count_co_exector_elements() == count_elements+1

    """

    Доп. e-mail для предложений

    """

    def should_be_add_offer_email_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.ADD_OFFER_EMAIL_NAME_LOCATOR)

    def should_be_add_offer_email_fields(self, field_name, text):
        self.should_be_add_offer_email_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.ADD_OFFER_EMAIL_FIELD_VIEW_MODE_LOCATOR)

    def enter_add_offer_email_field(self, field_name, text):
        self.should_be_add_offer_email_field(field_name)
        assert self.is_element_present(
            *RegulationDocumentLocators.ADD_OFFER_EMAIL_FIELD_LOCATOR), f"Не отображается поле '{RegulationFields.ADD_OFFER_EMAIL}'"

        if text != RegulationFields.NON_REQUIRED_FIELD:
            self.fill_field(
                *RegulationDocumentLocators.ADD_OFFER_EMAIL_FIELD_LOCATOR, text)

    """

    Основание для разработки НПА

    """

    def should_be_reason_create_npa_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.REASON_CREATE_NPA_NAME_LOCATOR)

    def should_be_reason_create_npa_fields(self, field_name, text):
        self.should_be_reason_create_npa_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.REASON_CREATE_NPA_FIELD_VIEW_MODE_LOCATOR)

    def enter_reason_create_npa_field(self, field_name, text):
        self.should_be_reason_create_npa_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.REASON_CREATE_NPA_FIELD_LOCATOR), f"Не отображается поле '{RegulationFields.REASON_CREATE_NPA}'"

        if text != RegulationFields.NON_REQUIRED_FIELD:
            self.fill_field(
                *RegulationDocumentLocators.REASON_CREATE_NPA_FIELD_LOCATOR, text)

    """

    ID связанных НПА

    """

    def should_be_link_id_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.NPA_LINK_ID_NAME_LOCATOR)

    def should_be_link_id_fields(self, field_name, text):
        self.should_be_link_id_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.NPA_LINK_ID_FIELD_VIEW_MODE_LOCATOR)

    def enter_link_id_field(self, field_name, text):
        self.should_be_link_id_field(field_name)

        assert self.is_element_present(
            *RegulationDocumentLocators.NPA_LINK_ID_FIELD_LOCATOR), f"Не отображается поле '{RegulationFields.LINK_ID}'"

        if text != RegulationFields.NON_REQUIRED_FIELD:
            self.fill_field(
                *RegulationDocumentLocators.NPA_LINK_ID_FIELD_LOCATOR, text)

    """

    Дополнительные материалы

    """

    def should_be_additional_materials_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.ADDITIONAL_MATERIALS_NAME_LOCATOR)

    def should_be_additional_materials_fields(self, field_name, text):
        self.should_be_additional_materials_field(field_name)

        assert text in self.return_text(
            *RegulationDocumentLocators.ADDITIONAL_MATERIALS_FIELD_VIEW_MODE_LOCATOR)

    def count_additonal_material_elments(self):
        return self.count_all_elements(*RegulationDocumentLocators.FOR_COUNT_ELEMENTS_IN_ADDITIONAL_MATERIALS_FIELD_CEM_LOCATOR)

    def click_to_additonal_material_add_button(self):
        additional_material_count_opened = self.count_additonal_material_elments()
        self.click_to(
            *RegulationDocumentLocators.ADDITIONAL_MATERIALS_ADD_BUTTON_LOCATOR)

        assert self.count_additonal_material_elments(
        ) == additional_material_count_opened + 1

    def click_to_additonal_material_delete_button(self):
        additional_material_count = self.count_additonal_material_elments()
        self.click_to(
            *RegulationDocumentLocators.REMOVE_LAST_ELEMENT_IN_ADDITIONAL_MATERIALS_LOCATOR)
        
        assert self.count_additonal_material_elments() == additional_material_count - 1

    def enter_additional_materials_field(self, field_name, text):
        self.should_be_additional_materials_field(field_name)
        
        assert self.is_element_present(
            *RegulationDocumentLocators.ADDITIONAL_MATERIALS_ADD_BUTTON_LOCATOR), f"Не отображается кнопка '{RegulationFields.ADDITIONAL_MATERIAL}'"

        if text != RegulationFields.NON_REQUIRED_FIELD:
            self.click_to_additonal_material_add_button()
            self.fill_field(
                *RegulationDocumentLocators.ADD_FILE_LAST_ELEMENT_IN_ADDITIONAL_MATERIALS_LOCATOR)
            self.fill_field(
                *RegulationDocumentLocators.ENTER_LAST_ELEMENT_IN_ADDITIONAL_MATERIALS_LOCATOR, text)

    """

    Регуляторная гильотина

    """

    def should_be_regulatory_gilliotine_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.REGULATORY_GILLIOTINE_NAME_LOCATOR)

    def should_be_regulatory_gilliotine_fields(self, field_name, text):
        self.should_be_regulatory_gilliotine_field(field_name)
        
        assert text == self.return_text(
            *RegulationDocumentLocators.REGULATORY_GILLIOTINE_FIELD_VIEW_MODE_LOCATOR)

    def activate_regulatory_gilliotine_checkbox(self, field_name, edit):
        self.should_be_regulatory_gilliotine_field(field_name)
        
        assert self.is_element_present(
            *RegulationDocumentLocators.REGULATORY_GILLIOTINE_CHECKBOX_LOCATOR)

        if edit != RegulationFields.NO_FIELD:
            self.click_to(
                *RegulationDocumentLocators.REGULATORY_GILLIOTINE_CHECKBOX_LOCATOR)

    """

    Уведомление о подготовке НПА не размещается

    """

    def should_be_notice_npa_not_placed_field(self, name, edit):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.NOTICE_NPA_NOT_PLACED_NAME_LOCATOR)

        types = {
            None: [RegulationFields.NO_FIELD],
            False: [RegulationFields.FILL_NOTICE_NPA_NAME, RegulationFields.DATE],
            True: [RegulationFields.FILL_NOTICE_NPA_NAME_EDIT, RegulationFields.DATE_EDIT]
        }

        return types[edit]

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
                self.click_to(
                    *RegulationDocumentLocators.NOTICE_NPA_NOT_PLACED_CHECKBOX_LOCATOR)
            else:
                self.click_to(
                    *RegulationDocumentLocators.NOTICE_NPA_NOT_PLASED_DELETE_BUTTON_LOCATOR)
            self.click_to(
                *RegulationDocumentLocators.NOTICE_NPA_NOT_PLACED_NEW_WINDOW_LOCATOR)
            self.work_with_windows(1)
            self.fill_field(
                *ChooseUserFromNewWindow.USER_FIND_LOCATOR, field[0])
            self.click_to(
                *AllDocumentFieldLocators.find_text_locator(field[0]))
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

        L = self.enter_notice_npa_not_placed_field if mods[mode][
            0] == True else self.should_be_notice_npa_not_placed_fields

        if index in [7, 8, 10, 12, 13]:
            L(RegulationFields.NOTICE_NPA_NOT_PLACED, mods[mode][1]) if first == True else L(
                RegulationFields.NOTICE_NPA_NOT_PLACED, None)

    """

    Номер государственной регистрации НПА

    """

    def should_be_state_number_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.STATE_NUMBER_NAME_LOCATOR)

    def should_be_state_number_fields(self, field_name, text):
        self.should_be_state_number_field(field_name)

        assert text == self.return_text(
            *RegulationDocumentLocators.STATE_NUMBER_FIELD_VIEW_MODE_LOCATOR)

    def enter_state_number_field(self, field_name, text):
        self.should_be_state_number_field(field_name)
        
        assert self.is_element_present(
            *RegulationDocumentLocators.STATE_NUMBER_FIELD_LOCATOR)

        if text != RegulationFields.NON_REQUIRED_FIELD:
            self.fill_field(
                *RegulationDocumentLocators.STATE_NUMBER_FIELD_LOCATOR, text)

    """

    Тип затрагиваемых вопросов

    """

    def should_be_issue_type_field(self, name):
        assert self.should_be_correct_field_name(
            name, RegulationDocumentLocators.ISSUE_TYPE_NAME_LOCATOR)

        for i in (RegulationDocumentLocators.ISSUE_TYPE_FIELD_LOCATOR, RegulationDocumentLocators.ISSUE_TYPE_FIELD_2_LOCATOR):
            if self.count_all_elements(*i) != 0:
                return i

    def should_be_issue_type_fields(self, field_name, text):
        self.should_be_issue_type_field(field_name)

        field_text = self.return_text(
            *RegulationDocumentLocators.ISSUE_TYPE_FIELD_VIEW_MODE_LOCATOR)
        field_text = (text == field_text) or (
            field_text == RegulationFields.NON_REQUIRED_FIELD)
        
        assert field_text

    def enter_issue_type_field(self, field_name, text):
        field = self.should_be_issue_type_field(field_name)
        
        assert self.is_element_present(*field)

        if text != "":
            self.work_with_selector(*field, visible_text=text)

    """

    Сообщение о повтороной Заявке

    """

    def should_be_repeat_message(self):
        assert self.is_element_present(
            *RegulationDocumentLocators.REPEAT_MESSAGE_LOCATOR)
        text_in_message = self.return_text(
            *RegulationDocumentLocators.REPEAT_MESSAGE_LOCATOR)

        assert text_in_message == "Обращаем внимание!\nДанный НПА размещается повторно."

    """

    Ответ

    """

    # * ID проекта НПА
    def should_be_npa_id_fields(self, type=1):
        if type == 4:
            locator = RegulationAnswerPageLocators.NPA_ID_NAME_LOCATOR_2
        else:
            locator = RegulationAnswerPageLocators.NPA_ID_NAME_LOCATOR

        assert self.is_element_present(*locator)

    def enter_npa_id_fields(self, id, create=False):
        if create == True:
            self.fill_field(
                *RegulationAnswerPageLocators.NPA_ID_FIELD_LOCATOR, str(id))
        else:
            self.driver.find_element(
                *AllDocumentFieldLocators.find_text_locator(id))

    # * Дата начала обсуждения уведомления
    def should_be_start_date_name_field(self):
        assert self.is_element_present(
            *RegulationAnswerPageLocators.DATE_START_NAME_LOCATOR)

    def should_be_start_date_fields(self, a_type: int):
        self.should_be_start_date_name_field()
        
        assert self.is_element_present(
            *RegulationAnswerPageLocators.DATE_START_FIELD_LOCATOR)

        text = self.return_text(
            *RegulationAnswerPageLocators.DATE_START_NAME_LOCATOR)

        types = {
            1: RegulationFields.ANSWER_START_1,
            2: RegulationFields.ANSWER_START_2,
            3: RegulationFields.ANSWER_START_3,
            4: RegulationFields.ANSWER_START_4,
        }

        assert types.get(a_type) in text

    def enter_start_date(self):
        self.fill_field(
            *RegulationAnswerPageLocators.DATE_START_FIELD_LOCATOR, self.date_return())

    # * Дата окончания обсуждения уведомления
    def should_be_end_date_name_field(self):
        assert self.is_element_present(
            *RegulationAnswerPageLocators.DATE_END_NAME_LOCATOR)

    def should_be_end_date_fields(self, a_type):
        self.should_be_start_date_name_field()
        
        assert self.is_element_present(
            *RegulationAnswerPageLocators.DATE_END_FIELD_LOCATOR)

        text = self.return_text(
            *RegulationAnswerPageLocators.DATE_END_NAME_LOCATOR)

        types = {
            1: RegulationFields.ANSWER_END_1,
            2: RegulationFields.ANSWER_END_2,
            3: RegulationFields.ANSWER_END_3,
            4: RegulationFields.ANSWER_END_4,
        }

        assert types[a_type] in text

    def enter_end_date(self):
        self.fill_field(
            *RegulationAnswerPageLocators.DATE_END_FIELD_LOCATOR, self.date_return())

    # Добавить файлы
    def should_be_add_file_button(self):
        assert self.is_element_present(
            *RegulationAnswerPageLocators.ADD_DOCUMENT_LOCATOR)

    """

    Остальное связанное с Regulation

    """

    def save_regulation_rcd(self, edit, index):
        def if_rcd_not_saved():
            if int(index) not in (4, 5, 6, 20, 21, 28, 33, 34):
                if self.is_not_element_present(*RegulationDocumentLocators.REGULATION_ERROR_MESSAGE_PHONE_EMAIL_LOCATOR, timeout=5) == False:
                    self.enter_responsible_review_phone_field(
                        RegulationFields.FILL_RESPONSIBLE_REVIEW_PHONE_EDIT if edit == True else RegulationFields.FILL_RESPONSIBLE_REVIEW_PHONE)
                    self.enter_responsible_review_email_field(
                        RegulationFields.FILL_RESPONSIBLE_REVIEW_EMAIL_EDIT if edit == True else RegulationFields.FILL_RESPONSIBLE_REVIEW_EMAIL)
            self.click_to(*save_button)

        url = self.driver.current_url

        save_button = AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR
        assert self.is_active(*save_button)
        self.click_to(*save_button)

        count = 0
        while self.url_change(url, timeout=20) == False:
            if_rcd_not_saved()
            count += 1

            if count >= 3:
                assert False, "Не удалось сохранить документ"

    def should_be_correct_error_message(self, error_message):
        locator = RegulationDocumentLocators.REGULATION_ERROR_MESSAGE_ID_LOCATOR if error_message == RegulationFields.CHAIN_NOT_FOUND_ERROR else RegulationDocumentLocators.REGULATION_ERROR_MESSAGE_LOCATOR

        self.is_appeared(*locator)
        text = self.return_text(*locator)
        count = 0

        while text == "":
            self.click_to(*AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR)
            text = self.return_text(*locator)
            count += 1

            if count >= 10:
                assert False

        return text == error_message

    def should_be_correct_saved_file(self):
        name = self.return_text(
            *AllDocumentFieldLocators.DOCUMENT_NAME_LOCATOR)
        self.click_to(*OpenDocumentPictagramsLocators.PRINT_PICTOGRAM_LOCATOR)
        self.click_to(
            *OpenDocumentPictagramsLocators.SAVE_ONLY_DOCUMENT_BUTTON_LOCATOR)

        text = self.pdf_to_html(name)
        
        assert "#" not in text, "Некорректно сформирован файл"

    def create_npa_regulation_id(self):
        npa_body = datetime.today().strftime("%Y%m%d%H%M%S")
        
        return f"autotest-{npa_body}-autotest"

    def modify_npa_type(self, npa_type, group=2):
        """Группа 2 возвращает название заявки, группа 1, возвращает номер"""
        npa = (search(r"(\d+)\. (.+)", npa_type))

        return (npa.group(2) if group == 2 else int(npa.group(1)))

    def register_and_send_enter_regulation_document(self, *func, answer=False):
        self.click_to_register_pictogram()
        self.should_be_required_fields(
            RegulationFields.ENTER_TITLE if answer == False else RegulationFields.ENTER_ANSWER_TITLE)

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
                return i
        return answer_type

    def create_and_send_answer(self, index, npa_id, create_id=False):
        answer_type = self.have_answer(index)
        if answer_type != 0:
            npa_id = self.create_answer(answer_type, create_id, npa_id)
            self.create_and_send_agree_sheet()
            self.register_and_send_enter_regulation_document(answer=True)
            self.send_medo()

        return npa_id

    def create_answer(self, answer_type, create_id, npa_id):
        self.click_to_answer_pictogram()

        self.should_be_required_fields(RegulationFields.SOGL_ANSWER_TITLE)
        self.fill_in_all_document_required_fields(
            "администратор", "суперадмин", 1)

        self.should_be_npa_id_fields(answer_type)
        self.should_be_start_date_fields(answer_type)
        self.should_be_end_date_fields(answer_type)
        self.should_be_add_file_button()

        self.fill_field(
            *RegulationAnswerPageLocators.ADD_DOCUMENT_LOCATOR, save_wait=True)
        npa_id = self.create_npa_regulation_id() if create_id == True else npa_id
        self.enter_npa_id_fields(npa_id, create_id)
        self.enter_start_date()
        self.enter_end_date()

        self.save_rcd()

        return npa_id

    def fields(self, args, fill=False, edit=False):
        arr_fields = [
            (RegulationFields.NPA_TYPE, self.should_be_npa_type_fields, self.select_npa_type_field,
             RegulationFields.FILL_NPA_TYPE, RegulationFields.FILL_NPA_TYPE_EDIT),
            (RegulationFields.NPA_NAME_1, self.should_be_npa_name_fields, self.enter_npa_name_field,
             RegulationFields.FILL_NPA_NAME_1, RegulationFields.FILL_NPA_NAME_1_EDIT),
            (RegulationFields.NPA_NAME_2, self.should_be_npa_name_fields, self.enter_npa_name_field,
             RegulationFields.FILL_NPA_NAME_2, RegulationFields.FILL_NPA_NAME_2_EDIT),
            (RegulationFields.NPA_PROJECT, self.should_be_npa_project_fields, self.enter_npa_project_field,
             RegulationFields.FILL_NPA_PROJECT, RegulationFields.FILL_NPA_PROJECT_EDIT),
            (RegulationFields.DISCUSS_PERIOD, self.should_be_discuss_period_fields, self.enter_discuss_period_field,
             RegulationFields.FILL_DISCUSS_PERIOD, RegulationFields.FILL_DISCUSS_PERIOD_EDIT),
            (RegulationFields.EA_TYPE, self.should_be_ea_type_fields, self.enter_new_window_ea_type,
             RegulationFields.FILL_EA_TYPE, RegulationFields.FILL_EA_TYPE_EDIT),
            (RegulationFields.KEYWORD, self.should_be_keyword_fields, self.enter_keyword_field,
             RegulationFields.FILL_KEYWORD, RegulationFields.FILL_KEYWORD_EDIT),
            (RegulationFields.NOTIFY_NPA, self.should_be_notify_npa_fields, self.enter_notify_npa_field,
             RegulationFields.FILL_NOTIFY_NPA, RegulationFields.FILL_NOTIFY_NPA_EDIT),
            (RegulationFields.SUMMARY_INFO, self.should_be_summary_info_fields, self.enter_summary_info_field,
             RegulationFields.FILL_SUMMARY_INFO, RegulationFields.FILL_SUMMARY_INFO_EDIT),
            (RegulationFields.TOTAL_COMMENT, self.should_be_total_comment_fields, self.enter_total_comment_field,
             RegulationFields.FILL_TOTAL_COMMENT, RegulationFields.FILL_TOTAL_COMMENT_EDIT),
            (RegulationFields.NUMBER_UNA_COMMENT, self.should_be_number_una_comment_fields, self.enter_number_una_comment_field,
             RegulationFields.FILL_NUMBER_UNA_COMMENT, RegulationFields.FILL_NUMBER_UNA_COMMENT_EDIT),
            (RegulationFields.NUMBER_COMMENT, self.should_be_number_comment_fields, self.enter_number_comment_field,
             RegulationFields.FILL_NUMBER_COMMENT, RegulationFields.FILL_NUMBER_COMMENT_EDIT),
            (RegulationFields.NUMBER_PTA_COMMENT, self.should_be_number_pta_comment_fields, self.enter_number_pta_comment_field,
             RegulationFields.FILL_NUMBER_PTA_COMMENT, RegulationFields.FILL_NUMBER_PTA_COMMENT_EDIT),
            (RegulationFields.DECISION_INFO, self.should_be_decision_info_fields, self.select_decision_info_field,
             RegulationFields.FILL_DECISION_INFO, RegulationFields.FILL_DECISION_INFO_EDIT),
            (RegulationFields.DECISION_INFO_2, self.should_be_decision_info_fields, self.select_decision_info_field,
             RegulationFields.FILL_DECISION_INFO_2, RegulationFields.FILL_DECISION_INFO_2_EDIT),
            (RegulationFields.ORG_INFO, self.should_be_org_info_fields,
             self.enter_org_info_field, False, True),
            (RegulationFields.EXPLAIN_NOTE, self.should_be_explain_note_fields, self.enter_explain_note_field,
             RegulationFields.FILL_EXPLAIN_NOTE, RegulationFields.FILL_EXPLAIN_NOTE_EDIT),
            (RegulationFields.MODIFIED_NPA, self.should_be_modified_npa_fields, self.enter_modified_npa_field,
             RegulationFields.FILL_MODIFIED_NPA, RegulationFields.FILL_MODIFIED_NPA_EDIT),
            (RegulationFields.AC_EXPERTISE, self.should_be_ac_expertise_fields, self.enter_ac_expertise_field,
             RegulationFields.FILL_AC_EXPERTISE, RegulationFields.FILL_AC_EXPERTISE_EDIT),
            (RegulationFields.EMAIL_AC_EXPERTISE, self.should_be_email_ac_expertise_fields, self.enter_email_ac_expertise_field,
             RegulationFields.FILL_EMAIL_AC_EXPERTISE, RegulationFields.FILL_EMAIL_AC_EXPERTISE_EDIT),
            (RegulationFields.MAIL_AC_EXPERTISE, self.should_be_mail_ac_expertise_fields, self.enter_mail_ac_expertise_field,
             RegulationFields.FILL_MAIL_AC_EXPERTISE, RegulationFields.FILL_MAIL_AC_EXPERTISE_EDIT),
            (RegulationFields.CORRUPTION_FACTOR, self.should_be_corruption_factor_fields, self.select_corruption_factor_field,
             RegulationFields.FILL_CORRUPTION_FACTOR, RegulationFields.FILL_CORRUPTION_FACTOR_EDIT),
            (RegulationFields.NUMBER_CONCLUSION, self.should_be_number_conclusion_fields, self.enter_number_conclusion_field,
             RegulationFields.FILL_NUMBER_CONCLUSION, RegulationFields.FILL_NUMBER_CONCLUSION_EDIT),
            (RegulationFields.GC_AC, self.should_be_gc_ac_fields, self.enter_gc_ac_field,
             RegulationFields.FILL_GC_AC, RegulationFields.FILL_GC_AC_EDIT),
            (RegulationFields.NPA_DRAFT, self.should_be_npa_draft_fields, self.enter_npa_draft_field,
             RegulationFields.FILL_NPA_DRAFT, RegulationFields.FILL_NPA_DRAFT_EDIT),
            (RegulationFields.APPROVED_NPA, self.should_be_approved_npa_fields, self.enter_approved_npa_field,
             RegulationFields.FILL_APPROVED_NPA, RegulationFields.FILL_APPROVED_NPA_EDIT),
            (RegulationFields.NPA_NUMBER, self.should_be_npa_number_fields, self.enter_npa_number_field,
             RegulationFields.FILL_NPA_NUMBER, RegulationFields.FILL_NPA_NUMBER_EDIT),
            (RegulationFields.ACCEPTED_NPA_NUMBER, self.should_be_npa_number_fields, self.enter_npa_number_field,
             RegulationFields.FILL_ACCEPTED_NPA_NUMBER, RegulationFields.FILL_ACCEPTED_NPA_NUMBER_EDIT),
            (RegulationFields.NPA_ADOPTION_DATE_1, self.should_be_npa_adoption_fields,
             self.enter_npa_adoption_field, RegulationFields.DATE, RegulationFields.DATE_EDIT),
            (RegulationFields.NPA_ADOPTION_DATE_2, self.should_be_npa_adoption_fields,
             self.enter_npa_adoption_field, RegulationFields.DATE, RegulationFields.DATE_EDIT),
            (RegulationFields.PD_NPA, self.should_be_pd_npa_fields, self.enter_pd_npa_field,
             RegulationFields.FILL_PD_NPA, RegulationFields.FILL_PD_NPA_EDIT),
            (RegulationFields.CONSOL_REPORT, self.should_be_consol_report_fields, self.enter_consol_report_field,
             RegulationFields.FILL_CONSOL_REPORT, RegulationFields.FILL_CONSOL_REPORT_EDIT),
            (RegulationFields.DECISION_PERIOD, self.should_be_decision_period_fields, self.enter_decision_period_field,
             RegulationFields.FILL_DECISION_PERIOD, RegulationFields.FILL_DECISION_PERIOD_EDIT),
            (RegulationFields.DEGREE_EXPOSURE, self.should_be_degree_exposure_fields, self.select_degree_exposure_field,
             RegulationFields.FILL_DEGREE_EXPOSURE, RegulationFields.FILL_DEGREE_EXPOSURE_EDIT),
            (RegulationFields.MSR, self.should_be_msr_fields, self.enter_msr_field,
             RegulationFields.FILL_MSR, RegulationFields.FILL_MSR_EDIT),
            (RegulationFields.EEC, self.should_be_eec_fields, self.enter_eec_field,
             RegulationFields.FILL_EEC, RegulationFields.FILL_EEC_EDIT),
            (RegulationFields.MDD, self.should_be_mdd_fields, self.enter_mdd_field,
             RegulationFields.FILL_MDD, RegulationFields.FILL_MDD_EDIT),
            (RegulationFields.ASSESSMENT_REPORT, self.should_be_assessment_report_fields, self.enter_assessment_report_field,
             RegulationFields.FILL_ASSESSMENT_REPORT, RegulationFields.FILL_ASSESSMENT_REPORT_EDIT),
            (RegulationFields.RR_NPA, self.should_be_rr_npa_fields, self.enter_rr_npa_field,
             RegulationFields.FILL_RR_NPA, RegulationFields.FILL_RR_NPA_EDIT),
            (RegulationFields.OFFERS_EMAIL, self.should_be_offers_email_fields,
             self.enter_offers_email_field, RegulationFields.FILL_EMAIL, RegulationFields.FILL_EMAIL_EDIT),
            (RegulationFields.RESPONSIBLE_REVIEW_1, self.should_be_resp_review_fields,
             self.enter_resp_review_field, False, True),
            (RegulationFields.RESPONSIBLE_REVIEW_2, self.should_be_resp_review_fields,
             self.enter_resp_review_field, False, True),
            (RegulationFields.RESPONSIBLE_REVIEW_3, self.should_be_resp_review_fields,
             self.enter_resp_review_field, False, True),

            (RegulationFields.STATE_NUMBER, self.should_be_state_number_fields, self.enter_state_number_field,
             RegulationFields.NON_REQUIRED_FIELD, RegulationFields.FILL_STATE_NUMBER_EDIT),
            (RegulationFields.REASON_CREATE_NPA, self.should_be_reason_create_npa_fields, self.enter_reason_create_npa_field,
             RegulationFields.NON_REQUIRED_FIELD, RegulationFields.FILL_REASON_CREATE_NPA_EDIT),
            (RegulationFields.ADD_OFFER_EMAIL, self.should_be_add_offer_email_fields,
             self.enter_add_offer_email_field, RegulationFields.NON_REQUIRED_FIELD, RegulationFields.FILL_EMAIL),
            (RegulationFields.LINK_ID, self.should_be_link_id_fields, self.enter_link_id_field,
             RegulationFields.NON_REQUIRED_FIELD, RegulationFields.FILL_LINK_ID_EDIT),
            (RegulationFields.CO_EXECTOR, self.should_be_co_exector_fields, self.enter_new_window_co_exector,
             RegulationFields.NON_REQUIRED_FIELD, RegulationFields.FILL_CO_EXECTOR_EDIT),
            (RegulationFields.ADDITIONAL_MATERIAL, self.should_be_additional_materials_fields, self.enter_additional_materials_field,
             RegulationFields.NON_REQUIRED_FIELD, RegulationFields.FILL_ADDITIONAL_MATERIAL_EDIT),
            (RegulationFields.REGULATORY_GILLIOTINE, self.should_be_regulatory_gilliotine_fields,
             self.activate_regulatory_gilliotine_checkbox, RegulationFields.NO_FIELD, RegulationFields.FILL_REGULATORY_GILLIOTINE_EDIT),
            (RegulationFields.ISSUE_TYPE, self.should_be_issue_type_fields,
             self.enter_issue_type_field, "", RegulationFields.FILL_ISSUE_TYPE_EDIT)    # Временное решение из-за ошибки. Оформлена в задаче T120524
        ]

        for i in range(len(args)):
            for q in range(len(arr_fields)):
                L = arr_fields[q]

                if args[i] == L[0]:
                    fill_arg = 1 if fill == False else 2
                    edit_arg = 3 if edit == False else 4

                    L[fill_arg](L[0], L[edit_arg])
                    break

    def main_regulation_fields(self, order, request_type, edit=False, from_rcsi=False):
        def elements_dont_show():
            self.should_not_be_order_enter_fields(order)
            self.should_not_be_request_type_enter_fields(
                self.modify_npa_type(request_type))

        if edit == False:
            self.should_be_required_fields(RegulationFields.SOGL_TITLE)
            self.fill_in_all_document_required_fields(
                "суперадмин", "администратор", 1)
            if from_rcsi == True:
                elements_dont_show()
            else:
                self.should_be_order_fields()
                self.should_be_request_type_fields()
                self.select_order_cm(order)
                self.select_type_request_cm(request_type)
        elif edit == True:
            elements_dont_show()

    def regulation_delete_all_added_files(self, fields):
        self.delete_all_added_files()

        rr_fields = (RegulationFields.RESPONSIBLE_REVIEW_1,
                     RegulationFields.RESPONSIBLE_REVIEW_2, RegulationFields.RESPONSIBLE_REVIEW_3)

        for i in rr_fields:
            if (i in fields) == True:
                self.click_to_responsible_review_delete_button()
                break

    def regulation_index_fields(self, index: int) -> list[str]:
        fields = {
            1: [RegulationFields.NOTIFY_NPA, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.DISCUSS_PERIOD, RegulationFields.EA_TYPE, RegulationFields.KEYWORD, RegulationFields.ORG_INFO, RegulationFields.REASON_CREATE_NPA, RegulationFields.ADD_OFFER_EMAIL, RegulationFields.LINK_ID, RegulationFields.CO_EXECTOR],
            4: [RegulationFields.SUMMARY_INFO, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.TOTAL_COMMENT, RegulationFields.NUMBER_UNA_COMMENT, RegulationFields.NUMBER_COMMENT, RegulationFields.NUMBER_PTA_COMMENT, RegulationFields.DECISION_INFO],
            7: [RegulationFields.NPA_PROJECT, RegulationFields.EXPLAIN_NOTE, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.DISCUSS_PERIOD, RegulationFields.EA_TYPE, RegulationFields.KEYWORD, RegulationFields.ORG_INFO, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.REGULATORY_GILLIOTINE, RegulationFields.REASON_CREATE_NPA, RegulationFields.ADD_OFFER_EMAIL, RegulationFields.LINK_ID, RegulationFields.CO_EXECTOR],
            8: [RegulationFields.NPA_PROJECT, RegulationFields.EXPLAIN_NOTE, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.DISCUSS_PERIOD, RegulationFields.EA_TYPE, RegulationFields.KEYWORD, RegulationFields.ORG_INFO, RegulationFields.AC_EXPERTISE, RegulationFields.EMAIL_AC_EXPERTISE, RegulationFields.MAIL_AC_EXPERTISE, RegulationFields.REGULATORY_GILLIOTINE, RegulationFields.REASON_CREATE_NPA, RegulationFields.ADD_OFFER_EMAIL, RegulationFields.LINK_ID, RegulationFields.CO_EXECTOR],
            9: [RegulationFields.NPA_PROJECT, RegulationFields.PD_NPA, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.AC_EXPERTISE, RegulationFields.EMAIL_AC_EXPERTISE, RegulationFields.MAIL_AC_EXPERTISE, RegulationFields.EA_TYPE, RegulationFields.KEYWORD, RegulationFields.ORG_INFO, RegulationFields.LINK_ID, RegulationFields.REASON_CREATE_NPA, RegulationFields.CO_EXECTOR],
            10: [RegulationFields.NPA_PROJECT, RegulationFields.CONSOL_REPORT, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.EA_TYPE, RegulationFields.KEYWORD, RegulationFields.ORG_INFO, RegulationFields.DEGREE_EXPOSURE, RegulationFields.ISSUE_TYPE, RegulationFields.REASON_CREATE_NPA, RegulationFields.ADD_OFFER_EMAIL, RegulationFields.LINK_ID, RegulationFields.CO_EXECTOR, RegulationFields.AC_EXPERTISE, RegulationFields.EMAIL_AC_EXPERTISE, RegulationFields.MAIL_AC_EXPERTISE, RegulationFields.DECISION_PERIOD],
            11: [RegulationFields.EEC, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.DECISION_PERIOD, RegulationFields.EA_TYPE, RegulationFields.KEYWORD, RegulationFields.ORG_INFO, RegulationFields.ISSUE_TYPE, RegulationFields.REASON_CREATE_NPA, RegulationFields.ADD_OFFER_EMAIL, RegulationFields.LINK_ID, RegulationFields.CO_EXECTOR],
            12: [RegulationFields.EXPLAIN_NOTE, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.NPA_PROJECT, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.DISCUSS_PERIOD, RegulationFields.EA_TYPE, RegulationFields.KEYWORD, RegulationFields.ORG_INFO, RegulationFields.FILL_REASON_CREATE_NPA_EDIT, RegulationFields.ADD_OFFER_EMAIL, RegulationFields.LINK_ID, RegulationFields.CO_EXECTOR],
            13: [RegulationFields.NPA_PROJECT, RegulationFields.EXPLAIN_NOTE, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.DISCUSS_PERIOD, RegulationFields.EA_TYPE, RegulationFields.KEYWORD, RegulationFields.ORG_INFO, RegulationFields.AC_EXPERTISE, RegulationFields.EMAIL_AC_EXPERTISE, RegulationFields.MAIL_AC_EXPERTISE, RegulationFields.REGULATORY_GILLIOTINE, RegulationFields.REASON_CREATE_NPA, RegulationFields.ADD_OFFER_EMAIL, RegulationFields.LINK_ID, RegulationFields.CO_EXECTOR],
            14: [RegulationFields.SUMMARY_INFO, RegulationFields.MODIFIED_NPA, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.TOTAL_COMMENT, RegulationFields.NUMBER_UNA_COMMENT, RegulationFields.NUMBER_COMMENT, RegulationFields.NUMBER_PTA_COMMENT, RegulationFields.DECISION_INFO],
            15: [RegulationFields.SUMMARY_INFO, RegulationFields.MODIFIED_NPA, RegulationFields.GC_AC, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.TOTAL_COMMENT, RegulationFields.NUMBER_UNA_COMMENT, RegulationFields.NUMBER_COMMENT, RegulationFields.NUMBER_PTA_COMMENT, RegulationFields.DECISION_INFO, RegulationFields.CORRUPTION_FACTOR, RegulationFields.NUMBER_CONCLUSION],
            16: [RegulationFields.SUMMARY_INFO, RegulationFields.GC_AC, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.TOTAL_COMMENT, RegulationFields.NUMBER_UNA_COMMENT, RegulationFields.NUMBER_COMMENT, RegulationFields.NUMBER_PTA_COMMENT, RegulationFields.CORRUPTION_FACTOR, RegulationFields.NUMBER_CONCLUSION],
            17: [RegulationFields.SUMMARY_INFO, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.TOTAL_COMMENT, RegulationFields.NUMBER_UNA_COMMENT, RegulationFields.NUMBER_COMMENT, RegulationFields.NUMBER_PTA_COMMENT],
            20: [RegulationFields.MODIFIED_NPA, RegulationFields.MSR, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.DECISION_INFO],
            21: [RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.DECISION_INFO, RegulationFields.MDD],
            22: [RegulationFields.NPA_PROJECT, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.AC_EXPERTISE, RegulationFields.EMAIL_AC_EXPERTISE, RegulationFields.MAIL_AC_EXPERTISE, RegulationFields.EA_TYPE, RegulationFields.KEYWORD, RegulationFields.REGULATORY_GILLIOTINE, RegulationFields.LINK_ID, RegulationFields.REASON_CREATE_NPA, RegulationFields.CO_EXECTOR],
            23: [RegulationFields.GC_AC, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.CORRUPTION_FACTOR, RegulationFields.NUMBER_CONCLUSION, RegulationFields.TOTAL_COMMENT, RegulationFields.NUMBER_COMMENT, RegulationFields.NUMBER_UNA_COMMENT, RegulationFields.NUMBER_PTA_COMMENT, RegulationFields.DECISION_INFO],
            24: [RegulationFields.NPA_DRAFT, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_1, RegulationFields.RESPONSIBLE_REVIEW_2, RegulationFields.DECISION_INFO_2],
            28: [RegulationFields.APPROVED_NPA, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_2, RegulationFields.ACCEPTED_NPA_NUMBER, RegulationFields.NPA_ADOPTION_DATE_1, RegulationFields.RESPONSIBLE_REVIEW_3, RegulationFields.STATE_NUMBER],
            32: [RegulationFields.APPROVED_NPA, RegulationFields.ASSESSMENT_REPORT, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NAME_2, RegulationFields.NPA_NUMBER, RegulationFields.NPA_ADOPTION_DATE_2, RegulationFields.RESPONSIBLE_REVIEW_1, RegulationFields.DISCUSS_PERIOD, RegulationFields.OFFERS_EMAIL, RegulationFields.EA_TYPE, RegulationFields.KEYWORD, RegulationFields.LINK_ID, RegulationFields.CO_EXECTOR],
            33: [RegulationFields.SUMMARY_INFO, RegulationFields.ADDITIONAL_MATERIAL, RegulationFields.NPA_TYPE, RegulationFields.NPA_NUMBER, RegulationFields.NPA_NAME_2, RegulationFields.NPA_ADOPTION_DATE_2, RegulationFields.TOTAL_COMMENT, RegulationFields.NUMBER_COMMENT, RegulationFields.NUMBER_UNA_COMMENT, RegulationFields.NUMBER_PTA_COMMENT],
            34: [RegulationFields.NPA_TYPE, RegulationFields.NPA_NUMBER, RegulationFields.NPA_NAME_2, RegulationFields.NPA_ADOPTION_DATE_2, RegulationFields.RR_NPA],
        }

        indexes = {
            1: (1, 2, 3),
            4: (4, 5, 6),
            14: (14, 18),
            15: (15, 19),
            24: (24, 25, 26, 27),
            28: (28, 29, 30, 31),
        }

        for i in indexes:
            if index in indexes[i]:
                index = i
                break

        return fields[int(index)]

    def check_regulation_doc(self, index, chain_index, first=False, edit=True):
        self.regulation_correct_npa_id_fields(index, chain_index, first, 3)
        self.regulation_correct_notice_npa_not_placed_fields(
            index, first, (3 if edit == True else 4))

        fields = self.regulation_index_fields(index)
        self.fields(fields, edit=edit)

    def regulation_doc(self, order, request_type, npa_id, edit=False, first=False, from_rcsi=False, error=False):
        def if_edit(fields=None):
            if edit == True:
                self.click_to_edit_pictogram(
                ) if fields == None else self.regulation_delete_all_added_files(fields)

        if_edit()
        edit_status = 1 if edit == False and from_rcsi == False else 2
        index = self.modify_npa_type(request_type, 1)
        fields = self.regulation_index_fields(index)

        self.main_regulation_fields(order, request_type, edit, from_rcsi)

        if_edit(fields)
        self.regulation_correct_npa_id_fields(
            index, npa_id, first, edit_status)
        self.regulation_correct_notice_npa_not_placed_fields(
            index, first, edit_status)

        self.fields(fields, fill=True, edit=edit)   # Заполнение полей

        if error == False:
            self.save_regulation_rcd(edit, index)
            self.check_regulation_doc(index, npa_id, first, edit)   # Проверка корректности заполнения полей
        else:
            self.click_to(*AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR)
            assert self.should_be_correct_error_message(error)


class ChangeResponsibleInfo(RegulationDocumentPage):
    # Тип заявки
    def should_be_request_type_35_fields(self, text, field_name):
        self.should_be_correct_field_name(
            field_name, ChangeResponsibleInfoLocators.REQUEST_TYPE_NAME_35_LOCATOR)

        field_text = self.return_text(
            *ChangeResponsibleInfoLocators.REQUEST_TYPE_FIELD_VIEW_MODE_35_LOCATOR)

        assert field_text == text

    # Наименование проекта НПА (отчета ОФВ)
    def should_be_npa_name_35_field(self, name):
        self.should_be_correct_field_name(
            name, ChangeResponsibleInfoLocators.NPA_NAME_NAME_FIELD_35_LOCATOR)

    def enter_npa_name_35_fields(self, text, field_name):
        self.should_be_correct_field_name(
            field_name, ChangeResponsibleInfoLocators.NPA_NAME_NAME_FIELD_35_LOCATOR)

        self.fill_field(
            *ChangeResponsibleInfoLocators.NPA_NAME_FIELD_35_LOCATOR, text)

    def should_be_npa_name_35_fields(self, text, field_name):
        self.should_be_correct_field_name(
            field_name, ChangeResponsibleInfoLocators.NPA_NAME_NAME_FIELD_35_LOCATOR)

        assert text == self.return_text(
            *ChangeResponsibleInfoLocators.NPA_NAME_VIEW_MODE_35_LOCATOR)

    # Текущий ответственный сотрудник
    def should_be_actual_rr_field(self, name):
        assert self.should_be_correct_field_name(
            name, ChangeResponsibleInfoLocators.CURRENT_RESPONSIBLE_USER_NAME_LOCATOR)

    def should_be_actual_rr_fields(self, name, field_name):
        self.should_be_actual_rr_field(field_name)
        text = self.return_text(
            *ChangeResponsibleInfoLocators.CURRENT_RESPONSIBLE_USER_VIEW_MODE_LOCATOR)
        assert name in text

    def enter_actual_rr_fields(self, text, field_name):
        self.should_be_actual_rr_field(field_name)

        assert self.is_element_present(
            *ChangeResponsibleInfoLocators.CURRENT_RESPONSIBLE_USER_FIELD_LOCATOR)
        self.click_to(
            *ChangeResponsibleInfoLocators.CURRENT_RESPONSIBLE_USER_NEW_WINDOW_LOCATOR)
        self.work_with_windows(1)
        self.fill_field(*ChooseUserFromNewWindow.USER_FIND_LOCATOR, text)
        self.click_to(*AllDocumentFieldLocators.find_text_locator(text))
        self.work_with_windows()

    # Новый ответственный сотрудник
    def should_be_new_rr_field(self, name, edit_mode):
        assert self.should_be_correct_field_name(
            name, ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_NAME_LOCATOR)

        if edit_mode == True:
            return [RegulationFields.FILL_RESPONSIBLE_REVIEW_NAME_EDIT, RegulationFields.FILL_RESPONSIBLE_REVIEW_PHONE_EDIT, RegulationFields.FILL_RESPONSIBLE_REVIEW_EMAIL_EDIT]
        else:
            return [RegulationFields.FILL_RESPONSIBLE_REVIEW_NAME, RegulationFields.FILL_RESPONSIBLE_REVIEW_PHONE, RegulationFields.FILL_RESPONSIBLE_REVIEW_EMAIL]

    def should_be_new_rr_fields(self, edit_mode, field_name):
        rr_fill_field = self.should_be_new_rr_field(field_name, edit_mode)
        text = self.return_text(
            *ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_VIEW_MODE_LOCATOR)

        for i in rr_fill_field:
            assert i in text

    def enter_new_rr_fields(self, edit_mode, field_name):
        rr_fill_field = self.should_be_new_rr_field(field_name, edit_mode)
        page_locators = [ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_FIELD_LOCATOR, ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_EMAIL_FIELD_LOCATOR,
                         ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_PHONE_FIELD_LOCATOR, ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_NEW_WINDOW_LOCATOR]

        for i in page_locators:
            assert self.is_element_present(*i)

        self.click_to(*page_locators[3])
        self.work_with_windows(1)
        self.fill_field(
            *ChooseUserFromNewWindow.USER_FIND_LOCATOR, rr_fill_field[0])
        self.click_to(
            *AllDocumentFieldLocators.find_text_locator(rr_fill_field[0]))
        self.work_with_windows()

        self.fill_field(*page_locators[2], rr_fill_field[1])
        self.fill_field(*page_locators[1], rr_fill_field[2])

    def click_to_save_with_error(self, text):
        save_button_locator = AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR
        error_locator = ChangeResponsibleInfoLocators.ERROR_ID_NOT_FOUND

        assert self.is_active(*save_button_locator)
        self.click_to(*save_button_locator)

        assert self.is_active(*error_locator)
        error_text = self.return_text(*error_locator)

        assert error_text == text

    def main_regulation_35_fields(self, edit=False):
        sogl_title_value = RegulationFields.SOGL_TITLE

        if edit == False:
            self.should_be_required_fields(sogl_title_value)
            self.fill_in_all_document_required_fields(
                "суперадмин", "администратор", 1)
        else:
            self.should_be_correct_title(sogl_title_value)

    def fields_35(self, fill, edit):
        text = "Заявка на изменение информации о работнике, ответственном за размещение информации на regulation.gov.ru"
        work_with_fields = [
            (RegulationFields.REQUEST_TYPE, self.should_be_request_type_35_fields,
             self.should_be_request_type_35_fields, text, text),
            (RegulationFields.NPA_NAME_35, self.should_be_npa_name_35_fields, self.enter_npa_name_35_fields,
             RegulationFields.FILL_NPA_NAME_3, RegulationFields.EDIT_NPA_NAME_3),
            (RegulationFields.ACTUAL_RR_35, self.should_be_actual_rr_fields, self.enter_actual_rr_fields,
             RegulationFields.FILL_RESPONSIBLE_REVIEW_NAME, RegulationFields.FILL_RESPONSIBLE_REVIEW_NAME_EDIT),
            (RegulationFields.NEW_RR_35, self.should_be_new_rr_fields,
             self.enter_new_rr_fields, False, True)
        ]

        for i in work_with_fields:
            fill_arg = 2 if fill == True else 1
            i[fill_arg](i[3 if edit == False else 4], i[0])

    def change_responsible_info_doc(self, edit=False, chain_index=None):
        if edit == True:
            self.click_to_edit_pictogram()
            self.click_to(
                *ChangeResponsibleInfoLocators.CURRENT_RESPONSIBLE_USER_DELETE_BUTTON)
            self.click_to(
                *ChangeResponsibleInfoLocators.NEW_RESPONSIBLE_USER_DELETE_BUTTON)

        self.main_regulation_35_fields(edit)

        if edit == False:
            self.enter_npa_id_fields("uncorrect-9999999999999999-id", True)
        self.fields_35(fill=True, edit=edit)
        if edit == False:
            self.click_to_save_with_error(
                RegulationFields.CHAIN_NOT_FOUND_ERROR)

        if edit == False:
            self.enter_project_npa_id_field(1, False, chain_index)
        else:
            self.should_be_project_npa_id_fields(1, False, True, chain_index)

        self.save_rcd()

        self.fields_35(fill=False, edit=edit)

    def register_and_send_enter_change_info_document(self, chain_index):
        self.click_to_register_pictogram()

        self.should_be_correct_title(RegulationFields.ENTER_TITLE)
        self.should_be_project_npa_id_fields(1, False, False, chain_index)
        self.fields_35(fill=False, edit=True)

        self.save_rcd()

        self.send_medo()


class RegulationRefuseDocument(RegulationDocumentPage):
    def create_refuse_document(self, request_name, doc_link):
        self.should_not_be_answer_pictogram() if self.have_answer(self.modify_npa_type(
            request_name, 1)) == 0 else self.should_be_answer_pictogram()
        self.should_be_refuse_pictogram()

        url = self.driver.current_url
        self.click_to_refuse_pictogram()
        self.url_change(url)

        self.should_be_required_fields(RegulationFields.SOGL_REFUSE_TITLE)
        self.fill_in_all_document_required_fields(
            "администратор", "суперадмин", 1)

        self.fill_field(*AllDocumentFieldLocators.ADD_FILE_BUTTON_LOCATOR)
        self.should_be_closed_short_content_fields(3)

        self.is_element_present(
            *AllDocumentFieldLocators.link_document("id=" + doc_link))

        self.save_rcd()

    def register_and_send_refuse_document(self, doc_link, from_rcsi=False):
        self.click_to_register_pictogram()
        self.should_be_required_fields(RegulationFields.ENTER_REFUSE_TITLE)
        self.save_rcd()
        self.send_medo()

        if from_rcsi == False:
            link_locator = AllDocumentFieldLocators.link_document(
                "id=" + doc_link)
            self.is_element_present(*link_locator)
            self.click_to(*link_locator)

            self.work_with_windows(1)
            self.should_be_correct_title(RegulationFields.ENTER_TITLE)
            self.should_not_be_answer_pictogram()
            self.should_not_be_refuse_pictogram()


class RegulationChainShowInstrument(RegulationRefuseDocument):
    def click_to_rcsi_repeat(self):
        repeat_link_locator = RegulationDocumentLocators.RCSI_REPEAT_LINK_LOCATOR

        self.click_to_rcsi_pictogram()
        self.is_element_present(*repeat_link_locator)

        url = self.driver.current_url

        self.click_to(*repeat_link_locator)
        self.url_change(url)

    def click_to_rcsi_next_doc(self, request_type):
        request_type = self.modify_npa_type(request_type)
        next_link_locator = RegulationDocumentLocators.rsci_next_request_link_locator(
            request_type)

        self.click_to_rcsi_pictogram()
        self.is_element_present(*next_link_locator)

        url = self.driver.current_url

        self.click_to(*next_link_locator)
        self.url_change(url)

    def check_rcsi_name(self, npa_id):
        rcsi_name_locator = RegulationDocumentLocators.RCSI_NAME_LOCATOR

        self.is_active(*rcsi_name_locator)
        text = self.return_text(*rcsi_name_locator)

        arr = ["Заявки по проекту НПА (отчету ОФВ)"]

        if npa_id != None:
            arr += ["ID", npa_id]

        for i in arr:
            assert i in text

    def check_rcsi_status(self, status, next_type):
        rcsi_status_locator = RegulationDocumentLocators.RCSI_STATUS_LOCATOR

        self.is_element_present(*rcsi_status_locator)
        text = self.return_text(*rcsi_status_locator)

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
            self.click_to(*RegulationDocumentLocators.RCSI_OPEN_CHAIN_AFTER_REFUSE)

        self.is_element_present(
            *RegulationDocumentLocators.find_rcsi_elements(number))

        rcsi_elements = {
            1: [RegulationDocumentLocators.find_rcsi_number, RegulationDocumentLocators.find_rcsi_name, RegulationDocumentLocators.find_rcsi_project, RegulationDocumentLocators.find_rcsi_request, RegulationDocumentLocators.find_rcsi_answer],
            2: [RegulationDocumentLocators.find_rcsi_project, RegulationDocumentLocators.find_rcsi_request, RegulationDocumentLocators.find_rcsi_number, RegulationDocumentLocators.find_rcsi_name],
            3: [RegulationDocumentLocators.find_rcsi_project, RegulationDocumentLocators.find_rcsi_request, RegulationDocumentLocators.find_rcsi_refuse, RegulationDocumentLocators.find_rcsi_number, RegulationDocumentLocators.find_rcsi_name],
            4: [RegulationDocumentLocators.find_rcsi_dots, RegulationDocumentLocators.find_rcsi_project, RegulationDocumentLocators.find_rcsi_request, RegulationDocumentLocators.find_rcsi_number, RegulationDocumentLocators.find_rcsi_name],
            5: [RegulationDocumentLocators.find_rcsi_project, RegulationDocumentLocators.find_rcsi_request, RegulationDocumentLocators.find_rcsi_refuse, RegulationDocumentLocators.find_rcsi_number, RegulationDocumentLocators.find_rcsi_name],
        }

        for i in rcsi_elements[status]:
            self.is_element_present(*i(number))
            if status == 5 and (i in (RegulationDocumentLocators.find_rcsi_project, RegulationDocumentLocators.find_rcsi_request)):
                assert self.count_all_elements(*i(number)) == 2
            elif i == RegulationDocumentLocators.find_rcsi_name:
                assert self.return_text(
                    *i(number)) == self.modify_npa_type(name)

    def check_rcsi(self, npa_id, doc_status, number, name, wait, repeat, num_satus, *next_type):
        if wait == True:
            self.should_be_status_on_agree()

        self.click_to_rcsi_pictogram()

        if repeat == True:
            self.is_element_present(
                *RegulationDocumentLocators.RCSI_ACTUAL_VERSION_LOCATOR)
        self.check_rcsi_name(npa_id)
        self.check_rcsi_status(doc_status, [self.modify_npa_type(
            next_type[i]) for i in range(len(next_type))])
        self.check_rcsi_number(number, name, num_satus)

        self.click_to_rcsi_pictogram()

    def check_rcsi_previous_version(self, version):
        self.click_to_rcsi_pictogram()
        self.is_element_present(
            *RegulationDocumentLocators.RCSI_ACTUAL_VERSION_LOCATOR)
        self.click_to(*RegulationDocumentLocators.go_to_rcsi_version(version))
        self.is_not_element_present(
            *RegulationDocumentLocators.RCSI_STATUS_LOCATOR)
        self.click_to_rcsi_pictogram()
