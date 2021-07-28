from .main_functions import MainFunc
from .all_document_fields_page import AllDocumentFieldPage
from .locators import MainPageLocators, SoglNewDocumentWindow, AllDocumentFieldLocators


class MainPage(MainFunc):
    def should_be_correct_fields(self):
        window_links = [
            [MainPageLocators("Расширенный поиск").top_panel.locator(
            ), "Расширенный поиск документов"],
            # [MainPageLocators("Бланки документов").top_panel.locator(), "Бланки документов"],
            [MainPageLocators("Не зарегистрировано в организации-адресате").top_panel.locator(),
             "Документы : Не зарегистрировано в организации-адресате"],
            [MainPageLocators(
                "События из МЭДО").top_panel.locator(), "События из МЭДО"],
            [MainPageLocators("Отказано в регистрации").top_panel.locator(
            ), "Документы : Отказано в регистрации"],
            [MainPageLocators("Отказано в регистрации (входящие)").top_panel.locator(
            ), "Отказано в регистрации (входящие)"],
            [MainPageLocators("Документы из МЭДО (Ведомственная)").top_panel.locator(
            ), "Входящие документы : Ведомственная"],
            [MainPageLocators("Документы из МЭДО (Правительственная)").top_panel.locator(
            ), "Входящие документы : Правительственная"],
            [MainPageLocators("Документы из МЭДО (Секретариат)").top_panel.locator(
            ), "Входящие документы : Секретариат"],
            [MainPageLocators("Документы из МЭДО (прочие)").top_panel.locator(
            ), "Входящие документы : Прочие"],

            [MainPageLocators("Все входящие", 0).closed_block.locator(
            ), "Входящие документы : Все документы"],
            [MainPageLocators("", 0).closed_block.open_block()],
            [MainPageLocators("На регистрации", 0).open_block.locator(
            ), "Входящие документы : На регистрации"],
            [MainPageLocators("Не отсканировано", 0).open_block.locator(
            ), "Входящие документы : Не отсканировано"],
            [MainPageLocators("На регистрации из МЭДО (Ведомственная)", 0).open_block.locator(
            ), "Входящие документы : Ведомственная"],
            [MainPageLocators("На регистрации из МЭДО (Правительственная)", 0).open_block.locator(
            ), "Входящие документы : Правительственная"],
            [MainPageLocators("На регистрации из МЭДО (Секретариат)", 0).open_block.locator(
            ), "Входящие документы : Секретариат"],
            [MainPageLocators("Оповещение об изменении резолюций", 0).open_block.locator(
            ), "Оповещение об изменении резолюций"],
            [MainPageLocators("Срочные", 0).open_block.locator(),
             "Входящие документы : Срочные"],
            [MainPageLocators("Удаленные", 0).open_block.locator(),
             "Входящие документы : Удаленные"],
            [MainPageLocators("Исполнительные листы", 0).open_block.locator(
            ), "Входящие документы : Исполнительные листы"],
            [MainPageLocators("Новый документ...",
                              0).open_block.locator(), "Входящий документ"],
            [MainPageLocators("Все документы", 0).open_block.locator(
            ), "Входящие документы : Все документы"],
            [MainPageLocators("", 0).open_block.close_block()],

            [MainPageLocators("Все исходящие", 1).closed_block.locator(
            ), "Исходящие документы : Все документы"],
            [MainPageLocators("", 1).closed_block.open_block()],
            [MainPageLocators("Все документы – МЭДО", 1).open_block.locator(
            ), "Исходящие документы : Все документы – МЭДО"],
            [MainPageLocators("На отправку по МЭДО", 1).open_block.locator(
            ), "Исходящие документы : На отправку по МЭДО"],
            [MainPageLocators("Зарегистрированы, но не отправлены - МЭДО", 1).open_block.locator(),
             "Исходящие документы : Зарегистрированы, но не отправлены – МЭДО"],
            [MainPageLocators("На регистрации", 1).open_block.locator(
            ), "Исходящие документы : На регистрации"],
            [MainPageLocators("На регистрации – МЭДО", 1).open_block.locator(
            ), "Исходящие документы : На регистрации – МЭДО"],
            [MainPageLocators("На регистрации с ЭП – МЭДО", 1).open_block.locator(
            ), "Исходящие документы : На регистрации с ЭП – МЭДО"],
            [MainPageLocators("Отказано в отправке по МЭДО", 1).open_block.locator(
            ), "Исходящие документы : Отказано в отправке по МЭДО"],
            [MainPageLocators("Отказано в отправке по почте", 1).open_block.locator(
            ), "Исходящие документы : Отказано в отправке по почте"],
            [MainPageLocators("Не отсканировано", 1).open_block.locator(
            ), "Исходящие документы : Не отсканировано"],
            [MainPageLocators("Удаленные", 1).open_block.locator(),
             "Исходящие документы : Удаленные"],
            [MainPageLocators("Новый документ...",
                              1).open_block.locator(), "Исходящий документ"],
            [MainPageLocators("Все документы", 1).open_block.locator(
            ), "Исходящие документы : Все документы"],
            [MainPageLocators("", 1).open_block.close_block()],

            [MainPageLocators("Все вх.обр.граждан", 2).closed_block.locator(
            ), "Входящие обращения граждан : Все документы"],
            [MainPageLocators("", 2).closed_block.open_block()],
            [MainPageLocators("На регистрации", 2).open_block.locator(
            ), "Входящие обращения граждан : На регистрации"],
            [MainPageLocators("На регистрации c ЭП", 2).open_block.locator(
            ), "Входящие обращения граждан : На регистрации с ЭП"],
            [MainPageLocators("На регистрации из МЭДО", 2).open_block.locator(
            ), "Входящие обращения граждан : На регистрации из МЭДО"],
            [MainPageLocators("На регистрации из ОСМФ", 2).open_block.locator(
            ), "Входящие обращения граждан : На регистрации из ОСМФ"],
            [MainPageLocators("Отказано в регистрации из ОСМФ", 2).open_block.locator(
            ), "Входящие обращения граждан : Отказано в регистрации из ОСМФ"],
            [MainPageLocators("Не отсканировано", 2).open_block.locator(
            ), "Входящие обращения граждан : Не отсканировано"],
            [MainPageLocators("Удаленные", 2).open_block.locator(
            ), "Входящие обращения граждан : Удаленные"],
            [MainPageLocators("Исполнительные листы", 2).open_block.locator(
            ), "Входящие обращения граждан : Исполнительные листы"],
            [MainPageLocators("Новый документ...", 2).open_block.locator(
            ), "Входящее обращение гражданина"],
            [MainPageLocators("Поиск...", 2).open_block.locator(
            ), "Расширенный поиск документов: обращения граждан"],
            [MainPageLocators("Все документы", 2).open_block.locator(
            ), "Входящие обращения граждан : Все документы"],
            [MainPageLocators("", 2).open_block.close_block()],

            [MainPageLocators("Все исх.обр.граждан", 3).closed_block.locator(
            ), "Исходящие обращения граждан : Все документы"],
            [MainPageLocators("", 3).closed_block.open_block()],
            [MainPageLocators("Все документы – МЭДО", 3).open_block.locator(
            ), "Исходящие обращения граждан : Все документы – МЭДО"],
            [MainPageLocators("На отправку по МЭДО", 3).open_block.locator(
            ), "Исходящие обращения граждан : На отправку по МЭДО"],
            [MainPageLocators("На отправку по электронной почте", 3).open_block.locator(
            ), "Исходящие обращения граждан : На отправку по электронной почте"],
            [MainPageLocators("Зарегистрированы, но не отправлены - МЭДО", 3).open_block.locator(
            ), "Исходящие обращения граждан : Зарегистрированы, но не отправлены – МЭДО"],
            [MainPageLocators("На регистрации", 3).open_block.locator(
            ), "Исходящие обращения граждан : На регистрации"],
            [MainPageLocators("На регистрации – МЭДО", 3).open_block.locator(
            ), "Исходящие обращения граждан : На регистрации – МЭДО"],
            [MainPageLocators("На регистрации с ЭП – МЭДО", 3).open_block.locator(
            ), "Исходящие обращения граждан : На регистрации с ЭП – МЭДО"],
            [MainPageLocators("Отказано в отправке по МЭДО", 3).open_block.locator(
            ), "Исходящие обращения граждан : Отказано в отправке по МЭДО"],
            [MainPageLocators("Отказано в отправке по почте", 3).open_block.locator(
            ), "Исходящие обращения граждан : Отказано в отправке по почте"],
            [MainPageLocators("Отказано в отправке по электронной почте", 3).open_block.locator(
            ), "Исходящие обращения граждан : Отказано в отправке по электронной почте"],
            [MainPageLocators("Не отсканировано", 3).open_block.locator(
            ), "Исходящие обращения граждан : Не отсканировано"],
            [MainPageLocators("Удаленные", 3).open_block.locator(
            ), "Исходящие обращения граждан : Удаленные"],
            [MainPageLocators("Новый документ...", 3).open_block.locator(
            ), "Исходящее обращение гражданина"],
            [MainPageLocators("Поиск...", 3).open_block.locator(
            ), "Расширенный поиск документов: обращения граждан"],
            [MainPageLocators("Все документы", 3).open_block.locator(
            ), "Исходящие обращения граждан : Все документы"],
            [MainPageLocators("", 3).open_block.close_block()],

            [MainPageLocators("Все внутренние", 4).closed_block.locator(
            ), "Внутренние документы : Все документы"],
            [MainPageLocators("", 4).closed_block.open_block()],
            [MainPageLocators("На регистрации", 4).open_block.locator(
            ), "Внутренние документы : На регистрации"],
            [MainPageLocators("На регистрации c ЭП", 4).open_block.locator(
            ), "Внутренние документы : На регистрации с ЭП"],
            [MainPageLocators("Не отправленные", 4).open_block.locator(
            ), "Внутренние документы : Не отправленные"],
            [MainPageLocators("Поручения", 4).open_block.locator(),
             "Внутренние документы : Поручения"],
            [MainPageLocators("Поступили из БП", 4).open_block.locator(
            ), "Внутренние документы : Поступили из БП"],
            [MainPageLocators("Не отсканировано", 4).open_block.locator(
            ), "Внутренние документы : Не отсканировано"],
            [MainPageLocators("Удаленные", 4).open_block.locator(),
             "Внутренние документы : Удаленные"],
            [MainPageLocators("Новый документ...",
                              4).open_block.locator(), "Внутренний документ"],
            [MainPageLocators("Все документы", 4).open_block.locator(
            ), "Внутренние документы : Все документы"],
            [MainPageLocators("", 4).open_block.close_block()],

            [MainPageLocators("Все ОРД", 5).closed_block.locator(
            ), "Организационно-распорядительные документы : Все документы"],
            [MainPageLocators("", 5).closed_block.open_block()],
            [MainPageLocators("На регистрации", 5).open_block.locator(
            ), "Организационно-распорядительные документы : На регистрации"],
            [MainPageLocators("На регистрации c ЭП", 5).open_block.locator(
            ), "Организационно-распорядительные документы : На регистрации с ЭП"],
            [MainPageLocators("Отказано в отправке по почте", 5).open_block.locator(
            ), "Организационно-распорядительные документы : Отказано в отправке по почте"],
            [MainPageLocators("Не отсканировано", 5).open_block.locator(
            ), "Организационно-распорядительные документы : Не отсканировано"],
            [MainPageLocators("Удаленные", 5).open_block.locator(
            ), "Организационно-распорядительные документы : Удаленные"],
            [MainPageLocators("Новый документ...", 5).open_block.locator(
            ), "Организационно-распорядительный документ"],
            [MainPageLocators("Все документы", 5).open_block.locator(
            ), "Организационно-распорядительные документы : Все документы"],
            [MainPageLocators("", 5).open_block.close_block()],

            [MainPageLocators("Все документы", 6).closed_block.locator(
            ), "Согласование документов : Все документы"],
            [MainPageLocators("", 6).closed_block.open_block()],
            [MainPageLocators("Новые поступившие", 6).open_block.locator(
            ), "Согласование документов : Новые поступившие"],
            [MainPageLocators("В работе", 6).open_block.locator(),
             "Согласование документов : В работе"],
            [MainPageLocators("Перенаправлено", 6).open_block.locator(
            ), "Согласование документов : Перенаправлено"],
            [MainPageLocators("Согласованные/ подписанные", 6).open_block.locator(),
             "Согласование документов : Согласованные/подписанные"],
            [MainPageLocators("Даны замечания/ предложения", 6).open_block.locator(),
             "Согласование документов : Даны замечания/предложения"],
            [MainPageLocators("Я готовлю к отправке", 6).open_block.locator(
            ), "Согласование документов : Готовлю к отправке"],
            [MainPageLocators("Находится на согласовании", 6).open_block.locator(
            ), "Согласование документов : Находится на согласовании"],
            [MainPageLocators("Вернули на доработку", 6).open_block.locator(
            ), "Согласование документов : Вернули на доработку"],
            [MainPageLocators("На собственноручную подпись", 6).open_block.locator(
            ), "Согласование документов : На собственноручную подпись"],
            [MainPageLocators("Прекратил(а) согласование", 6).open_block.locator(
            ), "Согласование документов : Прекратил(а) согласование"],
            [MainPageLocators("Направить на регистрацию (повторно)", 6).open_block.locator(
            ), "Согласование документов : Направить на регистрацию (повторно)"],
            [MainPageLocators("Ожидает регистрации", 6).open_block.locator(
            ), "Согласование документов : Ожидает регистрации"],
            [MainPageLocators("Зарегистрированы", 6).open_block.locator(
            ), "Согласование документов : Зарегистрированы"],
            [MainPageLocators("Зарегистрированы, но не отправлены - МЭДО", 6).open_block.locator(),
             "Согласование документов : Зарегистрированы, но не отправлены – МЭДО"],
            [MainPageLocators("На отправку по МЭДО", 6).open_block.locator(
            ), "Согласование документов : На отправку по МЭДО"],
            [MainPageLocators("Отправлено по МЭДО", 6).open_block.locator(
            ), "Согласование документов : Отправлено по МЭДО"],
            [MainPageLocators("Отказано в отправке по МЭДО", 6).open_block.locator(
            ), "Согласование документов : Отказано в отправке по МЭДО"],
            [MainPageLocators("Удаленные", 6).open_block.locator(),
             "Согласование документов : Удаленные"],
            [MainPageLocators("Новый документ...", 6).open_block.locator(
            ), "Создать проект документа для согласования"],
            [MainPageLocators("Все документы", 6).open_block.locator(
            ), "Согласование документов : Все документы"],
            [MainPageLocators("", 6).open_block.close_block()],

            [MainPageLocators("Для проектов резолюций").status.locator(
            ), "Документы : Для проектов резолюций"],
            # [MainPageLocators("Для подтверждения проектов резолюций").status.locator(), "Документы : Для подтверждения проектов резолюций"],
            [MainPageLocators("Для заливки в ноутбук").status.locator(
            ), "Документы : Для заливки в ноутбук"],
            [MainPageLocators("На рассмотрении").status.locator(),
             "Документы : На рассмотрении"],
            [MainPageLocators("Голосовые и графические резолюции").status.locator(
            ), "Документы : Голосовые и графические резолюции"],
            [MainPageLocators("Рассмотренные").status.locator(),
             "Документы : Рассмотренные"],
            [MainPageLocators("Изменить статус вручную").status.locator(
            ), "Изменение статуса всех документов пользователя"],

            [MainPageLocators("Исполнение документов").menu.locator(
            ), "Исполнение документов"],
            [MainPageLocators("Неисполненные документы").menu.locator(
            ), "Неисполненные документы"],
            [MainPageLocators("Личные папки").menu.locator(), "Личные папки"],
            [MainPageLocators("Личные папки для МО").menu.locator(),
             "Личные папки для МО"],
            [MainPageLocators("Новые письма").menu.locator(),
             "Документы : Новые письма"],
            [MainPageLocators("Все документы").menu.locator(),
             "Документы : Все документы"],
            [MainPageLocators("Автор").menu.locator(), "Документы : Автор"],
            [MainPageLocators("Адресат/исполнитель").menu.locator(),
             "Документы : Адресат/исполнитель"],
            # [MainPageLocators("Для подтверждения проектов резолюций").menu.locator(), "Документы : Для подтверждения проектов резолюций"],
            [MainPageLocators("Для заливки в ноутбук").menu.locator(
            ), "Документы : Для заливки в ноутбук"],
            [MainPageLocators("На рассмотрении").menu.locator(),
             "Документы : На рассмотрении"],
            [MainPageLocators("На рассмотрении (без страниц)").menu.locator(
            ), "Документы : На рассмотрении (без страниц)"],
            [MainPageLocators("На рассмотрении ДСП").menu.locator(),
             "Документы : На рассмотрении ДСП"],
            [MainPageLocators("Рассмотренные").menu.locator(),
             "Документы : Рассмотренные"],
            [MainPageLocators("Полный перечень документов").menu.locator(
            ), "Документы : Полный перечень документов"],
            [MainPageLocators("Настройки уведомлений").menu.locator(
            ), "Настройки уведомлений"],
            [MainPageLocators('Уведомления "Особый контроль"').menu.locator(
            ), 'Настройка уведомлений по "Особому контролю"'],
            [MainPageLocators("Передать права на документы").menu.locator(
            ), "Передать права на документы"],
            [MainPageLocators("Учёт исходящей корреспонденции").menu.locator(
            ), "Учёт исходящей корреспонденции: Список реестров"],
            [MainPageLocators("Архив сообщений").menu.locator(),
             "Сообщения : Архив"],
            [MainPageLocators("Написать сообщение").menu.locator(),
             "Сообщения : Написать"],

            [MainPageLocators("Отчеты по исполнению документов").statistic.locator(
            ), "Отчеты по исполнению документов"],
            [MainPageLocators("Отчеты по обращениям граждан").statistic.locator(
            ), "Отчеты по обращениям граждан"],
            [MainPageLocators("Контрольные отчеты по МЭДО документам").statistic.locator(
            ), "Контрольные отчеты по МЭДО документам"],
            [MainPageLocators("Количество направленных писем").statistic.locator(
            ), "Учёт исходящей корреспонденции: Количество направленных писем"],
            # [MainPageLocators("Уведомления").statistic.locator(), "Уведомления : Зарегистрирован"],
            [MainPageLocators("Контрольные документы").statistic.locator(
            ), "Исполнение документов : Все контрольные документы"],
            [MainPageLocators("Отчеты администратора").statistic.locator(
            ), "Отчеты администратора"],

            [MainPageLocators.SETTINGS_LINK_LOCATOR],

            [MainPageLocators.MAIN_PAGE_LINK_LOCATOR,
                "Входящие документы : Зарегистрирован"],
            [MainPageLocators.STP_PAGE_LINK_LOCATOR, "Страница техподдержки"],
            # [MainPageLocators.STP_EMAIL_LINK_LOCATOR],
            [MainPageLocators.NOTIFICATION_LINK_LOCATOR],
            [MainPageLocators.EXIT_LINK_LOCATOR],
        ]

        for i in window_links:
            assert self.is_element_present(*i[0])
            self.click_to(*i[0])

            if len(i) == 2:
                new_sogl = (i[0] == MainPageLocators(
                    "Новый документ...", 6).open_block.locator())
                if new_sogl:
                    self.work_with_windows(1)

                AllDocumentFieldPage(
                    self.driver).should_be_correct_title(i[1])
                if new_sogl:
                    self.driver.close()
                    self.work_with_windows()

    def go_to_settings_pages(self):
        url = self.driver.current_url
        self.click_to(*MainPageLocators.SETTINGS_LINK_LOCATOR)
        assert self.url_change(url)


