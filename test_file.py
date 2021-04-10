import time

link = "https://cryptopro.ru/sites/default/files/products/cades/demopage/cades_bes_sample.html"

def test_one(driver):
    driver.get(link)
    a = driver.find_element_by_id("SignBtn")
    a.click()
    time.sleep(100)