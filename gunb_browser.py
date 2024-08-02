import time
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from input_data_model import InputDataModel


def get_dict_input_model(model_data):
    model_names = InputDataModel().__dict__
    model_data = model_data.__dict__
    res = {}
    for key in model_names:
        res[model_names[key]] = model_data[key]

        if "od" in key:
            aa = 0

    return res


@dataclass
class DataModel:
    driver: WebDriver = None
    url: str = "https://wyszukiwarka.gunb.gov.pl/"

    def init_driver(self):
        # driver = Driver(uc=True)
        self.driver = webdriver.Chrome()
        time.sleep(0.5)
        # driver.maximize_window()
        self.driver.set_window_size(900, 900)
        time.sleep(0.5)

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

    def set_inputs(self, model_data):
        select_boxs = ["Typ dokumentu (Rejestr Wniosków i Decyzji)","Województwo","Organ administracji","Rodzaj zamierzenia budowlanego","Kategoria obiektu"]
        date_inputs = ["Data wydania decyzji", "Data złożenia\nwniosku / zgłoszenia"]

        self.driver.get(self.url)
        time.sleep(1.21)
        i_main = self.find_main_input_xpath()

        input_model = get_dict_input_model(model_data)
        for i in range(30):
            try:
                xpath_label = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/label"
                label = self.driver.find_element(By.XPATH, xpath_label).text
                value = input_model[label]

                # TODO - wszystkie daty
                # ToDo - pierwsze wojewodztwo

                xpath_input = "/html/body/div/div[2]/div/form/div[8]/label"
                xpath_input = "/html/body/div/div[2]/div/form/div[8]/div/input[1]"

                if label == '':
                    continue
                if value == '':
                    continue

                if label in select_boxs:
                    xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/select"
                    self.insert_select_box(xpath_input, value)
                    continue

                if label in date_inputs:
                    xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/input[1]"
                    self.insert_select_box(xpath_input, value)
                    xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/input[2]"
                    self.insert_select_box(xpath_input, value)
                    continue

                xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/input"
                self.insert_text_box(xpath_input, value)
                a = 0
            except Exception as eeee:
                print(eeee)

