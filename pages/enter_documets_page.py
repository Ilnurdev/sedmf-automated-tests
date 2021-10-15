from .main_functions import MainFunc
from .locators import EnterDocumentsLocators, PopupWindowLocators


class EnterDocumentsPage(MainFunc):
    def should_be_send_medo_button(self):
        assert self.is_element_present(
            *EnterDocumentsLocators.SEND_MEDO_BUTTON_LOCATOR)

    def click_to_send_medo_button(self):
        self.should_be_send_medo_button()
        self.click_to(*EnterDocumentsLocators.SEND_MEDO_BUTTON_LOCATOR)

    def agree_with_popup_window_enter_doc(self):
        self.click_to(*PopupWindowLocators.OK_RUS_BUTTON_LOCATOR)

    def agree_with_popup_window_continue(self):
        self.click_to(*PopupWindowLocators.CONTINUE_BUTTON_LOCATOR)

    def send_medo(self):
        self.agree_with_popup_window_enter_doc()
        self.click_to_send_medo_button()
        self.agree_with_popup_window_continue()
        self.is_not_element_present(
            *EnterDocumentsLocators.SEND_MEDO_BUTTON_LOCATOR)

class OutDocumentsPage(MainFunc):
    def should_be_attesting_button(self):
        assert self.is_element_present(*EnterDocumentsLocators.ATTESTING_BUTTON_LOCATOR)
    
    def click_to_attesting_button(self):
        self.should_be_attesting_button()
        attesting_button = EnterDocumentsLocators.ATTESTING_BUTTON_LOCATOR
        popup_error = EnterDocumentsLocators.EP_NOT_FOUND_POPAP_LOCATOR

        self.click_to(*attesting_button)
        trys = 0
        while self.is_active(*popup_error, 3):
            if trys > 5:
                assert False
            self.click_to(*popup_error)
            self.click_to(*attesting_button)
            trys += 1
