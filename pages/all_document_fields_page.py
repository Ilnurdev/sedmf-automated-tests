from .main_functions import MainFunc
from selenium.common.exceptions import StaleElementReferenceException
from .locators import AllDocumentFieldLocators, NomenclatureUnitWindowLocators, ChooseUserFromNewWindow, OpenDocumentPictagramsLocators, AgreeSheetLocators, PopupWindowLocators
from selenium import webdriver
import time


class PictogramsShow(MainFunc):
    def should_be_edit_pictogram(self):
        assert self.is_element_present(*OpenDocumentPictagramsLocators.EDIT_PICTAGRAM_LOCATOR), "Отсутствует пиктограмма Редактировать"
    
    def click_to_edit_pictogram(self):
        self.should_be_edit_pictogram()
        assert self.is_active(*OpenDocumentPictagramsLocators.EDIT_PICTAGRAM_LOCATOR)
        
        self.click_to(*OpenDocumentPictagramsLocators.EDIT_PICTAGRAM_LOCATOR)

    def should_not_be_edit_pictogram(self):
        assert self.is_not_appeared(*OpenDocumentPictagramsLocators.EDIT_PICTAGRAM_LOCATOR)

    def should_be_register_pictogram(self):
        assert self.is_element_present(*OpenDocumentPictagramsLocators.REGISTER_PICTOGRAM_LOCATOR), "Отсутствует пиктограмма Зарегистрировать документ"
    
    def click_to_register_pictogram(self):
        self.should_be_register_pictogram()

        self.click_to(*OpenDocumentPictagramsLocators.REGISTER_PICTOGRAM_LOCATOR)

    def should_be_answer_pictogram(self):
        assert self.is_element_present(*OpenDocumentPictagramsLocators.ANSWER_PICTOGRAM_LOCATOR)
    
    def click_to_answer_pictogram(self):
        self.should_be_answer_pictogram()
        self.click_to(*OpenDocumentPictagramsLocators.ANSWER_PICTOGRAM_LOCATOR)
    
    def should_not_be_answer_pictogram(self):
        assert self.is_not_element_present(*OpenDocumentPictagramsLocators.ANSWER_PICTOGRAM_LOCATOR)

    def should_be_refuse_pictogram(self):
        assert self.is_element_present(*OpenDocumentPictagramsLocators.REFUSE_PICTOGRAM_LOCATOR)
    
    def click_to_refuse_pictogram(self):
        self.should_be_refuse_pictogram()
        self.click_to(*OpenDocumentPictagramsLocators.REFUSE_PICTOGRAM_LOCATOR)
    
    def should_not_be_refuse_pictogram(self):
        assert self.is_not_element_present(*OpenDocumentPictagramsLocators.REFUSE_PICTOGRAM_LOCATOR)

    def should_be_refresh_pictogram(self):
        assert self.is_element_present(*OpenDocumentPictagramsLocators.REFRESH_PICTOGRAM_LOCATOR)
    
    def should_be_rcsi_pictogram(self):
        assert self.is_element_present(*OpenDocumentPictagramsLocators.REGULATION_CHAIN_SHOW_PICTOGRAM_LOCATOR)

    def click_to_rcsi_pictogram(self):
        self.should_be_rcsi_pictogram()
        self.click_to(*OpenDocumentPictagramsLocators.REGULATION_CHAIN_SHOW_PICTOGRAM_LOCATOR)

