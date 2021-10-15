from selenium.webdriver.common.by import By


VIEW_MODE = "/following::td[1]"


class AuthPageLocators:
    SELECT_ORG_LOCATOR = (By.CSS_SELECTOR, "#group_id")
    SELECT_USR_LOCATOR = (By.CSS_SELECTOR, "#user_id")
    ENTER_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "#password")
    ENTER_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".error-wrapper input")


class MainPageLocators:

    """

    Incoming = 0
    Outgoing = 1
    Incoming OG = 2
    Outgoing OG = 3
    Eneter = 4
    ORD = 5
    SOGL = 6

    """

    link_name: str
    block_num: int
    def __init__(self, link_name, block_num=1):
        self.top_panel = self.TopPanelBlock(link_name)
        self.closed_block = self.ClosedDocumentBlock(str(block_num))
        self.open_block = self.OpenDocumentBlock(link_name, str(block_num))
        self.status = self.DocumentStatuses(link_name)
        self.menu = self.UserMenu(link_name)
        self.statistic = self.Statistics(link_name)

    # Настройки системы
    SETTINGS_LINK_LOCATOR = (
        By.XPATH, "//div[@class='left_panel_box settings']//a[text()[contains(.,'Настройки системы')] and contains(@href,'/settings.php?')]")

    # Ссылки шапки
    MAIN_PAGE_LINK_LOCATOR = (By.XPATH, "//div[@class='minfinrf']/a")
    STP_PAGE_LINK_LOCATOR = (
        By.XPATH, "//div[@class='support']/a[not(@class='email')]")
    STP_EMAIL_LINK_LOCATOR = (
        By.XPATH, "//div[@class='support']/a[@class='email']")
    NOTIFICATION_LINK_LOCATOR = (By.XPATH, "//a[@id='notices-link']")
    EXIT_LINK_LOCATOR = (By.XPATH, "//div[@class='logoff']")

    class TopPanelBlock:
        def __init__(self, link_name):
            links = {
                "Расширенный поиск": "/document_search.php?",
                "Бланки документов": "/blanks/blanks_948014.php?",
                "Не зарегистрировано в организации-адресате": "/document.php?runnumbered=1&",
                "События из МЭДО": "/medo_history_all.php?",
                "Отказано в регистрации": "/document.php?refusedreg=1&",
                "Отказано в регистрации (входящие)": "/refused_docs.php?",
                "Документы из МЭДО (Ведомственная)": "/document.php?medo=1&medo_on_reg=0&status=0&category=0&folder_id=2&",
                "Документы из МЭДО (Правительственная)": "/document.php?medo=1&medo_on_reg=0&status=0&category=0&folder_id=1&",
                "Документы из МЭДО (Секретариат)": "/document.php?medo=1&medo_on_reg=0&status=0&category=0&folder_id=21&",
                "Документы из МЭДО (прочие)": "/document.php?medo=1&medo_on_reg=0&status=0&category=0&folder_id=-1&",
            }

            try:
                self.link = links[link_name]
            except:
                self.link = ""

        def locator(self):
            return (By.XPATH, f"//div[@id='left_top_panel']//a[contains(@href,'{self.link}')]")

    class ClosedDocumentBlock:
        def __init__(self, block_num):
            text = {
                0: "Все входящие",
                1: "Все исходящие",
                2: "Все вх.обр.граждан",
                3: "Все исх.обр.граждан",
                4: "Все внутренние",
                5: "Все ОРД",
                6: "Все документы",
            }

            self.block = block_num
            self.name = text[int(block_num)]

        def locator(self):
            return (By.XPATH, f"//div[@id='menu_top_{self.block}']//a[text()='{self.name}' and contains(@href,'/document.php?') and contains(@href,'all=1')]")

        def open_block(self):
            return (By.XPATH, f"//div[@id='menu_top_{self.block}']//a[@class='slide down']")

    class OpenDocumentBlock:
        def __init__(self, link_name, block_num):
            self.name = link_name
            self.block = block_num

        def return_locator(self, name):
            elements = ["На регистрации из МЭДО (Ведомственная)",
                        "На регистрации из МЭДО (Правительственная)", "На регистрации из МЭДО (Секретариат)"]
            if name in elements:
                index = name.index("(")
                return f"//div[@id='menu_bottom_{self.block}']//li[text()='{name[index-1:]}']/a[text()='{name[:index-1]}']"
            return f"//div[@id='menu_bottom_{self.block}']//a[text()='{self.name}']"

        def locator(self):
            return (By.XPATH, self.return_locator(self.name))

        def close_block(self):
            return (By.XPATH, f"//div[@id='menu_bottom_{self.block}']//a[@class='slide up']")

    # Статусы документов у пользователей
    class DocumentStatuses:
        def __init__(self, link_name):
            self.name = link_name

        def locator(self):
            return (By.XPATH, f"//div[@class='left_panel_box res_list']//a[text()[contains(.,'{self.name}')]]")

    # Меню пользователя
    class UserMenu:
        def __init__(self, link_name):
            self.name = link_name

        def locator(self):
            bold = ["Исполнение документов", "Написать сообщение"]
            locator = f"//div[@class='left_panel_box']/h3[text()='Меню пользователя']/following::a[text()[contains(.,'Полный перечень')]]" if self.name == "Полный перечень документов" else f"//div[@class='left_panel_box']/h3[text()='Меню пользователя']/following::a{'/b' if self.name in bold else ''}[text()='{self.name}']"

            return (By.XPATH, locator)

    # Статистика и исполнение документов
    class Statistics:
        def __init__(self, link_name):
            links = {
                "Отчеты по исполнению документов": "/public/reports/list-execution-document/index?",
                "Отчеты по обращениям граждан": "/public/reports/list-og/index?",
                "Контрольные отчеты по МЭДО документам": "/medo_reports.php?",
                "Количество направленных писем": "/public/outcorrespondence/report/total-sent/index?",
                "Уведомления": "/document.php?DNSID",
                "Контрольные документы": "/control_stats.php?",
                "Отчеты администратора": "/public/reports/admin/?",
            }

            try:
                self.link = links[link_name]
            except:
                self.link = ""

        def locator(self):
            return (By.XPATH, f"//div[@class='left_panel_box']/h3[text()='Статистика и исполнение документов']/following::a[contains(@href,'{self.link}')]")


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
    NEW_USER_INPUT_LOCATOR = (By.XPATH, "//span[@class='rtxt' and not(contains(@style,'none'))]//input")
    ADD_USER_BUTTON_LOCATOR = (By.XPATH, "//input[@type='button' and @value='Добавить согласующего']")

    # Попап окно отсутвия ЭП
    POPUP_WINDOW_ERROR = (By.XPATH, "//div[contains(@class, 'ui-dialog ui-widget')]")
    POPUP_WINDOW_ERROR_CANCEL_BUTTON = (By.XPATH, POPUP_WINDOW_ERROR[1] + "//span[text()='Отмена']/parent::button")

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
    def find_text_locator(element, attr="*"):
        return (By.XPATH, f"//{attr}[text()[contains(.,'{element}')]]")

    # Заголовок страницы
    TITLE_LOCATOR = (By.CSS_SELECTOR, "h1")

    # № документа
    DOCUMENT_NAME_LOCATOR = (By.XPATH, "//td[@class='b2 highlight']")

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
    
    def recipient_new_window_locator(text):
        return (By.XPATH, f"//span[@id='sp2_g_su_r_0']/a[text()='{text}']")

    # Выбор пользователя из выпадающего окна
    CHOOSE_USER_FROM_DROP_LIST = (
        By.XPATH, "//div[@class='sg-div']/div[@id='fio_0']")

    # Добавить файлы
    ADD_FILE_BUTTON_LOCATOR = (
        By.XPATH, "//div[@id='uploadifive-file_upload']/input[not(contains(@style,'none'))]")
    WAIT_FILE_DOWNLOAD_LOCATOR = (By.XPATH, "//div[@class='uploadifive-queue-item complete' and @style='display: none;']")

    # Сохранить + просмотр
    SAVE_RCD_BUTTON_LOCATOR = (By.XPATH, "//input[@id='save_view']")

    # Удалить документ
    DELETE_FILE_LOCATOR = (By.XPATH, "//tr[@class='file']//a[@class='delete']")

    # Автор обращения
    APPEAL_AUTHOR_NAME_LOCATOR = (By.XPATH, "//span[@class='required']/parent::td[contains(text(),'Автор обращения:')]")
    APPEAL_AUTHOR_FIELD_LOCATOR = (By.XPATH, f"{APPEAL_AUTHOR_NAME_LOCATOR[1]}/following-sibling::td//input[@type='text']")

    # Результат рассмотрения
    REVIEW_RESULT_NAME_LOCATOR = (By.XPATH, "//span[@class='required']/parent::td[contains(text(),'Результат рассмотрения')]")
    REVIEW_RESULT_FIELD_LOCATOR = (By.XPATH, f"{REVIEW_RESULT_NAME_LOCATOR[1]}/following-sibling::td/select")
    
    # Краткое содержание
    SHORT_CONTENT_FIELD_LOCATOR = (By.XPATH, "//tr[@class='shortContent']//textarea[@id='short_content']")
    SHORT_CONTENT_NAME_LOCATOR = (
        By.XPATH, "//span/following-sibling::acronym[contains(text(),'Краткое содержание:')]/parent::td")

    def choose_user_from_drop_list_locator(self, text=None):
        loc = "//div[@class='sg-div']"
        if text == None:
            return (By.XPATH, f"{loc}/div[@id='fio_0']")
        return (By.XPATH, f"{loc}//strong[text()[contains(.,'{text}')]]")

    # Связка
    @staticmethod
    def link_document(id):
        return (By.XPATH, f"//a[@target='_blank' and contains(@href,'{id}')]")


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
    
    # Печать
    PRINT_PICTOGRAM_LOCATOR = (By.XPATH, "//a[@id='card_button_7']/img")
    SAVE_ONLY_DOCUMENT_BUTTON_LOCATOR = (By.XPATH, "//a[@id='print_only_doc_csdr']")


