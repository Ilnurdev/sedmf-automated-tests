from .main_functions import MainFunc
from .locators import AllDocumentFieldLocators, NomenclatureUnitWindowLocators, ChooseUserFromNewWindow, ChooseOrganisationFromNewWindow, OpenDocumentPictagramsLocators, AgreeSheetLocators, PopupWindowLocators, ElSignatureLocators
from .value_for_fields import DocumentTitles
from selenium.common.exceptions import NoSuchWindowException
from time import sleep

class User:
    def __init__(self, user_type, dict_type=1):
        user_types = {
            1: ["superadmin_name", "superadmin_id", "enter_org"],
            2: ["admin_name", "admin_id", "enter_org"],
            3: ["user_ep_name", "user_ep_id", "out_org"],
            4: ["find_user_name", "find_user_id", "find_org"],
            5: ["user_enter_for_ep_name", "user_enter_for_ep_id", "out_org"],
            6: ["attesting_user_name", "attesting_user_id", "out_org"],
            7: ["ap_user_name", "ap_user_id", "ap_user_org"]
        }

        self.user = user_types[user_type]

        user_dict = {
            1: MainFunc.config(self.user[2]),
            2: "Департамент",
            3: "Прочие"
        }

        self.dict = user_dict[dict_type]
    
    def get_user(self):
        return self.user
    
    def get_dict(self):
        return self.dict


class PictogramsShow(MainFunc):
    def should_be_edit_pictogram(self):
        assert self.is_element_present(
            *OpenDocumentPictagramsLocators.EDIT_PICTAGRAM_LOCATOR), "Отсутствует пиктограмма Редактировать"

    def click_to_edit_pictogram(self):
        self.should_be_edit_pictogram()
        assert self.is_active(
            *OpenDocumentPictagramsLocators.EDIT_PICTAGRAM_LOCATOR)

        self.click_to(*OpenDocumentPictagramsLocators.EDIT_PICTAGRAM_LOCATOR)

    def should_not_be_edit_pictogram(self):
        assert self.is_not_appeared(
            *OpenDocumentPictagramsLocators.EDIT_PICTAGRAM_LOCATOR)

    def should_be_register_pictogram(self):
        assert self.is_element_present(
            *OpenDocumentPictagramsLocators.REGISTER_PICTOGRAM_LOCATOR), "Отсутствует пиктограмма Зарегистрировать документ"

    def click_to_register_pictogram(self):
        self.should_be_register_pictogram()

        self.click_to(
            *OpenDocumentPictagramsLocators.REGISTER_PICTOGRAM_LOCATOR)

    def should_be_answer_pictogram(self):
        assert self.is_element_present(
            *OpenDocumentPictagramsLocators.ANSWER_PICTOGRAM_LOCATOR)

    def click_to_answer_pictogram(self):
        self.should_be_answer_pictogram()
        self.click_to(*OpenDocumentPictagramsLocators.ANSWER_PICTOGRAM_LOCATOR)

    def should_not_be_answer_pictogram(self):
        assert self.is_not_element_present(
            *OpenDocumentPictagramsLocators.ANSWER_PICTOGRAM_LOCATOR)

    def should_be_refuse_pictogram(self):
        assert self.is_element_present(
            *OpenDocumentPictagramsLocators.REFUSE_PICTOGRAM_LOCATOR)

    def click_to_refuse_pictogram(self):
        self.should_be_refuse_pictogram()
        self.click_to(*OpenDocumentPictagramsLocators.REFUSE_PICTOGRAM_LOCATOR)

    def should_not_be_refuse_pictogram(self):
        assert self.is_not_element_present(
            *OpenDocumentPictagramsLocators.REFUSE_PICTOGRAM_LOCATOR)

    def should_be_refresh_pictogram(self):
        assert self.is_element_present(
            *OpenDocumentPictagramsLocators.REFRESH_PICTOGRAM_LOCATOR)

    def should_be_rcsi_pictogram(self):
        assert self.is_element_present(
            *OpenDocumentPictagramsLocators.REGULATION_CHAIN_SHOW_PICTOGRAM_LOCATOR)

    def click_to_rcsi_pictogram(self):
        self.should_be_rcsi_pictogram()
        self.click_to(
            *OpenDocumentPictagramsLocators.REGULATION_CHAIN_SHOW_PICTOGRAM_LOCATOR)


