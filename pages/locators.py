from selenium.webdriver.common.by import By


class AuthPageLocators:
    SELECT_ORG_LOCATOR = (By.CSS_SELECTOR, "#group_id")
    SELECT_USR_LOCATOR = (By.CSS_SELECTOR, "#user_id")
    ENTER_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#password")
    ENTER_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".error-wrapper input")


class MainPageLocators:

    ENTER_BLOCK_SLIDE_DOWN_BUTTON = (
        By.XPATH, "//div[@id='menu_top_4']//a[@class='slide down']")
    ENTER_BLOCK_ON_REGISTRATION_LINK = (
        By.XPATH, "//div[@id='menu_bottom_4']//a[text()='На регистрации']")

    SOGL_BLOCK_SLIDE_DOWN_BUTTON = (
        By.XPATH, "//div[@id='menu_top_6']//a[@class='slide down']")
    SOGL_BLOCK_ALL_DOCUMENT_LINK = (
        By.XPATH, "//div[@id='menu_bottom_6']//a[text()='Все документы']")
    SOGL_BLOCK_NEW_DOCUMENT_LINK = (
        By.XPATH, "//div[@id='menu_bottom_6']//a[text()='Новый документ...']")


class SoglNewDocumentWindow:
    OUTGOING_DOCUMENT_RADIO_BUTTON_LOCATOR = (
        By.XPATH, "//input[@id='category_1']")
    OUTGOING_DOCUMENT_NAME_LOCATOR = (By.XPATH, "//label[@for='category_1']")
    OUTGOING_OG_DOCUMENT_RADIO_BUTTON_LOCATOR = (
        By.XPATH, "//input[@id='category_2']")
    OUTGOING_OG_DOCUMENT_NAME_LOCATOR = (
        By.XPATH, "//label[@for='category_2']")
    ENTER_DOCUMENT_RADIO_BUTTON_LOCATOR = (
        By.XPATH, "//input[@id='category_3']")
    ENTER_DOCUMENT_NAME_LOCATOR = (By.XPATH, "//label[@for='category_3']")
    ORD_DOCUMENT_RADIO_BUTTON_LOCATOR = (By.XPATH, "//input[@id='category_4']")
    ORD_DOCUMENT_NAME_LOCATOR = (By.XPATH, "//label[@for='category_4']")
    REQUEST_DOCUMENT_RADIO_BUTTON_LOCATOR = (
        By.XPATH, "//input[@id='category_5']")
    REQUEST_DOCUMENT_NAME_LOCATOR = (By.XPATH, "//label[@for='category_5']")

    CONTINUE_BUTTON_LOCATOR = (By.XPATH, "//input[@id='continue']")
    CLOSE_BUTTON_LOCATOR = (By.XPATH, "//input[@value='Закрыть']")

    REQUEST_REQUEST_RADIO_BUTTON_LOCATOR = (
        By.XPATH, "//input[@id='list_item_0']")
    REQUEST_REQUEST_NAME_LOCATOR = (By.XPATH, "//label[@for='list_item_0']")
    REQUEST_REGULATION_RADIO_BUTTON_LOCATOR = (
        By.XPATH, "//input[@id='list_item_1']")
    REQUEST_REGULATION_NAME_LOCATOR = (By.XPATH, "//label[@for='list_item_1']")
    REQUEST_CHANGE_INFO_RADIO_BUTTON_LOCATOR = (
        By.XPATH, "//input[@id='list_item_2']")
    REQUEST_CHANGE_INFO_NAME_LOCATOR = (
        By.XPATH, "//label[@for='list_item_2']")


class EnterDocumentsLocators:
    SEND_MEDO_BUTTON_LOCATOR = (By.XPATH, "//input[@id='send-medo-button']")


class AgreeSheetLocators:
    CREATE_AGREE_SHEET_BUTTON_LOCATOR = (
        By.XPATH, "//input[@value='Создать лист согласования']")
    SEND_TO_AGREEMENT_BUTTON_LOCATOR = (
        By.XPATH, "//input[@value='Отправить на согласование']")

    # Селекторы на подписании
    APPROVE_BUTTON_LOCATOR = (By.XPATH, "//a[text()='согласовать']")
    COMMENT_BUTTON_LOCATOR = (By.XPATH, "//a[text()='замечания']")
    RESOLUTINS_BUTTON_LOCATOR = (By.XPATH, "//a[text()='резолюция']")

    # Селекторы в окне создания ЛС
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//input[@name='submit_button']")
    CLOSE_BUTTON_LOCATOR = (By.XPATH, "//input[@value='Закрыть']")

    # Селекторы в окне Согласования ЛС
    SUBMIT_AGREE_BUTTON_LOCATOR = (By.XPATH, "//input[@name='submit_agree']")
    SUBMIT_SUGN_BUTTON_LOCATOR = (By.XPATH, "//input[@name='submit_sign']")
    SUBMIT_DISAGREE_BUTTON_LOCATOR = (By.XPATH, "//input[@value='Отмена']")

    ON_AGREE_TEXT_LOCATOR = (
        By.XPATH, "//td[contains(text(),'На подписании')]")


class PopupWindowLocators:
    OK_ENG_BUTTON_LOCATOR = (By.XPATH, "//span[text()='OK']")
    OK_RUS_BUTTON_LOCATOR = (By.XPATH, "//span[text()='Ок']")
    CONTINUE_BUTTON_LOCATOR = (By.XPATH, "//span[text()='Продолжить']")
    DISMISS_BUTTON_LOCATOR = (By.XPATH, "//span[text()='Отмена']")


