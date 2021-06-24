import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from msedge.selenium_tools import Edge, EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

from os import path


folder_path = path.join(path.dirname(path.abspath(__file__)), 'extensions')
PATH_TO_CP_XPI = path.join(folder_path, 'CryptoPro_ff.xpi')
PATH_TO_CP_CRX = path.join(folder_path, 'CryptoPro-chrome.crx')
PATH_TO_CP_YD = path.join(folder_path, 'yandex-chromedriver.exe')


# Path to Chrome driver
WBC_PATH = ChromeDriverManager().install()

# Path to FireFox driver
WBFF_PATH = GeckoDriverManager().install()

# Path to IE driver
WBIE_PATH = IEDriverManager().install()

# # Path to MSEage driver
WBEAGE_PATH = EdgeChromiumDriverManager().install()

# # Path to Opera driver
WBO_PATH = OperaDriverManager().install()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome")


def chrome(browser_name):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('ignore-certificate-errors')
    # options.add_extension(
    #     extension=r"D:\WorkPlase\sed-tests\extensions\CryptoPro-chrome.crx")

    return webdriver.Chrome(executable_path=WBC_PATH, options=options)


def firefox(browser_name):
    ff_profile = webdriver.FirefoxProfile()
    options = Options()
    # options.headless = True
    ff_profile.add_extension(
        extension=PATH_TO_CP_XPI)

    return webdriver.Firefox(executable_path=WBFF_PATH, firefox_profile=ff_profile, options=options)


def ie(browser_name):
    options = webdriver.IeOptions()
    # options.require_window_focus = True
    options.native_events = False
    # options.ignore_protected_mode_settings = True
    # options.ignore_zoom_level = True

    return webdriver.Ie(executable_path=WBIE_PATH, options=options)


def edge(browser_name):
    options = EdgeOptions()
    options.use_chromium = True
    options.add_extension(extension=PATH_TO_CP_CRX)

    return Edge(executable_path=WBEAGE_PATH, options=options)


def yandex(browser_name):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('ignore-certificate-errors')
    # path to YandexDriver
    options.binary_location = r"C:\\Users\\User\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe"
    path = r"D:\\WorkSpace\\sedmf-automated-tests\\pages\\files\\yandexdriver.exe"

    return webdriver.Chrome(executable_path=path, chrome_options=options)


def opera(browser_name):
    return webdriver.Opera(executable_path=WBO_PATH)


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "ff":
        driver = firefox(browser_name)
    elif browser_name == "chrome":
        driver = chrome(browser_name)
    elif browser_name == "edge":
        driver = edge(browser_name)
    elif browser_name == "ie":
        driver = ie(browser_name)
    elif browser_name == "yandex":
        driver = yandex(browser_name)
    elif browser_name == "opera":
        driver = opera(browser_name)
    else:
        raise Exception("Uncorrect browser")

    yield driver

    driver.quit()
