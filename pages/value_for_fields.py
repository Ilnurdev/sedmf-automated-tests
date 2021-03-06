from datetime import timedelta, datetime


class DocumentTitles:
    INCOMING_DOC = "Входящий документ"
    OUTGOING_DOC = "Исходящий документ"
    INCOMING_CITIZEN_APPEAL = "Входящее обращение гражданина"
    OUTGOING_CITIZEN_APPEAL = "Исходящее обращение гражданина"
    OUTGOING_CITIZEN_APPEAL_2 = "Исходящий документ в ответ на обращение граждан"
    ENTER_DOC = "Внутренний документ"
    ORD_DOC = "Организационно-распорядительный документ"
    REQUEST = "Заявка"
    REGULATION_DOC = "Внутренний документ-заявка Regulation"
    ENTER_REQUEST_DOC = "Внутренний документ-заявка"
    OUTGOING_SOGL = "Согласование исходящего документа"
    OUTGOING_ANSWER_SOGL = "Согласование исходящего обращения гражданина"
    ENTER_SOGL = "Согласование внутреннего документа"
    ORD_SOGL = "Согласование организационно-распорядительного документа"
    ENTER_REQUEST_SOGL = "Согласование внутреннего документа-заявки"
    REGULATION_SOGL = "Согласование внутреннего документа-заявки Regulation"


