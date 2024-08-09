import json
import time

import requests

from utils_download_records import init_driver, find_main_input_xpath, get_option_idx, insert_captcha_in_search_window, \
    wait_for_element, wait_till_table_is_visible, solve_captcha_if_visible, find_table_indexes
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

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
from selenium.webdriver.chrome.options import Options

max_page_to_visit = 10  # max 10
max_inp_idx = 31

user_laptop_firmowy = False
user_komp_stacjo = not user_laptop_firmowy

if user_laptop_firmowy:
    screenshots_location = r"C:\Users\pkubon\Downloads"
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\pkubon\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
if user_komp_stacjo:
    screenshots_location = r"C:\Users\pkubo\Downloads"
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\pkubo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def insert_data(driver: WebDriver, model: dict, ):
    wojewodztwo_not_set = True
    i_main = find_main_input_xpath(driver)
    selects = BeautifulSoup(driver.page_source).find_all('select')
    options_typ_dokumentu = [op.text.strip() for op in selects[0].findAll('option')]
    options_wojewodztwo = [op.text.strip() for op in selects[2].findAll('option')]
    options_organ_administracji = [op.text.strip() for op in selects[3].findAll('option')]
    options_rodzaj_zamierzenia_budowlanego = [op.text.strip() for op in selects[5].findAll('option')]
    options_kategoria_obiektu = [op.text.strip() for op in selects[6].findAll('option')]

    for i in range(1, max_inp_idx):
        try:
            xpath_label = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/label"
            label = driver.find_element(By.XPATH, xpath_label).text

            key = "Typ dokumentu (Rejestr Wniosków i Decyzji)"
            if label == key:
                idx = get_option_idx(options_typ_dokumentu, model[key])
                xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/select"
                Select(driver.find_element(By.XPATH, xpath_input)).select_by_index(idx)
                continue
            key = "Data złożenia\nwniosku / zgłoszenia"
            if label == key:
                xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/input[1]"
                driver.find_element(By.XPATH, xpath_input).send_keys(model[key])
                continue
            key = "Rodzaj zamierzenia budowlanego"
            if label == key:
                idx = get_option_idx(options_rodzaj_zamierzenia_budowlanego, model[key])
                xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/select"
                Select(driver.find_element(By.XPATH, xpath_input)).select_by_index(idx)
                continue
            key = "Kategoria obiektu"
            if label == key:
                idx = get_option_idx(options_kategoria_obiektu, model[key])
                xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/select"
                Select(driver.find_element(By.XPATH, xpath_input)).select_by_index(idx)
                continue
            key = "Województwo"
            if label == key and wojewodztwo_not_set:
                idx = get_option_idx(options_wojewodztwo, model[key])
                xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/select"
                Select(driver.find_element(By.XPATH, xpath_input)).select_by_index(idx)
                wojewodztwo_not_set = False
                continue
            key = "Organ administracji"
            if label == key:
                r = requests.get("https://wyszukiwarka.gunb.gov.pl/")
                r.encoding = r.apparent_encoding
                selects = BeautifulSoup(r.text).find_all('select')
                options_wojewodztwo = {}
                for op in selects[2].findAll('option'):
                    options_wojewodztwo[op.text.strip()] = op['value']

                r = requests.get(
                    f"https://wyszukiwarka.gunb.gov.pl/json/Search/getOrgsByRegion/?region={options_wojewodztwo[model["Województwo"].lower()]}")
                r.encoding = r.apparent_encoding
                data_json = json.loads(r.text)

                organy = []
                for item in data_json["data"]:
                    organy.append(item["name"])

                idx = get_option_idx(organy, model[key])
                xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/div/select"
                Select(driver.find_element(By.XPATH, xpath_input)).select_by_index(idx)
                continue
            key = "Wpisz kod znajdujący się na obrazku poniżej:"
            if label == key:
                for xxx in range(0, 4, 1):
                    insert_captcha_in_search_window(driver, i_main, i, screenshots_location)

                    xpath_input = f"/html/body/div/div[{i_main}]/div/form/div[{i + 1}]/button"
                    driver.find_element(By.XPATH, xpath_input).click()
                    time.sleep(1.1)

                    xpath_head = f"/html/body/div/div[{i_main}]/div/div/h1"
                    wait_for_element(driver, xpath_head, 5)

                    try:
                        xpath_error = f"/html/body/div/div[{i_main}]/div/form/div[{i}]/span"
                        driver.find_element(By.XPATH, xpath_error)
                        continue
                    except:
                        return True
                raise Exception("Can't solve Captcha")

        except Exception as eeee:
            print(eeee)


