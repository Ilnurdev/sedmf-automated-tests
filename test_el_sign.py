import pytest
from pages.urls import URLs
from pages.authorization_page import AuthPage
from pages.ep_url_add_page import ElSignFixtures
from pages.main_functions import MainFunc
from pages.all_document_fields_page import AllDocumentFieldPage
from pages.main_page import MainPage


def setup(driver, root=None):
    link = URLs.AUTH_LINK
    page = AuthPage(driver, link, True)
    page.open()
    page.enter_in_account(root)

@pytest.mark.el_sign
class TestElSignature:
    @pytest.mark.dependency()
    def test_setup(self, driver):
        ep = ElSignFixtures(driver)
        ep.ep_setup()

    @pytest.mark.dependency(depends=["TestElSignature::test_setup"])
    def test_out_sogl_sign(self, driver):
        setup(driver, "u_ep")
        link = MainFunc.take_DNSID(URLs.OUT_SOGL_LINK, driver.current_url)
        page = AllDocumentFieldPage(driver, link)
        page.open()
        page.fill_in_all_document_required_fields(3, 4, 3)
        page.should_be_short_content_fields()
        page.fill_short_content_field("Автотест ЭП")
        page.should_be_save_button()
        page.add_files()
        page.save_rcd()
        page.create_and_send_agree_sheet(approve_with_ep=True)
        page.should_be_correct_el_sign_img()
        page.should_be_etalon_el_sign_img()
        page.click_to_register_pictogram()
        page.save_rcd()
        page.should_be_etalon_el_sign_img()
    
    @pytest.mark.dependency(depends=["TestElSignature::test_setup"])
    def test_enter_sogl_sign(self, driver):
        setup(driver, "u_ep")
        link = MainFunc.take_DNSID(URLs.ENTER_SOGL_LINK, driver.current_url)
        page = AllDocumentFieldPage(driver, link)
        page.open()
        page.fill_in_all_document_required_fields(3, 5, 2)
        page.should_be_short_content_fields()
        page.fill_short_content_field("Автотест ЭП")
        page.should_be_save_button()
        page.add_files()
        page.save_rcd()
        page.create_and_send_agree_sheet(approve_with_ep=True)
        page.should_be_correct_el_sign_img()
        page.should_be_etalon_el_sign_img()
        page.click_to_register_pictogram()
        page.save_rcd()
        page.should_be_etalon_el_sign_img()
    
    @pytest.mark.dependency(depends=["TestElSignature::test_setup"])
    def test_ord_sogl_sign(self, driver):
        setup(driver, "u_ep")
        link = MainFunc.take_DNSID(URLs.ORD_SOGL_LINK, driver.current_url)
        page = AllDocumentFieldPage(driver, link)
        page.open()
        page.fill_in_all_document_required_fields(3, 5, 2, ord=True)
        page.should_be_short_content_fields()
        page.fill_short_content_field("Автотест ЭП")
        page.add_files()
        page.should_be_save_button()
        page.save_rcd()
        page.create_and_send_agree_sheet(approve_with_ep=True, add_user=3)
        page.should_be_correct_el_sign_img()
        page.should_be_etalon_el_sign_img()
        page.click_to_register_pictogram()
        page.save_rcd()
        page.should_be_etalon_el_sign_img()
    
    @pytest.mark.dependency(depends=["TestElSignature::test_setup"])
    def test_out_og_sogl_sign(self, driver):
        setup(driver, "u_ep")
        link = MainFunc.take_DNSID(URLs.OUT_OG_SOGL_LINK, driver.current_url)
        page = AllDocumentFieldPage(driver, link)
        page.open()
        page.fill_in_all_document_required_fields(3, 5, 2, og=True)
        page.should_be_appeal_author_fields()
        page.should_be_review_result_fields()
        page.should_be_short_content_fields()
        page.fill_appeal_author_field()
        page.fill_review_result_field(42)
        page.fill_short_content_field("Автотест ЭП")
        page.add_files()
        page.should_be_save_button()
        page.save_rcd()
        page.create_and_send_agree_sheet(approve_with_ep=True)
        page.should_be_correct_el_sign_img()
        page.should_be_etalon_el_sign_img()
        page.click_to_register_pictogram()
        page.save_rcd()
        page.should_be_etalon_el_sign_img()


    @pytest.mark.dependency(depends=["TestElSignature::test_setup"])
    def test_teardown(self, driver):
        ep = ElSignFixtures(driver)
        ep.ep_teardown()
