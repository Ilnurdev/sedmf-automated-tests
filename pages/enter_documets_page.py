from .main_functions import MainFunc
from .locators import EnterDocumentsLocators, PopupWindowLocators

import time


class EnterDocumentsPage(MainFunc):
    def should_be_send_medo_button(self):
        assert self.is_element_present(*EnterDocumentsLocators.SEND_MEDO_BUTTON_LOCATOR)
    
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
        self.is_not_element_present(*EnterDocumentsLocators.SEND_MEDO_BUTTON_LOCATOR)
