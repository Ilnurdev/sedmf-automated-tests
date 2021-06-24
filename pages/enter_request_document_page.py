from .main_functions import MainFunc
from .all_document_fields_page import AllDocumentFieldPage
from .locators import AllDocumentFieldLocators, EnterRequestDocumentPageLocators
from .value_for_fields import EnterRequestValues, DateValues


class Fields(MainFunc):
    def enter_request_add_buttons(self, button_type, num=0, parent=0):
        buttons = {
            1: EnterRequestDocumentPageLocators(num, parent).change_root.add_resource_button(),
            2: EnterRequestDocumentPageLocators(num, parent).change_root.ADD_STAFF_BUTTON_LOCATOR,
            3: EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.ADD_UPDATE_BUTTON_LOCATOR,
            4: EnterRequestDocumentPageLocators(num, parent).provision_sh.ADD_DEVICE_BUTTON_LOCATOR,
        }

        self.click_to(*buttons[button_type])

    def delete_block_locator(self, del_blocks=1, num=0, parent=0):
        delete_buttons = self.count_all_elements(
            *EnterRequestDocumentPageLocators(num, parent).delete_block_button())
        self.click_to(*EnterRequestDocumentPageLocators(num,
                                                        parent).delete_block_button(True))
        assert self.count_all_elements(*EnterRequestDocumentPageLocators(
            num, parent).delete_block_button()) == (delete_buttons-del_blocks)

    """

    Тип заявки

    """

    def should_be_request_type_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators.REQUEST_TYPE_NAME_LOCATOR)

    def should_be_request_type_fields(self, num, parent, fill, text):
        self.should_be_request_type_field(num, parent)
        if fill == True:
            self.work_with_selector(
                *EnterRequestDocumentPageLocators.REQUEST_TYPE_FIELD_LOCATOR, visible_text=str(text))
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators.REQUEST_TYPE_VIEW_MODE_LOCATOR)
            assert taken_text == text

    """

    * Обрабатываются сведения

    """

    def should_be_information_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).change_root.INFORMATION_NAME_LOCATOR)

    def should_be_information_fields(self, num, parent, fill, text):
        self.should_be_information_field(num, parent)

        if fill == True:
            radiobuttons = {
                "Не составляющие гос. тайну": EnterRequestDocumentPageLocators(num, parent).change_root.INFORMATION_NOT_SECRET_RADIOBUTTON_LOCATOR,
                "Составляющие гос. тайну": EnterRequestDocumentPageLocators(num, parent).change_root.INFORMATION_SECRET_RADIOBUTTON_LOCATOR
            }

            self.click_to(*radiobuttons[text])
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).change_root.INFORMATION_VIEW_MODE_LOCATOR)
            assert taken_text == text

    """

    * ФИО

    """

    def should_be_fio_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).change_root.fio())

    def should_be_fio_fields(self, num, parent, fill, text):
        self.should_be_fio_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).change_root.fio_field(), text)
            self.choose_user_from_drop_list()
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).change_root.fio_view_mode())
            assert text in taken_text

    """

    * Наименование информационного ресурса

    """

    def should_be_information_resource_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).change_root.information_resource())

    def should_be_information_resource_fields(self, num, parent, fill, text):
        self.should_be_information_resource_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).change_root.information_resource_field(), text)
            self.click_to(*AllDocumentFieldLocators.find_text_locator(text))
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).change_root.information_resource_view_mode())
            assert text in taken_text

    """

    * Вид действий

    """

    def should_be_action_type_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).change_root.action_type())

    def should_be_action_type_fields(self, num, parent, fill, text):
        self.should_be_action_type_field(num, parent)
        if fill == True:
            self.work_with_selector(*EnterRequestDocumentPageLocators(
                num, parent).change_root.action_type_field(), visible_text=str(text))
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).change_root.action_type_view_mode())
            assert taken_text == text

    """

    * Описание функциональной роли

    """

    def should_be_functional_role_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).change_root.functional_role())

    def should_be_functional_role_fields(self, num, parent, fill, text):
        self.should_be_functional_role_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).change_root.functional_role_field(), text)
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).change_root.functional_role_view_mode())
            assert taken_text == text

    """

    Тип изменения

    """

    def should_be_change_type_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.CHANGE_TYPE_NAME_LOCATOR)

    def should_be_change_type_fields(self, num, parent, fill, text):
        self.should_be_change_type_field(num, parent)
        if fill == True:
            self.work_with_selector(*EnterRequestDocumentPageLocators(
                num, parent).offical_and_enter_mf.CHANGE_TYPE_FIELD_LOCATOR, visible_text=str(text))
        else:
            taken_text = self.return_text(*EnterRequestDocumentPageLocators(
                num, parent).offical_and_enter_mf.CHANGE_TYPE_VIEW_MODE_LOCATOR)
            assert taken_text == text

    """

    * Путь

    """

    def should_be_path_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.PATH_NAME_LOCATOR)

    def should_be_path_fields(self, num, parent, fill, text):
        self.should_be_path_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.PATH_FIELD_LOCATOR, text)
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.PATH_VIEW_MODE_LOCATOR)
            assert taken_text == text

    """

    * Переместить в

    """

    def should_be_move_to_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.MOVE_TO_NAME_LOCATOR)

    def should_be_move_to_fields(self, num, parent, fill, text):
        self.should_be_move_to_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.MOVE_TO_FIELD_LOCATOR, text)
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.MOVE_TO_VIEW_MODE)
            assert taken_text == text

    """

    Дата публикации

    """

    def should_be_publish_date_field(self, num, parent):
        assert self.is_element_present(*EnterRequestDocumentPageLocators(
            num, parent).offical_and_enter_mf.PUBLISH_DATE_NAME_LOCATOR)

    def should_be_publish_date_fields(self, num, parent, fill, text):
        self.should_be_publish_date_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.PUBLISH_DATE_FIELD_LOCATOR, text)
        else:
            taken_text = self.return_text(*EnterRequestDocumentPageLocators(
                num, parent).offical_and_enter_mf.PUBLISH_DATE_VIEW_MODE_LOCATOR)
            assert taken_text == text if text != "" else taken_text == "-"

    """

    * Ответственный

    """

    def should_be_responsible_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.RESPONSIBLE_NAME_LOCATOR)

    def should_be_responsible_fields(self, num, parent, fill, text):
        self.should_be_responsible_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.RESPONSIBLE_FIELD_LOCATOR, text)
            self.choose_user_from_drop_list()
        else:
            taken_text = self.return_text(*EnterRequestDocumentPageLocators(
                num, parent).offical_and_enter_mf.RESPONSIBLE_VIEW_MODE_LOCATOR)
            assert text in taken_text

    """

    * Телефон

    """

    def should_be_phone_field(self, num, parent):
        assert self.is_element_present(*EnterRequestDocumentPageLocators(
            num, parent).offical_and_enter_mf.PHONE_NUMBER_NAME_LOCATOR)

    def should_be_phone_fields(self, num, parent, fill, text):
        self.should_be_phone_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.PHONE_NUMBER_FIELD_LOCATOR, text)
        else:
            taken_text = self.return_text(*EnterRequestDocumentPageLocators(
                num, parent).offical_and_enter_mf.PHONE_NUMBER_VIEW_MODE_LOCATOR)
            assert taken_text == text

    """

    Комментарий

    """

    def should_be_comment_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.COMMENT_NAME_LOCATOR)

    def should_be_comment_fields(self, num, parent, fill, text):
        self.should_be_comment_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.COMMENT_FIELD_LOCATOR, text)
        else:
            taken_text = self.return_text(*EnterRequestDocumentPageLocators(
                num, parent).offical_and_enter_mf.COMMENT_VIEW_MODE_LOCATOR)
            assert taken_text == text

    """

    Операция

    """

    def should_be_operation_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.operation())

    def should_be_operation_fields(self, num, parent, fill, text):
        self.should_be_operation_field(num, parent)
        if fill == True:
            self.work_with_selector(*EnterRequestDocumentPageLocators(
                num, parent).offical_and_enter_mf.operation_field(), visible_text=str(text))
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.operation_view_mode())
            assert taken_text == text

    """

    Документ

    """

    def should_be_document_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.document())

    def should_be_document_fields(self, num, parent, fill, text):
        self.should_be_document_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.document_field(), text)
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.document_add_file(), f_type=1)
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.document_view_mode())
            assert taken_text == text

    def should_be_document_2_fields(self, num, parent, fill, text):
        self.should_be_document_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.document_field(), text)
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.document_view_mode())
            assert taken_text == text

    """

    Приложения

    """

    def should_be_application_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.application())

    def should_be_application_fields(self, num, parent, fill, text):
        self.should_be_application_field(num, parent)
        if fill == True:
            if text != "":
                self.click_to(*EnterRequestDocumentPageLocators(num,
                                                                parent).offical_and_enter_mf.application_button())
                self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                                  parent).offical_and_enter_mf.application_field(0), text)
                self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                                  parent).offical_and_enter_mf.application_add_file(0), f_type=1)
            else:
                assert self.is_element_present(
                    *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.application_button())
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.application_view_mode())
            assert text == taken_text

    """

    Приложение (структура рубрики/раздела)

    """

    def should_be_application_rubic_field(self, num, parent, check=False):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.application_2())
        if check == True:
            self.click_to(*EnterRequestDocumentPageLocators(num,
                                                            parent).offical_and_enter_mf.application_button())
            assert self.is_element_present(*EnterRequestDocumentPageLocators(
                num, parent).offical_and_enter_mf.application_button(check))

    def should_be_application_rubic_fields(self, num, parent, fill, text):
        self.should_be_application_rubic_field(num, parent)
        if fill == True:
            if text != "":
                self.click_to(*EnterRequestDocumentPageLocators(num,
                                                                parent).offical_and_enter_mf.application_button())
                self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                                  parent).offical_and_enter_mf.application_add_file(0), f_type=1)
            else:
                self.is_element_present(
                    *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.application_button())
        else:
            taken_text = self.return_text(*EnterRequestDocumentPageLocators(
                num, parent).offical_and_enter_mf.application_2_view_mode())
            assert taken_text == text

    """

    Вид информации

    """

    def should_be_information_type_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.information_type())

    def should_be_information_type_fields(self, num, parent, fill, text, check=False):
        self.should_be_information_type_field(num, parent)
        if fill == True:
            if text != "":
                self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                                  parent).offical_and_enter_mf.information_type_field(), text)
                if check == False:
                    self.click_to(
                        *AllDocumentFieldLocators.find_text_locator(text))
                else:
                    assert self.is_not_element_present(
                        *AllDocumentFieldLocators.find_text_locator(text))
            else:
                assert self.is_element_present(
                    *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.information_type_field())
        else:
            taken_text = self.return_text(*EnterRequestDocumentPageLocators(
                num, parent).offical_and_enter_mf.information_type_view_mode())
            assert taken_text == text if text != "" else taken_text == "-"

    """

    Состав инф-ии

    """

    def should_be_info_composition_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.info_composition())

    def should_be_info_composition_fields(self, num, parent, fill, text, check=False):
        self.should_be_info_composition_field(num, parent)
        if fill == True:
            if text != "":
                self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                                  parent).offical_and_enter_mf.info_composition_field(), text)
                if check == False:
                    self.click_to(
                        *AllDocumentFieldLocators.find_text_locator(text))
                else:
                    assert self.is_not_element_present(
                        *AllDocumentFieldLocators.find_text_locator(text))
            else:
                assert self.is_element_present(
                    *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.info_composition_field())
        else:
            taken_text = self.return_text(*EnterRequestDocumentPageLocators(
                num, parent).offical_and_enter_mf.info_composition_view_mode())
            assert taken_text == text if text != "" else taken_text == "-"

    """

    * Название

    """

    def should_be_name_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.name())

    def should_be_name_fields(self, num, parent, fill, text):
        self.should_be_name_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.name_field(), text)
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.name_view_mode())
            assert taken_text == text

    """

    * Новое название

    """

    def should_be_new_name_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.new_name())

    def should_be_new_name_fields(self, num, parent, fill, text):
        self.should_be_new_name_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.new_name_field(), text)
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.new_name_view_mode())
            assert taken_text == text

    """

    * Заменить (текущий)

    """

    def should_be_replace_doc_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.replace_doc())

    def should_be_replace_doc_fields(self, num, parent, fill, text):
        self.should_be_replace_doc_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.replace_doc_field(), text)
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.replace_doc_view_mode())
            assert taken_text == text

    """

    * Документ (новый)

    """

    def should_be_new_doc_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.new_doc())

    def should_be_new_doc_fields(self, num, parent, fill, text):
        self.should_be_new_doc_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.new_doc_field(), text)
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).offical_and_enter_mf.new_doc_add_file_button(), f_type=1)
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).offical_and_enter_mf.new_doc_view_mode())
            assert taken_text == text

    """

    * Вид работ

    """

    def should_be_work_type_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).provision_sh.work_type())

    def should_be_work_type_fields(self, num, parent, fill, text):
        self.should_be_work_type_field(num, parent)
        if fill == True:
            self.work_with_selector(*EnterRequestDocumentPageLocators(
                num, parent).provision_sh.work_type_selector(), visible_text=str(text))
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).provision_sh.work_type_view_mode())
            assert taken_text == text

    """

    * Снять с (ФИО, адрес)

    """

    def should_be_remove_from_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).provision_sh.remove_from())

    def should_be_remove_from_fields(self, num, parent, fill, text):
        self.should_be_remove_from_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).provision_sh.remove_from_field(), str(text))
            self.choose_user_from_drop_list(text)
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).provision_sh.remove_from_view_mode())
            assert text in taken_text

    # Адрес
    def should_be_remove_from_address_fields(self, num, parent, fill, text):
        if fill == True:
            self.work_with_selector(*EnterRequestDocumentPageLocators(
                num, parent).provision_sh.remove_from_address(), visible_text=str(text))
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).provision_sh.remove_from_address_view_mode())
            assert text in taken_text

    # № комн.
    def should_be_remove_from_room_number_fields(self, num, parent, fill, text):
        if fill == True:
            self.work_with_selector(*EnterRequestDocumentPageLocators(
                num, parent).provision_sh.remove_from_room(), visible_text=str(text))
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).provision_sh.remove_from_address_view_mode())
            assert text in taken_text

    """

    * Установить (ФИО, адрес)

    """

    def should_be_install_to_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).provision_sh.install_to())

    def should_be_install_to_fields(self, num, parent, fill, text):
        self.should_be_install_to_field(num, parent)
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).provision_sh.install_to_field(), str(text))
            self.choose_user_from_drop_list(text)
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).provision_sh.install_to_view_mode())
            assert text in taken_text

    # Адрес
    def should_be_install_to_address_fields(self, num, parent, fill, text):
        if fill == True:
            self.work_with_selector(*EnterRequestDocumentPageLocators(
                num, parent).provision_sh.install_to_address(), visible_text=str(text))
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).provision_sh.install_to_address_view_mode())
            assert text in taken_text

    # № комн.
    def should_be_install_to_room_number_fields(self, num, parent, fill, text):
        if fill == True:
            self.work_with_selector(*EnterRequestDocumentPageLocators(
                num, parent).provision_sh.install_to_room(), visible_text=str(text))
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).provision_sh.install_to_address_view_mode())
            assert text in taken_text

    """

    * Наименование устройства

    """

    def should_be_device_name_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).provision_sh.device_name())

    # Категория
    def should_be_device_category_fields(self, num, parent, fill, text):
        self.should_be_device_name_field(num, parent)
        if fill == True:
            self.work_with_selector(*EnterRequestDocumentPageLocators(
                num, parent).provision_sh.device_name_category(), visible_text=str(text))
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).provision_sh.device_name_view_mode())
            assert text in taken_text

    # Устройство
    def should_be_device_name_fields(self, num, parent, fill, text):
        self.should_be_device_name_field(num, parent)
        if fill == True:
            self.work_with_selector(*EnterRequestDocumentPageLocators(
                num, parent).provision_sh.device_name_device(), visible_text=str(text))
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).provision_sh.device_name_view_mode())
            assert text in taken_text

    """

    Перевод в департамент

    """

    def should_be_transfer_to_department_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).provision_sh.transfer_to_department())

    def should_be_transfer_to_department_fields(self, num, parent, fill, text):
        self.should_be_transfer_to_department_field(num, parent)
        if fill == True:
            if text != "":
                self.work_with_selector(*EnterRequestDocumentPageLocators(
                    num, parent).provision_sh.transfer_to_department_field(), visible_text=str(text))
            else:
                self.is_element_present(
                    *EnterRequestDocumentPageLocators(num, parent).provision_sh.transfer_to_department_field())
        else:
            taken_text = self.return_text(*EnterRequestDocumentPageLocators(
                num, parent).provision_sh.transfer_to_department_view_mode())
            assert taken_text == text[3:] if text != "" else taken_text == text

    """

    * В соответствии с карточкой учета СВТ

    """

    def should_be_svt_card_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).provision_sh.svt_card())

    def should_be_svt_card_fields(self, num, parent, fill, text=""):
        self.should_be_svt_card_field(num, parent)
        if fill == True:
            self.click_to(*EnterRequestDocumentPageLocators(num,
                                                            parent).provision_sh.svt_card_button())
            self.work_with_windows(1)
            self.click_to(*EnterRequestDocumentPageLocators(num,
                                                            parent).provision_sh.svt_window_first_element())
            self.click_to(*EnterRequestDocumentPageLocators(num,
                                                            parent).provision_sh.svt_window_continue_button())
            self.work_with_windows(0)
        else:
            text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).provision_sh.svt_card_view_mode())
            assert text != ""

    def should_be_address_fields(self, num, parent, fill, text):
        if fill == True:
            self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                              parent).provision_sh.svt_card_button(), str(text))
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).provision_sh.svt_card_view_mode())
            assert text in taken_text

    """

    Обоснование/комментарий

    """

    def should_be_justification_field(self, num, parent):
        assert self.is_element_present(
            *EnterRequestDocumentPageLocators(num, parent).provision_sh.justification())

    def should_be_justification_fields(self, num, parent, fill, text):
        self.should_be_justification_field(num, parent)
        if fill == True:
            if text != "":
                self.fill_field(*EnterRequestDocumentPageLocators(num,
                                                                  parent).provision_sh.justification_field(), str(text))
            else:
                assert self.is_element_present(
                    *EnterRequestDocumentPageLocators(num, parent).provision_sh.justification_field())
        else:
            taken_text = self.return_text(
                *EnterRequestDocumentPageLocators(num, parent).provision_sh.justification_view_mode())
            assert text == taken_text

    def fields(self, r_type, edit):
        field = {
            1: [[EnterRequestValues.CHANGE_INFO, EnterRequestValues.NOT_SECRET, EnterRequestValues.FIO, EnterRequestValues.INFO_RESOURCE, EnterRequestValues.ACTION_TYPE_HOOK, EnterRequestValues.FUNCTIONAL_ROLE],
                [EnterRequestValues.CHANGE_INFO, EnterRequestValues.SECRET, EnterRequestValues.FIO_EDIT, EnterRequestValues.INFO_RESOURCE_EDIT, EnterRequestValues.ACTION_TYPE_HOOK, EnterRequestValues.FUNCTIONAL_ROLE_EDIT]],
            2: [[EnterRequestValues.CHANGE_INFO, EnterRequestValues.NOT_SECRET, EnterRequestValues.FIO, EnterRequestValues.INFO_RESOURCE, EnterRequestValues.ACTION_TYPE_DISABLE, EnterRequestValues.FUNCTIONAL_ROLE],
                [EnterRequestValues.CHANGE_INFO, EnterRequestValues.SECRET, EnterRequestValues.FIO_EDIT, EnterRequestValues.INFO_RESOURCE_EDIT, EnterRequestValues.ACTION_TYPE_DISABLE, EnterRequestValues.FUNCTIONAL_ROLE_EDIT]],
            3: [[EnterRequestValues.CHANGE_INFO, EnterRequestValues.NOT_SECRET, EnterRequestValues.FIO, EnterRequestValues.INFO_RESOURCE, EnterRequestValues.ACTION_TYPE_CHANGE_ACCESS, EnterRequestValues.FUNCTIONAL_ROLE],
                [EnterRequestValues.CHANGE_INFO, EnterRequestValues.SECRET, EnterRequestValues.FIO_EDIT, EnterRequestValues.INFO_RESOURCE_EDIT, EnterRequestValues.ACTION_TYPE_CHANGE_ACCESS, EnterRequestValues.FUNCTIONAL_ROLE_EDIT]],

            4: [[EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE, EnterRequestValues.ADD_DOC, EnterRequestValues.PATH, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.DOCUMENT_NAME, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.NON_REQUIRED_FIELD],
                [EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE, EnterRequestValues.ADD_DOC, EnterRequestValues.PATH_EDIT, DateValues.DATE_YESTERDAY, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.DOCUMENT_NAME_EDIT, EnterRequestValues.APPS_NAME_EDIT, EnterRequestValues.INFORMATION_TYPE_EDIT, EnterRequestValues.INFO_COMPOSITION_EDIT]],
            5: [[EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE, EnterRequestValues.CHANGE_DOC, EnterRequestValues.PATH, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.CHANGE, EnterRequestValues.NEW, EnterRequestValues.NON_REQUIRED_FIELD],
                [EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE, EnterRequestValues.CHANGE_DOC, EnterRequestValues.PATH_EDIT, DateValues.DATE_YESTERDAY, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.CHANGE_EDIT, EnterRequestValues.NEW_EDIT, EnterRequestValues.APPS_NAME_EDIT]],
            6: [[EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE, EnterRequestValues.DEL_DOC, EnterRequestValues.PATH, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.DOCUMENT_NAME],
                [EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE, EnterRequestValues.DEL_DOC, EnterRequestValues.PATH_EDIT, DateValues.DATE_YESTERDAY, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.DOCUMENT_NAME_EDIT]],

            7: [[EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.ADD_DOC_SECTION, EnterRequestValues.PATH, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.NAME, EnterRequestValues.NON_REQUIRED_FIELD],
                [EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.ADD_DOC_SECTION, EnterRequestValues.PATH_EDIT, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.NAME_EDIT, "Test5.docx"]],
            8: [[EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.RENAME_DOC_SECTION, EnterRequestValues.PATH, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.NAME, EnterRequestValues.NEW_NAME],
                [EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.RENAME_DOC_SECTION, EnterRequestValues.PATH_EDIT, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.NAME_EDIT, EnterRequestValues.NEW_NAME_EDIT]],
            9: [[EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.DEL_DOC_SECTION, EnterRequestValues.PATH, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.NAME],
                [EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.DEL_DOC_SECTION, EnterRequestValues.PATH_EDIT, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.NAME_EDIT]],
            10: [[EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.TRANSFER_DOC_SECTION, EnterRequestValues.PATH, EnterRequestValues.PATH_EDIT, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.NAME],
                 [EnterRequestValues.OFFICIAL_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.TRANSFER_DOC_SECTION, EnterRequestValues.PATH_EDIT, EnterRequestValues.PATH, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.NAME_EDIT]],

            11: [[EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE, EnterRequestValues.ADD_DOC, EnterRequestValues.PATH, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.DOCUMENT_NAME, EnterRequestValues.NON_REQUIRED_FIELD],
                 [EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE, EnterRequestValues.ADD_DOC, EnterRequestValues.PATH_EDIT, DateValues.DATE_YESTERDAY, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.DOCUMENT_NAME_EDIT, EnterRequestValues.APPS_NAME_EDIT]],
            12: [[EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE, EnterRequestValues.CHANGE_DOC, EnterRequestValues.PATH, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.CHANGE, EnterRequestValues.NEW, EnterRequestValues.NON_REQUIRED_FIELD],
                 [EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE, EnterRequestValues.CHANGE_DOC, EnterRequestValues.PATH_EDIT, DateValues.DATE_YESTERDAY, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.CHANGE_EDIT, EnterRequestValues.NEW_EDIT, EnterRequestValues.APPS_NAME_EDIT]],
            13: [[EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE, EnterRequestValues.DEL_DOC, EnterRequestValues.PATH, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.DOCUMENT_NAME],
                 [EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE, EnterRequestValues.DEL_DOC, EnterRequestValues.PATH_EDIT, DateValues.DATE_YESTERDAY, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.DOCUMENT_NAME_EDIT]],

            14: [[EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.ADD_DOC_SECTION, EnterRequestValues.PATH, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.NAME, EnterRequestValues.NON_REQUIRED_FIELD],
                 [EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.ADD_DOC_SECTION, EnterRequestValues.PATH_EDIT, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.NAME_EDIT, "Test5.docx"]],
            15: [[EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.RENAME_DOC_SECTION, EnterRequestValues.PATH, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.NAME, EnterRequestValues.NEW_NAME],
                 [EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.RENAME_DOC_SECTION, EnterRequestValues.PATH_EDIT, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.NAME_EDIT, EnterRequestValues.NEW_NAME_EDIT]],
            16: [[EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.DEL_DOC_SECTION, EnterRequestValues.PATH, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.NAME],
                 [EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.DEL_DOC_SECTION, EnterRequestValues.PATH_EDIT, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.NAME_EDIT]],
            17: [[EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.TRANSFER_DOC_SECTION, EnterRequestValues.PATH, EnterRequestValues.PATH_EDIT, EnterRequestValues.FIO, EnterRequestValues.PHONE, EnterRequestValues.NON_REQUIRED_FIELD, EnterRequestValues.NAME],
                 [EnterRequestValues.ENTER_MF, EnterRequestValues.DOC_CHANGE_RUBIC, EnterRequestValues.TRANSFER_DOC_SECTION, EnterRequestValues.PATH_EDIT, EnterRequestValues.PATH, EnterRequestValues.FIO_EDIT, EnterRequestValues.PHONE_EDIT, EnterRequestValues.COMMENT_EDIT, EnterRequestValues.NAME_EDIT]],

            18: [[EnterRequestValues.PROVISION_SH, EnterRequestValues.CUT, EnterRequestValues.FIO, EnterRequestValues.ADRESS, EnterRequestValues.ROOM_NUMBER, None, EnterRequestValues.NON_REQUIRED_FIELD],
                 [EnterRequestValues.PROVISION_SH, EnterRequestValues.CUT, EnterRequestValues.FIO_EDIT, EnterRequestValues.ADRESS_EDIT, EnterRequestValues.ROOM_NUMBER_EDIT, None, EnterRequestValues.JUSTIFICATION_EDIT]],
            19: [[EnterRequestValues.PROVISION_SH, EnterRequestValues.INSTALLATION, EnterRequestValues.FIO, EnterRequestValues.ADRESS, EnterRequestValues.ROOM_NUMBER, EnterRequestValues.DEVICE_NAME_CATEGORY, EnterRequestValues.DEVICE_NAME, EnterRequestValues.NON_REQUIRED_FIELD],
                 [EnterRequestValues.PROVISION_SH, EnterRequestValues.INSTALLATION, EnterRequestValues.FIO_EDIT, EnterRequestValues.ADRESS_EDIT, EnterRequestValues.ROOM_NUMBER_EDIT, EnterRequestValues.DEVICE_NAME_CATEGORY_EDIT, EnterRequestValues.DEVICE_NAME_EDIT, EnterRequestValues.JUSTIFICATION_EDIT]],
            20: [[EnterRequestValues.PROVISION_SH, EnterRequestValues.MOVING, EnterRequestValues.FIO, EnterRequestValues.ADRESS, EnterRequestValues.ROOM_NUMBER, EnterRequestValues.ADRESS_EDIT, EnterRequestValues.ROOM_NUMBER_EDIT, EnterRequestValues.NON_REQUIRED_FIELD, None, EnterRequestValues.NON_REQUIRED_FIELD],
                 [EnterRequestValues.PROVISION_SH, EnterRequestValues.MOVING, EnterRequestValues.FIO_EDIT, EnterRequestValues.ADRESS_EDIT, EnterRequestValues.ROOM_NUMBER_EDIT, EnterRequestValues.ADRESS, EnterRequestValues.ROOM_NUMBER, EnterRequestValues.TRANSFER_DEPARTMENT, None, EnterRequestValues.JUSTIFICATION_EDIT]],
            21: [[EnterRequestValues.PROVISION_SH, EnterRequestValues.CENSUS, EnterRequestValues.FIO, EnterRequestValues.ADRESS, EnterRequestValues.ROOM_NUMBER, EnterRequestValues.FIO_EDIT, None, EnterRequestValues.NON_REQUIRED_FIELD],
                 [EnterRequestValues.PROVISION_SH, EnterRequestValues.CENSUS, EnterRequestValues.FIO_EDIT, EnterRequestValues.ADRESS_EDIT, EnterRequestValues.ROOM_NUMBER_EDIT, EnterRequestValues.FIO, None, EnterRequestValues.JUSTIFICATION_EDIT]],
            22: [[EnterRequestValues.PROVISION_SH, EnterRequestValues.CENSUS_MOVING, EnterRequestValues.FIO, EnterRequestValues.ADRESS, EnterRequestValues.ROOM_NUMBER, EnterRequestValues.FIO_EDIT, EnterRequestValues.ADRESS_EDIT, EnterRequestValues.ROOM_NUMBER_EDIT, None, EnterRequestValues.NON_REQUIRED_FIELD],
                 [EnterRequestValues.PROVISION_SH, EnterRequestValues.CENSUS_MOVING, EnterRequestValues.FIO_EDIT, EnterRequestValues.ADRESS_EDIT, EnterRequestValues.ROOM_NUMBER_EDIT, EnterRequestValues.FIO, EnterRequestValues.ADRESS, EnterRequestValues.ROOM_NUMBER, None, EnterRequestValues.JUSTIFICATION_EDIT]],
        }

        func = {
            1: [self.should_be_request_type_fields, self.should_be_information_fields, self.should_be_fio_fields, self.should_be_information_resource_fields, self.should_be_action_type_fields, self.should_be_functional_role_fields],

            4: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_publish_date_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_document_fields, self.should_be_application_fields, self.should_be_information_type_fields, self.should_be_info_composition_fields],
            5: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_publish_date_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_replace_doc_fields, self.should_be_new_doc_fields, self.should_be_application_fields],
            6: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_publish_date_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_document_2_fields],

            7: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_name_fields, self.should_be_application_rubic_fields],
            8: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_name_fields, self.should_be_new_name_fields],
            9: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_name_fields],
            10: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_move_to_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_name_fields],

            11: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_publish_date_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_document_fields, self.should_be_application_fields],
            12: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_publish_date_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_replace_doc_fields, self.should_be_new_doc_fields, self.should_be_application_fields],
            13: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_publish_date_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_document_2_fields],

            14: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_name_fields, self.should_be_application_rubic_fields],
            15: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_name_fields, self.should_be_new_name_fields],
            16: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_name_fields],
            17: [self.should_be_request_type_fields, self.should_be_change_type_fields, self.should_be_operation_fields, self.should_be_path_fields, self.should_be_move_to_fields, self.should_be_responsible_fields, self.should_be_phone_fields, self.should_be_comment_fields, self.should_be_name_fields],

            18: [self.should_be_request_type_fields, self.should_be_work_type_fields, self.should_be_remove_from_fields, self.should_be_remove_from_address_fields, self.should_be_remove_from_room_number_fields, self.should_be_svt_card_fields, self.should_be_justification_fields],
            19: [self.should_be_request_type_fields, self.should_be_work_type_fields, self.should_be_install_to_fields, self.should_be_install_to_address_fields, self.should_be_install_to_room_number_fields, self.should_be_device_category_fields, self.should_be_device_name_fields, self.should_be_justification_fields],
            20: [self.should_be_request_type_fields, self.should_be_work_type_fields, self.should_be_remove_from_fields, self.should_be_remove_from_address_fields, self.should_be_remove_from_room_number_fields, self.should_be_install_to_address_fields, self.should_be_install_to_room_number_fields, self.should_be_transfer_to_department_fields, self.should_be_svt_card_fields, self.should_be_justification_fields],
            21: [self.should_be_request_type_fields, self.should_be_work_type_fields, self.should_be_remove_from_fields, self.should_be_remove_from_address_fields, self.should_be_remove_from_room_number_fields, self.should_be_install_to_fields, self.should_be_svt_card_fields, self.should_be_justification_fields],
            22: [self.should_be_request_type_fields, self.should_be_work_type_fields, self.should_be_remove_from_fields, self.should_be_remove_from_address_fields, self.should_be_remove_from_room_number_fields, self.should_be_install_to_fields, self.should_be_install_to_address_fields, self.should_be_install_to_room_number_fields, self.should_be_svt_card_fields, self.should_be_justification_fields],
        }

        return [field[r_type][0] if edit == False else field[r_type][1], func[1 if r_type in [1, 2, 3] else r_type]]


class EnterRequestDocumentPage(Fields, AllDocumentFieldPage):

    def fill_enter_reqests_fields(self, num, fill, edit):
        field = self.fields(num, edit)

        if fill == True and edit == False:
            self.fill_in_all_document_required_fields(
                "суперадмин", "администратор")
        elif fill == True and edit == True:
            self.click_to_edit_pictogram()
            self.delete_all_added_files()

            locators = self.driver.find_elements(
                *EnterRequestDocumentPageLocators.DELETE_BUTTON_LOCATOR)
            for i in locators:
                self.driver.execute_script("arguments[0].click();", i)

        for i in range(len(field[1])):
            field[1][i](0, 0, fill, field[0][i])

        if (fill == True and edit == False) or (fill == True and edit == True):
            self.save_rcd()

    def delete_block_button(self):
        pass