class SaveDocumentBlock(PictogramsShow):
    def should_be_save_button(self):
        assert self.is_element_present(*AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR)

    def click_to_save_button(self):
        save_button = AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR
        assert self.is_active(*save_button)
        self.click_to(*save_button)

    def save_rcd(self, medo_window=False):
        url = self.driver.current_url

        self.click_to_save_button()
        if medo_window != False:
            if medo_window == 1:
                locator = AllDocumentFieldLocators.MEDO_WINDOW_EP_LOCATOR
            elif medo_window == 2:
                locator = AllDocumentFieldLocators.MEDO_WINDOW_SP_LOCATOR
            self.is_element_present(*locator)
            self.click_to(*locator)
            self.click_to_save_button()

        trys = 0
        while self.url_change(url, timeout=30) == False:
            if trys > 10:
                assert False, "Не удалось сохранить документ"
            trys += 1


class AgreeSheetPage(SaveDocumentBlock):
    def click_to_create_agree_sheet_button(self):
        locator = AgreeSheetLocators.CREATE_AGREE_SHEET_BUTTON_LOCATOR
        self.is_element_present(*locator)
        windows = len(self.driver.window_handles) + 1
        while len(self.driver.window_handles) != windows:
            self.click_to(*locator)

    def click_to_submit_button_create_window(self, add_user=False):
        self.work_with_windows(1)
        if add_user != False:
            if type(add_user) != list:
                add_user = [add_user]
            for i in add_user:
                self.add_user(i)
        assert self.is_appeared(*AgreeSheetLocators.SUBMIT_BUTTON_LOCATOR)
        self.click_to(*AgreeSheetLocators.SUBMIT_BUTTON_LOCATOR)
        self.work_with_windows()

    def click_to_send_on_agreement_button(self):
        locator = AgreeSheetLocators.SEND_TO_AGREEMENT_BUTTON_LOCATOR
        self.is_element_present(*locator)
        self.click_to(*locator)

        trys = 0
        while self.is_appeared(*PopupWindowLocators.OK_ENG_BUTTON_LOCATOR, 30) == False:
            if trys > 5:
                assert False
            self.click_to(*locator)
            trys += 1

    def dismiss_with_popup_window(self):
        self.click_to(*PopupWindowLocators.DISMISS_BUTTON_LOCATOR)

    def agree_with_popup_window_agree_sheet(self):
        self.click_to(*PopupWindowLocators.OK_ENG_BUTTON_LOCATOR)

    def should_be_status_on_agree(self):
        self.is_element_present(*AgreeSheetLocators.ON_AGREE_TEXT_LOCATOR)

    def approve_agree_sheet_button(self, solution=1):
        solution_type = {
            1: AgreeSheetLocators.APPROVE_BUTTON_LOCATOR,       # Согласовать
            2: AgreeSheetLocators.REFUSE_BUTTON_LOCATOR,        # Замечание
            3: AgreeSheetLocators.AGREE_WITH_OWN_HAND_LOCATOR,  # подписан собственноручно
            4: AgreeSheetLocators.RESOLUTINS_BUTTON_LOCATOR     # Резолюция
        }
        locator = solution_type[solution]
        self.is_element_present(*locator)
        self.click_to(*locator)

    def click_to_agree_button_on_agreement_window(self, approve_with_ep, remark):
        self.work_with_windows(1)

        if approve_with_ep == True:
            locator = AgreeSheetLocators.SUBMIT_SUGN_BUTTON_LOCATOR
        else:
            locator = AgreeSheetLocators.SUBMIT_AGREE_BUTTON_LOCATOR

        remark_textarea_locator = AgreeSheetLocators.REMARK_TEXTAREA_LOCATOR
        self.is_element_present(*remark_textarea_locator)
        if remark != False:
            self.fill_field(*remark_textarea_locator, remark)

        self.is_element_present(*locator)
        if approve_with_ep == True:
            try:
                trys = 0
                while self.is_element_present(*locator):
                    if trys > 30:
                        assert False
                    if self.is_active(*AgreeSheetLocators.POPUP_WINDOW_ERROR, 3):
                        self.click_to(*AgreeSheetLocators.POPUP_WINDOW_ERROR_CANCEL_BUTTON)
                    self.click_to(*locator)
                    trys += 1
                    sleep(3)
            except NoSuchWindowException:
                assert len(self.driver.window_handles) == 1
        else:
            self.click_to(*locator)
            assert self.alert_open()
            self.driver.switch_to.alert.accept()

        self.work_with_windows()

    def click_to_refuse_button_on_agreement_window(self, with_ep, remark):
        self.work_with_windows(1)

        if with_ep == True:
            locator = AgreeSheetLocators.SAVE_WITH_EP_BUTTON_LOCATOR
        else:
            locator = AgreeSheetLocators.SAVE_BUTTON_LOCATOR
        
        remark_textarea_locator = AgreeSheetLocators.REMARK_TEXTAREA_LOCATOR
        add_file_button = AgreeSheetLocators.ADD_FILE_LINK_LOCATOR
        self.is_element_present(*remark_textarea_locator)
        self.is_element_present(*add_file_button)

        if remark == None:
            self.click_to(*add_file_button)

            add_file_input = AgreeSheetLocators.ADD_FILE_INPUT_LOCATOR
            self.is_element_present(*add_file_input)
            self.fill_field(*add_file_input, f_type=1)
        elif remark not in [False, None]:
            self.fill_field(*remark_textarea_locator, remark)

        self.is_element_present(*locator)
        if with_ep == True:
            try:
                trys = 0
                while self.is_element_present(*locator):
                    if trys > 30:
                        assert False
                    self.click_to(*locator)
                    trys += 1
                    sleep(3)
            except NoSuchWindowException:
                assert len(self.driver.window_handles) == 1
        else:
            self.click_to(*locator)
            assert self.alert_open()
            self.driver.switch_to.alert.accept()

        self.work_with_windows()

    def delete_users_from_agree_sheet(self):
        delete_buttons = self.driver.find_elements_by_xpath(
            "//a[text()='удалить']")

        for i in delete_buttons:
            self.driver.execute_script("arguments[0].click();", i)
            self.work_with_windows(1)
            self.driver.execute_script(
                "arguments[0].click();", self.driver.find_element_by_xpath("//input[@type='submit']"))
            self.work_with_windows(0)

    def create_and_send_agree_sheet(self, solution=1, delete=False, with_ep=False, add_user=False, remark=False):
        window_type = {
            1: self.click_to_agree_button_on_agreement_window,
            2: self.click_to_refuse_button_on_agreement_window,
            3: "Подписан собственноручно"
        }
        self.click_to_create_agree_sheet_button()
        self.click_to_submit_button_create_window(add_user)
        self.click_to_send_on_agreement_button()
        self.agree_with_popup_window_agree_sheet()
        if delete:
            self.delete_users_from_agree_sheet()
        self.approve_agree_sheet_button(solution)
        if solution != 3:
            window_type[solution](with_ep, remark)

    def should_be_correct_el_sign_img(self):
        assert self.is_appeared(*ElSignatureLocators.Verification.AgreeSheet.EP_IS_OK_LOCATOR, 30)

    def add_user(self, user_num):
        input_locator = AgreeSheetLocators.NEW_USER_INPUT_LOCATOR
        add_user_button_locator = AgreeSheetLocators.ADD_USER_BUTTON_LOCATOR

        user_obj = User(user_num, 2)
        user_arr = user_obj.get_user()
        user_dict = user_obj.get_dict()

        if self.is_not_element_present(*input_locator, 1):
            self.click_to(*add_user_button_locator)

        user_dict = AllDocumentFieldLocators.find_text_locator(user_dict)
        self.is_element_present(*user_dict)
        self.click_to(*user_dict)

        self.work_with_windows(2)

        self.fill_field(*ChooseUserFromNewWindow.USER_FIND_LOCATOR, self.config(user_arr[0]))
        self.click_to(*ChooseUserFromNewWindow.FIRST_USER_LINK_LOCATOR)

        self.work_with_windows(1)