class AllDocumentFieldLocators:
    # Универсальный селектор поиска по тексту
    @staticmethod
    def find_text_locator(element):
        locator = (By.XPATH, f"//*[text()[contains(.,'{element}')]]")
        return locator

    # Заголовок страницы
    TITLE_LOCATOR = (By.CSS_SELECTOR, "h1")

    # Поле Индекс дела
    INDEX_DELA_LOCATOR = (By.XPATH, "//strong[text()='Индекс дела']")
    INDEX_DELA_FIELD_LOCATOR = (By.CSS_SELECTOR, "#unit_text_0")

    # Поле Подпись
    PODPIS_LOCATOR = (By.XPATH, "//acronym[text()='Подпись:']")
    PODPIS_FIELD_LOCATOR = (By.CSS_SELECTOR, "#inp_g_su_a_0")
    PODPIS_NEW_WINDOW_LOCATOR = (By.XPATH, "//span[@id='sp2_g_su_a_0']/a")

    # Поле Исполнитель

    # Поле Кому
    RECIPIENT_DELETE_BUTTON_LOCATOR = (By.XPATH, "//a[@id='remover_g_su_r_0']")
    RECIPIENT_NEW_WINDOW_LOCATOR = (
        By.XPATH, "//span[@id='sp2_g_su_r_0']/a[text()='Организация для автотестирования']")

    # Выбор пользователя из выпадающего окна
    CHOOSE_USER_FROM_DROP_LIST = (
        By.XPATH, "//div[@class='sg-div']/div[@id='fio_0']")

    # Добавить файлы
    ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-file_upload']/input[not(contains(@style,'none'))]")

    # Сохранить + просмотр
    SAVE_RCD_BUTTON_LOCATOR = (By.XPATH, "//input[@id='save_view']")

    # Удалить документ
    DELETE_FILE_LOCATOR = (By.XPATH, "//tr[@class='file']//a[@class='delete']")

    # Связка
    @staticmethod
    def link_document(id):
        locator = (
            By.XPATH, f"//a[@target='_blank' and contains(@href,'{id}')]")
        return locator


class FindDocumentInFolder:
    @staticmethod
    def find_doc_in_folder(id):
        locator = (By.XPATH, f"//tr[@data-document-id='{id}']")
        return locator


class OpenDocumentPictagramsLocators:
    EDIT_PICTAGRAM_LOCATOR = (
        By.XPATH, "//a[@title='Редактировать карточку документа']")
    REGISTER_PICTOGRAM_LOCATOR = (
        By.XPATH, "//a[@title='Зарегистрировать документ']")
    ANSWER_PICTOGRAM_LOCATOR = (By.XPATH, "//a[@title='Ответить']")
    REFUSE_PICTOGRAM_LOCATOR = (
        By.XPATH, "//a[@title='Отказать в исполнении']")
    REFRESH_PICTOGRAM_LOCATOR = (By.XPATH, "//a[@title='Обновить']")
    REGULATION_CHAIN_SHOW_PICTOGRAM_LOCATOR = (
        By.XPATH, "//a[@title='Показать цепочку заявок Regulation']")


class ChooseUserFromNewWindow:
    FIRST_USER_LINK_LOCATOR = (By.XPATH, "//li//a")
    USER_FIND_LOCATOR = (By.XPATH, "//input[@id='filter_name']")


class ChooseOrganisationFromNewWindow:
    ORG_FIND_LOCATOR = (By.XPATH, "//input[@id='org_name']")
    FIND_BUTTON_LOCATOR = (By.XPATH, "//input[@id='find']")


class NomenclatureUnitWindowLocators:
    FIRST_NOMENCLATURE_LOCATOR = (By.XPATH, "//tbody/tr[1]/td")


