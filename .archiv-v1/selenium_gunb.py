import os
import easyocr

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from XPathModel1 import XPathModel1
from XPathModel2 import XPathModel2
from data_model import DataModel

url_start = "https://wyszukiwarka.gunb.gov.pl/"


def get_init_driver() -> WebDriver:
    # driver = Driver(uc=True)
    driver = webdriver.Chrome()
    time.sleep(0.5)
    # driver.maximize_window()
    driver.set_window_size(900, 900)
    time.sleep(0.5)
    return driver


def wait_for_element(driver: WebDriver, x_path: str, max_wait_time_s: float):
    max_wait_time_s *= 100
    for time_s in range(1, int(max_wait_time_s), 1):
        try:
            driver.find_element(By.XPATH, x_path)
            return 0
        except:
            pass
        time.sleep(1 / 100)
    return 1


def insert_requested_values(driver: WebDriver, data_model: DataModel):
    xpath1_model = data_model.xpath_model_1
    x_path_vals = XPathModel1()

    if xpath1_model.rodzaj_wyszukiwania != "":
        if xpath1_model.rodzaj_wyszukiwania == "Wyszukiwanie pozwoleń na budowę":
            x_path_vals.rodzaj_wyszukiwania = "/html/body/div/div[2]/div/form/div[1]/div[1]/label/input"
        else:
            x_path_vals.rodzaj_wyszukiwania = "/html/body/div/div[2]/div/form/div[1]/div[2]/label/input"
        wait_for_element(driver, x_path_vals.rodzaj_wyszukiwania, 10)
        driver.find_element(By.XPATH, x_path_vals.rodzaj_wyszukiwania).click()
        time.sleep(1)

    if xpath1_model.typ_dokumentu != "":
        wait_for_element(driver, x_path_vals.typ_dokumentu, 10)
        my_select = Select(driver.find_element(By.XPATH, x_path_vals.typ_dokumentu))
        my_select.select_by_index(data_model.typ_dokumentu[xpath1_model.typ_dokumentu])
        time.sleep(1)

    if xpath1_model.numer_ewidencyjny_wniosku != "":
        wait_for_element(driver, x_path_vals.numer_ewidencyjny_wniosku, 10)
        driver.find_element(By.XPATH, x_path_vals.numer_ewidencyjny_wniosku).send_keys(
            xpath1_model.numer_ewidencyjny_wniosku)
        time.sleep(1)
    if xpath1_model.numer_ewidencyjny_decyzji != "":
        wait_for_element(driver, x_path_vals.numer_ewidencyjny_decyzji, 10)
        driver.find_element(By.XPATH, x_path_vals.numer_ewidencyjny_decyzji).send_keys(
            xpath1_model.numer_ewidencyjny_decyzji)
        time.sleep(1)
    if xpath1_model.data_zlozenia_wniosku_od != "":
        wait_for_element(driver, x_path_vals.data_zlozenia_wniosku_od, 10)
        driver.find_element(By.XPATH, x_path_vals.data_zlozenia_wniosku_od).send_keys(
            xpath1_model.data_zlozenia_wniosku_od)
        time.sleep(1)
    if xpath1_model.data_zlozenia_wniosku_do != "":
        wait_for_element(driver, x_path_vals.data_zlozenia_wniosku_do, 10)
        driver.find_element(By.XPATH, x_path_vals.data_zlozenia_wniosku_do).send_keys(
            xpath1_model.data_zlozenia_wniosku_do)
        time.sleep(1)
    if xpath1_model.data_wydania_decyzji_od != "":
        wait_for_element(driver, x_path_vals.data_wydania_decyzji_od, 10)
        driver.find_element(By.XPATH, x_path_vals.data_wydania_decyzji_od).send_keys(
            xpath1_model.data_wydania_decyzji_od)
        time.sleep(1)
    if xpath1_model.data_wydania_decyzji_do != "":
        wait_for_element(driver, x_path_vals.data_wydania_decyzji_do, 10)
        driver.find_element(By.XPATH, x_path_vals.data_wydania_decyzji_do).send_keys(
            xpath1_model.data_wydania_decyzji_do)
        time.sleep(1)
    if xpath1_model.wojewodztwo_1 != "":
        wait_for_element(driver, x_path_vals.wojewodztwo_1, 10)
        my_select = Select(driver.find_element(By.XPATH, x_path_vals.wojewodztwo_1))
        my_select.select_by_index(data_model.wojewodztwo[xpath1_model.wojewodztwo_1])
        time.sleep(1)
    if xpath1_model.organ_administracji != "":
        wait_for_element(driver, x_path_vals.organ_administracji, 10)
        driver.find_element(By.XPATH, x_path_vals.organ_administracji).send_keys(xpath1_model.organ_administracji)
        time.sleep(1)
    if xpath1_model.wojewodztwo_2 != "":
        wait_for_element(driver, x_path_vals.wojewodztwo_2, 10)
        my_select = Select(driver.find_element(By.XPATH, x_path_vals.wojewodztwo_2))
        my_select.select_by_index(data_model.wojewodztwo[xpath1_model.wojewodztwo_2])
        time.sleep(1)
    if xpath1_model.miejscowosc != "":
        wait_for_element(driver, x_path_vals.miejscowosc, 10)
        driver.find_element(By.XPATH, x_path_vals.miejscowosc).send_keys(xpath1_model.miejscowosc)
        time.sleep(1)
    if xpath1_model.ulica != "":
        wait_for_element(driver, x_path_vals.ulica, 10)
        driver.find_element(By.XPATH, x_path_vals.ulica).send_keys(xpath1_model.ulica)
        time.sleep(1)
    if xpath1_model.numer_domu != "":
        wait_for_element(driver, x_path_vals.numer_domu, 10)
        driver.find_element(By.XPATH, x_path_vals.numer_domu).send_keys(xpath1_model.numer_domu)
        time.sleep(1)
    if xpath1_model.nr_dzialki_ew != "":
        wait_for_element(driver, x_path_vals.nr_dzialki_ew, 10)
        driver.find_element(By.XPATH, x_path_vals.nr_dzialki_ew).send_keys(xpath1_model.nr_dzialki_ew)
        time.sleep(1)
    if xpath1_model.obreb_ew != "":
        wait_for_element(driver, x_path_vals.obreb_ew, 10)
        driver.find_element(By.XPATH, x_path_vals.obreb_ew).send_keys(xpath1_model.obreb_ew)
        time.sleep(1)
    if xpath1_model.arkusz_mapy != "":
        wait_for_element(driver, x_path_vals.arkusz_mapy, 10)
        driver.find_element(By.XPATH, x_path_vals.arkusz_mapy).send_keys(xpath1_model.arkusz_mapy)
        time.sleep(1)
    if xpath1_model.rodzaj_zamierzenia_budowlanego != "":
        wait_for_element(driver, x_path_vals.rodzaj_zamierzenia_budowlanego, 10)
        my_select = Select(driver.find_element(By.XPATH, x_path_vals.rodzaj_zamierzenia_budowlanego))
        my_select.select_by_index(
            data_model.rodzaj_zamierzenia_budowlanego[xpath1_model.rodzaj_zamierzenia_budowlanego])
        time.sleep(1)
    if xpath1_model.kategoria_obiektu != "":
        wait_for_element(driver, x_path_vals.kategoria_obiektu, 10)
        my_select = Select(driver.find_element(By.XPATH, x_path_vals.kategoria_obiektu))
        my_select.select_by_index(data_model.kategoria_obiektu[xpath1_model.kategoria_obiektu])
        time.sleep(1)
    if xpath1_model.nazwa_zamierzenia != "":
        wait_for_element(driver, x_path_vals.nazwa_zamierzenia, 10)
        driver.find_element(By.XPATH, x_path_vals.nazwa_zamierzenia).send_keys(xpath1_model.nazwa_zamierzenia)
        time.sleep(1)

    wait_for_element(driver, x_path_vals.captcha_img_src, 10)
    path = os.path.join(data_model.screenshot_location, "captcha_screen.png")
    driver.find_element(By.XPATH, x_path_vals.captcha_img_src).screenshot(path)
    reader = easyocr.Reader(['en'])
    result = reader.readtext(path)[0]
    wait_for_element(driver, x_path_vals.captcha_img_inp, 10)
    driver.find_element(By.XPATH, x_path_vals.captcha_img_inp).send_keys(result[1])
    time.sleep(1)
    wait_for_element(driver, x_path_vals.search, 10)
    driver.find_element(By.XPATH, x_path_vals.search).click()
    time.sleep(1)




