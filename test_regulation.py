import pytest
from pages.main_functions import MainFunc
from pages.urls import URLs
from pages.value_for_fields import RegulationFields
from pages.authorization_page import AuthPage
from pages.all_document_fields_page import AllDocumentFieldPage
from pages.enter_documets_page import EnterDocumentsPage
from pages.regulation_document_page import RegulationDocumentPage, ChangeResponsibleInfo, RegulationRefuseDocument, RegulationChainShowInstrument
from pages.main_page import SoglDocumentsBlock


def setup(driver, root=None):
    link = URLs.AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account(root)


@pytest.mark.regulation
class TestUIDocumentOpenLink:
    def test_open_regulation_document(self, driver):
        setup(driver)
        page = SoglDocumentsBlock(driver)
        page.go_to_sogl_block_new_document()
        page.should_be_correct_elements_sogl_new_window()
        page.choose_request_block_documents(1)
        page.should_be_correct_elements_sogl_request_new_window()
        page.choose_request_block_documents(2)

        page = AllDocumentFieldPage(driver)
        page.should_be_required_fields(RegulationFields.SOGL_TITLE)
        page.should_be_correct_url(URLs.REGULATION_LINK)
        page = RegulationDocumentPage(driver)
        page.should_be_closed_short_content_fields(1)

    def test_open_change_info_document(self, driver):
        setup(driver)
        page = SoglDocumentsBlock(driver)
        page.go_to_sogl_block_new_document()
        page.should_be_correct_elements_sogl_new_window()
        page.choose_request_block_documents(1)
        page.should_be_correct_elements_sogl_request_new_window()
        page.choose_request_block_documents(4)

        page = AllDocumentFieldPage(driver)
        page.should_be_required_fields(RegulationFields.SOGL_TITLE)
        page.should_be_correct_url(URLs.CHANGE_INFO_LINK)
        page = RegulationDocumentPage(driver)
        page.should_be_closed_short_content_fields(1)


