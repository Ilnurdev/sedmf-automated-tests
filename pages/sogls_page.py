from .main_functions import MainFunc
from .locators import SoglLocators


class OutSogl(MainFunc):
    def __init__(self, driver, link=""):
        super().__init__(driver, link)

        self.out_loc = SoglLocators().out_sogl

    def should_be_document_kind_field(self):
        self.is_element_present(*self.out_loc.DOCUMENT_KIND_LOCATOR)
    
    def fill_document_kind_field(self, value):
        locator = self.out_loc.DOCUMENT_KIND_LOCATOR
        self.is_element_present(*locator)
        self.work_with_selector(*locator, value=str(value))
