import os
import easyocr

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from XPathModel1 import XPathModel1
from XPathModel2 import XPathModel2
from XPathModel3 import XPathModel3
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
        my_select.select_by_index(data_model.wojewodztwo_1[xpath1_model.wojewodztwo_1])
        time.sleep(1)
    if xpath1_model.organ_administracji != "":
        wait_for_element(driver, x_path_vals.organ_administracji, 10)
        driver.find_element(By.XPATH, x_path_vals.organ_administracji).send_keys(xpath1_model.organ_administracji)
        time.sleep(1)
    if xpath1_model.wojewodztwo_2 != "":
        wait_for_element(driver, x_path_vals.wojewodztwo_2, 10)
        my_select = Select(driver.find_element(By.XPATH, x_path_vals.wojewodztwo_2))
        my_select.select_by_index(data_model.wojewodztwo_2[xpath1_model.wojewodztwo_2])
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


def solve_captcha_if_visible(driver: WebDriver, data_model: DataModel):
    x_path_caphta = "/html/body/div/div[2]/div/form/div[1]/div[1]/img"
    x_path_input = "/html/body/div/div[2]/div/form/div[1]/div[1]/input[1]"
    x_path_submit = "/html/body/div/div[2]/div/form/div[2]/button"

    for i in range(0,5):
        try:
            driver.find_element(By.XPATH, x_path_caphta)
            driver.find_element(By.XPATH, x_path_input)
            driver.find_element(By.XPATH, x_path_submit)
        except:
            return False

        path = os.path.join(data_model.screenshot_location, "captcha_screen.png")
        driver.find_element(By.XPATH, x_path_caphta).screenshot(path)
        reader = easyocr.Reader(['en'])
        result = reader.readtext(path)[0]
        driver.find_element(By.XPATH, x_path_input).send_keys(result[1])
        time.sleep(1)
        driver.find_element(By.XPATH, x_path_submit).click()
        time.sleep(1)

        solved_successful = True
        try:
            driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/table")
        except:
            solved_successful = False

        if solved_successful:
            return False


def get_documents_links(driver: WebDriver, data_model: DataModel) -> list[XPathModel2]:
    url = driver.current_url
    result = []
    for page_number in range(1, 11):
        driver.get(url + f"&page={page_number}")
        solve_captcha_if_visible(driver, data_model)

        for row_num in range(1, 11):
            try:
                model2 = XPathModel2(row_num)
                model2.url = driver.find_element(By.XPATH, model2.url).get_attribute('href')
                model2.data_wplywu = driver.find_element(By.XPATH, model2.data_wplywu).text
                model2.inwestor = driver.find_element(By.XPATH, model2.inwestor).text
                model2.nazwa_zamieszkania = driver.find_element(By.XPATH, model2.nazwa_zamieszkania).text
                model2.stan_prawny = driver.find_element(By.XPATH, model2.stan_prawny).text
                model2.data_wydania_decyzji = driver.find_element(By.XPATH, model2.data_wydania_decyzji).text
                result.append(model2)
            except:
                return result
    return result
