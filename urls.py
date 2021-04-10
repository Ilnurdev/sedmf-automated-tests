from pages.main_functions import MainFunc


SERVER = MainFunc.config()


class URLs:
    # Все документы
    AUTH_LINK = SERVER + "/auth.php"
    OPENED_DOCUMENT_LINK = SERVER + "/document.card.php?"

    # Regulation документы
    REGULATION_LINK = OPENED_DOCUMENT_LINK + "category=6&r_category=4&card_type=2&version_id=2"
    CHANGE_INFO_LINK = OPENED_DOCUMENT_LINK + "category=6&r_category=4&card_type=2&request_type=59"