@pytest.mark.regulation
class TestRegulation:
    NPA_ID = None

    @pytest.mark.parametrize("npa_number,regulation_type,first", [
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_1, True, marks=[
                     pytest.mark.dependency(name="1-1"), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_4, False, marks=[
                     pytest.mark.dependency(name="1-4", depends=["1-1"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_7, False, marks=[
                     pytest.mark.dependency(name="1-7", depends=["1-4"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_14, False, marks=[
                     pytest.mark.dependency(name="1-14", depends=["1-7"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_22, False, marks=[
                     pytest.mark.dependency(name="1-22", depends=["1-14"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_23, False, marks=[
                     pytest.mark.dependency(name="1-23", depends=["1-22"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_24, False, marks=[
                     pytest.mark.dependency(name="1-24", depends=["1-23"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_28, False, marks=[
                     pytest.mark.dependency(name="1-28", depends=["1-24"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),

        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_7, True, marks=[
                     pytest.mark.dependency(name="2-7"), pytest.mark.reg_851, pytest.mark.reg_chain_2]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_14, False, marks=[
                     pytest.mark.dependency(name="2-14", depends=["2-7"]), pytest.mark.reg_851, pytest.mark.reg_chain_2]),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_22, False, marks=[
                     pytest.mark.dependency(name="2-22", depends=["2-14"]), pytest.mark.reg_851, pytest.mark.reg_chain_2]),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_23, False, marks=[
                     pytest.mark.dependency(name="2-23", depends=["2-22"]), pytest.mark.reg_851, pytest.mark.reg_chain_2]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_24, False, marks=[
                     pytest.mark.dependency(name="2-24", depends=["2-23"]), pytest.mark.reg_851, pytest.mark.reg_chain_2]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_28, False, marks=[
                     pytest.mark.dependency(name="2-28", depends=["2-24"]), pytest.mark.reg_851, pytest.mark.reg_chain_2]),

        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_1, True, marks=[
                     pytest.mark.dependency(name="3-1"), pytest.mark.reg_851, pytest.mark.reg_chain_3]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_4, False, marks=[
                     pytest.mark.dependency(name="3-4", depends=["3-1"]), pytest.mark.reg_851, pytest.mark.reg_chain_3]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_8, False, marks=[
                     pytest.mark.dependency(name="3-8", depends=["3-4"]), pytest.mark.reg_851, pytest.mark.reg_chain_3]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_15, False, marks=[
                     pytest.mark.dependency(name="3-15", depends=["3-8"]), pytest.mark.reg_851, pytest.mark.reg_chain_3]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_24, False, marks=[
                     pytest.mark.dependency(name="3-24", depends=["3-15"]), pytest.mark.reg_851, pytest.mark.reg_chain_3]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_28, False, marks=[
                     pytest.mark.dependency(name="3-28", depends=["3-24"]), pytest.mark.reg_851, pytest.mark.reg_chain_3]),

        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_8, True, marks=[
                     pytest.mark.dependency(name="4-8"), pytest.mark.reg_851, pytest.mark.reg_chain_4]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_15, False, marks=[
                     pytest.mark.dependency(name="4-15", depends=["4-8"]), pytest.mark.reg_851, pytest.mark.reg_chain_4]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_24, False, marks=[
                     pytest.mark.dependency(name="4-24", depends=["4-15"]), pytest.mark.reg_851, pytest.mark.reg_chain_4]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_28, False, marks=[
                     pytest.mark.dependency(name="4-28", depends=["4-24"]), pytest.mark.reg_851, pytest.mark.reg_chain_4]),

        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_9, True, marks=[
                     pytest.mark.dependency(name="5-22"), pytest.mark.reg_851, pytest.mark.reg_chain_5]),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_23, False, marks=[
                     pytest.mark.dependency(name="5-23", depends=["5-22"]), pytest.mark.reg_851, pytest.mark.reg_chain_5]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_24, False, marks=[
                     pytest.mark.dependency(name="5-24", depends=["5-23"]), pytest.mark.reg_851, pytest.mark.reg_chain_5]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_28, False, marks=[
                     pytest.mark.dependency(name="5-28", depends=["5-24"]), pytest.mark.reg_851, pytest.mark.reg_chain_5]),

        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_2, True, marks=[
                     pytest.mark.dependency(name="6-2"), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_5, False, marks=[
                     pytest.mark.dependency(name="6-5", depends=["6-2"]), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_10, False, marks=[
                     pytest.mark.dependency(name="6-10", depends=["6-5"]), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_16, False, marks=[
                     pytest.mark.dependency(name="6-16", depends=["6-10"]), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_20, False, marks=[
                     pytest.mark.dependency(name="6-20", depends=["6-16"]), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_25, False, marks=[
                     pytest.mark.dependency(name="6-25", depends=["6-20"]), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_29, False, marks=[
                     pytest.mark.dependency(name="6-29", depends=["6-25"]), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),

        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_10, True, marks=[
                     pytest.mark.dependency(name="7-10"), pytest.mark.reg_1318, pytest.mark.reg_chain_7]),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_16, False, marks=[
                     pytest.mark.dependency(name="7-16", depends=["7-10"]), pytest.mark.reg_1318, pytest.mark.reg_chain_7]),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_20, False, marks=[
                     pytest.mark.dependency(name="7-20", depends=["7-16"]), pytest.mark.reg_1318, pytest.mark.reg_chain_7]),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_25, False, marks=[
                     pytest.mark.dependency(name="7-25", depends=["7-20"]), pytest.mark.reg_1318, pytest.mark.reg_chain_7]),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_29, False, marks=[
                     pytest.mark.dependency(name="7-29", depends=["7-25"]), pytest.mark.reg_1318, pytest.mark.reg_chain_7]),

        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_11, True, marks=[
                     pytest.mark.dependency(name="8-11"), pytest.mark.reg_1318, pytest.mark.reg_chain_8]),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_17, False, marks=[
                     pytest.mark.dependency(name="8-17", depends=["8-11"]), pytest.mark.reg_1318, pytest.mark.reg_chain_8]),
        pytest.param(RegulationFields.NPA_1318, RegulationFields.REGULATION_TYPE_1318_21, False, marks=[
                     pytest.mark.dependency(name="8-21", depends=["8-17"]), pytest.mark.reg_1318, pytest.mark.reg_chain_8]),

        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_3, True, marks=[
                     pytest.mark.dependency(name="9-3"), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_6, False, marks=[
                     pytest.mark.dependency(name="9-6", depends=["9-3"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_12, False, marks=[
                     pytest.mark.dependency(name="9-12", depends=["9-6"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_18, False, marks=[
                     pytest.mark.dependency(name="9-18", depends=["9-12"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_22, False, marks=[
                     pytest.mark.dependency(name="9-22", depends=["9-18"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_23, False, marks=[
                     pytest.mark.dependency(name="9-23", depends=["9-22"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_26, False, marks=[
                     pytest.mark.dependency(name="9-26", depends=["9-23"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_30, False, marks=[
                     pytest.mark.dependency(name="9-30", depends=["9-26"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),

        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_12, True, marks=[
                     pytest.mark.dependency(name="10-12"), pytest.mark.reg_373, pytest.mark.reg_chain_10]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_18, False, marks=[
                     pytest.mark.dependency(name="10-18", depends=["10-12"]), pytest.mark.reg_373, pytest.mark.reg_chain_10]),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_22, False, marks=[
                     pytest.mark.dependency(name="10-22", depends=["10-18"]), pytest.mark.reg_373, pytest.mark.reg_chain_10]),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_23, False, marks=[
                     pytest.mark.dependency(name="10-23", depends=["10-22"]), pytest.mark.reg_373, pytest.mark.reg_chain_10]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_26, False, marks=[
                     pytest.mark.dependency(name="10-26", depends=["10-23"]), pytest.mark.reg_373, pytest.mark.reg_chain_10]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_30, False, marks=[
                     pytest.mark.dependency(name="10-30", depends=["10-26"]), pytest.mark.reg_373, pytest.mark.reg_chain_10]),

        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_3, True, marks=[
                     pytest.mark.dependency(name="11-3"), pytest.mark.reg_373, pytest.mark.reg_chain_11]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_6, False, marks=[
                     pytest.mark.dependency(name="11-6", depends=["11-3"]), pytest.mark.reg_373, pytest.mark.reg_chain_11]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_13, False, marks=[
                     pytest.mark.dependency(name="11-13", depends=["11-6"]), pytest.mark.reg_373, pytest.mark.reg_chain_11]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_19, False, marks=[
                     pytest.mark.dependency(name="11-19", depends=["11-13"]), pytest.mark.reg_373, pytest.mark.reg_chain_11]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_26, False, marks=[
                     pytest.mark.dependency(name="11-26", depends=["11-19"]), pytest.mark.reg_373, pytest.mark.reg_chain_11]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_30, False, marks=[
                     pytest.mark.dependency(name="11-30", depends=["11-26"]), pytest.mark.reg_373, pytest.mark.reg_chain_11]),

        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_13, True, marks=[
                     pytest.mark.dependency(name="12-13"), pytest.mark.reg_373, pytest.mark.reg_chain_12]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_19, False, marks=[
                     pytest.mark.dependency(name="12-19", depends=["12-13"]), pytest.mark.reg_373, pytest.mark.reg_chain_12]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_26, False, marks=[
                     pytest.mark.dependency(name="12-26", depends=["12-19"]), pytest.mark.reg_373, pytest.mark.reg_chain_12]),
        pytest.param(RegulationFields.NPA_373, RegulationFields.REGULATION_TYPE_373_30, False, marks=[
                     pytest.mark.dependency(name="12-30", depends=["12-26"]), pytest.mark.reg_373, pytest.mark.reg_chain_12]),

        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_22, True, marks=[
                     pytest.mark.dependency(name="13-22"), pytest.mark.reg_96]),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_23, False, marks=[
                     pytest.mark.dependency(name="13-23", depends=["13-22"]), pytest.mark.reg_96]),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_27, False, marks=[
                     pytest.mark.dependency(name="13-27", depends=["13-23"]), pytest.mark.reg_96]),
        pytest.param(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_31, False, marks=[
                     pytest.mark.dependency(name="13-31", depends=["13-27"]), pytest.mark.reg_96]),

        pytest.param(RegulationFields.NPA_83, RegulationFields.REGULATION_TYPE_83_32, True, marks=[
                     pytest.mark.dependency(name="14-32"), pytest.mark.reg_83]),
        pytest.param(RegulationFields.NPA_83, RegulationFields.REGULATION_TYPE_83_33, False, marks=[
                     pytest.mark.dependency(name="14-33", depends=["14-32"]), pytest.mark.reg_83]),
        pytest.param(RegulationFields.NPA_83, RegulationFields.REGULATION_TYPE_83_34, False, marks=[
                     pytest.mark.dependency(name="14-34", depends=["14-33"]), pytest.mark.reg_83]),
    ])
    def test_regulation_document(self, driver, npa_number, regulation_type, first):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(npa_number, regulation_type,
                            TestRegulation.NPA_ID, False, first)
        page.regulation_doc(npa_number, regulation_type,
                            TestRegulation.NPA_ID, True, first)
        page.should_be_correct_saved_file()
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        index = page.modify_npa_type(regulation_type, 1)
        page.register_and_send_enter_regulation_document(
            page.check_regulation_doc, index, TestRegulation.NPA_ID, first)
        page.send_medo()

        TestRegulation.NPA_ID = page.create_and_send_answer(
            index, TestRegulation.NPA_ID, first)


@pytest.mark.regulation
@pytest.mark.change_info
class TestChangeInfoResponsibleDocument:
    NPA_ID = None

    @pytest.mark.parametrize("npa_number,regulation_type,first", [
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_1,
                     True, marks=pytest.mark.dependency(name="1-1")),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_4,
                     False, marks=pytest.mark.dependency(name="1-4", depends=["1-1"])),
    ])
    def test_regulation_document(self, driver, npa_number, regulation_type, first):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(npa_number, regulation_type,
                            TestChangeInfoResponsibleDocument.NPA_ID, False, first)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        index = page.modify_npa_type(regulation_type, 1)
        page.register_and_send_enter_regulation_document()
        page.send_medo()

        TestChangeInfoResponsibleDocument.NPA_ID = page.create_and_send_answer(
            index, TestChangeInfoResponsibleDocument.NPA_ID, first)

    @pytest.mark.dependency(depends=["1-4"])
    def test_change_info(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.CHANGE_INFO_LINK, driver.current_url)
        page = ChangeResponsibleInfo(driver, link)
        page.open()
        page.change_responsible_info_doc(
            False, TestChangeInfoResponsibleDocument.NPA_ID)
        page.change_responsible_info_doc(
            True, TestChangeInfoResponsibleDocument.NPA_ID)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = ChangeResponsibleInfo(driver, link)
        page.open()
        page.register_and_send_enter_change_info_document(
            TestChangeInfoResponsibleDocument.NPA_ID)


@pytest.mark.regulation
@pytest.mark.regulation_refuse
class TestRegulationRefuse:
    NPA_ID = None

    # Отказ - заявка первая
    def test_regulation_refuse_1_1_doc(self, driver):
        setup(driver)

        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationRefuseDocument(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_1,
                            TestRegulationRefuse.NPA_ID, False, True)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationRefuseDocument(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()
        doc_id = page.save_document_id()

        page.create_refuse_document(
            RegulationFields.REGULATION_TYPE_851_1, doc_id)
        page.create_and_send_agree_sheet()
        page.register_and_send_refuse_document(doc_id)

    # Отказ - заявка НЕ первая, не имеет обязательного ответа

    @pytest.mark.dependency()
    def test_regulation_refuse_2_1_doc(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_1,
                            TestRegulationRefuse.NPA_ID, False, True)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()

        TestRegulationRefuse.NPA_ID = page.create_and_send_answer(page.modify_npa_type(
            RegulationFields.REGULATION_TYPE_851_1, 1), TestRegulationRefuse.NPA_ID, True)

    @pytest.mark.dependency(depends=["TestRegulationRefuse::test_regulation_refuse_2_1_doc"])
    def test_regulation_refuse_2_2_doc(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_4,
                            TestRegulationRefuse.NPA_ID, False, False)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")

        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationRefuseDocument(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()
        doc_id = page.save_document_id()

        page.create_refuse_document(
            RegulationFields.REGULATION_TYPE_851_4, doc_id)
        page.create_and_send_agree_sheet()
        page.register_and_send_refuse_document(doc_id)

    # Отказ - заявка НЕ первая, имеет обязательный ответ

    @pytest.mark.parametrize("npa_number,regulation_type,first", [
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_1, True, marks=[
                     pytest.mark.dependency(name="refuse-1-1")]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_4, False, marks=[
                     pytest.mark.dependency(name="refuse-1-4", depends=["refuse-1-1"])]),
    ])
    def test_regulation_refuse_3_doc(self, driver, npa_number, regulation_type, first):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(npa_number, regulation_type,
                            TestRegulationRefuse.NPA_ID, False, first)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()

        TestRegulationRefuse.NPA_ID = page.create_and_send_answer(
            page.modify_npa_type(regulation_type, 1), TestRegulationRefuse.NPA_ID, first)

    @pytest.mark.dependency(depends=["refuse-1-4"])
    def test_regulation_refuse_3_2_doc(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_7,
                            TestRegulationRefuse.NPA_ID, False, False)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationRefuseDocument(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()
        doc_id = page.save_document_id()

        page.create_refuse_document(
            RegulationFields.REGULATION_TYPE_851_7, doc_id)
        page.create_and_send_agree_sheet()
        page.register_and_send_refuse_document(doc_id)


@pytest.mark.regulation
@pytest.mark.regulation_chain_show
class TestRegulationChainShowInstrument:
    NPA_ID = None
    doc_id = None

    @pytest.mark.dependency()
    def test_chain_show_index_22(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationChainShowInstrument(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_22,
                            TestRegulationChainShowInstrument.NPA_ID, False, True, False)

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 1,
                        1, RegulationFields.REGULATION_TYPE_96_22, False, False, 1)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 2,
                        1, RegulationFields.REGULATION_TYPE_96_22, True, False, 1)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 3,
                        1, RegulationFields.REGULATION_TYPE_96_22, False, False, 1)

        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 4,
                        1, RegulationFields.REGULATION_TYPE_96_22, False, False, 1)

        npa_id = page.create_answer(page.have_answer(page.modify_npa_type(
            RegulationFields.REGULATION_TYPE_96_22, 1)), True, TestRegulationChainShowInstrument.NPA_ID)

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 5,
                        1, RegulationFields.REGULATION_TYPE_96_22, False, False, 1)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 6,
                        1, RegulationFields.REGULATION_TYPE_96_22, True, False, 1)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 7,
                        1, RegulationFields.REGULATION_TYPE_96_22, False, False, 1)

        page.register_and_send_enter_regulation_document(answer=True)
        page.agree_with_popup_window_enter_doc()

        TestRegulationChainShowInstrument.NPA_ID = npa_id
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 8, 1,
                        RegulationFields.REGULATION_TYPE_96_22, False, False, 1, RegulationFields.REGULATION_TYPE_96_23)

    @pytest.mark.dependency(depends=["TestRegulationChainShowInstrument::test_chain_show_index_22"])
    def test_chain_show_index_23(self, driver):
        setup(driver)
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.click_to_rcsi_next_doc(RegulationFields.REGULATION_TYPE_96_23)
        page.regulation_doc(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_23,
                            TestRegulationChainShowInstrument.NPA_ID, False, False, True)

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 1,
                        2, RegulationFields.REGULATION_TYPE_96_23, False, False, 2)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 2,
                        2, RegulationFields.REGULATION_TYPE_96_23, True, False, 2)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 3,
                        2, RegulationFields.REGULATION_TYPE_96_23, False, False, 2)

        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()

        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 8, 2,
                        RegulationFields.REGULATION_TYPE_96_23, False, False, 2, RegulationFields.REGULATION_TYPE_96_27)

    @pytest.mark.dependency(depends=["TestRegulationChainShowInstrument::test_chain_show_index_23"])
    def test_chain_show_repeat_22(self, driver):
        setup(driver)
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.click_to_rcsi_repeat()
        page.regulation_doc(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_22,
                            TestRegulationChainShowInstrument.NPA_ID, False, False, True)
        page.should_be_repeat_message()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 1,
                        3, RegulationFields.REGULATION_TYPE_96_22, False, True, 1)
        page.check_rcsi_previous_version(1)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 2,
                        3, RegulationFields.REGULATION_TYPE_96_22, True, False, 1)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 3,
                        3, RegulationFields.REGULATION_TYPE_96_22, False, False, 1)

        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 4,
                        3, RegulationFields.REGULATION_TYPE_96_22, False, False, 1)

        page.create_answer(page.have_answer(page.modify_npa_type(
            RegulationFields.REGULATION_TYPE_96_22, 1)), False, TestRegulationChainShowInstrument.NPA_ID)

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 5,
                        3, RegulationFields.REGULATION_TYPE_96_22, False, False, 1)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 6,
                        3, RegulationFields.REGULATION_TYPE_96_22, True, False, 1)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 7,
                        3, RegulationFields.REGULATION_TYPE_96_22, False, False, 1)

        page.register_and_send_enter_regulation_document(answer=True)
        page.agree_with_popup_window_enter_doc()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 8, 3,
                        RegulationFields.REGULATION_TYPE_96_22, False, False, 1, RegulationFields.REGULATION_TYPE_96_23)

    @pytest.mark.dependency(depends=["TestRegulationChainShowInstrument::test_chain_show_repeat_22"])
    def test_chain_show_refuse_23(self, driver):
        setup(driver)
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.click_to_rcsi_next_doc(RegulationFields.REGULATION_TYPE_96_23)
        page.regulation_doc(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_23,
                            TestRegulationChainShowInstrument.NPA_ID, False, False, True)

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 1,
                        4, RegulationFields.REGULATION_TYPE_96_23, False, True, 2)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 2,
                        4, RegulationFields.REGULATION_TYPE_96_23, True, True, 2)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 3,
                        4, RegulationFields.REGULATION_TYPE_96_23, False, True, 2)

        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 8, 4,
                        RegulationFields.REGULATION_TYPE_96_23, False, True, 2, RegulationFields.REGULATION_TYPE_96_27)

        page.create_refuse_document(
            RegulationFields.REGULATION_TYPE_96_23, TestRegulationChainShowInstrument.doc_id)

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 9,
                        4, RegulationFields.REGULATION_TYPE_96_23, False, True, 2)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 10,
                        4, RegulationFields.REGULATION_TYPE_96_23, True, True, 2)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 11,
                        4, RegulationFields.REGULATION_TYPE_96_23, False, True, 2)

        page.register_and_send_refuse_document(
            TestRegulationChainShowInstrument.doc_id, True)
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 8, 4,
                        RegulationFields.REGULATION_TYPE_96_23, False, True, 3, RegulationFields.REGULATION_TYPE_96_23)

    @pytest.mark.dependency(depends=["TestRegulationChainShowInstrument::test_chain_show_refuse_23"])
    def test_chain_show_after_refuse_23(self, driver):
        setup(driver)
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.click_to_rcsi_next_doc(RegulationFields.REGULATION_TYPE_96_23)
        page.regulation_doc(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_23,
                            TestRegulationChainShowInstrument.NPA_ID, False, False, True)

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 1,
                        4, RegulationFields.REGULATION_TYPE_96_23, False, True, 4)
        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 1,
                        4, RegulationFields.REGULATION_TYPE_96_23, False, True, 5)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 2,
                        4, RegulationFields.REGULATION_TYPE_96_23, True, False, 4)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 3,
                        4, RegulationFields.REGULATION_TYPE_96_23, False, False, 4)

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 8, 4, RegulationFields.REGULATION_TYPE_96_23,
                        False, False, 4, RegulationFields.REGULATION_TYPE_96_27, RegulationFields.REGULATION_TYPE_96_22)

    @pytest.mark.dependency(depends=["TestRegulationChainShowInstrument::test_chain_show_after_refuse_23"])
    def test_chain_show_index_27(self, driver):
        setup(driver)
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.click_to_rcsi_next_doc(RegulationFields.REGULATION_TYPE_96_27)
        page.regulation_doc(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_27,
                            TestRegulationChainShowInstrument.NPA_ID, False, False, True)

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 1,
                        5, RegulationFields.REGULATION_TYPE_96_27, False, True, 2)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 2,
                        5, RegulationFields.REGULATION_TYPE_96_27, True, False, 2)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 3,
                        5, RegulationFields.REGULATION_TYPE_96_27, False, False, 2)

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 8, 5, RegulationFields.REGULATION_TYPE_96_27,
                        False, False, 2, RegulationFields.REGULATION_TYPE_96_31, RegulationFields.REGULATION_TYPE_96_22)

    @pytest.mark.dependency(depends=["TestRegulationChainShowInstrument::test_chain_show_index_27"])
    def test_chain_show_index_31(self, driver):
        setup(driver)
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.click_to_rcsi_next_doc(RegulationFields.REGULATION_TYPE_96_31)
        page.regulation_doc(RegulationFields.NPA_96, RegulationFields.REGULATION_TYPE_96_31,
                            TestRegulationChainShowInstrument.NPA_ID, False, False, True)

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 1,
                        6, RegulationFields.REGULATION_TYPE_96_31, False, True, 2)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 2,
                        6, RegulationFields.REGULATION_TYPE_96_31, True, False, 2)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 3,
                        6, RegulationFields.REGULATION_TYPE_96_31, False, False, 2)

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(TestRegulationChainShowInstrument.NPA_ID, 12,
                        6, RegulationFields.REGULATION_TYPE_96_31, False, False, 2)