def get_data_from_table(driver: WebDriver):
    result = []
    [iii, jjj] = find_table_indexes(driver)
    for row_num in range(1, 11):
        try:
            xpath = f"/html/body/div/div[{iii}]/div/div[{jjj}]/table/tbody/tr[{row_num}]/td[6]/a"
            in_url = driver.find_element(By.XPATH, xpath).get_attribute('href')
            xpath = f"/html/body/div/div[{iii}]/div/div[{jjj}]/table/tbody/tr[{row_num}]/td[2]"
            in_inwestor = driver.find_element(By.XPATH, xpath).text
            xpath = f"/html/body/div/div[{iii}]/div/div[{jjj}]/table/tbody/tr[{row_num}]/td[3]"
            in_nazwa_zamieszkania = driver.find_element(By.XPATH, xpath).text
            xpath = f"/html/body/div/div[{jjj}]/div/div[{jjj}]/table/tbody/tr[{row_num}]/td[1]"
            in_data_wplywu = driver.find_element(By.XPATH, xpath).text
            result.append({
                "Url": in_url,
                "Inwestor": in_inwestor,
                "Nazwa zamierzenia": in_nazwa_zamieszkania,
                "Data złożenia\nwniosku / zgłoszenia": in_data_wplywu
            })
        except:
            return result
    return result


def download_records():
    with open('data.json', encoding='utf-8') as f:
        model = json.load(f)

    driver = init_driver()
    # time.sleep(0.51)
    # driver.get("https://wyszukiwarka.gunb.gov.pl/")
    # time.sleep(1.21)

    # selects = BeautifulSoup(driver.page_source).find_all('select')
    # model["Województwo"] = [op.text.strip() for op in selects[2].findAll('option')]
    # model["Organ administracji"] = [op.text.strip() for op in selects[3].findAll('option')]

    result = []
    for typ_dokumentu in model["Typ dokumentu (Rejestr Wniosków i Decyzji)"]:
        for data_zlozenia_wniosku in model["Data złożenia\nwniosku / zgłoszenia"]:
            for rodzaj_zamierzenia_budowlanego in model["Rodzaj zamierzenia budowlanego"]:
                for kategoria_obiektu in model["Kategoria obiektu"]:
                    for wojewodztwo in model["Województwo"]:
                        for organ_administracji in model["Organ administracji"]:
                            item = {
                                "Typ dokumentu (Rejestr Wniosków i Decyzji)": typ_dokumentu,
                                "Data złożenia\nwniosku / zgłoszenia": data_zlozenia_wniosku,
                                "Rodzaj zamierzenia budowlanego": rodzaj_zamierzenia_budowlanego,
                                "Kategoria obiektu": kategoria_obiektu,
                                "Województwo": wojewodztwo,
                                "Organ administracji": organ_administracji
                            }
                            time.sleep(0.51)
                            driver.get("https://wyszukiwarka.gunb.gov.pl/")
                            time.sleep(1.21)
                            insert_data(driver, item)
                            wait_till_table_is_visible(driver)

                            url = driver.current_url
                            for page_number in range(1, max_page_to_visit + 1):
                                driver.get(url + f"&page={page_number}")

                                wait_till_table_is_visible(driver)
                                solve_captcha_if_visible(driver, screenshots_location)
                                wait_till_table_is_visible(driver)

                                time.sleep(1.2)
                                tmp_res = get_data_from_table(driver)
                                item.pop("Data złożenia\nwniosku / zgłoszenia","2000-01-01")
                                for key in item:
                                    for aaa in tmp_res:
                                        aaa[key] = item[key]
                                result += tmp_res

                                with open('result.json', 'w', encoding='utf-8') as f:
                                    json.dump(result, f)

                                if len(tmp_res) < 10:
                                    break

# download_records()