class RegulationDocumentLocators:
    # № постановления
    SELECT_ORDER_FIELD_CM_LOCATOR = (
        By.XPATH, "//select[@name='request[npa_num]']")
    SELECT_ORDER_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'№ постановления:')]]")
    ORDER_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'№ постановления:')]]/following-sibling::td")

    # Тип заявки
    SELECT_REQUEST_TYPE_FIELD_LOCATOR = (
        By.XPATH, "//select[@name='request[request_type]']")
    SELECT_REQUEST_TYPE_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Тип заявки:')]]")
    REQUEST_TYPE_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Тип заявки:')]]/following-sibling::td")

    # Вид НПА
    SELECT_NPA_TYPE_FIELD_LOCATOR = (
        By.XPATH, "//select[@name='request[npa_type]']")
    SELECT_NPA_TYPE_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Вид НПА:')]]")
    NPA_TYPE_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Вид НПА:')]]/following-sibling::td")

    # Наименование проекта НПА & Наименование НПА
    NPA_NAME_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[npa_name]']")

    NPA_NAME_1_FIELD_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Наименование проекта НПА:')]]")
    NPA_NAME_1_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Наименование проекта НПА:')]]/following-sibling::td")

    NPA_NAME_2_FIELD_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Наименование НПА:')]]")
    NPA_NAME_2_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Наименование НПА:')]]/following-sibling::td")

    # Сведения об органах и организациях(Наименование, E-mail)
    FOR_COUNT_ELEMENTS_IN_ORG_INFO_FIELD_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Сведения об органах и организациях:')]]/parent::tr//div[contains(@class,'item')]")
    ORG_INFO_NAME_FIELD_LOCATOR = (
        By.XPATH, "//div[@class='flex-row item'][last()]/div[@class='w60']/input")
    ORG_INFO_EMAIL_FIELD_LOCATOR = (
        By.XPATH, "//div[@class='flex-row item'][last()]/div[@class='w35']/input")
    LAST_REMOVE_BUTTON_IN_ORG_INFO_LOCATOR = (
        By.XPATH, "//div[@class='flex-row item'][last()]//input[@class='remove']")
    ADD_NEW_ELEMENT_IN_ORG_INFO_LOCATOR = (
        By.XPATH, "//input[@class='append']")
    CHOOSE_ORG_FROM_NEW_WINDOW = (
        By.XPATH, "//div[@class='flex-row item'][last()]//a[@class='select']")
    ORG_INFO_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Сведения об органах и организациях:')]]")
    ORG_INFO_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Сведения об органах и организациях:')]]/following-sibling::td")

    # Виды экономической деятельности
    FOR_COUNT_ELEMENTS_IN_EA_TYPE_FIELD_CEM_LOCATOR = (
        By.XPATH, "//div[@id='ea_type-container']//div[@class='item' and span]")
    FOR_COUNT_ELEMENTS_IN_EA_TYPE_FIELD_VM_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Виды экономической деятельности')]]/following-sibling::td/br")
    ENTER_NEW_ELEMENT_IN_EA_TYPE_LOCATOR = (
        By.XPATH, "//input[@class='fill search ui-autocomplete-input']")
    LAST_REMOVE_BUTTON_IN_EA_TYPE_LOCATOR = (
        By.XPATH, "//div[@id='ea_type-container']//div[@class='item'][last()]/a[@class='remove']")
    CHOOSE_EA_TYPE_FROM_NEW_WINDOW = (
        By.XPATH, "//input[@class='fill search ui-autocomplete-input']/following-sibling::span/a")
    CHOOSE_EA_TYPE_DROP_LIST = (By.XPATH, "//ul[@id='ui-id-1']/li")
    EA_TYPE_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Виды экономической деятельности')]]")
    EA_TYPE_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Виды экономической деятельности:')]]/following-sibling::td")

    # Ключевые слова
    KEYWORD_INPUT_FILELD_LOCATOR = (
        By.XPATH, "//textarea[@name='request[keywords]']")
    KEYWORD_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(., 'Ключевые слова:')]]")
    KEYWORD_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Ключевые слова:')]]/following-sibling::td")

    # Срок обсуждения
    DISCUSS_PERIOD_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[discuss_period]']")
    DISCUSS_PERIOD_NAME_LOCATOR = (
        By.XPATH, "//td[text()[contains(.,'Срок обсуждения')]]")
    DISCUSS_PERIOD_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Срок обсуждения:')]]/following-sibling::td")

    # Органы гос. власти – соисполнители
    FOR_COUNT_ELEMENTS_IN_CO_EXECTOR_FIELD_CEM_LOCATOR = (
        By.XPATH, "//div[@id='co_executor-container']//div[@class='item' and span]")
    FOR_COUNT_ELEMENTS_IN_CO_EXECTOR_FIELD_VM_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Органы гос. власти – соисполнители:')]]/following-sibling::td/br")
    LAST_REMOVE_BUTTON_IN_CO_EXECTOR_LOCATOR = (
        By.XPATH, "//div[@id='co_executor-container']//div[@class='item'][last()]/a[@class='remove']")
    CHOOSE_CO_EXECTOR_FROM_NEW_WINDOW = (
        By.XPATH, "//input[@class='fill search']/following-sibling::span/a")
    CO_EXECTOR_FIELD_LOCATOR = (
        By.XPATH, "//input[@class='fill search']")
    CO_EXECTOR_NAME_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Органы гос. власти – соисполнители:')]]")
    CO_EXECTOR_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Органы гос. власти – соисполнители:')]]/following-sibling::td")

    # Доп. e-mail для предложений
    ADD_OFFER_EMAIL_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[add_offers_email]']")
    ADD_OFFER_EMAIL_NAME_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Доп. e-mail для предложений:')]]")
    ADD_OFFER_EMAIL_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Доп. e-mail для предложений:')]]/following-sibling::td")

    # Е-mail для предложений
    OFFERS_EMAIL_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[offers_email]']")
    OFFERS_EMAIL_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Е-mail для предложений:')]]")
    OFFERS_EMAIL_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Е-mail для предложений:')]]/following-sibling::td")

    # Основание для разработки НПА
    REASON_CREATE_NPA_FIELD_LOCATOR = (
        By.XPATH, "//textarea[@name='request[dasis_dev_npa]']")
    REASON_CREATE_NPA_NAME_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Основание для разработки НПА:')]]")
    REASON_CREATE_NPA_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Основание для разработки НПА:')]]/following-sibling::td")

    # ID связанных НПА
    NPA_LINK_ID_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[ref_id_prav_act]']")
    NPA_LINK_ID_NAME_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'ID связанных НПА:')]]")
    NPA_LINK_ID_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'ID связанных НПА:')]]/following-sibling::td")

    # Дополнительные материалы(Наименование, Выбрать файл)
    FOR_COUNT_ELEMENTS_IN_ADDITIONAL_MATERIALS_FIELD_CEM_LOCATOR = (
        By.XPATH, "//div[@id='am_file-container']/div[@class='item']")
    ENTER_LAST_ELEMENT_IN_ADDITIONAL_MATERIALS_LOCATOR = (
        By.XPATH, "//div[@id='am_file-container']//div[@class='item'][last()]//input[@class='fill']")
    ADD_FILE_LAST_ELEMENT_IN_ADDITIONAL_MATERIALS_LOCATOR = (
        By.XPATH, "//div[@id='am_file-container']//div[@class='item'][last()]//input[@type='file']")
    REMOVE_LAST_ELEMENT_IN_ADDITIONAL_MATERIALS_LOCATOR = (
        By.XPATH, "//div[@id='am_file-container']//div[@class='item'][last()]//a[@class='remove']")
    ADDITIONAL_MATERIALS_ADD_BUTTON_LOCATOR = (
        By.XPATH, "//td[contains(text(),'Дополнительные материалы:')]/parent::tr//a[@class='append']")
    ADDITIONAL_MATERIALS_NAME_LOCATOR = (
        By.XPATH, "//td[not(span) and contains(text(),'Дополнительные материалы:')]")
    ADDITIONAL_MATERIALS_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Дополнительные материалы:')]]/following-sibling::td")

    # Ответственный за рассмотрение предложений & Ответственный за направление информации & Ответственный за направление НПА
    RESPONSIBLE_REVIEW_FIO_FIELD_LOCATOR = (
        By.XPATH, "//div[contains(.,'ФИО:')]/div[contains(@id,'request_resp_for_')]//input[contains(@id,'inp')]")
    RESPONSIBLE_REVIEW_PHONE_FIELD_LOCATOR = (
        By.XPATH, "//div[contains(.,'Телефон:')]/input")
    RESPONSIBLE_REVIEW_EMAIL_FIELD_LOCATOR = (
        By.XPATH, "//div[contains(.,'E-mail:')]/input")
    CHOOSE_RESPONSIBLE_REVIEW_FROM_NEW_WINDOW = (
        By.XPATH, "//span[contains(@id,'sp2_request_resp_for_')]/a[@class='ins']")
    RESPONSIBLE_REVIEW_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Ответственный за')]]")
    RESPONSIBLE_REVIEW_FIELD_VIEW_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Ответственный за')]]/following-sibling::td")
    RESPONSIBLE_REVIEW_DELETE_BUTTON_LOCATOR = (
        By.XPATH, "//a[contains(@id,'remover_request_resp_for_')]")
    REGULATION_ERROR_MESSAGE_PHONE_EMAIL_LOCATOR = (
        By.XPATH, "//div[contains(@data-name,'request_resp_for_') and @style='display: block;']")

    # Уведомление о подготовке проекта НПА(Наименование, Выбрать файл)
    NOTIFY_NPA_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[notify_npa_file][0][name]']")
    NOTIFY_NPA_CHOOSE_FILE_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestnotify_npa_file0']/input[@type='file'][last()]")
    NOTIFY_NPA_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Уведомление о подготовке проекта НПА:')]]")
    NOTIFY_NPA_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Уведомление о подготовке проекта НПА:')]]/following-sibling::td")

    # ID проекта НПА
    ID_NPA_PROJECT_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[id_prav_act]']")
    ID_NPA_PROJECT_NAME_LOCATOR = (
        By.XPATH, "//td[text()[contains(.,'ID проекта НПА:')]]")
    ID_NPA_PROJECT_NAME_LOCATOR_2 = (
        By.XPATH, "//td[text()[contains(.,'ID отчета об оценке фактического воздействия:')]]")

    ID_NPA_PROJECT_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[text()[contains(.,'ID проекта НПА:')]]/following-sibling::td")
    ID_NPA_PROJECT_FIELD_VIEW_MODE_LOCATOR_2 = (
        By.XPATH, "//td[text()[contains(.,'ID отчета об оценке фактического воздействия:')]]/following-sibling::td")

    @staticmethod
    def find_npa_id_locator(id):
        locator = (By.XPATH, f"//*[text()[contains(.,'{id}')]]/a")
        return locator

    # Общее кол-во замечаний
    TOTAL_COMMENT_FIELD_LOCATOR = (
        By.XPATH, "//input[contains(@name,'request[total_comment')]")
    TOTAL_COMMENT_FIELD_2_LOCATOR = (
        By.XPATH, "//input[contains(@name,'request[total_comment2')]")
    TOTAL_COMMENT_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Общее кол-во замечаний:')]]")
    TOTAL_COMMENT_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Общее кол-во замечаний:')]]//following-sibling::td")
    TOTAL_COMMENT_FIELD_2_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[text()[contains(.,'Антикоррупционная экспертиза:')]]/following::td[span and text()[contains(.,'Общее кол-во замечаний:')]]//following-sibling::td[1]")

    # Кол-во учтенных замечаний
    NUMBER_COMMENT_FIELD_LOCATOR = (
        By.XPATH, "//input[contains(@name,'request[number_comment')]")
    NUMBER_COMMENT_FIELD_2_LOCATOR = (
        By.XPATH, "//input[contains(@name,'request[number_comment2')]")
    NUMBER_COMMENT_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Кол-во учтенных замечаний:')]]")
    NUMBER_COMMENT_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Кол-во учтенных замечаний:')]]//following-sibling::td")
    NUMBER_COMMENT_FIELD_2_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[text()[contains(.,'Антикоррупционная экспертиза:')]]/following::td[span and text()[contains(.,'Кол-во учтенных замечаний:')]]//following-sibling::td")

    # Кол-во неучтенных замечаний
    NUMBER_UNA_COMMENT_FIELD_LOCATOR = (
        By.XPATH, "//input[contains(@name,'request[number_una_comment')]")
    NUMBER_UNA_COMMENT_FIELD_2_LOCATOR = (
        By.XPATH, "//input[contains(@name,'request[number_una_comment2')]")
    NUMBER_UNA_COMMENT_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Кол-во неучтенных замечаний:')]]")
    NUMBER_UNA_COMMENT_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Кол-во неучтенных замечаний:')]]//following-sibling::td")
    NUMBER_UNA_COMMENT_FIELD_2_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[text()[contains(.,'Антикоррупционная экспертиза:')]]/following::td[span and text()[contains(.,'Кол-во неучтенных замечаний:')]]//following-sibling::td")

    # Кол-во частично учтенных замечаний
    NUMBER_PTA_COMMENT_FIELD_LOCATOR = (
        By.XPATH, "//input[contains(@name,'request[number_pta_comment')]")
    NUMBER_PTA_COMMENT_FIELD_2_LOCATOR = (
        By.XPATH, "//input[contains(@name,'request[number_pta_comment2')]")
    NUMBER_PTA_COMMENT_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Кол-во частично учтенных замечаний:')]]")
    NUMBER_PTA_COMMENT_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Кол-во частично учтенных замечаний:')]]//following-sibling::td")
    NUMBER_PTA_COMMENT_FIELD_2_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[text()[contains(.,'Антикоррупционная экспертиза:')]]/following::td[span and text()[contains(.,'Кол-во частично учтенных замечаний:')]]//following-sibling::td")

    # Информация о принятом решении
    DECISION_INFO_SELECT_LOCATOR = (
        By.XPATH, "//select[@name='request[decision_info]']")
    DECISION_INFO_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Информация о принятом решении:')]]")
    DECISION_INFO_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Информация о принятом решении:')]]//following-sibling::td")

    # Принятое решение по проекту НПА
    DECISION_INFO_2_SELECT_LOCATOR = (
        By.XPATH, "//select[@name='request[decision_info]']")
    DECISION_INFO_2_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Принятое решение по проекту НПА:')]]")
    DECISION_INFO_2_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Принятое решение по проекту НПА:')]]/following-sibling::td")

    # Сводка предложений
    SUMMARY_INFO_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[summary_file][0][name]']")
    SUMMARY_INFO_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestsummary_file0']//input[@type='file']")
    SUMMARY_INFO_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Сводка предложений:')]]")
    SUMMARY_INFO_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Сводка предложений:')]]/following-sibling::td")

    # Проект НПА
    NPA_PROJECT_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[npa_project_file][0][name]']")
    NPA_PROJECT_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestnpa_project_file0']/input[@type='file']")
    NPA_PROJECT_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Проект НПА:')]]")
    NPA_PROJECT_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Проект НПА:')]]/following-sibling::td")

    # Пояснительная записка
    EXPLAIN_NOTE_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[exp_note_file][0][name]']")
    EXPLAIN_NOTE_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestexp_note_file0']//input[@type='file']")
    EXPLAIN_NOTE_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Пояснительная записка:')]]")
    EXPLAIN_NOTE_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Пояснительная записка:')]]/following-sibling::td")

    # Регуляторная гильотина
    REGULATORY_GILLIOTINE_CHECKBOX_LOCATOR = (
        By.XPATH, "//input[@name='request[reg_guillotine]']")
    REGULATORY_GILLIOTINE_NAME_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Регуляторная гильотина:')]]")
    REGULATORY_GILLIOTINE_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Регуляторная гильотина:')]]/following-sibling::td")

    # Уведомление о подготовке НПА не размещается
    NOTICE_NPA_NOT_PLACED_CHECKBOX_LOCATOR = (
        By.XPATH, "//input[@name='request[notice_npa_not_placed][checkbox]']")
    NOTICE_NPA_NOT_PLACED_NAME_LOCATOR = (
        By.XPATH, "//input[@name='inp_request_notice_npa_not_placed_var']")
    NOTICE_NPA_NOT_PLACED_DATE_LOCATOR = (
        By.XPATH, "//input[@name='request[notice_npa_not_placed][date]']")
    NOTICE_NPA_NOT_PLACED_NEW_WINDOW_LOCATOR = (
        By.XPATH, "//span[@id='sp2_request_notice_npa_not_placed_var']/a[@class='ins']")
    NOTICE_NPA_NOT_PLASED_DELETE_BUTTON_LOCATOR = (
        By.XPATH, "//a[@id='remover_request_notice_npa_not_placed_var']")
    NOTICE_NPA_NOT_PLACED_NAME_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Уведомление о подготовке НПА не размещается:')]]")
    NOTICE_NPA_NOT_PLACED_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Уведомление о подготовке НПА не размещается:')]]/following-sibling::td")

    # Доработанный проект НПА
    MODIFIED_NPA_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[md_npa_file][0][name]']")
    MODIFIED_NPA_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestmd_npa_file0']/input[@type='file']")
    MODIFIED_NPA_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Доработанный проект НПА:')]]")
    MODIFIED_NPA_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Доработанный проект НПА:')]]/following-sibling::td")

    # Прием заключений антикоррупционной экспертизы
    AC_EXPERTISE_FIELD_LOCATOR = (
        By.XPATH, "//input[@id='request_ac_expertise']")
    AC_EXPERTISE_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Прием заключений антикоррупционной экспертизы:')]]/following-sibling::td")
    AC_EXPERTISE_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Прием заключений антикоррупционной экспертизы:')]]")

    # E-mail для заключений антикоррупционной экспертизы
    EMAIL_AC_EXPERTISE_FIELD_LOCATOR = (
        By.XPATH, "//input[@id='request_email_ac_expertise']")
    EMAIL_AC_EXPERTISE_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'E-mail для заключений антикоррупционной экспертизы:')]]")
    EMAIL_AC_EXPERTISE_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'E-mail для заключений антикоррупционной экспертизы:')]]/following-sibling::td")

    # Почта для заключений антикоррупционной экспертизы
    MAIL_AC_EXPERTISE_FIELD_LOCATOR = (
        By.XPATH, "//input[@id='request_mail_ac_expertise']")
    MAIL_AC_EXPERTISE_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Почта для заключений антикоррупционной экспертизы:')]]")
    MAIL_AC_EXPERTISE_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Почта для заключений антикоррупционной экспертизы:')]]/following-sibling::td")

    # Коррупциогенные факторы
    CORRUPTION_FACTOR_FIELD_LOCATOR = (
        By.XPATH, "//select[@id='request_corruption_factor']")
    CORRUPTION_FACTOR_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Коррупциогенные факторы:')]")
    CORRUPTION_FACTOR_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Коррупциогенные факторы:')]/following-sibling::td")

    # Кол-во заключений
    NUMBER_CONCLUSION_FIELD_LOCATOR = (
        By.XPATH, "//input[@id='request_number_conclusion']")
    NUMBER_CONCLUSION_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Кол-во заключений:')]")
    NUMBER_CONCLUSION_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Кол-во заключений:')]/following-sibling::td")

    # Общее заключение по итогам антикоррупционной экспертизы
    GC_AC_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[gc_ac_file][0][name]']")
    GC_AC_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestgc_ac_file0']//input[@type='file']")
    GC_AC_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Общее заключение по итогам антикоррупционной экспертизы:')]")
    GC_AC_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Общее заключение по итогам антикоррупционной экспертизы:')]/following-sibling::td")

    # Нормативный правовой акт (проект)
    NPA_DRAFT_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[npa_draft][0][name]']")
    NPA_DRAFT_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestnpa_draft0']//input[@type='file']")
    NPA_DRAFT_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Нормативный правовой акт (проект):')]]")
    NPA_DRAFT_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Нормативный правовой акт (проект):')]]/following-sibling::td")

    # Номер принятого НПА & Номер НПА
    NPA_NUMBER_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[npa_number]']")
    NPA_NUMBER_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Номер ')]]")
    NPA_NUMBER_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Номер ')]]/following-sibling::td")

    # Номер государственной регистрации НПА
    STATE_NUMBER_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[state_reg_number]']")
    STATE_NUMBER_NAME_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Номер государственной регистрации НПА:')]]")
    STATE_NUMBER_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Номер государственной регистрации НПА:')]]/following-sibling::td")

    # Утвержденный НПА
    APPROVED_NPA_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[approved_npa_file][0][name]']")
    APPROVED_NPA_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestapproved_npa_file0']/input[@type='file']")
    APPROVED_NPA_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Утвержденный НПА:')]]")
    APPROVED_NPA_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Утвержденный НПА:')]]/following-sibling::td")

    # Дата принятия НПА & Дата НПА
    NPA_ADOPTION_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[npa_adoption_date]']")
    NPA_DATE_FIELD_LOCATOR = (By.XPATH, "//input[@name='request[npa_date]']")
    NPA_ADOPTION_NAME_LOCATOR = (
        By.XPATH, "//tr[@class='regulation-field']//td[span and text()[contains(.,'Дата ')]]")
    NPA_ADOPTION_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//tr[@class='regulation-field']//td[span and text()[contains(.,'Дата ')]]/following-sibling::td")

    # Обоснование отказа от общественного обсуждения проекта НПА
    PD_NPA_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[pd_npa_file][0][name]']")
    PD_NPA_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestpd_npa_file0']/input[@type='file']")
    PD_NPA_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Обоснование  отказа  от общественного обсуждения проекта НПА:')]")
    PD_NPA_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Обоснование  отказа  от общественного обсуждения проекта НПА:')]/following-sibling::td")

    # Сводный отчет
    CONSOL_REPORT_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[consol_report_file][0][name]']")
    CONSOL_REPORT_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestconsol_report_file0']/input[@type='file']")
    CONSOL_REPORT_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Сводный отчет:')]")
    CONSOL_REPORT_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Сводный отчет:')]/following-sibling::td")

    # Срок принятия предложений
    DECISION_PERIOD_FIELD_LOCATOR = (
        By.XPATH, "//input[@id='request_decision_period']")
    DECISION_PERIOD_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Срок принятия предложений')]")
    DECISION_PERIOD_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Срок принятия предложений')]/following-sibling::td")

    # Степень воздействия
    DEGREE_EXPOSURE_FIELD_LOCATOR = (
        By.XPATH, "//select[@id='request_degree_exposure']")
    DEGREE_EXPOSURE_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Степень воздействия:')]")
    DEGREE_EXPOSURE_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Степень воздействия:')]/following-sibling::td")

    # Тип затрагиваемых вопросов
    ISSUE_TYPE_FIELD_LOCATOR = (
        By.XPATH, "//div[@id='request_issue_addr_type_container']/select")
    ISSUE_TYPE_FIELD_2_LOCATOR = (
        By.XPATH, "//select[@id='request_issue_addr_type']")
    ISSUE_TYPE_NAME_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Тип затрагиваемых вопросов:')]]")
    ISSUE_TYPE_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Тип затрагиваемых вопросов:')]]/following-sibling::td")

    # Доработанный сводный отчет
    MSR_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[msr_file][0][name]']")
    MSR_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestmsr_file0']/input[@type='file']")
    MSR_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Доработанный сводный отчет:')]]")
    MSR_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Доработанный сводный отчет:')]]/following-sibling::td")

    # Проект решения ЕЭК
    EEC_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[decision_project_file][0][name]']")
    EEC_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestdecision_project_file0']/input[@type='file' and not(contains(@style,'none'))]")
    EEC_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Проект решения ЕЭК:')]")
    EEC_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Проект решения ЕЭК:')]/following-sibling::td")

    # Доработанный проект решения ЕЭК
    MDD_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[mdd_file][0][name]']")
    MDD_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestmdd_file0']/input[@type='file' and not(contains(@style,'none'))]")
    MDD_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Доработанный проект решения ЕЭК:')]")
    MDD_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Доработанный проект решения ЕЭК:')]/following-sibling::td")

    # Отчет об оценке фактического воздействия НПА
    ASSESSMENT_REPORT_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[assessment_report][0][name]']")
    ASSESSMENT_REPORT_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestassessment_report0']/input[@type='file' and not(contains(@style,'none'))]")
    ASSESSMENT_REPORT_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Отчет об оценке фактического воздействия НПА:')]")
    ASSESSMENT_REPORT_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Отчет об оценке фактического воздействия НПА:')]/following-sibling::td")

    # Доработанный отчет об оценке фактического воздействия НПА
    RR_NPA_FIELD_LOCATOR = (
        By.XPATH, "//input[@name='request[rr_npa_file][0][name]']")
    RR_NPA_ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-requestrr_npa_file0']/input[@type='file' and not(contains(@style,'none'))]")
    RR_NPA_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Доработанный отчет об оценке фактического воздействия НПА:')]")
    RR_NPA_FIELD_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Доработанный отчет об оценке фактического воздействия НПА:')]/following-sibling::td")

    # Краткое содержание
    SHORT_CONTENT_FIELD_LOCATOR = (
        By.XPATH, "//textarea[@name='short_content' and @disabled]")
    SHORT_CONTENT_NAME_LOCATOR = (
        By.XPATH, "//span/following-sibling::acronym[contains(text(),'Краткое содержание:')]")

    # Окно Отображения цепочки Regulation
    RCSI_NAME_LOCATOR = (By.XPATH, "//div[@class='wrapper']")
    RCSI_STATUS_LOCATOR = (
        By.XPATH, "//div[@class='version-content version-1 active']//div[@data-v-2fbf3edd][2]")

    RCSI_REPEAT_LINK_LOCATOR = (
        By.XPATH, "//span[contains(text(),'Повторно!')]/parent::a")

    RCSI_OPEN_CHAIN_AFTER_REFUSE = (By.XPATH, "//span[text()='...']/parent::a")

    @staticmethod
    def rsci_next_request_link_locator(request_type):
        locator = (By.XPATH, f"//span[text()='{request_type}']/parent::a")
        return locator

    RCSI_ACTUAL_VERSION_LOCATOR = (
        By.XPATH, "//a[contains(text(),'Актуальная версия')]")

    @staticmethod
    def go_to_rcsi_version(version):
        locator = (By.XPATH, f"//a[text()='Версия ({version})']")
        return locator

    @staticmethod
    def find_rcsi_elements(number):
        locator = (
            By.XPATH, f"//div[contains(@class,'version-content version-')]//div[text()='{number}']/../../../../..")
        return locator

    @staticmethod
    def find_rcsi_number(number):
        locator = RegulationDocumentLocators.find_rcsi_elements(number)
        locator = (locator[0], locator[1] + "//div[@class='text']")
        return locator

    @staticmethod
    def find_rcsi_name(number):
        locator = RegulationDocumentLocators.find_rcsi_elements(number)
        locator = (locator[0], locator[1] + "//div[@class='title-text']")
        return locator

    @staticmethod
    def find_rcsi_project(number):
        locator = RegulationDocumentLocators.find_rcsi_elements(number)
        locator = (locator[0], locator[1] +
                   "//span[text()='Проект']/../../parent::li[not(contains(@class,'hide'))]")
        return locator

    @staticmethod
    def find_rcsi_request(number):
        locator = RegulationDocumentLocators.find_rcsi_elements(number)
        locator = (locator[0], locator[1] +
                   "//span[text()='Заявка']/../../parent::li[not(contains(@class,'hide'))]")
        return locator

    @staticmethod
    def find_rcsi_answer(number):
        locator = RegulationDocumentLocators.find_rcsi_elements(number)
        locator = (locator[0], locator[1] + "//span[text()='Ответ']")
        return locator

    @staticmethod
    def find_rcsi_refuse(number):
        locator = RegulationDocumentLocators.find_rcsi_elements(number)
        locator = (locator[0], locator[1] +
                   "//span[text()='Отказ']/../../parent::li[not(contains(@class,'hide'))]")
        return locator

    @staticmethod
    def find_rcsi_dots(number):
        locator = RegulationDocumentLocators.find_rcsi_elements(number)
        locator = (locator[0], locator[1] +
                   "//span[text()='...']/../../parent::li[not(contains(@class,'hide'))]")
        return locator

    # Предупреждение о повторности заявки
    REPEAT_MESSAGE_LOCATOR = (
        By.XPATH, "//div[@id='regulation_alert_of_repeat']")

    # Ошибки
    REGULATION_ERROR_MESSAGE_LOCATOR = (
        By.XPATH, "//div[@data-name='request_regulation_common']")
    REGULATION_ERROR_MESSAGE_ID_LOCATOR = (
        By.XPATH, "//div[@data-name='request_id_prav_act']")


