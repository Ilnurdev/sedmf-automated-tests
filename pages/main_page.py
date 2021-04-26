import pytest
from .main_functions import MainFunc
from .all_document_fields_page import AllDocumentFieldPage
from .locators import MainPageLocators, SoglNewDocumentWindow


class MainPage(MainFunc):
    def __should_be_correct_fields():
        links = [
            
        ]


class EnterDocumentsBlock(MainFunc):
    def open_enter_document_block(self):
        if self.is_active(*MainPageLocators.ENTER_BLOCK_SLIDE_DOWN_BUTTON) == True:
            self.driver.find_element(*MainPageLocators.ENTER_BLOCK_SLIDE_DOWN_BUTTON).click()

    def go_to_enter_document_on_register(self):
        self.open_enter_document_block()
        self.driver.find_element(*MainPageLocators.ENTER_BLOCK_ON_REGISTRATION_LINK).click()


class SoglDocumentsBlock(MainFunc):
    def should_be_correct_elements_sogl_request_new_window(self):
        window_elements = [
            SoglNewDocumentWindow.REQUEST_REQUEST_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.REQUEST_REQUEST_NAME_LOCATOR,
            SoglNewDocumentWindow.REQUEST_REGULATION_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.REQUEST_REGULATION_NAME_LOCATOR,
            SoglNewDocumentWindow.REQUEST_CHANGE_INFO_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.REQUEST_CHANGE_INFO_NAME_LOCATOR,
            SoglNewDocumentWindow.CLOSE_BUTTON_LOCATOR,
            SoglNewDocumentWindow.CONTINUE_BUTTON_LOCATOR,
            ]

        for i in window_elements:
            self.is_element_present(*i)

    def should_be_correct_elements_sogl_new_window(self):
        self.work_with_windows(1)
        window_elements = [
            SoglNewDocumentWindow.OUTGOING_DOCUMENT_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.OUTGOING_DOCUMENT_NAME_LOCATOR,
            SoglNewDocumentWindow.OUTGOING_OG_DOCUMENT_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.OUTGOING_OG_DOCUMENT_NAME_LOCATOR,
            SoglNewDocumentWindow.ENTER_DOCUMENT_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.ENTER_DOCUMENT_NAME_LOCATOR,
            SoglNewDocumentWindow.ORD_DOCUMENT_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.ORD_DOCUMENT_NAME_LOCATOR,
            SoglNewDocumentWindow.REQUEST_DOCUMENT_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.REQUEST_DOCUMENT_NAME_LOCATOR,
            SoglNewDocumentWindow.CLOSE_BUTTON_LOCATOR,
            SoglNewDocumentWindow.CONTINUE_BUTTON_LOCATOR,
            ]
        
        for i in window_elements:
            self.is_element_present(*i)
    
    def choose_request_document(self):
        self.click_to(*SoglNewDocumentWindow.REQUEST_DOCUMENT_NAME_LOCATOR)
        self.click_to(*SoglNewDocumentWindow.CONTINUE_BUTTON_LOCATOR)
    
    def choose_request_regulation_document(self):
        self.click_to(*SoglNewDocumentWindow.REQUEST_REGULATION_NAME_LOCATOR)
        self.click_to(*SoglNewDocumentWindow.CONTINUE_BUTTON_LOCATOR)
        self.work_with_windows(0)
    
    def choose_request_request_document(self):
        self.click_to(*SoglNewDocumentWindow.REQUEST_REQUEST_NAME_LOCATOR)
        self.click_to(*SoglNewDocumentWindow.CONTINUE_BUTTON_LOCATOR)
        self.work_with_windows(0)
    
    def choose_request_change_responsible_info_document(self):
        self.click_to(*SoglNewDocumentWindow.REQUEST_CHANGE_INFO_NAME_LOCATOR)
        self.click_to(*SoglNewDocumentWindow.CONTINUE_BUTTON_LOCATOR)
        self.work_with_windows(0)

    def open_sogl_document_block(self):
        locator = MainPageLocators.SOGL_BLOCK_SLIDE_DOWN_BUTTON

        if self.is_active(*locator, timeout=0) == True:
            self.driver.find_element(*locator).click()
    
    def go_to_sogl_block_all_documents(self):
        self.open_sogl_document_block()
        self.click_to(*MainPageLocators.SOGL_BLOCK_ALL_DOCUMENT_LINK)
    
    def go_to_sogl_block_new_document(self):
        self.open_sogl_document_block()
        self.click_to(*MainPageLocators.SOGL_BLOCK_NEW_DOCUMENT_LINK)
    