def get_documents_links(driver: WebDriver, data_model: DataModel):
    url = driver.current_url
    result = []
    for page_number in range(1, 11):
        url += f"&page={1}"
        driver.get(url)
        for row_num in range(1,11):
            try:
                model2 = XPathModel2(row_num)
                model2.url = driver.find_element(By.XPATH, model2.url).text
                model2.data_wplywu = driver.find_element(By.XPATH, model2.data_wplywu).text
                model2.inwestor = driver.find_element(By.XPATH, model2.inwestor).text
                model2.nazwa_zamieszkania = driver.find_element(By.XPATH, model2.nazwa_zamieszkania).text
                model2.stan_prawny = driver.find_element(By.XPATH, model2.stan_prawny).text
                model2.data_wydania_decyzji = driver.find_element(By.XPATH, model2.data_wydania_decyzji).text
                result.append(model2)
            except:
                return result
    return result
    a = 0


def main():
    model = DataModel()

    driver = get_init_driver()
    driver.get(model.xpath_model_1.url)
    time.sleep(5)
    insert_requested_values(driver, model)
    get_documents_links(driver, model)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    total_s = end_time - start_time
    total_m = int(total_s / 60)
    total_s = int(total_s - total_m * 60)
    print(f"")
    print(f"#####################################")
    print(f"Total time: {total_m}m {total_s}s")
    print(f"#####################################")