class ChangeResponsibleInfoLocators(RegulationDocumentLocators):
    # Тип заявки
    REQUEST_TYPE_NAME_35_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Тип заявки:')]]")
    REQUEST_TYPE_FIELD_VIEW_MODE_35_LOCATOR = (
        By.XPATH, "//td[not(span) and text()[contains(.,'Тип заявки:')]]/following-sibling::td")

    # Наименование проекта НПА (отчета ОФВ)
    NPA_NAME_FIELD_35_LOCATOR = RegulationDocumentLocators.NPA_NAME_FIELD_LOCATOR
    NPA_NAME_NAME_FIELD_35_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Наименование проекта НПА (отчета ОФВ):')]")
    NPA_NAME_VIEW_MODE_35_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Наименование проекта НПА (отчета ОФВ):')]/following-sibling::td")

    # ID проекта НПА
    ID_NPA_PROJECT_NAME_35_LOCATOR = RegulationDocumentLocators.ID_NPA_PROJECT_NAME_LOCATOR
    ID_NPA_PROJECT_FIELD_35_LOCATOR = RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_LOCATOR
    ID_NPA_PROJECT_FIELD_VIEW_MODE_35_LOCATOR = RegulationDocumentLocators.ID_NPA_PROJECT_FIELD_VIEW_MODE_LOCATOR

    # Текущий ответственный сотрудник
    CURRENT_RESPONSIBLE_USER_FIELD_LOCATOR = (
        By.XPATH, "//input[@id='inp_request_current_resp_user_var']")
    CURRENT_RESPONSIBLE_USER_NEW_WINDOW_LOCATOR = (
        By.XPATH, "//input[@id='inp_request_current_resp_user_var']//parent::span/a")
    CURRENT_RESPONSIBLE_USER_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Текущий ответственный сотрудник:')]")
    CURRENT_RESPONSIBLE_USER_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Текущий ответственный сотрудник:')]/following-sibling::td")
    CURRENT_RESPONSIBLE_USER_DELETE_BUTTON = (
        By.XPATH, "//a[@id='remover_request_current_resp_user_var']")

    # Новый ответственный сотрудник
    NEW_RESPONSIBLE_USER_FIELD_LOCATOR = (
        By.XPATH, "//input[@id='inp_request_new_resp_user_var']")
    NEW_RESPONSIBLE_USER_PHONE_FIELD_LOCATOR = (
        By.XPATH, "//input[@id='request_new_resp_user_phone']")
    NEW_RESPONSIBLE_USER_EMAIL_FIELD_LOCATOR = (
        By.XPATH, "//input[@id='request_new_resp_user_email']")
    NEW_RESPONSIBLE_USER_NEW_WINDOW_LOCATOR = (
        By.XPATH, "//input[@id='inp_request_new_resp_user_var']//parent::span/a")
    NEW_RESPONSIBLE_USER_NAME_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Новый ответственный сотрудник:')]")
    NEW_RESPONSIBLE_USER_VIEW_MODE_LOCATOR = (
        By.XPATH, "//td[span and contains(.,'Новый ответственный сотрудник:')]/following-sibling::td")
    NEW_RESPONSIBLE_USER_DELETE_BUTTON = (
        By.XPATH, "//a[@id='remover_request_new_resp_user_var']")

    # Ошибка "Не найдена связанная цепочка заявок"
    ERROR_ID_NOT_FOUND = (By.XPATH, "//div[@data-name='request_id_prav_act']")


