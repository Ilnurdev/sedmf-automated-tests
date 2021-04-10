import pytest
from pages.main_functions import MainFunc
from pages.authorization_page import AuthPage
from pages.all_document_fields_page import AllDocumentFieldPage
from pages.enter_documets_page import EnterDocumentsPage
from pages.regulation_document_page import RegulationDocumentPage, ChangeResponsibleInfo, RegulationRefuseDocument, RegulationChainShowInstrument
from pages.settings_pages import SystemNotificationPage, RegulationControlPage
from pages.main_page import SoglDocumentsBlock

import time

SERVER = MainFunc.config()
AUTH_LINK = SERVER + "/auth.php"
OPENED_DOCUMENT_LINK = SERVER + "/document.card.php?"
SYSTEM_NOTIFY_LINK = SERVER + "/public/notify/system/?"
REGULATION_LINK = OPENED_DOCUMENT_LINK + "category=6&r_category=4&card_type=2&version_id=2"
CHANGE_INFO_LINK = OPENED_DOCUMENT_LINK + "category=6&r_category=4&card_type=2&request_type=59"


NPA_851 = "851"
NPA_1318 = "1318"
NPA_96 = "96"
NPA_373 = "373"
NPA_83 = "83"

REGULATION_TYPE_851_1 = "1. Заявка на размещение уведомления о подготовке проекта НПА"
REGULATION_TYPE_851_4 = "4. Заявка на размещение сводки предложений, поступивших в рамках обсуждения уведомления о подготовке проекта НПА"
REGULATION_TYPE_851_7 = "7. Заявка на размещение проекта НПА"
REGULATION_TYPE_851_8 = "8. Заявка на размещение проекта НПА (параллельное размещение)"
REGULATION_TYPE_851_9 = "9. Заявка на размещение проекта НПА в случае принятия решения об отказе от общественного обсуждения"
REGULATION_TYPE_851_14 = "14. Заявка на размещение сводки предложений, поступивших в рамках общественного обсуждения проекта НПА"
REGULATION_TYPE_851_15 = "15. Заявка на размещение сводки предложений, поступивших в рамках общественного обсуждения проекта НПА (параллельное размещение)"
REGULATION_TYPE_851_24 = "24. Заявка на размещение решения по проекту НПА"
REGULATION_TYPE_851_28 = "28. Заявка на размещение НПА"
REGULATION_TYPE_1318_2 = "2. Заявка на размещение уведомления о подготовке проекта НПА"
REGULATION_TYPE_1318_5 = "5. Заявка на размещение сводки предложений, поступивших в рамках обсуждения уведомления о подготовке проекта НПА"
REGULATION_TYPE_1318_10 = "10. Заявка на размещение проекта НПА (параллельное размещение)"
REGULATION_TYPE_1318_11 = "11. Заявка на размещение проекта решения ЕЭК"
REGULATION_TYPE_1318_16 = "16. Заявка на размещение сводки предложений, поступивших в рамках публичного обсуждения проекта НПА (параллельное размещение)"
REGULATION_TYPE_1318_17 = "17. Заявка на размещение сводки предложений, поступивших в рамках публичного обсуждения проекта решения ЕЭК"
REGULATION_TYPE_1318_20 = "20. Заявка на размещение результатов публичного обсуждения проекта НПА"
REGULATION_TYPE_1318_21 = "21. Заявка на размещение результатов публичного обсуждения проекта решения ЕЭК"
REGULATION_TYPE_1318_25 = "25. Заявка на размещение решения по проекту НПА"
REGULATION_TYPE_1318_29 = "29. Заявка на размещение НПА"
REGULATION_TYPE_373_3 = "3. Заявка на размещение уведомления о подготовке проекта НПА"
REGULATION_TYPE_373_6 = "6. Заявка на размещение сводки предложений, поступивших в рамках обсуждения уведомления о подготовке проекта НПА"
REGULATION_TYPE_373_12 = "12. Заявка на размещение проекта НПА (независимая экспертиза административного регламента в рамках процедуры общественного обсуждения)"
REGULATION_TYPE_373_13 = "13. Заявка на размещение проекта НПА (независимая экспертиза административного регламента в рамках процедуры общественного обсуждения, параллельное размещение)"
REGULATION_TYPE_373_18 = "18. Заявка на размещение сводки предложений, поступивших в рамках общественного обсуждения проекта НПА (результаты рассмотрения проекта административного регламента в рамках сводки предложений)"
REGULATION_TYPE_373_19 = "19. Заявка на размещение сводки предложений, поступивших в рамках общественного обсуждения проекта НПА (результаты рассмотрения проекта административного регламента в рамках сводки предложений, параллельное размещение)"
REGULATION_TYPE_373_26 = "26. Заявка на размещение решения по проекту НПА"
REGULATION_TYPE_373_30 = "30. Заявка на размещение НПА"
REGULATION_TYPE_96_22 = "22. Заявка на размещение проекта НПА для проведения независимой антикоррупционной экспертизы"
REGULATION_TYPE_96_23 = "23. Заявка на размещение общего заключения по проекту НПА по итогам независимой антикоррупционной экспертизы"
REGULATION_TYPE_96_27 = "27. Заявка на размещение решения по проекту НПА"
REGULATION_TYPE_96_31 = "31. Заявка на размещение НПА"
REGULATION_TYPE_83_32 = "32. Заявка на размещение НПА и отчета об оценке фактического воздействия"
REGULATION_TYPE_83_33 = "33. Заявка на размещение сводки предложений, поступивших в рамках публичного обсуждения отчета об оценке фактического воздействия"
REGULATION_TYPE_83_34 = "34. Заявка на размещение доработанного отчета об оценке фактического воздействия"