@pytest.mark.regulation
@pytest.mark.regulation_chain_break
class TestRegulationChainBreaking:
    NPA_ID = None

    # Пропуск заявки в цепочке
    @pytest.mark.dependency()
    def test_skip_request_1(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_851,
                            RegulationFields.REGULATION_TYPE_851_1, TestRegulationChainBreaking.NPA_ID, False, True)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")

        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        enter_page = EnterDocumentsPage(driver, link)
        enter_page.send_medo()

        TestRegulationChainBreaking.NPA_ID = page.create_and_send_answer(page.modify_npa_type(
            RegulationFields.REGULATION_TYPE_851_1, 1), TestRegulationChainBreaking.NPA_ID, True)

    @pytest.mark.dependency(depends=["TestRegulationChainBreaking::test_skip_request_1"])
    def test_skip_request_2(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_7,
                            TestRegulationChainBreaking.NPA_ID, error=RegulationFields.REQUEST_PLACING_ERROR)

    # Создание следующей заявки до регистрации ответа

    @pytest.mark.dependency()
    def test_without_answer_1(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_1,
                            TestRegulationChainBreaking.NPA_ID, False, True)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")

        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        enter_page = EnterDocumentsPage(driver, link)
        enter_page.send_medo()

        TestRegulationChainBreaking.NPA_ID = page.create_answer(page.have_answer(page.modify_npa_type(
            RegulationFields.REGULATION_TYPE_851_1, 1)), True, TestRegulationChainBreaking.NPA_ID)

    @pytest.mark.dependency(depends=["TestRegulationChainBreaking::test_without_answer_1"])
    def test_without_answer_2(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_7,
                            TestRegulationChainBreaking.NPA_ID, error=RegulationFields.CHAIN_NOT_FOUND_ERROR)

    # Создание следующей заявки, когда предыдущая получила отказ

    @pytest.mark.dependency()
    def test_with_refuse_1(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_1,
                            TestRegulationChainBreaking.NPA_ID, False, True)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()

        TestRegulationChainBreaking.NPA_ID = page.create_and_send_answer(page.modify_npa_type(
            RegulationFields.REGULATION_TYPE_851_1, 1), TestRegulationChainBreaking.NPA_ID, True)

    @pytest.mark.dependency(depends=["TestRegulationChainBreaking::test_with_refuse_1"])
    def test_with_refuse_2(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationRefuseDocument(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_4,
                            TestRegulationChainBreaking.NPA_ID, False, False)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationRefuseDocument(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()
        doc_id = page.save_document_id()

        page.create_refuse_document(
            RegulationFields.REGULATION_TYPE_851_4, doc_id)
        page.create_and_send_agree_sheet()
        page.register_and_send_refuse_document(doc_id, True)

    @pytest.mark.dependency(depends=["TestRegulationChainBreaking::test_with_refuse_2"])
    def test_with_refuse_3(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_7,
                            TestRegulationChainBreaking.NPA_ID, error=RegulationFields.REQUEST_PLACING_ERROR)

    # Создание дубля заявки, не допускающей повторы

    @pytest.mark.parametrize("npa_number,regulation_type,first", [
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_1, True, marks=[
                     pytest.mark.dependency(name="chain_break_4-1")]),
        pytest.param(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_4, False, marks=[
                     pytest.mark.dependency(name="chain_break_4-2", depends=["chain_break_4-1"])]),
    ])
    def test_not_repeat(self, driver, npa_number, regulation_type, first):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(npa_number, regulation_type,
                            TestRegulationChainBreaking.NPA_ID, False, first)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(
            URLs.OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()

        TestRegulationChainBreaking.NPA_ID = page.create_and_send_answer(
            page.modify_npa_type(regulation_type, 1), TestRegulationChainBreaking.NPA_ID, first)

    @pytest.mark.dependency(depends=["chain_break_4-2"])
    def test_not_repeat_2(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(URLs.REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(RegulationFields.NPA_851, RegulationFields.REGULATION_TYPE_851_4,
                            TestRegulationChainBreaking.NPA_ID, False, False, error=RegulationFields.REQUEST_PLACING_ERROR)