class RegulationEATypeWindow:
    FILTER_LICATOR = (By.XPATH, "//input[@id='filter']")
    ADD_BUTTON_LOCATOR = (By.XPATH, "//button")

    @staticmethod
    def find_element_in_ea_window(text):
        locator = (By.XPATH, f"//span[text()='{text}']/parent::label/input")
        return locator


class RegulationAnswerPageLocators:
    NPA_ID_FIELD_LOCATOR = (By.XPATH, "//input[@id='request_id_prav_act']")
    NPA_ID_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'ID проекта НПА')]]")
    NPA_ID_NAME_LOCATOR_2 = (
        By.XPATH, "//td[span and text()[contains(.,'ID отчета об оценке фактического воздействия')]]")

    DATE_START_FIELD_LOCATOR = (
        By.XPATH, "//input[@id='request_start_of_discuss']")
    DATE_START_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Дата начала')]]")

    DATE_END_FIELD_LOCATOR = (
        By.XPATH, "//input[@id='request_end_of_discuss']")
    DATE_END_NAME_LOCATOR = (
        By.XPATH, "//td[span and text()[contains(.,'Дата окончания')]]")

    ADD_DOCUMENT_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-file_upload']//input[last()]")


class AdministrationRegulationLocators:
    VERSON_LINK_LOCATOR = (
        By.XPATH, "//ul[@class='menu']//a[text()='Версии процессов']")
    PROCESS_LINK_LOCATOR = (
        By.XPATH, "//ul[@class='menu']//a[text()='Процессы рассмотрения заявок']")
    TYPE_LINK_LOCATOR = (
        By.XPATH, "//ul[@class='menu']//a[text()='Типы заявок']")
    REF_EA_TYPE_LINK_LOCATOR = (
        By.XPATH, "//ul[@class='menu']//a[text()='Справочник видов экономической деятельности']")
    CONTROL_LINK_LOCATOR = (
        By.XPATH, "//ul[@class='menu']//a[text()='Контроль']")


