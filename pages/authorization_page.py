from .main_functions import MainFunc
from .locators import AuthPageLocators


class AuthPage(MainFunc):
    def __init__(self, driver, link="", el_sign=False):
        super().__init__(driver, link)

        if el_sign == False:
            self.org_id = MainFunc.config("organisation")
        else:
            self.org_id = MainFunc.config("organisation_ep")
        
        self.password = MainFunc.config("password")
        self.value = {
            "u_ep": "user_ep_id",
            "a_ep": "admin_ep_id",

            "a": "admin_id",
            "awn": "admin_without_nomenclature_id",
            "u": "user_id",
            "mou": "mo_user_id",
            None: "superadmin_id"
        }

    def choose_org(self):
        self.work_with_selector(
            *AuthPageLocators.SELECT_ORG_LOCATOR, self.org_id)

    def choose_user(self, value):
        self.work_with_selector(*AuthPageLocators.SELECT_USR_LOCATOR, value)

    def enter_password(self):
        self.fill_field(*AuthPageLocators.ENTER_PASSWORD_LOCATOR, self.password)

    def click_to_enter_button(self):
        self.click_to(*AuthPageLocators.ENTER_BUTTON_LOCATOR)

    def enter_in_account(self, root=None):
        def if_passwerd_not_entred():
            self.enter_password()
            url = self.driver.current_url
            self.click_to_enter_button()

            return url

        self.choose_org()
        self.choose_user(MainFunc.config(self.value[root]))

        url, count = if_passwerd_not_entred(), 0
        while self.url_change(url, 15) == False:
            if count > 10:
                assert False
            url = if_passwerd_not_entred()
            count += 1