class SaveDocumentBlock(PictogramsShow):
    def save_rcd(self):
        save_button = AllDocumentFieldLocators.SAVE_RCD_BUTTON_LOCATOR
        assert self.is_active(*save_button)
        self.click_to(*save_button)

        url = self.driver.current_url
        try:
            none_attribute = self.driver.find_element(*save_button).get_attribute("style")
        except:
            none_attribute = "none"
        if "none" not in none_attribute:
            try:
                self.click_to(*save_button)
            except:
                pass
        if self.url_change(url) == True:
            pass
        else:
            try:
                self.click_to(*save_button)
            except:
                pass
            assert self.url_change(url) == True
        
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
    
    def dismiss_with_popup_window(self):
        self.click_to(*PopupWindowLocators.DISMISS_BUTTON_LOCATOR)
    
    def agree_with_popup_window_agree_sheet(self):
        self.click_to(*PopupWindowLocators.OK_ENG_BUTTON_LOCATOR)
    
    def should_be_status_on_agree(self):
        self.is_element_present(*AgreeSheetLocators.ON_AGREE_TEXT_LOCATOR)
    
    def approve_agree_sheet_button(self):
        assert self.is_appeared(*AgreeSheetLocators.APPROVE_BUTTON_LOCATOR)
        self.click_to(*AgreeSheetLocators.APPROVE_BUTTON_LOCATOR)
    
    def click_to_agree_button_on_agreement_window(self):
        self.work_with_windows(1)
        self.click_to(*AgreeSheetLocators.SUBMIT_AGREE_BUTTON_LOCATOR)
        self.alert_open()
        self.driver.switch_to.alert.accept()
        self.work_with_windows()
    
    def create_and_send_agree_sheet(self):
        self.click_to_create_agree_sheet_button()
        self.click_to_submit_button_create_window()
        self.click_to_send_on_agreement_button()
        self.agree_with_popup_window_agree_sheet()
        self.approve_agree_sheet_button()
        self.click_to_agree_button_on_agreement_window()

class AllDocumentFieldPage(AgreeSheetPage):
    def should_be_correct_title(self, correct_title):
        title = self.driver.find_element(*AllDocumentFieldLocators.TITLE_LOCATOR)
        assert title.text == correct_title, f"Заголовок должен быть {correct_title}"
    
    def should_be_correct_url(self, url):
        received_url = self.driver.current_url
        assert url in received_url

    def should_be_index_del(self):
        index_dela = self.driver.find_element(*AllDocumentFieldLocators.INDEX_DELA_LOCATOR)
        assert index_dela.text == "Индекс дела", "Не отображается поле 'Индекс дела'"
    
    def should_be_index_del_field(self):
        assert self.is_element_present(*AllDocumentFieldLocators.INDEX_DELA_FIELD_LOCATOR), "Отсутвует поле для 'Индексов дел'"

    def should_be_podpish(self):
        podpish = self.driver.find_element(*AllDocumentFieldLocators.PODPIS_LOCATOR)
        assert podpish.text == "Подпись:", "Не отображается поле 'Подпись'"

    def should_be_podpish_field(self):
        assert self.is_element_present(*AllDocumentFieldLocators.PODPIS_FIELD_LOCATOR), "Отсутвует поле для 'Подписанта'"

    def enter_index_del(self):
        self.is_active(*AllDocumentFieldLocators.INDEX_DELA_LOCATOR)
        self.click_to(*AllDocumentFieldLocators.INDEX_DELA_LOCATOR)
        self.work_with_windows(1)
        self.is_active(*NomenclatureUnitWindowLocators.FIRST_NOMENCLATURE_LOCATOR)
        self.click_to(*NomenclatureUnitWindowLocators.FIRST_NOMENCLATURE_LOCATOR)
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
        self.click_to(*AllDocumentFieldLocators.RECIPIENT_DELETE_BUTTON_LOCATOR)
    
    def enter_recipient(self, user):
        self.click_to(*AllDocumentFieldLocators.RECIPIENT_NEW_WINDOW_LOCATOR)
        self.work_with_windows(1)
        self.fill_field(
            *ChooseUserFromNewWindow.USER_FIND_LOCATOR, user)
        self.click_to(
            *ChooseUserFromNewWindow.FIRST_USER_LINK_LOCATOR)
        self.work_with_windows()
    
    def delete_all_added_files(self):
        count = self.count_all_elements(*AllDocumentFieldLocators.DELETE_FILE_LOCATOR)
        for i in range(count):
            delete_button = (AllDocumentFieldLocators.DELETE_FILE_LOCATOR)
            self.click_to(*delete_button)
            while self.alert_open() == False:
                self.click_to(*delete_button)
            self.driver.switch_to.alert.accept()

    def fill_in_all_document_required_fields(self, podpish, recipient):
        self.enter_index_del()
        self.enter_podpish(podpish)
        self.delete_recipient()
        self.enter_recipient(recipient)
    
    def should_be_required_fields(self, correct_title):
        self.should_be_correct_title(correct_title)
        self.should_be_index_del()
        self.should_be_index_del_field()
        self.should_be_podpish()
        self.should_be_podpish_field()




    
        