class DirectoryVEDLocators(AdministrationRegulationLocators):
    BANNED_SELECTOR_LOCATOR = (By.XPATH, "//select[@id='is_disabled']")
    ADD_REF_EA_TYPE_LINK_LOCATOR = (By.XPATH, "//a[text()='добавить']")
    TABLE_HEAD_LOCATOR = (By.XPATH, "//thead")

    # Поиск выбранного типа экономической деятельности
    @staticmethod
    def find_created_ea_type(text):
        locator = (
            By.XPATH, f"//strong[text()='{text}']/parent::td/parent::tr")
        return locator

    @staticmethod
    def edit_created_ea_type(text):
        locator = DirectoryVEDLocators.find_created_ea_type(text)
        locator = (locator[0], locator[1] + "//a[text()='редактировать']")
        return locator

    @staticmethod
    def delete_created_ea_type(text):
        locator = DirectoryVEDLocators.find_created_ea_type(text)
        locator = (locator[0], locator[1] + "//a[text()='удалить']")
        return locator

    # Страница "Создание нового вида экономической деятельности"
    CODE_NAME_LOCATOR = (
        By.XPATH, "//div[@class='title' and span and text()='Код:']")
    CODE_INPUT_LOCATOR = (By.XPATH, "//input[@id='code']")
    NAME_NAME_LOCATOR = (
        By.XPATH, "//div[@class='title' and span and text()='Наименование:']")
    NAME_INPUT_LOCATOR = (By.XPATH, "//input[@id='name']")
    START_DATE_INPUT_LOCATOR = (By.XPATH, "//input[@id='start_date']")
    NAME_DATE_LOCATOR = (
        By.XPATH, "//div[@class='title' and not(span) and text()='Период действия:']")
    END_DATE_INPUT_LOCATOR = (By.XPATH, "//input[@id='end_date']")
    SAVE_BUTTON_LOCATOR = (By.XPATH, "//input[@value='Сохранить']")


