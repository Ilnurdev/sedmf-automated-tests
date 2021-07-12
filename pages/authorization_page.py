from .main_functions import MainFunc
from .locators import AuthPageLocators


ORG_VALUE = MainFunc.config("organisation")
CORRECT_PASSWORD = MainFunc.config("password")


class AuthPage(MainFunc):
    def choose_org(self):
        self.work_with_selector(
            *AuthPageLocators.SELECT_ORG_LOCATOR, ORG_VALUE)

    def choose_user(self, value):
        self.work_with_selector(*AuthPageLocators.SELECT_USR_LOCATOR, value)

    def enter_password(self):
        password = self.driver.find_element(
            *AuthPageLocators.ENTER_PASSWORD_LOCATOR)
        password.send_keys(CORRECT_PASSWORD)

    def click_to_enter_button(self):
        enter_button = self.driver.find_element(
            *AuthPageLocators.ENTER_BUTTON_LOCATOR)
        enter_button.click()

    def enter_in_account(self, root=None):
        if root == "a":
            value = MainFunc.config("admin")
        elif root == "awn":
            value = MainFunc.config("a_without_nomenclature")
        elif root == "u":
            value = MainFunc.config("user")
        elif root == "mou":
            value = MainFunc.config("mo_u")
        else:
            value = MainFunc.config("superadmin")

        self.choose_org()
        self.choose_user(value)
        self.enter_password()
        url = self.driver.current_url
        self.click_to_enter_button()
        self.url_change(url)