def setup(driver, root=None):
    link = AUTH_LINK
    page = AuthPage(driver, link)
    page.open()
    page.enter_in_account(root)


@pytest.mark.regulation
class TestUIDocumentOpenLink:
    def test_open_regulation_document(self, driver):
        setup(driver)
        page = SoglDocumentsBlock(driver, driver.current_url)
        page.go_to_sogl_block_new_document()
        page.should_be_correct_elements_sogl_new_window()
        page.choose_request_document()
        page.should_be_correct_elements_sogl_request_new_window()
        page.choose_request_regulation_document()

        page = AllDocumentFieldPage(driver, driver.current_url)
        page.should_be_required_fields("Согласование внутреннего документа-заявки Regulation")
        page.should_be_correct_url(REGULATION_LINK)
        page = RegulationDocumentPage(driver, driver.current_url)
        page.should_be_closed_short_content_fields(1)
    
    def test_open_change_info_document(self, driver):
        setup(driver)
        page = SoglDocumentsBlock(driver, driver.current_url)
        page.go_to_sogl_block_new_document()
        page.should_be_correct_elements_sogl_new_window()
        page.choose_request_document()
        page.should_be_correct_elements_sogl_request_new_window()
        page.choose_request_change_responsible_info_document()

        page = AllDocumentFieldPage(driver, driver.current_url)
        page.should_be_required_fields("Согласование внутреннего документа-заявки Regulation")
        page.should_be_correct_url(CHANGE_INFO_LINK)
        page = RegulationDocumentPage(driver, driver.current_url)
        page.should_be_closed_short_content_fields(1)