class RegulationControlLocators(AdministrationRegulationLocators):
    NPA_IDENTIFICATOR_NAME_LOCATOR = (
        By.XPATH, "//div[text()='Идентификатор НПА:']")
    NPA_IDENTIFICATOR_FIELD_LOCATOR = (By.XPATH, "//input[@id='id_prav_act']")

    DOCUMENT_IDENTIFICATOR_NAME_LOCATOR = (
        By.XPATH, "//div[text()='Идентификатор документа:']")
    DOCUMENT_IDENTIFICATOR_FIELD_LOCATOR = (
        By.XPATH, "//input[@id='document_id']")

    FIND_BUTTON_LOCATOR = (
        By.XPATH, "//div[@class='tools']/input[@value='Найти']")

    KEY_DATE_1_LOCATOR = (
        By.XPATH, "//td[text()='Завершение обсуждения/экспертизы проекта НПА']/parent::tr//input[@class='key_date']")
    SAVE_CHANGES_1_LOCATOR = (
        By.XPATH, "//td[text()='Завершение обсуждения/экспертизы проекта НПА']/parent::tr//a[@class='update']")
    SEND_NOTIFICATION_1_LOCATOR = (
        By.XPATH, "//td[text()='Завершение обсуждения/экспертизы проекта НПА']/parent::tr//a[@class='send-notify']")

    KEY_DATE_2_LOCATOR = (
        By.XPATH, "//td[text()='Срок исполнения заявки']/parent::tr//input[@class='key_date']")
    SAVE_CHANGES_2_LOCATOR = (
        By.XPATH, "//td[text()='Срок исполнения заявки']/parent::tr//a[@class='update']")
    SEND_NOTIFICATION_2_LOCATOR = (
        By.XPATH, "//td[text()='Срок исполнения заявки']/parent::tr//a[@class='send-notify']")


