import chromedriver_autoinstaller
import pytesseract
from PIL import Image
import os
import time
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from input_data_model import InputDataModel
from selenium.webdriver.chrome.options import Options




screenshots_location = r"C:\Users\pkubon\Downloads"
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\pkubon\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
max_page_to_visit = 10  # max 10

def get_dict_input_model(model_data):
    model_names = InputDataModel().__dict__
    model_data = model_data.__dict__
    res = {}
    for key in model_names:
        res[model_names[key]] = model_data[key]
    return res


def solve_captcha(path) -> str:
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    result = text.strip()
    return result



@dataclass
class DataModel:
    driver: WebDriver = None
    url: str = "https://wyszukiwarka.gunb.gov.pl/"
    max_inp_idx = 31
    woj_set = False
    select_boxs = ["Typ dokumentu (Rejestr Wniosków i Decyzji)", "Organ administracji","Rodzaj zamierzenia budowlanego", "Kategoria obiektu"]
    date_inputs = ["Data wydania decyzji", "Data złożenia\nwniosku / zgłoszenia"]
    woj_inputs = ["Województwo"]
    captha_inputs = ['Wpisz kod znajdujący się na obrazku poniżej:']

    def init_driver(self):
        chromedriver_autoinstaller.install()
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        # driver = Driver(uc=True, chromium_arg = "--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(options=chrome_options)
        time.sleep(0.5)
        # driver.maximize_window()
        self.driver.set_window_size(900, 900)
        time.sleep(0.5)

    def solve_captcha_if_visible(self, path) -> bool:
        # find img if exist
        i_elem = -1
        for i in range(1, 4):
            try:
                xpath_img = f"/html/body/div/div[{i}]/div/form/div[1]/div[1]/img"
                self.driver.find_element(By.XPATH, xpath_img)
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
            self.wait_for_element(xpath_head, 5)
            try:
                path = os.path.join(screenshots_location, "captcha_screen.png")
                self.driver.find_element(By.XPATH, xpath_img).screenshot(path)
                value = solve_captcha(path)
                self.insert_text_box(xpath_inp, value)
                self.driver.find_element(By.XPATH, xpath_submit).click()
                continue
            except:
                return True

        raise Exception("=== Can't solve Captcha ===")



    def find_main_input_xpath(self):
        for i in range(1, 5):
            xpath = f"/html/body/div/div[{i}]/div/form/div[5]/div/input"
            try:
                self.driver.find_element(By.XPATH, xpath)
                return i
            except:
                pass

    def insert_select_box(self, xpath_input, idx: int):
        my_select = Select(self.driver.find_element(By.XPATH, xpath_input))
        my_select.select_by_index(idx)

    def insert_text_box(self, xpath_input, value: str):
        self.driver.find_element(By.XPATH, xpath_input).send_keys(value)

    def skip_on_empty(self, label, value):
        if label == '':
            return True
        if value == '':
            return True
        return False

    def try_insert_select_box(self, i_main, i, label, value):
        if label in self.select_boxs:
            xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/select"
            self.insert_select_box(xpath_input, value)
            return True
        return False

    def try_insert_date_box(self, i_main, i, label, value):
        if label in self.date_inputs:
            val_od = value.split("&")[0]
            val_do = value.split("&")[1]
            xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/input[1]"
            self.insert_text_box(xpath_input, val_od)
            xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/input[2]"
            self.insert_text_box(xpath_input, val_do)
            return True
        return False
    def try_insert_woj_box(self, i_main, i, label, value):
        if label in self.woj_inputs and not self.woj_set:
            woj_1 = value.split("&")[0]
            woj_2 = value.split("&")[1]
            xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/select"
            self.insert_select_box(xpath_input, woj_1)

            for j in range(i + 1, self.max_inp_idx, 1):
                try:
                    xpath_label = f"/html/body/div/div[{i_main}]/div/form/div[{j}]/label"
                    label_2 = self.driver.find_element(By.XPATH, xpath_label).text
                    if label == label_2:  # Wojewodztwo
                        xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{j}]/div/select"
                        self.insert_select_box(xpath_input, woj_2)
                        self.woj_set = True
                        break
                except:
                    pass
            return True
        return False
    def try_insert_text_box(self, i_main, i, label, value):
        xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/input"
        self.insert_text_box(xpath_input, value)
        return True

    def try_insert_captcha(self, i_main, i, label, value):
        if label in self.captha_inputs:
            for xxx in range(0, 4, 1):
                xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div[1]/input"
                xpath_captcha = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div[1]/img"

                path = os.path.join(screenshots_location, "captcha_screen.png")
                self.driver.find_element(By.XPATH, xpath_captcha).screenshot(path)

                value = solve_captcha(path)
                self.insert_text_box(xpath_input, value)

                xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i+1}]/button"
                self.driver.find_element(By.XPATH, xpath_input).click()

                xpath_head = f"/html/body/div/div[{i_main}]/div/div/h1"
                self.wait_for_element(xpath_head, 5)

                xpath_error = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/span"
                try:
                    self.driver.find_element(By.XPATH, xpath_error)
                    continue
                except:
                    return True
        return False

    def set_inputs(self, model_data):
        self.driver.get(self.url)
        time.sleep(1.21)
        i_main = self.find_main_input_xpath()

        input_model = get_dict_input_model(model_data)
        for i in range(self.max_inp_idx):
            try:
                xpath_label = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/label"
                label = self.driver.find_element(By.XPATH, xpath_label).text
                value = input_model[label]

                if self.skip_on_empty(label, value):
                    continue
                if self.try_insert_select_box(i_main, i, label, value):
                    continue
                if self.try_insert_date_box(i_main, i, label, value):
                    continue
                if self.try_insert_woj_box(i_main, i, label, value):
                    continue
                if self.try_insert_captcha(i_main, i, label, value):
                    return True

                if self.try_insert_text_box(i_main, i, label, value):
                    continue

            except Exception as eeee:
                print(eeee)
        return False

    def wait_for_element(self, x_path: str, max_wait_time_s: float):
        max_wait_time_s *= 100
        for time_s in range(1, int(max_wait_time_s), 1):
            try:
                self.driver.find_element(By.XPATH, x_path)
                return True
            except:
                pass
            time.sleep(1 / 100)
        return False

    def wait_till_table_is_visible(self):
        xpath = f"/html/body/div/div[2]/div/div[1]/h1"
        if not self.wait_for_element(xpath, 30):
            raise Exception("=== Page not working ===")

    def find_table_indexes(self):
        for i in range(0, 11):
            for j in range(0, 11):
                try:
                    xpath = f"/html/body/div/div[{i}]/div/div[{j}]/table/tbody/tr[1]/td[1]"
                    self.driver.find_element(By.XPATH, xpath)
                    return [i, j]
                except:
                    pass
        raise Exception("==== Table not exist ====")

    def get_data_from_table(self, model):
        self.wait_till_table_is_visible()
        self.solve_captcha_if_visible(screenshots_location)
        self.wait_till_table_is_visible()
        [iii, jjj] = self.find_table_indexes()

        url = self.driver.current_url
        result = []
        for page_number in range(1, max_page_to_visit+1):
            self.driver.get(url + f"&page={page_number}")
            self.wait_till_table_is_visible()
            self.solve_captcha_if_visible(screenshots_location)
            self.wait_till_table_is_visible()

            for row_num in range(1, 11):
                try:
                    xpath = f"/html/body/div/div[{iii}]/div/div[{jjj}]/table/tbody/tr[{row_num}]/td[6]/a"
                    in_url = self.driver.find_element(By.XPATH, xpath).get_attribute('href')
                    xpath = f"/html/body/div/div[{iii}]/div/div[{jjj}]/table/tbody/tr[{row_num}]/td[2]"
                    in_inwestor = self.driver.find_element(By.XPATH, xpath).text
                    xpath = f"/html/body/div/div[{iii}]/div/div[{jjj}]/table/tbody/tr[{row_num}]/td[3]"
                    in_nazwa_zamieszkania = self.driver.find_element(By.XPATH, xpath).text
                    result.append({"url": in_url, "inwestor": in_inwestor, "nazwa_zamieszkania": in_nazwa_zamieszkania})
                except:
                    return result
        return result












