import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as ff_options
from msedge.selenium_tools import Edge, EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from ast import literal_eval
from os import path


class Paths:
    # Extensions
    def extensions_path(self, chromium=True) -> str:
        folder_path = path.join(path.dirname(
            path.abspath(__file__)), 'extensions')
        xpi = path.join(folder_path, 'CryptoPro_ff.xpi')
        crx = path.join(folder_path, 'CryptoPro_chrome.crx')

        return crx if chromium == True else xpi

    # Save file in
    def save_folder(self):
        save_folder_path = path.join(path.dirname(
            path.abspath(__file__)), 'pages\\files')

        return save_folder_path

    # Yandex Path
    def yandex_path(self):
        yandex_binary_file_path = path.abspath(
            "C:\\Users\\User\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe")
        webdriver_yandex_path = path.join(
            self.save_folder(), "yandexdriver.exe")

        return yandex_binary_file_path, webdriver_yandex_path

    # Chrome Path
    def chrome_path(self):
        webdriver_chrome_path = ChromeDriverManager().install()

        return webdriver_chrome_path

    # Firefox Path
    def firefox_path(self):
        webdriver_firefox_path = GeckoDriverManager().install()

        return webdriver_firefox_path

    # MSEdge Path
    def msedge_path(self):
        webdriver_edge_path = EdgeChromiumDriverManager(log_level=1).install()

        return webdriver_edge_path

    # Opera Path
    def opera_path(self):
        opera_binary_file_path = path.abspath(
            "C:\\Users\\User\\AppData\\Local\\Programs\\Opera\\77.0.4054.203\\opera.exe")
        webdriver_opera_path = OperaDriverManager().install()

        return opera_binary_file_path, webdriver_opera_path

    # IE Path
    def ie_path(self):
        webdriver_ie_path = IEDriverManager(log_level=1).install()

        return webdriver_ie_path


class WebDriver(Paths):
    def chrome(self, sign_test: bool):
        chrome_webriver = self.chrome_path()
        save_folder = self.save_folder()
        extensions = self.extensions_path()

        options = webdriver.ChromeOptions()

        if sign_test == False:
            options.headless = True
        else:
            options.add_extension(extension=extensions)
        options.add_argument('ignore-certificate-errors')
        options.add_experimental_option(
            "prefs", {"download.default_directory": save_folder})

        return webdriver.Chrome(executable_path=chrome_webriver, options=options)

    def firefox(self, sign_test: bool):
        ff_webdriver = self.firefox_path()
        save_folder = self.save_folder()
        extensions = self.extensions_path(False)

        ff_profile = webdriver.FirefoxProfile()
        options = ff_options()

        if sign_test == False:
            options.headless = True
        else:
            ff_profile.add_extension(extension=extensions)
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", save_folder)
        options.set_preference("browser.download.useDownloadDir", True)
        options.set_preference(
            "browser.download.viewableInternally.enabledTypes", "")
        options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               "application/pdf;text/plain;application/text;text/xml;application/xml")
        options.set_preference("pdfjs.disabled", True)

        return webdriver.Firefox(executable_path=ff_webdriver, firefox_profile=ff_profile, options=options)

    def edge(self, sign_test: bool):
        edge_webriver = self.msedge_path()
        save_folder = self.save_folder()
        extensions = self.extensions_path()

        options = EdgeOptions()

        if sign_test == False:
            options.headless = True
        else:
            options.add_extension(extension=extensions)
        options.use_chromium = True
        options.add_experimental_option(
            "prefs", {"download.default_directory": save_folder})

        return Edge(executable_path=edge_webriver, options=options)

    def yandex(self, sign_test: bool):
        yandex_exe, yandex_webdriver = self.yandex_path()
        save_folder = self.save_folder()
        extensions = self.extensions_path()

        options = webdriver.ChromeOptions()

        if sign_test == False:
            options.headless = True

        # Сделать запуск расширением для ЭП не удалось
        else:
            options.add_extension(extension=extensions)
        options.add_experimental_option("extensions:", [extensions])
        options.add_argument('ignore-certificate-errors')
        options.add_experimental_option(
            "prefs", {"download.default_directory": save_folder})
        options.binary_location = yandex_exe

        return webdriver.Chrome(executable_path=yandex_webdriver, options=options)

    def opera(self, sign_test: bool):
        opera_exe, opera_webdriver = self.opera_path()
        save_folder = self.save_folder()
        extensions = self.extensions_path()

        options = webdriver.ChromeOptions()
        # options.headless = True
        if sign_test == True:
            options.add_argument('ignore-certificate-errors')
        options.binary_location = opera_exe
        options.add_extension(extension=extensions)
        options.add_experimental_option(
            "prefs", {"download.default_directory": save_folder()})

        return webdriver.Chrome(executable_path=opera_webdriver, options=options)

    def ie(self, sign_test: bool):
        ie_webdriver = self.ie_path()
        options = webdriver.IeOptions()

        if sign_test == False:
            options.headless = True
        # options.require_window_focus = True
        options.native_events = False
        # options.ignore_protected_mode_settings = True
        # options.ignore_zoom_level = True

        return webdriver.Ie(executable_path=ie_webdriver, options=options)


def pytest_addoption(parser):
    parser.addoption('--browser_name', default="chrome")
    parser.addoption("--sign_test", default="False")


@pytest.fixture(scope="function")
def driver(request):
    wb = WebDriver()
    browser_name = request.config.getoption("browser_name")
    sign_test = literal_eval(request.config.getoption("sign_test"))

    if browser_name == "ff":
        driver = wb.firefox(sign_test)
    elif browser_name == "chrome":
        driver = wb.chrome(sign_test)
    elif browser_name == "edge":
        driver = wb.edge(sign_test)
    # elif browser_name == "yandex":
    #     driver = wb.yandex(sign_test)
    # elif browser_name == "ie":
    #     driver = wb.ie(sign_test)
    # elif browser_name == "opera":
    #     driver = wb.opera(sign_test)
    else:
        raise Exception("Uncorrect browser")

    yield driver

    driver.quit()