class RegulationFields:
    # Номера постанолений
    NPA_851 = "851"
    NPA_1318 = "1318"
    NPA_96 = "96"
    NPA_373 = "373"
    NPA_83 = "83"

    # Типы заявок
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

    # Заголовки страниц
    SOGL_TITLE = "Согласование внутреннего документа-заявки Regulation"
    ENTER_TITLE = "Внутренний документ-заявка Regulation"
    SOGL_ANSWER_TITLE = "Согласование внутреннего документа-ответа на заявку Regulation"
    ENTER_ANSWER_TITLE = "Внутренний документ-ответ на заявку Regulation"
    SOGL_REFUSE_TITLE = "Согласование внутреннего документа-отказа на заявку Regulation"
    ENTER_REFUSE_TITLE = "Внутренний документ-отказ на заявку Regulation"

    # Ответ
    ANSWER_START_1 = "Дата начала обсуждения уведомления"
    ANSWER_END_1 = "Дата окончания обсуждения уведомления"
    ANSWER_START_2 = "Дата начала обсуждения проекта НПА"
    ANSWER_END_2 = "Дата окончания обсуждения проекта НПА"
    ANSWER_START_3 = "Дата начала экспертизы"
    ANSWER_END_3 = "Дата окончания экспертизы"
    ANSWER_START_4 = "Дата начала обсуждения отчета"
    ANSWER_END_4 = "Дата окончания обсуждения отчета"

    # Краткое содержание
    SHORT_CONTENT_TEXT = "Заявка на размещение информации на официальном сайте regulation.gov.ru"
    SHORT_CONTENT_ANSWER_TEXT = "Ответ на заявку на размещение информации на официальном сайте regulation.gov.ru"
    SHORT_CONTENT_REFUSE_TEXT = "Отказ на заявку на размещение информации на официальном сайте regulation.gov.ru"

    # Поля Regulation
    ORDER_FIELD = "* № постановления"
    REQUEST_TYPE = "* Тип заявки"
    NPA_TYPE = "* Вид НПА"
    NPA_NAME_1 = "* Наименование проекта НПА"
    NPA_NAME_2 = "* Наименование НПА"
    ORG_INFO = "* Сведения об органах и организациях"
    ORG_INFO_NAME = "* Сведения об органах и организациях, Наименование"
    ORG_INFO_EMAIL = "* Сведения об органах и организациях, E-mail"
    EA_TYPE = "* Виды экономической деятельности"
    KEYWORD = "* Ключевые слова"
    DISCUSS_PERIOD = "* Срок обсуждения"
    RESPONSIBLE_REVIEW_1 = "* Ответственный за рассмотрение предложений"
    RESPONSIBLE_REVIEW_2 = "* Ответственный за направление информации"
    RESPONSIBLE_REVIEW_3 = "* Ответственный за направление НПА"
    NOTIFY_NPA = "* Уведомление о подготовке проекта НПА"
    PROJECT_NPA_ID = "* ID проекта НПА"
    TOTAL_COMMENT = "* Общее кол-во замечаний"
    NUMBER_COMMENT = "* Кол-во учтенных замечаний"
    NUMBER_UNA_COMMENT = "* Кол-во неучтенных замечаний"
    NUMBER_PTA_COMMENT = "* Кол-во частично учтенных замечаний"
    DECISION_INFO = "* Информация о принятом решении"
    DECISION_INFO_2 = "* Принятое решение по проекту НПА"
    SUMMARY_INFO = "* Сводка предложений"
    SHORT_CONTENT = "* Краткое содержание"
    NPA_PROJECT = "* Проект НПА"
    EXPLAIN_NOTE = "* Пояснительная записка"
    MODIFIED_NPA = "* Доработанный проект НПА"
    AC_EXPERTISE = "* Прием заключений антикоррупционной экспертизы"
    EMAIL_AC_EXPERTISE = "* E-mail для заключений антикоррупционной экспертизы"
    MAIL_AC_EXPERTISE = "* Почта для заключений антикоррупционной экспертизы"
    CORRUPTION_FACTOR = "* Коррупциогенные факторы"
    NUMBER_CONCLUSION = "* Кол-во заключений"
    GC_AC = "* Общее заключение по итогам антикоррупционной экспертизы"
    NPA_DRAFT = "* Нормативный правовой акт (проект)"
    NPA_NUMBER = "* Номер НПА"
    ACCEPTED_NPA_NUMBER = "* Номер принятого НПА"
    APPROVED_NPA = "* Утвержденный НПА"
    NPA_ADOPTION_DATE_1 = "* Дата принятия НПА"
    NPA_ADOPTION_DATE_2 = "* Дата НПА"
    PD_NPA = "* Обоснование отказа от общественного обсуждения проекта НПА"
    CONSOL_REPORT = "* Сводный отчет"
    DECISION_PERIOD = "* Срок принятия предложений"
    DEGREE_EXPOSURE = "* Степень воздействия"
    MSR = "* Доработанный сводный отчет"
    EEC = "* Проект решения ЕЭК"
    MDD = "* Доработанный проект решения ЕЭК"
    ASSESSMENT_REPORT = "* Отчет об оценке фактического воздействия НПА"
    RR_NPA = "* Доработанный отчет об оценке фактического воздействия НПА"
    OFFERS_EMAIL = "* Е-mail для предложений"
    REGULATORY_GILLIOTINE = "Регуляторная гильотина"
    NOTICE_NPA_NOT_PLACED = "Уведомление о подготовке НПА не размещается"
    CO_EXECTOR = "Органы гос. власти – соисполнители"
    ADD_OFFER_EMAIL = "Доп. e-mail для предложений"
    REASON_CREATE_NPA = "Основание для разработки НПА"
    LINK_ID = "ID связанных НПА"
    ADDITIONAL_MATERIAL = "Дополнительные материалы"
    STATE_NUMBER = "Номер государственной регистрации НПА"
    ISSUE_TYPE = "Тип затрагиваемых вопросов"


    # Заполнение/Заполненные поля Regulation
    FILL_FIELD = "Автотест - ЗАПОЛНЕНИЕ поля: "

    FILL_NPA_TYPE = "Иное"
    FILL_NPA_NAME_1 = FILL_FIELD + NPA_NAME_1
    FILL_NPA_NAME_2 = FILL_FIELD + NPA_NAME_2
    FILL_ORG_INFO_NAME = FILL_FIELD + ORG_INFO_NAME
    FILL_ORG_INFO_EMAIL = FILL_FIELD + ORG_INFO_EMAIL
    FILL_EA_TYPE = "Внешнеэкономическая деятельность"
    FILL_KEYWORD = FILL_FIELD + KEYWORD
    FILL_DISCUSS_PERIOD = "20"
    FILL_RESPONSIBLE_REVIEW_NAME = "администратор"
    FILL_RESPONSIBLE_REVIEW_PHONE = "88005553535"
    FILL_RESPONSIBLE_REVIEW_EMAIL = "in9334459@gmail.com"
    FILL_NOTIFY_NPA = FILL_FIELD + NOTIFY_NPA
    FILL_EMAIL = "autotest@autotest.autotest"
    FILL_NUMBER_COMMENT = 2
    FILL_NUMBER_UNA_COMMENT = 3
    FILL_NUMBER_PTA_COMMENT = 4
    FILL_TOTAL_COMMENT = FILL_NUMBER_COMMENT + FILL_NUMBER_UNA_COMMENT + FILL_NUMBER_PTA_COMMENT
    FILL_DECISION_INFO = "Отказ от разработки проекта нормативного правового акта"
    FILL_DECISION_INFO_2 = "Отказ от разработки (принятия) проекта нормативного правового акта"
    FILL_SUMMARY_INFO = FILL_FIELD + SUMMARY_INFO
    FILL_NPA_PROJECT = FILL_FIELD + NPA_PROJECT
    FILL_EXPLAIN_NOTE = FILL_FIELD + EXPLAIN_NOTE
    FILL_MODIFIED_NPA = FILL_FIELD + MODIFIED_NPA
    FILL_AC_EXPERTISE = "20"
    FILL_EMAIL_AC_EXPERTISE = "autotestemailacex@autotestemailacex.autotestemailacex"
    FILL_MAIL_AC_EXPERTISE = FILL_FIELD + MAIL_AC_EXPERTISE
    FILL_CORRUPTION_FACTOR = "Выявлены"
    FILL_NUMBER_CONCLUSION = "5"
    FILL_GC_AC = FILL_FIELD + GC_AC
    FILL_NPA_DRAFT = FILL_FIELD + NPA_DRAFT
    FILL_NPA_NUMBER = FILL_FIELD + NPA_NUMBER
    FILL_ACCEPTED_NPA_NUMBER = FILL_FIELD + ACCEPTED_NPA_NUMBER
    FILL_APPROVED_NPA = FILL_FIELD + APPROVED_NPA
    FILL_NOTICE_NPA_NAME = "администратор"
    FILL_PD_NPA = FILL_FIELD + PD_NPA
    FILL_CONSOL_REPORT = FILL_FIELD + CONSOL_REPORT
    FILL_DECISION_PERIOD = "6"
    FILL_DEGREE_EXPOSURE = "Высокая"
    FILL_MSR = FILL_FIELD + MSR
    FILL_EEC = FILL_FIELD + EEC
    FILL_MDD = FILL_FIELD + MDD
    FILL_ASSESSMENT_REPORT = FILL_FIELD + ASSESSMENT_REPORT
    FILL_RR_NPA = FILL_FIELD + RR_NPA

    NO_FIELD = "Нет"
    NON_REQUIRED_FIELD = "-"

    # Поля после редактирования
    EDIT_FIELD = "Автотест - РЕДАКТИРОВАНИЕ поля: "

    FILL_NPA_TYPE_EDIT = "Постановление Правительства Российской Федерации"
    FILL_NPA_NAME_1_EDIT = EDIT_FIELD + NPA_NAME_1
    FILL_NPA_NAME_2_EDIT = EDIT_FIELD + NPA_NAME_2
    FILL_ORG_INFO_NAME_EDIT = EDIT_FIELD + ORG_INFO_NAME
    FILL_ORG_INFO_EMAIL_EDIT = EDIT_FIELD + ORG_INFO_EMAIL
    FILL_EA_TYPE_EDIT = "Налоговое администрирование"
    FILL_KEYWORD_EDIT = EDIT_FIELD + KEYWORD
    FILL_DISCUSS_PERIOD_EDIT = "30"
    FILL_RESPONSIBLE_REVIEW_NAME_EDIT = "пользователь"
    FILL_RESPONSIBLE_REVIEW_PHONE_EDIT = "89600540342"
    FILL_RESPONSIBLE_REVIEW_EMAIL_EDIT = "resprev@resprev.resprev"
    FILL_NOTIFY_NPA_EDIT = EDIT_FIELD + NOTIFY_NPA
    FILL_CO_EXECTOR_EDIT = "Testovaya organizaciya"
    FILL_EMAIL_EDIT = "autotestred@autotestred.autotestred"
    FILL_REASON_CREATE_NPA_EDIT = EDIT_FIELD + REASON_CREATE_NPA
    FILL_LINK_ID_EDIT = EDIT_FIELD + LINK_ID
    FILL_ADDITIONAL_MATERIAL_EDIT = EDIT_FIELD + ADDITIONAL_MATERIAL
    FILL_NUMBER_COMMENT_EDIT = 6
    FILL_NUMBER_UNA_COMMENT_EDIT = 7
    FILL_NUMBER_PTA_COMMENT_EDIT = 8
    FILL_TOTAL_COMMENT_EDIT = FILL_NUMBER_COMMENT_EDIT + FILL_NUMBER_UNA_COMMENT_EDIT + FILL_NUMBER_PTA_COMMENT_EDIT
    FILL_DECISION_INFO_EDIT = "Разработка проекта нормативного правового акта"
    FILL_DECISION_INFO_2_EDIT = "Проект нормативного правового акта направлен в Правительство Российской Федерации"
    FILL_DECISION_INFO_3_EDIT = "Направление проекта нормативного правового акта и сводного отчета на согласование, оценку"
    FILL_SUMMARY_INFO_EDIT = EDIT_FIELD + SUMMARY_INFO
    FILL_NPA_PROJECT_EDIT = EDIT_FIELD + NPA_PROJECT
    FILL_EXPLAIN_NOTE_EDIT = EDIT_FIELD + EXPLAIN_NOTE
    FILL_REGULATORY_GILLIOTINE_EDIT = "Да"
    FILL_MODIFIED_NPA_EDIT = EDIT_FIELD + MODIFIED_NPA
    FILL_AC_EXPERTISE_EDIT = "35"
    FILL_EMAIL_AC_EXPERTISE_EDIT = "autotestemailacexred@autotestemailacexred.autotestemailacexred"
    FILL_MAIL_AC_EXPERTISE_EDIT = EDIT_FIELD + MAIL_AC_EXPERTISE
    FILL_CORRUPTION_FACTOR_EDIT = "Не выявлены"
    FILL_NUMBER_CONCLUSION_EDIT = "9"
    FILL_GC_AC_EDIT = EDIT_FIELD + GC_AC
    FILL_NPA_DRAFT_EDIT = EDIT_FIELD + NPA_DRAFT
    FILL_NPA_NUMBER_EDIT = EDIT_FIELD + NPA_NUMBER
    FILL_ACCEPTED_NPA_NUMBER_EDIT = EDIT_FIELD + ACCEPTED_NPA_NUMBER
    FILL_STATE_NUMBER_EDIT = EDIT_FIELD + STATE_NUMBER
    FILL_APPROVED_NPA_EDIT = EDIT_FIELD + APPROVED_NPA
    FILL_NOTICE_NPA_NAME_EDIT = "суперадмин"
    FILL_PD_NPA_EDIT = EDIT_FIELD + PD_NPA
    FILL_CONSOL_REPORT_EDIT = EDIT_FIELD + CONSOL_REPORT
    FILL_DECISION_PERIOD_EDIT = "25"
    FILL_DEGREE_EXPOSURE_EDIT = "Средняя"
    FILL_ISSUE_TYPE_EDIT = "Контрольно-надзорная деятельность"
    FILL_MSR_EDIT = EDIT_FIELD + MSR
    FILL_EEC_EDIT = EDIT_FIELD + EEC
    FILL_MDD_EDIT = EDIT_FIELD + MDD
    FILL_ASSESSMENT_REPORT_EDIT = EDIT_FIELD + ASSESSMENT_REPORT
    FILL_RR_NPA_EDIT = EDIT_FIELD + RR_NPA

    # Дата
    DATE = datetime.today().strftime("%d.%m.%Y")
    DATE_EDIT = (datetime.today() - timedelta(days=1)).strftime("%d.%m.%Y")

    # 35 тип
    REQUEST_TYPE_35 = "Тип заявки"
    NPA_NAME_35 = "* Наименование проекта НПА (отчета ОФВ)"
    PROJECT_NPA_ID_35 = PROJECT_NPA_ID
    ACTUAL_RR_35 = "* Текущий ответственный сотрудник"
    NEW_RR_35 = "* Новый ответственный сотрудник"
    FILL_NPA_NAME_3 = FILL_FIELD + NPA_NAME_35
    EDIT_NPA_NAME_3 = EDIT_FIELD + NPA_NAME_35

    # Ошибки
    REQUEST_PLACING_ERROR = "Нарушение последовательности размещения заявок"
    CHAIN_NOT_FOUND_ERROR = "Не найдена связанная цепочка заявок"


