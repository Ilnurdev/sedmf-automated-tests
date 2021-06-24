from pages.main_functions import MainFunc


SERVER = MainFunc.config()


class URLs:
    # Все документы
    AUTH_LINK = SERVER + "/auth.php"
    OPENED_DOCUMENT_LINK = SERVER + "/document.card.php?"

    # Regulation документы
    REGULATION_LINK = OPENED_DOCUMENT_LINK + "category=6&r_category=4&card_type=2&version_id=2"
    CHANGE_INFO_LINK = OPENED_DOCUMENT_LINK + "category=6&r_category=4&card_type=2&request_type=59"

    # Внутренние заявки
    ENTER_REQUEST_LINK = OPENED_DOCUMENT_LINK + "category=6&r_category=4&card_type=1"

    # Настройки
    SETTINGS_LINK = SERVER + "/settings.php?"

    # Настройки/Настройка системных уведомлений
    SYSTEM_NOTIFY_LINK = SERVER + "/public/notify/system/?"

    # Настройки/Администрирование заявок Regulation
    ADMINISTRATION_REGULATION_REQUEST = SERVER + "/public/regulation/settings/?"
    DIRECTORY_VED_LINK = ADMINISTRATION_REGULATION_REQUEST[:-1] + "ref-ea-type/?"
    REGULATION_CONTROL_LINK = ADMINISTRATION_REGULATION_REQUEST[:-1] + "control/?"

    # Настройки/Вид информации ОСМФ
    OSMF_INFORMATION_LINK = SERVER + "/public/ref/request-information-kind/?"
    OSMF_INFORMATION_PLACE_LINK = SERVER + "/public/ref/request-osmf-information/?"