class AllDocumentFieldPage(AgreeSheetPage):
    def should_be_correct_title(self, correct_title):
        title = self.driver.find_element(
            *AllDocumentFieldLocators.TITLE_LOCATOR)
        assert title.text == correct_title, f"Заголовок должен быть {correct_title}"

    def should_be_correct_url(self, url):
        received_url = self.driver.current_url
        assert url in received_url

    def should_be_index_del(self):
        index_dela = self.driver.find_element(
            *AllDocumentFieldLocators.INDEX_DELA_LOCATOR)
        assert index_dela.text == "Индекс дела", "Не отображается поле 'Индекс дела'"

    def should_be_index_del_field(self):
        assert self.is_element_present(
            *AllDocumentFieldLocators.INDEX_DELA_FIELD_LOCATOR), "Отсутвует поле для 'Индексов дел'"

    def should_be_podpish(self):
        podpish = self.driver.find_element(
            *AllDocumentFieldLocators.PODPIS_LOCATOR)
        assert podpish.text == "Подпись:", "Не отображается поле 'Подпись'"

    def should_be_podpish_field(self):
        assert self.is_element_present(
            *AllDocumentFieldLocators.PODPIS_FIELD_LOCATOR), "Отсутвует поле для 'Подписанта'"

    def enter_index_del(self):
        self.is_active(*AllDocumentFieldLocators.INDEX_DELA_LOCATOR)
        self.click_to(*AllDocumentFieldLocators.INDEX_DELA_LOCATOR)
        self.work_with_windows(1)
        self.is_active(
            *NomenclatureUnitWindowLocators.FIRST_NOMENCLATURE_LOCATOR)
        self.click_to(
            *NomenclatureUnitWindowLocators.FIRST_NOMENCLATURE_LOCATOR)
        self.work_with_windows()

    def enter_podpish(self, user):
        
        try:
            user_name = self.config(user[1])
        except:
            user_name = self.config(user[0])
        is_id = user_name.isdigit()

        self.click_to(*AllDocumentFieldLocators.PODPIS_NEW_WINDOW_LOCATOR)
        a = self.work_with_windows(1)

        if is_id:
            user_locator = ChooseUserFromNewWindow.find_user_by_id(user_name)
            self.is_element_present(*user_locator)
            self.click_to(*user_locator)
        else:
            search_input_locator = ChooseUserFromNewWindow.USER_FIND_LOCATOR
            self.is_element_present(*search_input_locator)
            self.fill_field(*search_input_locator, user_name)
            self.click_to(
                *ChooseUserFromNewWindow.FIRST_USER_LINK_LOCATOR)
        self.work_with_windows()

    def delete_recipient(self):
        self.click_to(
            *AllDocumentFieldLocators.RECIPIENT_DELETE_BUTTON_LOCATOR)

    def enter_recipient(self, user: str, recipient_type: str, organization):
        """Переменная recipient_type может получать значения: Организация, Департамент, Прочие"""
        def work_with_frame(windows):
            frame_elements = self.driver.find_elements_by_xpath("//frame")
            self.driver.switch_to.frame(frame_elements[0])

            self.fill_field(
                *ChooseOrganisationFromNewWindow.USER_FIND_LOCATOR, user_name)
            self.click_to(*ChooseOrganisationFromNewWindow.FIND_BUTTON_LOCATOR)
            org = AllDocumentFieldLocators.find_text_locator(org_name)
            self.is_active(*org)
            self.click_to(*org)

            self.driver.switch_to.window(windows[1])

            self.driver.switch_to.frame(frame_elements[1])

            trys = 0
            while len(self.driver.window_handles) != 1:
                if trys > 100:
                    assert False
                self.click_to(*AllDocumentFieldLocators.find_text_locator(user_name))
                trys += 1
        
        user_name = self.config(user)
        org_name = self.config(organization)

        self.click_to(
            *AllDocumentFieldLocators.recipient_new_window_locator(recipient_type))
        windows = self.work_with_windows(1)

        if recipient_type == "Прочие":
            work_with_frame(windows)
        else:
            self.fill_field(*ChooseUserFromNewWindow.USER_FIND_LOCATOR, user_name)
            self.click_to(*ChooseUserFromNewWindow.FIRST_USER_LINK_LOCATOR)

        self.driver.switch_to.window(windows[0])

    def add_files(self):
        locator = AllDocumentFieldLocators.ADD_FILE_BUTTON_LOCATOR
        self.is_element_present(*locator)
        self.fill_field(*locator)

    def delete_all_added_files(self):
        delete_button_locator = AllDocumentFieldLocators.DELETE_FILE_LOCATOR
        count_delete_buttons = self.count_all_elements(*delete_button_locator)

        for i in range(count_delete_buttons):
            self.click_to(*delete_button_locator)

            trys = 0
            while self.alert_open() == False:
                if trys > 10:
                    assert False
                self.click_to(*delete_button_locator)
                trys += 1

            self.driver.switch_to.alert.accept()
    
    def fill_in_all_document_required_fields(self, podpish, recipient, recipient_type, ord=False, og=False):
        """

        1 - Суперадмин, 
        2 - Админ, 
        3 - Пользователь с ЭП, 
        4 - Пользователь из другой организации
        5 - Пользователь из организации пользователя с ЭП
        6 - Пользователь доступный для заверения
        7 - Пользователь из АП

        """

        podpish_obj = User(podpish)
        recipient_obj = User(recipient, recipient_type)

        podpish_el = podpish_obj.get_user()
        recipient_el = recipient_obj.get_user()
        recipient_dict = recipient_obj.get_dict()

        if ord == False:
            self.enter_index_del()
        self.enter_podpish(podpish_el)

        title = self.return_text(*AllDocumentFieldLocators.TITLE_LOCATOR)
        # [DocumentTitles.OUTGOING_CITIZEN_APPEAL, DocumentTitles.OUTGOING_ANSWER_SOGL, DocumentTitles.ENTER_REQUEST_SOGL, DocumentTitles.REGULATION_SOGL]
        if title in [DocumentTitles.OUTGOING_CITIZEN_APPEAL, DocumentTitles.ENTER_REQUEST_SOGL, DocumentTitles.REGULATION_SOGL]:
            self.delete_recipient()
        
        if og == False:
            self.enter_recipient(recipient_el[0], recipient_dict, recipient_el[2])

    def should_be_required_fields(self, correct_title):
        self.should_be_correct_title(correct_title)
        self.should_be_index_del()
        self.should_be_index_del_field()
        self.should_be_podpish()
        self.should_be_podpish_field()

    def register_doc(self, title):
        self.click_to_register_pictogram()

        self.should_be_required_fields(title)
        self.save_rcd()
    
    def should_be_short_content_fields(self):
        short_content = self.is_element_present(*AllDocumentFieldLocators.SHORT_CONTENT_NAME_LOCATOR)
        assert self.is_element_present(*AllDocumentFieldLocators.SHORT_CONTENT_FIELD_LOCATOR)
        assert short_content
        assert short_content.text == "* Краткое содержание:"

    def fill_short_content_field(self, text):
        locator = AllDocumentFieldLocators.SHORT_CONTENT_FIELD_LOCATOR
        self.click_to(*locator)
        self.fill_field(*locator, text)

    def should_be_etalon_el_sign_img(self):
        assert self.is_element_present(*ElSignatureLocators.Verification.Etalon.EP_IS_OK_LOCATOR)

    def should_be_appeal_author_fields(self):
        appeal_author = self.is_element_present(*AllDocumentFieldLocators.APPEAL_AUTHOR_NAME_LOCATOR)
        assert self.is_element_present(*AllDocumentFieldLocators.APPEAL_AUTHOR_FIELD_LOCATOR)
        assert appeal_author
        assert appeal_author.text == "* Автор обращения:"
    
    def fill_appeal_author_field(self):
        locator = AllDocumentFieldLocators.APPEAL_AUTHOR_FIELD_LOCATOR
        user_obj = User(4)
        user_arr = user_obj.get_user()
        user = self.config(user_arr[0]).split()
        self.click_to(*locator)
        self.fill_field(*locator, user[0])
        self.click_to(*AllDocumentFieldLocators.find_text_locator(user[0], "li"))

    def should_be_review_result_fields(self):
        review_result = self.is_element_present(*AllDocumentFieldLocators.REVIEW_RESULT_NAME_LOCATOR)
        assert self.is_element_present(*AllDocumentFieldLocators.REVIEW_RESULT_FIELD_LOCATOR)
        assert review_result
        assert review_result.text == "* Результат рассмотрения"
    
    def fill_review_result_field(self, text):
        locator = AllDocumentFieldLocators.REVIEW_RESULT_FIELD_LOCATOR
        self.click_to(*locator)
        self.work_with_selector(*locator, value=text)

    def save_and_check_ep(self, solution):
        self.should_be_correct_el_sign_img()
        if solution == 1:
            self.should_be_etalon_el_sign_img()
            self.click_to_register_pictogram()
            self.save_rcd()
            self.should_be_etalon_el_sign_img()