class DateValues:
    DATE_TODAY = datetime.today().strftime("%d.%m.%Y")
    DATE_YESTERDAY = (datetime.today() - timedelta(days=1)).strftime("%d.%m.%Y")
    DATE_TOMORROW = (datetime.today() + timedelta(days=1)).strftime("%d.%m.%Y")
    DATE_YESTERDAY_2 = (datetime.today() - timedelta(days=2)).strftime("%d.%m.%Y")
    DATE_TOMORROW_2 = (datetime.today() + timedelta(days=2)).strftime("%d.%m.%Y")


class EnterRequestValues:
    NON_REQUIRED_FIELD = ""

    ENTER_REQUEST_TITLE = "Внутренний документ-заявка"
    SOGL_ENTER_REQUEST_TITLE = "Согласование внутреннего документа-заявки"

    # Тип заявки
    CHANGE_INFO = "Заявка на предоставление, изменение, прекращение прав доступа к информационным ресурсам Минфина России"
    OFFICIAL_MF = "Заявка на размещение информации на Официальном сайте Минфина России"
    ENTER_MF = "Заявка на размещение информации на Внутреннем портале Минфина России"
    PROVISION_SH = "Заявка на обеспечение программно-техническими ресурсами"

    # Тип изменения
    DOC_CHANGE = "Изменение документов"
    DOC_CHANGE_RUBIC = "Изменение структуры рубрик (разделов)"

    # Обрабатываются сведения
    NOT_SECRET = "Не составляющие гос. тайну"
    SECRET = "Составляющие гос. тайну"

    # ФИО / Ответственный / Снять с (ФИО, адрес) / Установить (ФИО, адрес)
    FIO = "Суперадмин"
    FIO_EDIT = "Админ"

    # Телефон
    PHONE = "88005553535"
    PHONE_EDIT = "89600470942"

    # Наименование информационного ресурса
    INFO_RESOURCE = "2,01,08"
    INFO_RESOURCE_EDIT = "2,01,10"

    # Вид действий
    ACTION_TYPE_HOOK = "Подключить"
    ACTION_TYPE_DISABLE = "Отключить"
    ACTION_TYPE_CHANGE_ACCESS = "Изменение прав доступа"

    # Описание функциональной роли
    FUNCTIONAL_ROLE = "Автотест - заполнение поля 'Описание функциональной роли'"
    FUNCTIONAL_ROLE_EDIT = "Автотест - редактирование поля 'Описание функциональной роли'"

    # Путь
    PATH = "Минфин России / Документы / Проекты"
    PATH_EDIT = "Минфин России / Исполнение судебных актов / Нормативные документы"

    # Комментарий
    COMMENT = "Автотест - заполнение поля 'Комментарий'"
    COMMENT_EDIT = "Автотест - редактирование поля 'Комментарий'"

    # Операция
    ADD_DOC = "Добавление документа"
    CHANGE_DOC = "Замена документа"
    DEL_DOC = "Удаление документа"

    ADD_DOC_SECTION = "Добавление рубрики (раздела)"
    RENAME_DOC_SECTION = "Переименование рубрики (раздела)"
    DEL_DOC_SECTION = "Удаление рубрики (раздела)"
    TRANSFER_DOC_SECTION = "Перенос рубрики (раздела)"

    # Документ
    DOCUMENT_NAME = "Автотест - заполнение поля 'Документ'"
    DOCUMENT_NAME_EDIT = "Автотест - редактирование поля 'Документ'"
    
    # Приложения
    APPS_NAME = "Автотест - заполнение поля 'Приложения'"
    APPS_NAME_EDIT = "Автотест - редактирование поля 'Приложения'"

    # Вид информации
    INFORMATION_TYPE = "Анонс"
    INFORMATION_TYPE_EDIT = "Высказывание"

    # Состав инф-ии
    INFO_COMPOSITION = "Административные регламенты и стандарты государственных услуг"
    INFO_COMPOSITION_EDIT = "Доклад о ходе реализации плана деятельности Министерства"

    # Название
    NAME = "Автотест - заполнение поля 'Название'"
    NAME_EDIT = "Автотест - редактирование поля 'Название'"

    # Новое название
    NEW_NAME = "Автотест - заполнение поля 'Новое название'"
    NEW_NAME_EDIT = "Автотест - редактирование поля 'Новое название'"

    # Приложение (структура рубрики/раздела)
    RUBIC_APPS_NAME = "Автотест - заполнение поля 'Приложение (структура рубрики/раздела)'"
    RUBIC_APPS_NAME_EDIT = "Автотест - редактирование поля 'Приложение (структура рубрики/раздела)'"

    # Заменить (текущий)
    CHANGE = "Автотест - заполнение поля 'Заменить (текущий)'"
    CHANGE_EDIT = "Автотест - редактирование поля 'Заменить (текущий)'"

    # Документ (новый)
    NEW = "Автотест - заполнение поля 'Документ (новый)'"
    NEW_EDIT = "Автотест - редактирование поля 'Документ (новый)'"

    # Виды работ
    CUT = "Снятие"
    INSTALLATION = "Установка"
    MOVING = "Перемещение"
    CENSUS = "Перепись"
    CENSUS_MOVING = "Перепись с перемещением"

    # Снять с (ФИО, адрес)
    FIO = "Абрадушкина А.Ю."
    FIO_EDIT = "Абрамова Т.Б."

    # Адрес
    ADRESS = "Мясницкая"
    ADRESS_EDIT = "Фили"

    # № комн.
    ROOM_NUMBER = "208"
    ROOM_NUMBER_EDIT = "306"

    # В соответствии с карточкой учета СВТ

    # Наименование устройства - Категория
    DEVICE_NAME_CATEGORY = "Периферийное оборудование"
    DEVICE_NAME_CATEGORY_EDIT = "Компьютерное оборудование"

    # Наименование устройства - Устройство
    DEVICE_NAME = "Принтер с функцией цветной печати а4"
    DEVICE_NAME_EDIT = "Рабочая станция на основе системного блока"

    # Перевод в департамент
    TRANSFER_DEPARTMENT = "01 Департамент"

    # Обоснование/комментарий
    JUSTIFICATION = "Автотест - заполнение поля 'Обоснование/комментарий'"
    JUSTIFICATION_EDIT = "Автотест - редактирование поля 'Обоснование/комментарий'"

