from .locators import ElSignatureLocators
from .main_functions import MainFunc

class ElSignExtensionPage(MainFunc):
    def __init__(self, driver, link):
        super().__init__(driver, link)
        self.server = MainFunc.config("server")
        self.el_sign_extension = ElSignatureLocators().extention
    
    def add_url(self):
        trys = 0
        while self.is_active(*self.el_sign_extension.delete_url_button(self.server), 0) == False:
            if trys > 10:
                assert False
            self.fill_field(*self.el_sign_extension.ENTER_URL_INPUT_LOCATOR, self.server)
            self.click_to(*self.el_sign_extension.ADD_BUTTON_LOCATOR)
            self.click_to(*self.el_sign_extension.SAVE_BUTTON_LOCATOR)
            trys += 1

    def delete_url(self):
        self.click_to(*self.el_sign_extension.delete_url_button(self.server))
        assert self.is_not_element_present(*self.el_sign_extension.delete_url_button(self.server))
        self.click_to(*self.el_sign_extension.SAVE_BUTTON_LOCATOR)


class ElSignFixtures:
    def __init__(self, driver):
        self.driver = driver

    def open_link(self):
        link = MainFunc.config("path_to_crypto_pro_config")
        page = ElSignExtensionPage(self.driver, link)
        page.open()
        return page
    
    def ep_setup(self):
        page = self.open_link()
        page.add_url()
    
    def ep_teardown(self):
        page = self.open_link()
        page.delete_url()