class ChooseUserFromNewWindow:
    FIRST_USER_LINK_LOCATOR = (By.XPATH, "//li//a")
    USER_FIND_LOCATOR = (By.XPATH, "//input[@id='filter_name']")

    @staticmethod
    def find_user_by_id(id):
        return (By.XPATH, f"//input[@value='{id}']/parent::li/a")


class ChooseOrganisationFromNewWindow:
    ORG_FIND_LOCATOR = (By.XPATH, "//input[@id='org_name']")
    USER_FIND_LOCATOR = (By.XPATH, "//input[@id='fio']")
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


class SettingsPageLocators:
    def __init__(self, name):
        self.name = name

    def choose_setting(self):
        locator = (By.XPATH, f"//a[text()='{self.name}']")
        return locator


class EnterRequestDocumentPageLocators:
    def __init__(self, num, parent=0):
        self.change_root = self.ChangeRoot(num, parent)
        self.offical_and_enter_mf = self.OfficialEnterMF(num)
        self.provision_sh = self.ProvisionSoftwareHardware(num)

    # Тип заявки
    REQUEST_TYPE_NAME_LOCATOR = (
        By.XPATH, "//tr[@id='request']/td[text()[contains(.,'Тип заявки:')]]")
    REQUEST_TYPE_FIELD_LOCATOR = (By.XPATH, "//select[@id='request_type']")
    REQUEST_TYPE_VIEW_MODE_LOCATOR = (
        REQUEST_TYPE_NAME_LOCATOR[0], REQUEST_TYPE_NAME_LOCATOR[1] + VIEW_MODE)

    # Кнопка удаления добавленных блоков
    def delete_block_button(self, last=False):
        locator = (
            By.XPATH, "(//tr[not(@style='display: none;') and contains(@class,'request-field')]//a[@data-role='remove-btn'])")
        return locator if last == False else (locator[0], locator[1] + "[last()]")

    # Кнопки удаления
    DELETE_BUTTON_LOCATOR = (
        By.XPATH, "//tr[contains(@class,'request-field')]//a[text()='Удалить' or text()='удалить']")

    class ChangeRoot:
        # Обрабатываются сведения
        INFORMATION_NAME_LOCATOR = (
            By.XPATH, "//tr[@class='request-field']//td[contains(text(),'Обрабатываются сведения:')]")  # //td[text()[contains(.,'Обрабатываются сведения:')] and span]
        INFORMATION_NOT_SECRET_RADIOBUTTON_LOCATOR = (
            By.XPATH, "//input[@id='is_secret_0']")
        INFORMATION_SECRET_RADIOBUTTON_LOCATOR = (
            By.XPATH, "//input[@id='is_secret_1']")
        INFORMATION_VIEW_MODE_LOCATOR = (
            INFORMATION_NAME_LOCATOR[0], INFORMATION_NAME_LOCATOR[1] + VIEW_MODE)

        # Добавить сотрудника
        ADD_STAFF_BUTTON_LOCATOR = (
            By.XPATH, "//button[@data-role='add-staff']")

        def __init__(self, num, parent):
            self.num = str(num)
            self.parent = str(parent)

        # ФИО
        def fio(self):
            # //tr[@data-num='{self.parent}']/td[text()[contains(.,'ФИО:')] and span]
            return (By.XPATH, f"//td[text()[contains(.,'ФИО:')]]")

        def fio_field(self):
            return (By.XPATH, f"//input[@id='inp_userField[{self.parent}]']")

        def fio_delete(self):
            return (By.XPATH, f"//a[@id='remover_userField[{self.parent}]']")

        def fio_view_mode(self):
            return (By.XPATH, "//td[text()[contains(.,'ФИО:')]]" + VIEW_MODE)

        # Наименование информационного ресурса
        def information_resource(self):
            # //tr[@data-num='{self.num}' and @data-parent-num='{self.parent}']/td[text()[contains(.,'Наименование информационного ресурса:')] and span]
            return (By.XPATH, f"//td[text()[contains(.,'Наименование информационного ресурса:')]]")

        def information_resource_field(self):
            return (By.XPATH, f"//tr[@data-num='{self.num}' and @data-parent-num='{self.parent}']//input[@class='ui-autocomplete-input']")

        def information_resource_delete(self):
            return (By.XPATH, f"//tr[@data-num='{self.num}' and @data-parent-num='{self.parent}']//a[@class='remove']")

        def information_resource_view_mode(self):
            return (By.XPATH, "//td[text()[contains(.,'Наименование информационного ресурса:')]]" + VIEW_MODE)

        # Вид действий
        def action_type(self):
            # //tr[@data-num='{self.num}' and @data-parent-num='{self.parent}']/td[text()[contains(.,'Вид действий:')] and span]
            return (By.XPATH, f"//td[text()[contains(.,'Вид действий:')]]")

        def action_type_field(self):
            return (By.XPATH, f"//select[@name='request[staff][{self.parent}][resources][{self.num}][action]']")

        def action_type_view_mode(self):
            return (By.XPATH, "//td[text()[contains(.,'Вид действий:')]]" + VIEW_MODE)

        # Описание функциональной роли
        def functional_role(self):
            # //tr[@data-num='{self.num}' and @data-parent-num='{self.parent}']/td[span and text()[contains(.,'Описание функциональной роли:')]]
            return (By.XPATH, f"//td[text()[contains(.,'Описание функциональной роли:')]]")

        def functional_role_field(self):
            return (By.XPATH, f"//textarea[@name='request[staff][{self.parent}][resources][{self.num}][description]']")

        def functional_role_view_mode(self):
            return (By.XPATH, f"//td[text()[contains(.,'Описание функциональной роли:')]]" + VIEW_MODE)

        # Добавить ресурс
        def add_resource_button(self):
            return (By.XPATH, f"//button[@data-role='add-resource' and @data-num='{self.num}']")

    class OfficialEnterMF:
        # Тип изменения
        CHANGE_TYPE_NAME_LOCATOR = (
            By.XPATH, "//tr[@data-table='requests']/td[text()[contains(.,'Тип изменения:')]]")
        CHANGE_TYPE_FIELD_LOCATOR = (
            By.XPATH, "//select[@name='request[updates][type_change]']")
        CHANGE_TYPE_VIEW_MODE_LOCATOR = (
            CHANGE_TYPE_NAME_LOCATOR[0], CHANGE_TYPE_NAME_LOCATOR[1] + VIEW_MODE)

        # * Путь
        PATH_NAME_LOCATOR = (
            By.XPATH, "//tr[@data-table='requests']/td[span and text()[contains(.,'Путь:')]]")
        PATH_FIELD_LOCATOR = (By.XPATH, "//textarea[@id='ws-path-id']")
        PATH_BUTTON_LOCATOR = (
            By.XPATH, "//tr[@data-role='update-path']//button[@data-role='ws-category-button']")
        PATH_VIEW_MODE_LOCATOR = (
            PATH_NAME_LOCATOR[0], PATH_NAME_LOCATOR[1] + VIEW_MODE)

        # * Переместить в
        MOVE_TO_NAME_LOCATOR = (
            By.XPATH, "//tr[@data-table='requests']/td[span and text()[contains(.,'Переместить в:')]]")
        MOVE_TO_FIELD_LOCATOR = (By.XPATH, "//textarea[@id='ws-move-path-id']")
        MOVE_TO_VIEW_MODE = (
            MOVE_TO_NAME_LOCATOR[0], MOVE_TO_NAME_LOCATOR[1] + VIEW_MODE)

        # Дата публикации
        PUBLISH_DATE_NAME_LOCATOR = (
            By.XPATH, "//tr[@data-role='update-publish-date']//td[contains(text(),'Дата публикации:')]")
        PUBLISH_DATE_FIELD_LOCATOR = (
            By.XPATH, "//input[@name='request[updates][published_at]']")
        PUBLISH_DATE_VIEW_MODE_LOCATOR = (
            PUBLISH_DATE_NAME_LOCATOR[0], PUBLISH_DATE_NAME_LOCATOR[1] + VIEW_MODE)

        # Ответственный
        RESPONSIBLE_NAME_LOCATOR = (
            By.XPATH, "//tr[@data-block='update']/td[span and text()[contains(.,'Ответственный')]]")
        RESPONSIBLE_FIELD_LOCATOR = (
            By.XPATH, "//input[contains(@id,'inp_userField[')]")
        RESPONSIBLE_VIEW_MODE_LOCATOR = (
            RESPONSIBLE_NAME_LOCATOR[0], RESPONSIBLE_NAME_LOCATOR[1] + VIEW_MODE)

        # Телефон
        PHONE_NUMBER_NAME_LOCATOR = (
            By.XPATH, "//tr[@data-block='update']//td[span and text()[contains(.,'Телефон:')]]")
        PHONE_NUMBER_FIELD_LOCATOR = (
            By.XPATH, "//input[@name='request[updates][phone_number]']")
        PHONE_NUMBER_VIEW_MODE_LOCATOR = (
            PHONE_NUMBER_NAME_LOCATOR[0], PHONE_NUMBER_NAME_LOCATOR[1] + VIEW_MODE)

        # Комментарий
        COMMENT_NAME_LOCATOR = (
            By.XPATH, "//tr[@data-table='requests']/td[not(span) and text()[contains(.,'Комментарий:')]]")
        COMMENT_FIELD_LOCATOR = (
            By.XPATH, "//input[@name='request[updates][review]']")
        COMMENT_VIEW_MODE_LOCATOR = (
            COMMENT_NAME_LOCATOR[0], COMMENT_NAME_LOCATOR[1] + VIEW_MODE)

        # Добавить тип операции
        ADD_UPDATE_BUTTON_LOCATOR = (
            By.XPATH, "//button[@data-role='add-update']")

        def __init__(self, num):
            self.num = num
            self.block = f"//tr[@data-block='update' and @data-num='{num}' and not(contains(@style,'none'))]"

        # Операция
        def operation(self):
            return (By.XPATH, f"//tr[@data-block='update' and @data-num='{self.num}']/td[text()[contains(.,'Операция:')]]")

        def operation_field(self):
            return (By.XPATH, f"//select[@name='request[updates][block][{self.num}][type]']")

        def operation_view_mode(self):
            return (By.XPATH, "//td[text()[contains(.,'Операция:')]]" + VIEW_MODE)

        # Документ
        def document(self):
            return (By.XPATH, self.block + "/td[span and text()[contains(.,'Документ:')]]")

        def document_field(self):
            return (By.XPATH, self.block + f"//textarea[contains(@name,'request[updates][block][{self.num}]')]")

        def document_add_file(self):
            return (By.XPATH, self.block + "//input[@type='file']")

        def document_view_mode(self):
            return (By.XPATH, self.block + "//td[span and text()[contains(.,'Документ:')]]" + VIEW_MODE)

        # Приложения / Приложение (структура рубрики/раздела)
        def application(self):
            return (By.XPATH, self.block + "/td[text()[contains(.,'Приложения:')]]")

        def application_2(self):
            return (By.XPATH, self.block + "/td[text()[contains(.,'Приложение (структура рубрики/раздела):')]]")

        def application_button(self, disable=False):
            locator = (By.XPATH, self.block + "//button")
            if disable == True:
                return (locator[0], locator[1] + "[@disabled]")
            return locator

        def application_field(self, num):
            return (By.XPATH, self.block + f"//div[@data-role='app-item' and @data-num='{num}']//textarea")

        def application_add_file(self, num):
            return (By.XPATH, self.block + f"//div[@data-role='app-item' and @data-num='{num}']//input[@type='file']")

        def application_delete_button(self, num):
            return (By.XPATH, self.block + f"//div[@data-role='app-item' and @data-num='{num}']//a")

        def application_view_mode(self):
            return (By.XPATH, "//td[text()[contains(.,'Приложения:')]]" + VIEW_MODE)

        def application_2_view_mode(self):
            return (By.XPATH, "//td[text()[contains(.,'Приложение (структура рубрики/раздела):')]]" + VIEW_MODE)

        # Вид информации
        def information_type(self):
            return (By.XPATH, self.block + "/td[text()[contains(.,'Вид информации:')]]")

        def information_type_field(self):
            return (By.XPATH, self.block + "//div[@class='info-container custom-autocomplete']//input")

        def information_type_view_mode(self):
            return (By.XPATH, "//td[text()[contains(.,'Вид информации:')]]" + VIEW_MODE)

        # Состав инф-ии
        def info_composition(self):
            return (By.XPATH, self.block + "/td[text()[contains(.,'Состав инф-ии:')]]")

        def info_composition_field(self):
            return (By.XPATH, self.block + "//div[@class='info-content-container custom-autocomplete']//input")

        def info_composition_view_mode(self):
            return (By.XPATH, "//td[text()[contains(.,'Состав инф-ии:')]]" + VIEW_MODE)

        # Название
        def name(self):
            return (By.XPATH, self.block + "/td[span and text()[contains(.,'Название:')]]")

        def name_field(self):
            return (By.XPATH, self.block + f"//input[@name='request[updates][block][{self.num}][name]']")

        def name_view_mode(self):
            locator = self.name()
            return (locator[0], locator[1] + VIEW_MODE)

        # Новое название
        def new_name(self):
            return (By.XPATH, self.block + "/td[span and text()[contains(.,'Новое название:')]]")

        def new_name_field(self):
            return (By.XPATH, self.block + f"//input[@name='request[updates][block][{self.num}][new_name]']")

        def new_name_view_mode(self):
            locator = self.new_name()
            return (locator[0], locator[1] + VIEW_MODE)

        # Заменить (текущий)
        def replace_doc(self):
            return (By.XPATH, self.block + "//td[span and text()[contains(.,'Заменить (текущий):')]]")

        def replace_doc_field(self):
            return (By.XPATH, self.block + f"//textarea[@name='request[updates][block][{self.num}][new_name]']")

        def replace_doc_view_mode(self):
            return (By.XPATH, "//td[span and text()[contains(.,'Заменить (текущий):')]]" + VIEW_MODE)

        # Документ (новый)
        def new_doc(self):
            return (By.XPATH, self.block + "/td[span and text()[contains(.,'Документ (новый):')]]")

        def new_doc_field(self):
            return (By.XPATH, self.block + "//div[@data-role='files-placeholder']//textarea")

        def new_doc_add_file_button(self):
            return (By.XPATH, self.block + "//input[@data-role='upload-doc-file']")

        def new_doc_view_mode(self):
            return (By.XPATH, "//td[span and text()[contains(.,'Документ (новый):')]]" + VIEW_MODE)

    class ProvisionSoftwareHardware:
        ADD_DEVICE_BUTTON_LOCATOR = (
            By.XPATH, "//button[@data-role='add-device']")

        def __init__(self, num):
            self.num = num
            self.block = f"//tr[@data-num='{self.num}' and not(contains(@style, 'none'))]"

        # Вид работ
        def work_type(self):
            # //td[span and text()[contains(.,'Вид работ:')]]
            return (By.XPATH, "//td[text()[contains(.,'Вид работ:')]]")

        def work_type_selector(self):
            return (By.XPATH, self.block + f"//select[@name='request[devices][{self.num}][job]']")

        def work_type_view_mode(self):
            locator = self.work_type()
            return (locator[0], locator[1] + VIEW_MODE)

        # Снять с (ФИО, адрес)
        def remove_from(self):
            # /td[span[text()='Снять с'] and text()[contains(.,'(ФИО, адрес)')]]
            return (By.XPATH, self.block + "/td[text()[contains(.,'(ФИО, адрес)')]]")

        def remove_from_field(self):
            return (By.XPATH, self.block + "//input[@class='text']")

        def remove_from_address(self):
            return (By.XPATH, self.block + f"//select[@name='request[devices][{self.num}][fromAddr]']")

        def remove_from_room(self):
            return (By.XPATH, self.block + f"//select[@name='request[devices][{self.num}][fromRoom]']")

        def remove_from_view_mode(self):
            locator = self.remove_from()
            return (locator[0], locator[1] + VIEW_MODE)

        def remove_from_address_view_mode(self):
            locator = self.remove_from()
            return (locator[0], locator[1] + "/following::td[2]")

        # Установить (ФИО, адрес)
        def install_to(self):
            return (By.XPATH, self.block + "/td[text()[contains(.,'Установить (ФИО, адрес)')]]")

        def install_to_field(self):
            return (By.XPATH, self.block + "//span[@data-role='to-user']//input[@class='text']")

        def install_to_address(self):
            return (By.XPATH, self.block + f"//select[@name='request[devices][{self.num}][toAddr]']")

        def install_to_room(self):
            return (By.XPATH, self.block + f"//select[@name='request[devices][{self.num}][toRoom]']")

        def install_to_view_mode(self):
            locator = self.install_to()
            return (locator[0], locator[1] + VIEW_MODE)

        def install_to_address_view_mode(self):
            locator = self.install_to()
            return (locator[0], locator[1] + "/following::td[2]")

        # В соответствии с карточкой учета СВТ
        def svt_card(self):
            # //td[span and text()[contains(.,'В соответствии с карточкой учета СВТ:')]]
            return (By.XPATH, self.block + "//td[text()[contains(.,'В соответствии с карточкой учета СВТ:')]]")

        def svt_card_button(self):
            return (By.XPATH, self.block + f"//button[@data-num='{self.num}']")

        def svt_card_view_mode(self):
            locator = self.svt_card()
            return (locator[0], locator[1] + VIEW_MODE)

        def svt_window_first_element(self):
            return (By.XPATH, "//input")

        def svt_window_continue_button(self):
            return (By.XPATH, "//button[@data-role='select']")

        # Наименование устройства
        def device_name(self):
            return (By.XPATH, self.block + "//td[text()[contains(.,'Наименование устройства:')]]")

        def device_name_category(self):
            return (By.XPATH, self.block + f"//select[@name='request[devices][{self.num}][deviceCategoryId]']")

        def device_name_device(self):
            return (By.XPATH, self.block + f"//select[@name='request[devices][{self.num}][deviceId]']")

        def device_name_view_mode(self):
            locator = self.device_name()
            return (locator[0], locator[1] + VIEW_MODE)

        # Перевод в департамент
        def transfer_to_department(self):
            return (By.XPATH, self.block + f"//td[text()[contains(.,'Перевод в департамент:')]]")

        def transfer_to_department_field(self):
            return (By.XPATH, self.block + f"//select[@name='request[devices][{self.num}][toDepId]']")

        def transfer_to_department_view_mode(self):
            locator = self.transfer_to_department()
            return (locator[0], locator[1] + VIEW_MODE)

        # Обоснование/комментарий
        def justification(self):
            return (By.XPATH, "//td[text()[contains(.,'Обоснование/комментарий')]]")

        def justification_field(self):
            return (By.XPATH, self.block + f"//textarea[@name='request[devices][{self.num}][comment]']")

        def justification_view_mode(self):
            locator = self.justification()
            return (locator[0], locator[1] + VIEW_MODE)