def get_documents_data(driver: WebDriver, url:str, data_model: DataModel) -> XPathModel3:
    driver.get(url)
    solve_captcha_if_visible(driver, data_model)

    model3 = XPathModel3()
    last_i = 0
    for i in range(1,50):
        try:
            x_path_sel = f"/html/body/div/div[2]/div/div[2]/div[{i}]/div[1]"
            x_path_val = f"/html/body/div/div[2]/div/div[2]/div[{i}]/div[2]/p"

            model3.szczegoly_wniosku_nr = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/h2/small/b").text

            if driver.find_element(By.XPATH, x_path_sel).text == model3.stan_prawny:
                model3.stan_prawny = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.wojewodztwo:
                model3.wojewodztwo = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.kod_pocztowy:
                model3.kod_pocztowy = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.poczta:
                model3.poczta = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.miejscowosc:
                model3.miejscowosc = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.ulica:
                model3.ulica = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.numer_domu:
                model3.numer_domu = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.numer_lokalu:
                model3.numer_lokalu = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.nr_dzialki_ew:
                model3.nr_dzialki_ew = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.obreb_ew:
                model3.obreb_ew = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.jednostka_ew:
                model3.jednostka_ew = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.rodzaj_obiektu:
                model3.rodzaj_obiektu = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.kategoria_obiektu:
                model3.kategoria_obiektu = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.kubatura_budynku:
                model3.kubatura_budynku = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.nazwa_zamierzenia_budowlanego:
                model3.nazwa_zamierzenia_budowlanego = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.rodzaj_zamierzenia_budowlanego:
                model3.rodzaj_zamierzenia_budowlanego = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.nazwisko_pojektanta and model3.nazwisko_inwestora != "Nazwisko":
                model3.nazwisko_pojektanta = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.imie_pojektanta and model3.imie_inwestora != "Imię":
                model3.imie_pojektanta = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.nazwisko_inwestora and model3.nazwisko_inwestora == "Nazwisko":
                model3.nazwisko_inwestora = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.imie_inwestora and model3.imie_inwestora == "Imię":
                model3.imie_inwestora = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.numer_uprawnien_budowlanych_pojektanta:
                model3.numer_uprawnien_budowlanych_pojektanta = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.pozostali_projektanci_pojektanta:
                model3.pozostali_projektanci_pojektanta = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.nazwa_organu:
                model3.nazwa_organu = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.adres_organu:
                model3.adres_organu = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.numer_ewidencyjny_wniosku_nadawany_w_urzedzie:
                model3.numer_ewidencyjny_wniosku_nadawany_w_urzedzie = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.data_wplywu_wniosku_do_urzedu:
                model3.data_wplywu_wniosku_do_urzedu = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.data_rejestracji_w_systemie_komputerowym:
                model3.data_rejestracji_w_systemie_komputerowym = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.numer_ewidencyjny_decyzji_nadawany_w_urzedzie:
                model3.numer_ewidencyjny_decyzji_nadawany_w_urzedzie = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.data_wydania_decyzji:
                model3.data_wydania_decyzji = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.decyzja:
                model3.decyzja = driver.find_element(By.XPATH, f"/html/body/div/div[2]/div/div[2]/div[{i}]/div[2]/p[2]/b").text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.czy_inwestor_byl_wezwany_do_uzupelnienia_brakow_formalnych:
                model3.czy_inwestor_byl_wezwany_do_uzupelnienia_brakow_formalnych = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.data_wyslania_wezwania_do_uzupelnienia_brakow_formalnych:
                model3.data_wyslania_wezwania_do_uzupelnienia_brakow_formalnych = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.data_uzupelnienia_brakow_formalnych:
                model3.data_uzupelnienia_brakow_formalnych = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.wniosek_wycofany_przez_inwestora:
                model3.wniosek_wycofany_przez_inwestora = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.data_wycofania_wniosku:
                model3.data_wycofania_wniosku = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.wniosek_bez_rozpoznania:
                model3.wniosek_bez_rozpoznania = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.wniosek_przekazany_zgodnie_z_wlasciwoscia:
                model3.wniosek_przekazany_zgodnie_z_wlasciwoscia = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.czy_inwestor_byl_wezwany_do_uzupelnienia_dokumentacji:
                model3.czy_inwestor_byl_wezwany_do_uzupelnienia_dokumentacji = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.data_wyslania_postanowienia:
                model3.data_wyslania_postanowienia = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.data_otrzymania_uzupelnienia_dokumentacji_uplyw_terminu_na_uzupelnienie:
                model3.data_otrzymania_uzupelnienia_dokumentacji_uplyw_terminu_na_uzupelnienie = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.liczba_dni:
                model3.liczba_dni = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.czy_wniosek_wymagal_uzgodnien_z_wojewodzkim_konserwatorem_zabytkow:
                model3.czy_wniosek_wymagal_uzgodnien_z_wojewodzkim_konserwatorem_zabytkow = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.data_wyslania_dokumentow_do_konserwatora:
                model3.data_wyslania_dokumentow_do_konserwatora = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.data_otrzymania_uzgodnien_z_konserwatorem:
                model3.data_otrzymania_uzgodnien_z_konserwatorem = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.zawieszenie_postepowania:
                model3.zawieszenie_postepowania = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.data_zawieszenia_postepowania:
                model3.data_zawieszenia_postepowania = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.data_podjecia_postepowania:
                model3.data_podjecia_postepowania = driver.find_element(By.XPATH, x_path_val).text
            if driver.find_element(By.XPATH, x_path_sel).text == model3.czy_zaistnialy_inne_przyczyny_wydluzenia_ustawowego_czasu_wydania_decyzji:
                model3.czy_zaistnialy_inne_przyczyny_wydluzenia_ustawowego_czasu_wydania_decyzji = driver.find_element(By.XPATH, x_path_val).text
                last_i = i
        except:
            pass

    try:
        x_path_val = f"/html/body/div/div[2]/div/div[2]/div[{last_i+1}]"
        path = os.path.join(data_model.screenshot_location, f"mapa-{model3.szczegoly_wniosku_nr}.png")
        driver.find_element(By.XPATH, x_path_val).screenshot(path)
        model3.polozenie_na_mapie = path
    except:
        model3.polozenie_na_mapie = "-"

    return model3


def main():
    model = DataModel()
    result = []

    # driver = get_init_driver()
    # # driver.get(model.xpath_model_1.url)
    # # time.sleep(5)
    # # insert_requested_values(driver, model)
    # # list_xpath_model2 = get_documents_links(driver, model)
    # # # model.save_search_result_1(list_xpath_model2)
    # #
    # # for x2_model in list_xpath_model2:
    # url = "https://wyszukiwarka.gunb.gov.pl/wniosek/eabeab1c-606d-4e4b-a67d-214e5b4ed042/"
    # url = "https://wyszukiwarka.gunb.gov.pl/wniosek/823daa0b-69b3-4cb2-afe5-59b6ce441875/"
    # model3 = get_documents_data(driver, url, model)
    # result.append(model3)

    result = [XPathModel3(),XPathModel3(),XPathModel3(),XPathModel3()]
    model.save_search_result_2(result)



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
