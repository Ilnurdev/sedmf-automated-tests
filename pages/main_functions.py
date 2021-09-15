from .locators import AllDocumentFieldLocators, FindDocumentInFolder
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from datetime import timedelta, datetime
from os import path, listdir, remove
from re import search
from time import sleep
from json import load
from subprocess import call


class MainFunc:
    folder_path = path.join(path.dirname(path.abspath(__file__)), 'files')
    PATH_TO_CONFIG = path.join(folder_path, 'config.json')
    PATH_TO_FILE = path.join(folder_path, 'Test5.docx')
    PATH_TO_ID_DOC = path.join(folder_path, 'saved-id.txt')

    def __init__(self, driver, url="", timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def work_with_selector(self, how, what, value=None, visible_text=None):
        select = Select(self.driver.find_element(how, what))
        if value != None:
            select.select_by_value(value)
        elif visible_text != None:
            select.select_by_visible_text(visible_text)

    def fill_field(self, how, what, text=None, f_type=0, save_wait=False):
        locator = self.driver.find_element(how, what)
        if text != None:
            locator.clear()
            locator.send_keys(text)
        else:
            locator.send_keys(self.PATH_TO_FILE)
            if f_type == 0:
                WebDriverWait(self.driver, 0).until_not(
                    EC.element_to_be_clickable((how, what)))
            if save_wait == True:
                def wait(how, what): return WebDriverWait(self.driver, 30).until(
                    EC.invisibility_of_element((how, what)))
                wait(*AllDocumentFieldLocators.WAIT_FILE_DOWNLOAD_LOCATOR)

    def click_to(self, how, what):
        try:
            locator = self.driver.find_element(how, what)
            self.driver.execute_script("arguments[0].click();", locator)
        except (NoSuchElementException):
            return False

    def choose_user_from_drop_list(self, text=None):
        """Если не указан текст, выбирается первое элемент в дроп листе, иначе, ищется и выбирается указанный элемент"""
        user_locator = AllDocumentFieldLocators.choose_user_from_drop_list_locator(
            text)

        self.is_element_present(*user_locator)
        self.click_to(*user_locator)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_appeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((how, what))
            )
            return True
        except:
            return False

    def is_not_appeared(self, how, what, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.invisibility_of_element((how, what))
            )
            return False
        except:
            return True

    def is_not_element_present(self, how, what, timeout=0):
        driver = self.driver
        element_found = False
        driver.implicitly_wait(0)

        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((how, what)))
        except:
            element_found = True
            
        driver.implicitly_wait(30)
        return element_found

    def url_change(self, url, timeout=60):
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_changes((url)))
        except TimeoutException:
            return False
        return True

    def alert_open(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        except TimeoutException:
            return False
        return True

    def is_active(self, how, what, timeout=30):
        driver = self.driver
        element_found = True
        driver.implicitly_wait(0)

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            element_found = False
        driver.implicitly_wait(30)

        return element_found

    def count_all_elements(self, how, what, timeout=0):
        driver = self.driver
        driver.implicitly_wait(0)
        elements = 0
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((how, what)))
        except:
            elements = []
        driver.implicitly_wait(30)

        return len(elements)

    def work_with_windows(self, value=0, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.number_of_windows_to_be((value+1)))
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[value])
        except:
            raise ValueError("Отсутствует выбранное окно")
            
        return windows

    def save_document_id(self):
        url_for_take_id = self.driver.current_url
        document_id = (search(r"(\&|\?)id=((\d|\w)+)", url_for_take_id)[2])

        return document_id

    def return_text(self, how, what):
        self.is_appeared(how, what)
        r_text = lambda: self.driver.find_element(how, what).text
        text = r_text()

        count = 0
        while text == "" and count < 10:
            text = r_text()
            count += 1
            sleep(0.2)

        return text

    def date_return(self, add_days=0):
        return (datetime.today() + timedelta(days=add_days)).strftime("%d.%m.%Y")

    def find_document_in_folder(self):
        document_id = self.save_document_id(False)
        assert self.is_element_present(
            *FindDocumentInFolder.find_doc_in_folder(document_id))
        self.click_to(*FindDocumentInFolder.find_doc_in_folder(document_id))

    def pdf_to_html(self, file_name, file_in_folder=folder_path) -> str:
        """Конвертирует pdf в html при помощи LibreOffice, удаляет скачанный и конверитированный файлы, возвращает текст"""

        def find_file(files, file_name):
            """Ищет файл в папке, возвращает название"""
            for i in files:
                if (file_name in i) and ("crd" not in i):
                    for num in range(len(i))[::-1]:
                        if i[num] == ".":
                            return i[:num]
            return file_name

        def found_file_in_folder(file_name, timeout=30):
            """Обновляет файлы в папке, возвращает название файла"""
            count = timeout
            while count != 0:
                if count <= 0:
                    assert False, "Файл не загружен"

                files = listdir(file_in_folder)
                name = find_file(files, file_name)

                if file_name != name:
                    return name

                count -= 1
                sleep(1)

        name = found_file_in_folder(file_name + ".pdf")
        path_to_soffice = self.config("path_to_soffice")
        path_to_file = file_in_folder + "\\" + name + ".pdf"
        text = None

        if path_to_soffice != "":
            call(
                f'"{path_to_soffice}" --headless --convert-to html:draw_html_Export --outdir "{self.folder_path}" "{path_to_file}"', shell=True)

            name = found_file_in_folder(file_name + ".html")
            html_file = self.folder_path + "\\" + name + ".html"

            with open(html_file, mode="r", encoding="UTF-8") as f:
                text = f.read()

            remove(html_file)
        remove(path_to_file)

        return text

    @staticmethod
    def take_DNSID(url, url_for_take_dnsid):
        dnsid = (search(r"DNSID=(\d|\w)+", url_for_take_dnsid)[0])
        return (url + "&" + dnsid)

    @staticmethod
    def create_doc_link(url, doc_id):
        return (url + "&id=" + doc_id)

    @staticmethod
    def config(value="server"):
        with open(MainFunc.PATH_TO_CONFIG) as f:
            data = load(f)
            try:
                return data[value]
            except KeyError:
                return data["server"]