class OSMFInformationSettingsLocators:
    ADD_BUTTON_LOCATOR = (By.XPATH, "//a[text()='Добавить']")
    BACK_BUTTON_LOCATOR = (By.XPATH, "//a[text()='Назад']")
    ENTER_NEW_OSMF_LOCATOR = (
        By.XPATH, "//tr[@class='r0 new']//input[@type='text']")
    SAVE_BUTTON_LOCATOR = (By.XPATH, "//input[@value='Сохранить']")

    def __init__(self, name):
        self.name = name

    def osmf_type(self):
        return (By.XPATH, f"//div[text()='{self.name}']")

    def edit_osmf(self):
        locator = self.osmf_type()
        return (locator[0], locator[1] + "/following::td/a[@class='dotted edit']")

    def delete_osmf(self):
        locator = self.osmf_type()
        return (locator[0], locator[1] + "/following::td/a[@class='dotted delete']")

    def input_edit_osmf(self):
        return (By.XPATH, f"//input[@value='{self.name}']")


class ElSignatureLocators:
    def __init__(self):
        self.extention = self.Extention()
        self.setting = self.Setting()
        self.verification = self.Verification()

    class Extention:
        ENTER_URL_INPUT_LOCATOR = (By.XPATH, "//input[@id='new_node_name']")
        ADD_BUTTON_LOCATOR = (By.XPATH, "//button[@id='add_button']")
        SAVE_BUTTON_LOCATOR = (By.XPATH, "//button[@id='btn_save']")

        def delete_url_button(self, url):
            return (By.XPATH, f"//li[text()='{url}']/button")
    
    class Setting:
        SIGN_BUTTON_LOCATOR = (By.XPATH, "//input[@value='Подписать ЭП']")
        SIGN_INFO_TEXTAREA_LOCATOR = (By.XPATH, "//textarea")
        SEND_SIGN_BUTTON_LOCATOR = (By.XPATH, "//input[@value='Отправить']")
        SIGN_CORRECT_MESSAGE = (By.XPATH, "//div[text()[contains(.,'Подробности: ДЕЙСТВИТЕЛЕН, сертификат выдан аккредитованным удостоверяющим центром')]]")
    
    class Verification:
        def __init__(self):
            self.agree_sheet = self.AgreeSheet()
            self.etalon = self.Etalon()
            self.window = self.ChekWindow()

        class AgreeSheet:
            EP_IS_OK_LOCATOR = (By.XPATH, "//div[@class='agreesheet']//img[contains(@src,'encrypted_ok.gif')]")
        
        class Etalon:
            EP_IS_OK_LOCATOR = (By.XPATH, "//div[@class='author-signatures']//img[contains(@src,'encrypted_ok.gif')]")

        class ChekWindow:
            EP_IS_OK_LOCATOR = (By.XPATH, "//div[@class='green' and contains(.,'Подпись верна')]")
            LINKS_LOCATOR = (By.XPATH, "//div[@class='bg']//a")
