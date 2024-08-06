import chromedriver_autoinstaller
import pytesseract
from PIL import Image
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


def init_driver() -> WebDriver:
    chromedriver_autoinstaller.install()
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options=chrome_options)
    time.sleep(0.5)
    driver.set_window_size(900, 900)
    time.sleep(0.5)
    return driver


def find_main_input_xpath(driver: WebDriver) -> int:
    for i in range(1, 5):
        xpath = f"/html/body/div/div[{i}]/div/form/div[5]/div/input"
        try:
            driver.find_element(By.XPATH, xpath)
            return i
        except:
            pass
    raise Exception("Not found...")


def get_option_idx(options, option):
    for i, tmp_option in enumerate(options):
        if tmp_option == option:
            return i
    return -1












def wait_for_element(driver:WebDriver, x_path: str, max_wait_time_s: float):
    max_wait_time_s *= 100
    for time_s in range(1, int(max_wait_time_s), 1):
        try:
            driver.find_element(By.XPATH, x_path)
            return True
        except:
            time.sleep(1 / 100)
    return False
def insert_text_box(driver: WebDriver, xpath_input, value: str):
    driver.find_element(By.XPATH, xpath_input).send_keys(value)

def solve_captcha(path) -> str:
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    result = text.strip()
    return result
def insert_captcha_in_search_window(driver: WebDriver, i_main, i, screenshots_location):
    xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div[1]/input"
    xpath_captcha = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div[1]/img"

    path = os.path.join(screenshots_location, "captcha_screen.png")
    driver.find_element(By.XPATH, xpath_captcha).screenshot(path)

    value = solve_captcha(path)
    insert_text_box(driver, xpath_input, value)
    time.sleep(0.6)





def wait_till_table_is_visible(driver: WebDriver):
    xpath = f"/html/body/div/div[2]/div/div[1]/h1"
    if not wait_for_element(driver, xpath, 30):
        raise Exception("=== Page not working ===")

def solve_captcha_if_visible(driver:WebDriver, screenshots_location):
    # find img if exist
    i_elem = -1
    for i in range(1, 4):
        try:
            xpath_img = f"/html/body/div/div[{i}]/div/form/div[1]/div[1]/img"
            driver.find_element(By.XPATH, xpath_img)
            i_elem = i
        except:
            pass
    if i_elem < 0:
        return False

    xpath_inp = f"/html/body/div/div[{i_elem}]/div/form/div[1]/div[1]/input[1]"
    xpath_img = f"/html/body/div/div[{i_elem}]/div/form/div[1]/div[1]/img"
    xpath_submit = f"/html/body/div/div[{i_elem}]/div/form/div[2]/button"
    for j in range(0, 4, 1):
        xpath_head = f"/html/body/div/div[{i_elem}]/div/div/h1"
        wait_for_element(driver, xpath_head, 5)
        try:
            path = os.path.join(screenshots_location, "captcha_screen.png")
            driver.find_element(By.XPATH, xpath_img).screenshot(path)
            value = solve_captcha(path)
            insert_text_box(driver, xpath_inp, value)
            time.sleep(0.71)
            driver.find_element(By.XPATH, xpath_submit).click()
            time.sleep(1.1)
            continue
        except:
            return True

    raise Exception("=== Can't solve Captcha ===")

def find_table_indexes(driver: WebDriver):
    for i in range(0, 11):
        for j in range(0, 11):
            try:
                xpath = f"/html/body/div/div[{i}]/div/div[{j}]/table/tbody/tr[1]/td[1]"
                driver.find_element(By.XPATH, xpath)
                return [i, j]
            except:
                pass
    raise Exception("==== Table not exist ====")


