class SystemNotificationLocators:
    SAVE_BUTTON_LOCATOR = (By.XPATH, "//input[@value='Сохранить']")
    RETURN_LINK_LOCATOR = (By.XPATH, "//a[text()='Вернуться']")

    def __init__(self, field_name):
        fields = {
            "Уведомлять об ошибке отправки статуса документа в ОСМФ": "email-group-1",
            "Уведомлять об ошибках ССТУ": "email-group-2",
            "Уведомлять об ошибках интеграции c ОСМФ": "email-group-4",
            "Уведомлять об ошибках подписания документа ЭП": "email-group-5",
            "Уведомлять об ошибках сервиса проверки сертификата ЭП": "email-group-13",
            "Уведомлять об окончании срока исполнения заявок regulation": "email-group-6",
            "Уведомлять о завершении обсуждения/экспертизы проекта НПА на сайте regulation.gov.ru": "email-group-7",
            "Уведомлять о падении процесса МЭДО интеграции": "email-group-10",
            'Уведомлять о возниконовении ошибок при взаимодействии с системой "Аудит"': "email-group-11",
            "Уведомлять об ошибках интеграции c Kremlin": "email-group-12",
        }

        self.field = fields[field_name]
        self.title = field_name

    def notification_field_locator(self):
        locator = (By.XPATH, f"//div[@id='{self.field}']")
        return locator

    def notification_title_locator(self):
        locator = self.notification_field_locator()
        locator = (locator[0], locator[1] +
                   f"/div[@class='title' and contains(text(),'{self.title}')]")
        return locator

    def notification_input_email_locator(self):
        locator = self.notification_field_locator()
        locator = (locator[0], locator[1] + "/input[@class='add']")
        return locator

    def notification_add_button_locator(self):
        locator = self.notification_field_locator()
        locator = (locator[0], locator[1] + "/input[@type='button']")
        return locator

    def notification_email_locator(self, email):
        locator = self.notification_field_locator()
        locator = (locator[0], locator[1] + f"//span[text()='{email}']")
        return locator

    def notification_all_emails_locator(self):
        locator = self.notification_field_locator()
        locator = (locator[0], locator[1] + "//div[@class='item']")
        return locator

    @staticmethod
    def notification_email_locator(email):
        locator = (By.XPATH, f"//span[text()='{email}']")
        return locator
