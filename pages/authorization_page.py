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
        def if_passwerd_not_entred():
            self.enter_password()
            url = self.driver.current_url
            self.click_to_enter_button()

            return url

        value = {
            "a": "admin",
            "awn": "admin_without_nomenclature",
            "u": "user",
            "mou": "mo_user",
            None: "superadmin"
        }

        self.choose_org()
        self.choose_user(MainFunc.config(value[root]))
        url = if_passwerd_not_entred()

        count = 3
        while self.url_change(url, 15) == False and count != 0:
            url = if_passwerd_not_entred()
            count != 3