# Настройки
class SettingsValues:
    class SystemNotification:
        REGULATION_DEADLINE = "Уведомлять об окончании срока исполнения заявок regulation"
        REGULATION_DISCUSS_NPA = "Уведомлять о завершении обсуждения/экспертизы проекта НПА на сайте regulation.gov.ru"

# Настройки / Администрирование заявок regulation
class DirectoryVEDValues:
    CODE = "CODE-AUTOTEST"
    CODE_EDIT = "CODE-EDIT-AUTOTEST"
    NAME = "ААА-Тестовая экономическая деятельность"
    NAME_EDIT = "ААА-Редактирование экономической деятельности"

# Настройки / Вид информации ОСМФ | Состав информации, размещаемой на ОСМФ
class OSMFInformationValues:
    INFORMATION_TYPE = "Тестовый вид информации"
    INFORMATION_TYPE_EDIT = "Редактирование тестового вида информации"


class AgreeSheetValues:
    SIGN = "Автотест подписание ЭП"
    SIGN_COMMENT = "Автотест подписание ЭП с замечанием"
    REFUSE = "Автотест отказ ЭП"
    REFUSE_COMMENT = "Автотест отказ ЭП с комментарием"
    REFUSE_DOCUMENT = "Автотест отказ ЭП с документом"

    REMARK = "Автотест замечание"
