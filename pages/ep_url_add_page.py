from .locators import ElSignExtentionsLocators
from .main_functions import MainFunc

class ElSignExtensionPage(MainFunc):
    URL = MainFunc.config("server")
    
    def add_url(self):
        self.fill_field(*ElSignExtentionsLocators.ENTER_URL_INPUT_LOCATOR, self.URL)
        self.click_to(*ElSignExtentionsLocators.ADD_BUTTON_LOCATOR)
        assert self.is_active(*ElSignExtentionsLocators.delete_url_button(self.URL))
        self.click_to(*ElSignExtentionsLocators.SAVE_BUTTON_LOCATOR)

    def delete_url(self):
        self.click_to(*ElSignExtentionsLocators.delete_url_button(self.URL))
        assert self.is_not_element_present(*ElSignExtentionsLocators.delete_url_button(self.URL))
        self.click_to(*ElSignExtentionsLocators.SAVE_BUTTON_LOCATOR)
        
    
    def added_test(self):
        assert self.is_active(*ElSignExtentionsLocators.delete_url_button(self.URL))
    
    def is_empty(self):
        assert self.is_not_element_present(*ElSignExtentionsLocators.delete_url_button(self.URL), 3)