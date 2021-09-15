from time import sleep
from .main_functions import MainFunc
from .locators import AllDocumentFieldLocators, NomenclatureUnitWindowLocators, ChooseUserFromNewWindow, ChooseOrganisationFromNewWindow, OpenDocumentPictagramsLocators, AgreeSheetLocators, PopupWindowLocators
from .value_for_fields import DocumentTitles


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
    def click_to_save_button(self):
        save_button = AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR
        assert self.is_active(*save_button)
        self.click_to(*save_button)

    def save_rcd(self):
        url = self.driver.current_url
        count = 0

        self.click_to_save_button()

        while self.url_change(url, timeout=20) == False and count < 3:
            count += 1

        if count >= 3:
            assert False, "Не удалось сохранить документ"


class AgreeSheetPage(SaveDocumentBlock):
    def click_to_create_agree_sheet_button(self):
        self.click_to(*AgreeSheetLocators.CREATE_AGREE_SHEET_BUTTON_LOCATOR)

    def click_to_submit_button_create_window(self):
        self.work_with_windows(1)
        assert self.is_appeared(*AgreeSheetLocators.SUBMIT_BUTTON_LOCATOR)
        self.click_to(*AgreeSheetLocators.SUBMIT_BUTTON_LOCATOR)
        self.work_with_windows()

    def click_to_send_on_agreement_button(self):
        self.click_to(*AgreeSheetLocators.SEND_TO_AGREEMENT_BUTTON_LOCATOR)

        count = 0
        while self.is_element_present(*PopupWindowLocators.OK_ENG_BUTTON_LOCATOR) == False and count <= 3:
            self.click_to(*AgreeSheetLocators.SEND_TO_AGREEMENT_BUTTON_LOCATOR)
            count += 1

    def dismiss_with_popup_window(self):
        self.click_to(*PopupWindowLocators.DISMISS_BUTTON_LOCATOR)

    def agree_with_popup_window_agree_sheet(self):
        self.click_to(*PopupWindowLocators.OK_ENG_BUTTON_LOCATOR)

    def should_be_status_on_agree(self):
        self.is_element_present(*AgreeSheetLocators.ON_AGREE_TEXT_LOCATOR)

    def approve_agree_sheet_button(self):
        # assert self.is_appeared(*AgreeSheetLocators.APPROVE_BUTTON_LOCATOR, timeout=30)
        self.click_to(*AgreeSheetLocators.APPROVE_BUTTON_LOCATOR)

    def click_to_agree_button_on_agreement_window(self):
        self.work_with_windows(1)
        self.click_to(*AgreeSheetLocators.SUBMIT_AGREE_BUTTON_LOCATOR)
        self.alert_open()
        self.driver.switch_to.alert.accept()
        self.work_with_windows()

    def delete_users_from_agree_sheet(self):
        delete_buttons = self.driver.find_elements_by_xpath("//a[text()='удалить']")

        for i in delete_buttons:
            self.driver.execute_script("arguments[0].click();", i)
            self.work_with_windows(1)
            self.driver.execute_script(
                "arguments[0].click();", self.driver.find_element_by_xpath("//input[@type='submit']"))
            self.work_with_windows(0)

    def create_and_send_agree_sheet(self, delete=False):
        self.click_to_create_agree_sheet_button()
        self.click_to_submit_button_create_window()
        self.click_to_send_on_agreement_button()
        self.agree_with_popup_window_agree_sheet()
        if delete == False:
            self.delete_users_from_agree_sheet()
        self.approve_agree_sheet_button()
        self.click_to_agree_button_on_agreement_window()


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
        self.click_to(*AllDocumentFieldLocators.PODPIS_NEW_WINDOW_LOCATOR)
        self.work_with_windows(1)
        self.fill_field(
            *ChooseUserFromNewWindow.USER_FIND_LOCATOR, user)
        self.click_to(
            *ChooseUserFromNewWindow.FIRST_USER_LINK_LOCATOR)
        self.work_with_windows()

    def delete_recipient(self):
        self.click_to(
            *AllDocumentFieldLocators.RECIPIENT_DELETE_BUTTON_LOCATOR)

    def enter_recipient(self, user: str, recipient_type: str):
        """Переменная recipient_type может получать значения: Организация для автотестирования, Департамент, Прочие"""
        def work_with_frame(windows):
            frame_elements = self.driver.find_elements_by_xpath("//frame")
            self.driver.switch_to.frame(frame_elements[0])
            
            self.fill_field(
                *ChooseOrganisationFromNewWindow.USER_FIND_LOCATOR, user)
            self.click_to(*ChooseOrganisationFromNewWindow.FIND_BUTTON_LOCATOR)
            organization = AllDocumentFieldLocators.find_text_locator('Организация для автотестирования')
            self.is_active(*organization)
            self.click_to(*organization)

            self.driver.switch_to.window(windows[1])

            self.driver.switch_to.frame(frame_elements[1])
            self.click_to(*AllDocumentFieldLocators.find_text_locator(user))
            
            # self.driver.switch_to.window(windows[0])

            # try: self.driver.switch_to.default_content()
            # except: pass
        
        
        self.click_to(*AllDocumentFieldLocators.recipient_new_window_locator(recipient_type))
        windows = self.work_with_windows(1)

        if recipient_type == "Прочие":
            work_with_frame(windows)
        else:
            self.fill_field(
                *ChooseUserFromNewWindow.USER_FIND_LOCATOR, user)
            self.click_to(
                *ChooseUserFromNewWindow.FIRST_USER_LINK_LOCATOR)
        self.driver.switch_to.window(windows[0])

    def delete_all_added_files(self):
        delete_button_locator = AllDocumentFieldLocators.DELETE_FILE_LOCATOR
        count_delete_buttons = self.count_all_elements(*delete_button_locator)

        for i in range(count_delete_buttons):
            self.click_to(*delete_button_locator)

            while self.alert_open() == False:
                self.click_to(*delete_button_locator)

            self.driver.switch_to.alert.accept()

    def fill_in_all_document_required_fields(self, podpish, recipient, recipient_type):
        recipients_dict = {
            1: "Организация для автотестирования",
            2: "Департамент",
            3: "Прочие"
        }

        self.enter_index_del()
        self.enter_podpish(podpish)

        title = self.return_text(*AllDocumentFieldLocators.TITLE_LOCATOR)

        if title in [DocumentTitles.OUTGOING_CITIZEN_APPEAL, DocumentTitles.OUTGOING_ANSWER_SOGL, DocumentTitles.ENTER_REQUEST_SOGL, DocumentTitles.REGULATION_SOGL]:
            self.delete_recipient()
        self.enter_recipient(recipient, recipients_dict[recipient_type])

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