class EnterDocumentsBlock(MainFunc):
    def open_enter_document_block(self):
        if self.is_active(*MainPageLocators.ENTER_BLOCK_SLIDE_DOWN_BUTTON) == True:
            self.click_to(*MainPageLocators.ENTER_BLOCK_SLIDE_DOWN_BUTTON)

    def go_to_enter_document_on_register(self):
        self.open_enter_document_block()
        self.click_to(*MainPageLocators.ENTER_BLOCK_ON_REGISTRATION_LINK)


class SoglDocumentsBlock(MainFunc):
    ALL_DOC = "Все документы"
    NEW_DOC = "Новый документ..."

    def should_be_correct_elements_sogl_request_new_window(self):
        window_elements = [
            SoglNewDocumentWindow.REQUEST_REQUEST_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.REQUEST_REQUEST_NAME_LOCATOR,
            SoglNewDocumentWindow.REQUEST_REGULATION_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.REQUEST_REGULATION_NAME_LOCATOR,
            SoglNewDocumentWindow.REQUEST_CHANGE_INFO_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.REQUEST_CHANGE_INFO_NAME_LOCATOR,
            SoglNewDocumentWindow.CLOSE_BUTTON_LOCATOR,
            SoglNewDocumentWindow.CONTINUE_BUTTON_LOCATOR,
        ]

        for i in window_elements:
            self.is_element_present(*i)

    def should_be_correct_elements_sogl_new_window(self):
        self.work_with_windows(1)
        window_elements = [
            SoglNewDocumentWindow.OUTGOING_DOCUMENT_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.OUTGOING_DOCUMENT_NAME_LOCATOR,
            SoglNewDocumentWindow.OUTGOING_OG_DOCUMENT_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.OUTGOING_OG_DOCUMENT_NAME_LOCATOR,
            SoglNewDocumentWindow.ENTER_DOCUMENT_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.ENTER_DOCUMENT_NAME_LOCATOR,
            SoglNewDocumentWindow.ORD_DOCUMENT_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.ORD_DOCUMENT_NAME_LOCATOR,
            SoglNewDocumentWindow.REQUEST_DOCUMENT_RADIO_BUTTON_LOCATOR,
            SoglNewDocumentWindow.REQUEST_DOCUMENT_NAME_LOCATOR,
            SoglNewDocumentWindow.CLOSE_BUTTON_LOCATOR,
            SoglNewDocumentWindow.CONTINUE_BUTTON_LOCATOR,
        ]

        for i in window_elements:
            self.is_element_present(*i)

    def choose_request_document(self):
        self.click_to(*SoglNewDocumentWindow.REQUEST_DOCUMENT_NAME_LOCATOR)
        self.click_to(*SoglNewDocumentWindow.CONTINUE_BUTTON_LOCATOR)

    def choose_request_regulation_document(self):
        self.click_to(*SoglNewDocumentWindow.REQUEST_REGULATION_NAME_LOCATOR)
        self.click_to(*SoglNewDocumentWindow.CONTINUE_BUTTON_LOCATOR)
        self.work_with_windows(0)

    def choose_request_request_document(self):
        self.click_to(*SoglNewDocumentWindow.REQUEST_REQUEST_NAME_LOCATOR)
        self.click_to(*SoglNewDocumentWindow.CONTINUE_BUTTON_LOCATOR)
        self.work_with_windows(0)

    def choose_request_change_responsible_info_document(self):
        self.click_to(*SoglNewDocumentWindow.REQUEST_CHANGE_INFO_NAME_LOCATOR)
        self.click_to(*SoglNewDocumentWindow.CONTINUE_BUTTON_LOCATOR)
        self.work_with_windows(0)

    def open_sogl_document_block(self):
        locator = MainPageLocators("", 6).closed_block.open_block()

        if self.is_active(*locator, timeout=0) == True:
            self.click_to(*locator)

    def go_to_sogl_block_all_documents(self):
        self.open_sogl_document_block()
        self.click_to(*MainPageLocators(self.ALL_DOC, 6).open_block.locator())

    def go_to_sogl_block_new_document(self):
        self.open_sogl_document_block()
        self.click_to(*MainPageLocators(self.NEW_DOC, 6).open_block.locator())
