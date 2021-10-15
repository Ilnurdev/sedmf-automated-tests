import pytest
from pages.urls import URLs
from pages.authorization_page import AuthPage
from pages.ep_url_add_page import ElSignFixtures
from pages.main_functions import MainFunc
from pages.all_document_fields_page import AllDocumentFieldPage
from pages.value_for_fields import AgreeSheetValues
from pages.sogls_page import OutSogl
from pages.enter_documets_page import OutDocumentsPage


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
    @pytest.mark.parametrize("url,req,comment,solution,remark,user", [
        pytest.param(URLs.OUT_SOGL_LINK, [3, 4, 3, False, False], AgreeSheetValues.SIGN, 1, False, False, id="Out_document: Sign"),
        pytest.param(URLs.OUT_SOGL_LINK, [3, 4, 3, False, False], AgreeSheetValues.SIGN_COMMENT, 1, AgreeSheetValues.REMARK, False, id="Out_document: Sign with comment"),
        pytest.param(URLs.OUT_SOGL_LINK, [3, 4, 3, False, False], AgreeSheetValues.REFUSE, 2, False, False, id="Out_document: Refuse"),
        pytest.param(URLs.OUT_SOGL_LINK, [3, 4, 3, False, False], AgreeSheetValues.REFUSE_COMMENT, 2, AgreeSheetValues.REMARK, False, id="Out_document: Refuse with comment"),
        pytest.param(URLs.OUT_SOGL_LINK, [3, 4, 3, False, False], AgreeSheetValues.REFUSE_DOCUMENT, 2, None, False, id="Out_document: Refuse with document"),

        pytest.param(URLs.ENTER_SOGL_LINK, [3, 5, 2, False, False], AgreeSheetValues.SIGN, 1, False, False, id="Enter_document: Sign"),
        pytest.param(URLs.ENTER_SOGL_LINK, [3, 5, 2, False, False], AgreeSheetValues.SIGN_COMMENT, 1, AgreeSheetValues.REMARK, False, id="Enter_document: Sign with comment"),
        pytest.param(URLs.ENTER_SOGL_LINK, [3, 5, 2, False, False], AgreeSheetValues.REFUSE, 2, False, False, id="Enter_document: Refuse"),
        pytest.param(URLs.ENTER_SOGL_LINK, [3, 5, 2, False, False], AgreeSheetValues.REFUSE_COMMENT, 2, AgreeSheetValues.REMARK, False, id="Enter_document: Refuse with comment"),
        pytest.param(URLs.ENTER_SOGL_LINK, [3, 5, 2, False, False], AgreeSheetValues.REFUSE_DOCUMENT, 2, None, False, id="Enter_document: Refuse with document"),

        pytest.param(URLs.ORD_SOGL_LINK, [3, 5, 2, True, False], AgreeSheetValues.SIGN, 1, False, 3, id="ORD_document: Sign"),
        pytest.param(URLs.ORD_SOGL_LINK, [3, 5, 2, True, False], AgreeSheetValues.SIGN_COMMENT, 1, AgreeSheetValues.REMARK, 3, id="ORD_document: Sign with comment"),
        pytest.param(URLs.ORD_SOGL_LINK, [3, 5, 2, True, False], AgreeSheetValues.REFUSE, 2, False, 3, id="ORD_document: Refuse"),
        pytest.param(URLs.ORD_SOGL_LINK, [3, 5, 2, True, False], AgreeSheetValues.REFUSE_COMMENT, 2, AgreeSheetValues.REMARK, 3, id="ORD_document: Refuse with comment"),
        pytest.param(URLs.ORD_SOGL_LINK, [3, 5, 2, True, False], AgreeSheetValues.REFUSE_DOCUMENT, 2, None, 3, id="ORD_document: Refuse with document"),
    ])
    def test_sogls_sign(self, driver, url, req, comment, solution, remark, user):
        setup(driver, "u_ep")
        link = MainFunc.take_DNSID(url, driver.current_url)
        page = AllDocumentFieldPage(driver, link)
        page.open()
        page.fill_in_all_document_required_fields(*req)
        page.should_be_short_content_fields()
        page.fill_short_content_field(comment)
        page.add_files()
        page.should_be_save_button()
        page.save_rcd()
        page.create_and_send_agree_sheet(solution=solution, with_ep=True, remark=remark, add_user=user)
        page.save_and_check_ep(solution)
    
    @pytest.mark.dependency(depends=["TestElSignature::test_setup"])
    @pytest.mark.parametrize("comment,solution,remark", [
        pytest.param(AgreeSheetValues.SIGN, 1, False, id="Out_OG_document: Sign"),
        pytest.param(AgreeSheetValues.SIGN_COMMENT, 1, AgreeSheetValues.REMARK, id="Out_OG_document: Sign with comment"),
        pytest.param(AgreeSheetValues.REFUSE, 2, False, id="Out_OG_document: Refuse"),
        pytest.param(AgreeSheetValues.REFUSE_COMMENT, 2, AgreeSheetValues.REMARK, id="Out_OG_document: Refuse with comment"),
        pytest.param(AgreeSheetValues.REFUSE_DOCUMENT, 2, None, id="Out_OG_document: Refuse with document"),
    ])
    def test_out_og_sogl_sign(self, driver, comment, solution, remark):
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
        page.fill_short_content_field(comment)
        page.add_files()
        page.should_be_save_button()
        page.save_rcd()
        page.create_and_send_agree_sheet(solution=solution, with_ep=True, remark=remark)
        page.save_and_check_ep(solution)
    
    @pytest.mark.dependency(depends=["TestElSignature::test_setup"])
    def test_attesting_sign(self, driver):
        setup(driver, "u_ep")
        link = MainFunc.take_DNSID(URLs.OUT_SOGL_LINK, driver.current_url)
        page = AllDocumentFieldPage(driver, link)
        out_sogl_page = OutSogl(driver)
        out_doc_page = OutDocumentsPage(driver)
        page.open()
        page.fill_in_all_document_required_fields(6, 7, 3)
        page.should_be_short_content_fields()
        page.fill_short_content_field("Автотест заверить")
        page.add_files()
        page.should_be_save_button()
        out_sogl_page.fill_document_kind_field(410)
        page.save_rcd(2)
        page.create_and_send_agree_sheet(solution=3)
        page.click_to_register_pictogram()
        page.save_rcd()
        out_doc_page.click_to_attesting_button()
        page.should_be_etalon_el_sign_img()

    @pytest.mark.dependency(depends=["TestElSignature::test_setup"])
    def test_teardown(self, driver):
        ep = ElSignFixtures(driver)
        ep.ep_teardown()
