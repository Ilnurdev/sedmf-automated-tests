from pages.main_functions import MainFunc
from pages.authorization_page import AuthPage


AUTH_LINK = "http://release9.sedmf-pg/auth.php"
SA_VALUE = "877523"


class TestAuthorizationForm:
    def test_auth_sa(self, driver):
        link = AUTH_LINK
        page = AuthPage(driver, link)
        page.open()
        page.choose_org()
        page.choose_user(SA_VALUE)
        page.enter_password()
        page.click_to_enter_button()