@pytest.mark.regulation
class TestRegulation:
    @pytest.mark.parametrize("npa_number,regulation_type,chain_index,first", [
        pytest.param(NPA_851, REGULATION_TYPE_851_1, 1, True, marks=[pytest.mark.dependency(name="1-1"), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(NPA_851, REGULATION_TYPE_851_4, 1, False, marks=[pytest.mark.dependency(name="1-4", depends=["1-1"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(NPA_851, REGULATION_TYPE_851_7, 1, False, marks=[pytest.mark.dependency(name="1-7", depends=["1-4"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(NPA_851, REGULATION_TYPE_851_14, 1, False, marks=[pytest.mark.dependency(name="1-14", depends=["1-7"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(NPA_96, REGULATION_TYPE_96_22, 1, False, marks=[pytest.mark.dependency(name="1-22", depends=["1-14"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(NPA_96, REGULATION_TYPE_96_23, 1, False, marks=[pytest.mark.dependency(name="1-23", depends=["1-22"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(NPA_851, REGULATION_TYPE_851_24, 1, False, marks=[pytest.mark.dependency(name="1-24", depends=["1-23"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),
        pytest.param(NPA_851, REGULATION_TYPE_851_28, 1, False, marks=[pytest.mark.dependency(name="1-28", depends=["1-24"]), pytest.mark.reg_851, pytest.mark.reg_chain_1]),

        pytest.param(NPA_851, REGULATION_TYPE_851_7, 2, True, marks=[pytest.mark.dependency(name="2-7"), pytest.mark.reg_851, pytest.mark.reg_chain_2]),
        pytest.param(NPA_851, REGULATION_TYPE_851_14, 2, False, marks=[pytest.mark.dependency(name="2-14", depends=["2-7"]), pytest.mark.reg_851, pytest.mark.reg_chain_2]),
        pytest.param(NPA_96, REGULATION_TYPE_96_22, 2, False, marks=[pytest.mark.dependency(name="2-22", depends=["2-14"]), pytest.mark.reg_851, pytest.mark.reg_chain_2]),
        pytest.param(NPA_96, REGULATION_TYPE_96_23, 2, False, marks=[pytest.mark.dependency(name="2-23", depends=["2-22"]), pytest.mark.reg_851, pytest.mark.reg_chain_2]),
        pytest.param(NPA_851, REGULATION_TYPE_851_24, 2, False, marks=[pytest.mark.dependency(name="2-24", depends=["2-23"]), pytest.mark.reg_851, pytest.mark.reg_chain_2]),
        pytest.param(NPA_851, REGULATION_TYPE_851_28, 2, False, marks=[pytest.mark.dependency(name="2-28", depends=["2-24"]), pytest.mark.reg_851, pytest.mark.reg_chain_2]),

        pytest.param(NPA_851, REGULATION_TYPE_851_1, 3, True, marks=[pytest.mark.dependency(name="3-1"), pytest.mark.reg_851, pytest.mark.reg_chain_3]),
        pytest.param(NPA_851, REGULATION_TYPE_851_4, 3, False, marks=[pytest.mark.dependency(name="3-4", depends=["3-1"]), pytest.mark.reg_851, pytest.mark.reg_chain_3]),
        pytest.param(NPA_851, REGULATION_TYPE_851_8, 3, False, marks=[pytest.mark.dependency(name="3-8", depends=["3-4"]), pytest.mark.reg_851, pytest.mark.reg_chain_3]),
        pytest.param(NPA_851, REGULATION_TYPE_851_15, 3, False, marks=[pytest.mark.dependency(name="3-15", depends=["3-8"]), pytest.mark.reg_851, pytest.mark.reg_chain_3]),
        pytest.param(NPA_851, REGULATION_TYPE_851_24, 3, False, marks=[pytest.mark.dependency(name="3-24", depends=["3-15"]), pytest.mark.reg_851, pytest.mark.reg_chain_3]),
        pytest.param(NPA_851, REGULATION_TYPE_851_28, 3, False, marks=[pytest.mark.dependency(name="3-28", depends=["3-24"]), pytest.mark.reg_851, pytest.mark.reg_chain_3]),
        
        pytest.param(NPA_851, REGULATION_TYPE_851_8, 4, True, marks=[pytest.mark.dependency(name="4-8"), pytest.mark.reg_851, pytest.mark.reg_chain_4]),
        pytest.param(NPA_851, REGULATION_TYPE_851_15, 4, False, marks=[pytest.mark.dependency(name="4-15", depends=["4-8"]), pytest.mark.reg_851, pytest.mark.reg_chain_4]),
        pytest.param(NPA_851, REGULATION_TYPE_851_24, 4, False, marks=[pytest.mark.dependency(name="4-24", depends=["4-15"]), pytest.mark.reg_851, pytest.mark.reg_chain_4]),
        pytest.param(NPA_851, REGULATION_TYPE_851_28, 4, False, marks=[pytest.mark.dependency(name="4-28", depends=["4-24"]), pytest.mark.reg_851, pytest.mark.reg_chain_4]),

        pytest.param(NPA_851, REGULATION_TYPE_851_9, 5, True, marks=[pytest.mark.dependency(name="5-22"), pytest.mark.reg_851, pytest.mark.reg_chain_5]),
        pytest.param(NPA_96, REGULATION_TYPE_96_23, 5, False, marks=[pytest.mark.dependency(name="5-23", depends=["5-22"]), pytest.mark.reg_851, pytest.mark.reg_chain_5]),
        pytest.param(NPA_851, REGULATION_TYPE_851_24, 5, False, marks=[pytest.mark.dependency(name="5-24", depends=["5-23"]), pytest.mark.reg_851, pytest.mark.reg_chain_5]),
        pytest.param(NPA_851, REGULATION_TYPE_851_28, 5, False, marks=[pytest.mark.dependency(name="5-28", depends=["5-24"]), pytest.mark.reg_851, pytest.mark.reg_chain_5]),
    
        pytest.param(NPA_1318, REGULATION_TYPE_1318_2, 6, True, marks=[pytest.mark.dependency(name="6-2"), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_5, 6, False, marks=[pytest.mark.dependency(name="6-5", depends=["6-2"]), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_10, 6, False, marks=[pytest.mark.dependency(name="6-10", depends=["6-5"]), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_16, 6, False, marks=[pytest.mark.dependency(name="6-16", depends=["6-10"]), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_20, 6, False, marks=[pytest.mark.dependency(name="6-20", depends=["6-16"]), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_25, 6, False, marks=[pytest.mark.dependency(name="6-25", depends=["6-20"]), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_29, 6, False, marks=[pytest.mark.dependency(name="6-29", depends=["6-25"]), pytest.mark.reg_1318, pytest.mark.reg_chain_6]),

        pytest.param(NPA_1318, REGULATION_TYPE_1318_10, 7, True, marks=[pytest.mark.dependency(name="7-10"), pytest.mark.reg_1318, pytest.mark.reg_chain_7]),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_16, 7, False, marks=[pytest.mark.dependency(name="7-16", depends=["7-10"]), pytest.mark.reg_1318, pytest.mark.reg_chain_7]),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_20, 7, False, marks=[pytest.mark.dependency(name="7-20", depends=["7-16"]), pytest.mark.reg_1318, pytest.mark.reg_chain_7]),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_25, 7, False, marks=[pytest.mark.dependency(name="7-25", depends=["7-20"]), pytest.mark.reg_1318, pytest.mark.reg_chain_7]),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_29, 7, False, marks=[pytest.mark.dependency(name="7-29", depends=["7-25"]), pytest.mark.reg_1318, pytest.mark.reg_chain_7]),

        pytest.param(NPA_1318, REGULATION_TYPE_1318_11, 8, True, marks=[pytest.mark.dependency(name="8-11"), pytest.mark.reg_1318, pytest.mark.reg_chain_8]),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_17, 8, False, marks=[pytest.mark.dependency(name="8-17", depends=["8-11"]), pytest.mark.reg_1318, pytest.mark.reg_chain_8]),
        pytest.param(NPA_1318, REGULATION_TYPE_1318_21, 8, False, marks=[pytest.mark.dependency(name="8-21", depends=["8-17"]), pytest.mark.reg_1318, pytest.mark.reg_chain_8]),

        pytest.param(NPA_373, REGULATION_TYPE_373_3, 9, True, marks=[pytest.mark.dependency(name="9-3"), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(NPA_373, REGULATION_TYPE_373_6, 9, False, marks=[pytest.mark.dependency(name="9-6", depends=["9-3"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(NPA_373, REGULATION_TYPE_373_12, 9, False, marks=[pytest.mark.dependency(name="9-12", depends=["9-6"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(NPA_373, REGULATION_TYPE_373_18, 9, False, marks=[pytest.mark.dependency(name="9-18", depends=["9-12"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(NPA_96, REGULATION_TYPE_96_22, 9, False, marks=[pytest.mark.dependency(name="9-22", depends=["9-18"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(NPA_96, REGULATION_TYPE_96_23, 9, False, marks=[pytest.mark.dependency(name="9-23", depends=["9-22"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(NPA_373, REGULATION_TYPE_373_26, 9, False, marks=[pytest.mark.dependency(name="9-26", depends=["9-23"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),
        pytest.param(NPA_373, REGULATION_TYPE_373_30, 9, False, marks=[pytest.mark.dependency(name="9-30", depends=["9-26"]), pytest.mark.reg_373, pytest.mark.reg_chain_9]),

        pytest.param(NPA_373, REGULATION_TYPE_373_12, 10, True, marks=[pytest.mark.dependency(name="10-12"), pytest.mark.reg_373, pytest.mark.reg_chain_10]),
        pytest.param(NPA_373, REGULATION_TYPE_373_18, 10, False, marks=[pytest.mark.dependency(name="10-18", depends=["10-12"]), pytest.mark.reg_373, pytest.mark.reg_chain_10]),
        pytest.param(NPA_96, REGULATION_TYPE_96_22, 10, False, marks=[pytest.mark.dependency(name="10-22", depends=["10-18"]), pytest.mark.reg_373, pytest.mark.reg_chain_10]),
        pytest.param(NPA_96, REGULATION_TYPE_96_23, 10, False, marks=[pytest.mark.dependency(name="10-23", depends=["10-22"]), pytest.mark.reg_373, pytest.mark.reg_chain_10]),
        pytest.param(NPA_373, REGULATION_TYPE_373_26, 10, False, marks=[pytest.mark.dependency(name="10-26", depends=["10-23"]), pytest.mark.reg_373, pytest.mark.reg_chain_10]),
        pytest.param(NPA_373, REGULATION_TYPE_373_30, 10, False, marks=[pytest.mark.dependency(name="10-30", depends=["10-26"]), pytest.mark.reg_373, pytest.mark.reg_chain_10]),
    
        pytest.param(NPA_373, REGULATION_TYPE_373_3, 11, True, marks=[pytest.mark.dependency(name="11-3"), pytest.mark.reg_373, pytest.mark.reg_chain_11]),
        pytest.param(NPA_373, REGULATION_TYPE_373_6, 11, False, marks=[pytest.mark.dependency(name="11-6", depends=["11-3"]), pytest.mark.reg_373, pytest.mark.reg_chain_11]),
        pytest.param(NPA_373, REGULATION_TYPE_373_13, 11, False, marks=[pytest.mark.dependency(name="11-13", depends=["11-6"]), pytest.mark.reg_373, pytest.mark.reg_chain_11]),
        pytest.param(NPA_373, REGULATION_TYPE_373_19, 11, False, marks=[pytest.mark.dependency(name="11-19", depends=["11-13"]), pytest.mark.reg_373, pytest.mark.reg_chain_11]),
        pytest.param(NPA_373, REGULATION_TYPE_373_26, 11, False, marks=[pytest.mark.dependency(name="11-26", depends=["11-19"]), pytest.mark.reg_373, pytest.mark.reg_chain_11]),
        pytest.param(NPA_373, REGULATION_TYPE_373_30, 11, False, marks=[pytest.mark.dependency(name="11-30", depends=["11-26"]), pytest.mark.reg_373, pytest.mark.reg_chain_11]),
    
        pytest.param(NPA_373, REGULATION_TYPE_373_13, 12, True, marks=[pytest.mark.dependency(name="12-13"), pytest.mark.reg_373, pytest.mark.reg_chain_12]),
        pytest.param(NPA_373, REGULATION_TYPE_373_19, 12, False, marks=[pytest.mark.dependency(name="12-19", depends=["12-13"]), pytest.mark.reg_373, pytest.mark.reg_chain_12]),
        pytest.param(NPA_373, REGULATION_TYPE_373_26, 12, False, marks=[pytest.mark.dependency(name="12-26", depends=["12-19"]), pytest.mark.reg_373, pytest.mark.reg_chain_12]),
        pytest.param(NPA_373, REGULATION_TYPE_373_30, 12, False, marks=[pytest.mark.dependency(name="12-30", depends=["12-26"]), pytest.mark.reg_373, pytest.mark.reg_chain_12]),
    
        pytest.param(NPA_96, REGULATION_TYPE_96_22, 13, True, marks=[pytest.mark.dependency(name="13-22"), pytest.mark.reg_96]),
        pytest.param(NPA_96, REGULATION_TYPE_96_23, 13, False, marks=[pytest.mark.dependency(name="13-23", depends=["13-22"]), pytest.mark.reg_96]),
        pytest.param(NPA_96, REGULATION_TYPE_96_27, 13, False, marks=[pytest.mark.dependency(name="13-27", depends=["13-23"]), pytest.mark.reg_96]),
        pytest.param(NPA_96, REGULATION_TYPE_96_31, 13, False, marks=[pytest.mark.dependency(name="13-31", depends=["13-27"]), pytest.mark.reg_96]),
    
        pytest.param(NPA_83, REGULATION_TYPE_83_32, 14, True, marks=[pytest.mark.dependency(name="14-32"), pytest.mark.reg_83]),
        pytest.param(NPA_83, REGULATION_TYPE_83_33, 14, False, marks=[pytest.mark.dependency(name="14-33", depends=["14-32"]), pytest.mark.reg_83]),
        pytest.param(NPA_83, REGULATION_TYPE_83_34, 14, False, marks=[pytest.mark.dependency(name="14-34", depends=["14-33"]), pytest.mark.reg_83]),
    ])
    def test_regulation_documet(self, driver, npa_number, regulation_type, chain_index, first):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(npa_number, regulation_type, chain_index, False, first)
        page.regulation_doc(npa_number, regulation_type, chain_index, True, first)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        index = page.modify_npa_type(regulation_type, 1)
        page.register_and_send_enter_regulation_document(
            page.check_regulation_doc, index, chain_index, first)
        page.send_medo()

        page.create_and_send_answer(index, chain_index, first)


@pytest.mark.regulation
@pytest.mark.change_info
class TestChangeInfoResponsibleDocument:
    def test_change_info(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(CHANGE_INFO_LINK, driver.current_url)
        page = ChangeResponsibleInfo(driver, link)
        page.open()
        chain_index = page.choose_chain()
        page.change_responsible_info_doc(False, chain_index)
        page.change_responsible_info_doc(True, chain_index)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = ChangeResponsibleInfo(driver, link)
        page.open()
        page.register_and_send_enter_change_info_document(chain_index)


@pytest.mark.regulation
@pytest.mark.regulation_refuse
class TestRegulationRefuse:
    # Отказ - заявка первая
    def test_regulation_refuse_1_1_doc(self, driver):
        setup(driver)

        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationRefuseDocument(driver, link)
        page.open()
        page.regulation_doc(NPA_851, REGULATION_TYPE_851_1, 1, False, True)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationRefuseDocument(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()
        doc_id = page.save_document_id()

        page.create_refuse_document(True, doc_id)
        page.create_and_send_agree_sheet()
        page.register_and_send_refuse_document(doc_id)


    # Отказ - заявка НЕ первая, не имеет обязательного ответа
    @pytest.mark.dependency()
    def test_regulation_refuse_2_1_doc(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(NPA_851, REGULATION_TYPE_851_1, 1, False, True)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()

        page.create_and_send_answer(page.modify_npa_type(REGULATION_TYPE_851_1, 1), 1, True)

    @pytest.mark.dependency(depends=["TestRegulationRefuse::test_regulation_refuse_2_1_doc"])
    def test_regulation_refuse_2_2_doc(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(NPA_851, REGULATION_TYPE_851_4, 1, False, False)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")

        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationRefuseDocument(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()
        doc_id = page.save_document_id()

        page.create_refuse_document(False, doc_id)
        page.create_and_send_agree_sheet()
        page.register_and_send_refuse_document(doc_id)


    # Отказ - заявка НЕ первая, имеет обязательный ответ
    @pytest.mark.parametrize("npa_number,regulation_type,chain_index,first", [
        pytest.param(NPA_851, REGULATION_TYPE_851_1, 1, True, marks=[pytest.mark.dependency(name="refuse-1-1")]),
        pytest.param(NPA_851, REGULATION_TYPE_851_4, 1, False, marks=[pytest.mark.dependency(name="refuse-1-4", depends=["refuse-1-1"])]),
    ])
    def test_regulation_refuse_3_doc(self, driver, npa_number, regulation_type, chain_index, first):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(npa_number, regulation_type, chain_index, False, first)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        index = page.modify_npa_type(regulation_type, 1)
        page.register_and_send_enter_regulation_document()
        page.send_medo()

        page.create_and_send_answer(index, chain_index, first)

    @pytest.mark.dependency(depends=["refuse-1-4"])
    def test_regulation_refuse_3_2_doc(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(NPA_851, REGULATION_TYPE_851_7, 1, False, False)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationRefuseDocument(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()
        doc_id = page.save_document_id()

        page.create_refuse_document(True, doc_id)
        page.create_and_send_agree_sheet()
        page.register_and_send_refuse_document(doc_id)


@pytest.mark.regulation
@pytest.mark.regulation_chain_show
class TestRegulationChainShowInstrument:
    doc_id = None

    @pytest.mark.dependency()
    def test_chain_show_index_22(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationChainShowInstrument(driver, link)
        page.open()
        page.regulation_doc(NPA_96, REGULATION_TYPE_96_22, 13, False, True, False)

        page.check_rcsi(False, 1, 1, REGULATION_TYPE_96_22, False, False, 1)
        
        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(False, 2, 1, REGULATION_TYPE_96_22, True, False, 1)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(False, 3, 1, REGULATION_TYPE_96_22, False, False, 1)

        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()

        page.check_rcsi(False, 4, 1, REGULATION_TYPE_96_22, False, False, 1)

        page.create_answer(page.modify_npa_type(REGULATION_TYPE_96_22, 1), True, 13)

        page.check_rcsi(False, 5, 1, REGULATION_TYPE_96_22, False, False, 1)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(False, 6, 1, REGULATION_TYPE_96_22, True, False, 1)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(False, 7, 1, REGULATION_TYPE_96_22, False, False, 1)

        page.register_and_send_enter_regulation_document(answer=True)
        page.agree_with_popup_window_enter_doc()

        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(True, 8, 1, REGULATION_TYPE_96_22, False, False, 1, REGULATION_TYPE_96_23)

    @pytest.mark.dependency(depends=["TestRegulationChainShowInstrument::test_chain_show_index_22"])
    def test_chain_show_index_23(self, driver):
        setup(driver)
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.click_to_rcsi_next_doc(REGULATION_TYPE_96_23)
        page.regulation_doc(NPA_96, REGULATION_TYPE_96_23, 13, False, False, True)

        page.check_rcsi(True, 1, 2, REGULATION_TYPE_96_23, False, False, 2)
        
        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(True, 2, 2, REGULATION_TYPE_96_23, True, False, 2)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(True, 3, 2, REGULATION_TYPE_96_23, False, False, 2)

        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()
        
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(True, 8, 2, REGULATION_TYPE_96_23, False, False, 2, REGULATION_TYPE_96_27)
    
    @pytest.mark.dependency(depends=["TestRegulationChainShowInstrument::test_chain_show_index_23"])
    def test_chain_show_repeat_22(self, driver):
        setup(driver)
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.click_to_rcsi_repeat()
        page.regulation_doc(NPA_96, REGULATION_TYPE_96_22, 13, False, False, True)
        page.should_be_repeat_message()

        page.check_rcsi(True, 1, 3, REGULATION_TYPE_96_22, False, True, 1)
        page.check_rcsi_previous_version(1)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(True, 2, 3, REGULATION_TYPE_96_22, True, False, 1)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(True, 3, 3, REGULATION_TYPE_96_22, False, False, 1)

        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(True, 4, 3, REGULATION_TYPE_96_22, False, False, 1)

        page.create_answer(page.modify_npa_type(REGULATION_TYPE_96_22, 1), False, 13)

        page.check_rcsi(True, 5, 3, REGULATION_TYPE_96_22, False, False, 1)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(True, 6, 3, REGULATION_TYPE_96_22, True, False, 1)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(True, 7, 3, REGULATION_TYPE_96_22, False, False, 1)

        page.register_and_send_enter_regulation_document(answer=True)
        page.agree_with_popup_window_enter_doc()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(True, 8, 3, REGULATION_TYPE_96_22, False, False, 1, REGULATION_TYPE_96_23)

    @pytest.mark.dependency(depends=["TestRegulationChainShowInstrument::test_chain_show_repeat_22"])
    def test_chain_show_refuse_23(self, driver):
        setup(driver)
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.click_to_rcsi_next_doc(REGULATION_TYPE_96_23)
        page.regulation_doc(NPA_96, REGULATION_TYPE_96_23, 13, False, False, True)

        page.check_rcsi(True, 1, 4, REGULATION_TYPE_96_23, False, True, 2)
        
        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(True, 2, 4, REGULATION_TYPE_96_23, True, True, 2)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(True, 3, 4, REGULATION_TYPE_96_23, False, True, 2)

        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(True, 8, 4, REGULATION_TYPE_96_23, False, True, 2, REGULATION_TYPE_96_27)

        page.create_refuse_document(False, TestRegulationChainShowInstrument.doc_id)

        page.check_rcsi(True, 9, 4, REGULATION_TYPE_96_23, False, True, 2)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(True, 10, 4, REGULATION_TYPE_96_23, True, True, 2)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()

        page.check_rcsi(True, 11, 4, REGULATION_TYPE_96_23, False, True, 2)

        page.register_and_send_refuse_document(TestRegulationChainShowInstrument.doc_id, True)
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(True, 8, 4, REGULATION_TYPE_96_23, False, True, 3, REGULATION_TYPE_96_23)

    @pytest.mark.dependency(depends=["TestRegulationChainShowInstrument::test_chain_show_refuse_23"])
    def test_chain_show_after_refuse_23(self, driver):
        setup(driver)
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.click_to_rcsi_next_doc(REGULATION_TYPE_96_23)
        page.regulation_doc(NPA_96, REGULATION_TYPE_96_23, 13, False, False, True)

        page.check_rcsi(True, 1, 4, REGULATION_TYPE_96_23, False, True, 4)
        page.check_rcsi(True, 1, 4, REGULATION_TYPE_96_23, False, True, 5)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(True, 2, 4, REGULATION_TYPE_96_23, True, False, 4)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(True, 3, 4, REGULATION_TYPE_96_23, False, False, 4)

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(True, 8, 4, REGULATION_TYPE_96_23, False, False, 4, REGULATION_TYPE_96_27, REGULATION_TYPE_96_22)

    @pytest.mark.dependency(depends=["TestRegulationChainShowInstrument::test_chain_show_after_refuse_23"])
    def test_chain_show_index_27(self, driver):
        setup(driver)
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.click_to_rcsi_next_doc(REGULATION_TYPE_96_27)
        page.regulation_doc(NPA_96, REGULATION_TYPE_96_27, 13, False, False, True)

        page.check_rcsi(True, 1, 5, REGULATION_TYPE_96_27, False, True, 2)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(True, 2, 5, REGULATION_TYPE_96_27, True, False, 2)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(True, 3, 5, REGULATION_TYPE_96_27, False, False, 2)

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(True, 8, 5, REGULATION_TYPE_96_27, False, False, 2, REGULATION_TYPE_96_31, REGULATION_TYPE_96_22)

    @pytest.mark.dependency(depends=["TestRegulationChainShowInstrument::test_chain_show_index_27"])
    def test_chain_show_index_31(self, driver):
        setup(driver)
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.click_to_rcsi_next_doc(REGULATION_TYPE_96_31)
        page.regulation_doc(NPA_96, REGULATION_TYPE_96_31, 13, False, False, True)

        page.check_rcsi(True, 1, 6, REGULATION_TYPE_96_31, False, True, 2)

        page.click_to_create_agree_sheet_button()
        page.click_to_submit_button_create_window()
        page.click_to_send_on_agreement_button()
        page.agree_with_popup_window_agree_sheet()

        page.check_rcsi(True, 2, 6, REGULATION_TYPE_96_31, True, False, 2)

        page.approve_agree_sheet_button()
        page.click_to_agree_button_on_agreement_window()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(True, 3, 6, REGULATION_TYPE_96_31, False, False, 2)

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), TestRegulationChainShowInstrument.doc_id)
        page = RegulationChainShowInstrument(driver, link)
        page.open()

        page.register_and_send_enter_regulation_document()
        page.agree_with_popup_window_enter_doc()
        TestRegulationChainShowInstrument.doc_id = page.save_document_id()

        page.check_rcsi(True, 12, 6, REGULATION_TYPE_96_31, False, False, 2)


@pytest.mark.regulation
@pytest.mark.regulation_chain_break
class TestRegulationChainBreaking:
    # Пропуск заявки в цепочке
    @pytest.mark.dependency()
    def test_skip_request_1(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(NPA_851, REGULATION_TYPE_851_1, 1, False, True)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")

        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        enter_page = EnterDocumentsPage(driver, link)
        enter_page.send_medo()

        page.create_and_send_answer(page.modify_npa_type(REGULATION_TYPE_851_1, 1), 1, True)
    
    @pytest.mark.dependency(depends=["TestRegulationChainBreaking::test_skip_request_1"])
    def test_skip_request_2(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(NPA_851, REGULATION_TYPE_851_7, 1, error="Нарушение последовательности размещения заявок")


    # Создание следующей заявки до регистрации ответа
    @pytest.mark.dependency()
    def test_without_answer_1(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(NPA_851, REGULATION_TYPE_851_1, 1, False, True)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")

        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        enter_page = EnterDocumentsPage(driver, link)
        enter_page.send_medo()

        page.create_answer(page.have_answer(page.modify_npa_type(REGULATION_TYPE_851_1, 1)), True, 1)
    
    @pytest.mark.dependency(depends=["TestRegulationChainBreaking::test_without_answer_1"])
    def test_without_answer_2(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(NPA_851, REGULATION_TYPE_851_7, 1, error="Не найдена связанная цепочка заявок")
    

    # Создание следующей заявки, когда предыдущая получила отказ
    @pytest.mark.dependency()
    def test_with_refuse_1(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(NPA_851, REGULATION_TYPE_851_1, 1, False, True)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()

        page.create_and_send_answer(page.modify_npa_type(REGULATION_TYPE_851_1, 1), 1, True)

    @pytest.mark.dependency(depends=["TestRegulationChainBreaking::test_with_refuse_1"])
    def test_with_refuse_2(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationRefuseDocument(driver, link)
        page.open()
        page.regulation_doc(NPA_851, REGULATION_TYPE_851_4, 1, False, False)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationRefuseDocument(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()
        doc_id = page.save_document_id()

        page.create_refuse_document(False, doc_id)
        page.create_and_send_agree_sheet()
        page.register_and_send_refuse_document(doc_id ,True)

    @pytest.mark.dependency(depends=["TestRegulationChainBreaking::test_with_refuse_2"])
    def test_with_refuse_3(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(NPA_851, REGULATION_TYPE_851_7, 1, error="Нарушение последовательности размещения заявок")
    

    # Создание дубля заявки, не допускающей повторы
    @pytest.mark.parametrize("npa_number,regulation_type,chain_index,first", [
        pytest.param(NPA_851, REGULATION_TYPE_851_1, 1, True, marks=[pytest.mark.dependency(name="chain_break_4-1")]),
        pytest.param(NPA_851, REGULATION_TYPE_851_4, 1, False, marks=[pytest.mark.dependency(name="chain_break_4-2", depends=["chain_break_4-1"])]),
    ])
    def test_not_repeat(self, driver, npa_number, regulation_type, chain_index, first):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(npa_number, regulation_type, chain_index, False, first)
        page.create_and_send_agree_sheet()
        doc_id = page.save_document_id()

        setup(driver, "a")
        link = MainFunc.create_doc_link(MainFunc.take_DNSID(OPENED_DOCUMENT_LINK, driver.current_url), doc_id)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.register_and_send_enter_regulation_document()
        page.send_medo()

        page.create_and_send_answer(page.modify_npa_type(regulation_type, 1), chain_index, first)

    @pytest.mark.dependency(depends=["chain_break_4-2"])
    def test_not_repeat_2(self, driver):
        setup(driver)
        link = MainFunc.take_DNSID(REGULATION_LINK, driver.current_url)
        page = RegulationDocumentPage(driver, link)
        page.open()
        page.regulation_doc(NPA_851, REGULATION_TYPE_851_4, 1, False, False, error="Нарушение последовательности размещения заявок")

