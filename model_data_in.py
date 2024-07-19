import json
from datetime import datetime
from dataclasses import dataclass, field
from typing import List

@dataclass
class InXPathModel_1:
    rodzaj_wyszukiwania: str = "/html/body/div/div[2]/div/form/div[1]/div[1]/label/input"
    typ_dokumentu: str = "/html/body/div/div[2]/div/form/div[3]/div/select/option[1]" #/html/body/div/div[2]/div/form/div[3]/div/select/option[7] # od 1 do 7
    numer_ewidencyjny_wniosku: str = "/html/body/div/div[2]/div/form/div[5]/div/input"
    numer_ewidencyjny_decyzji: str = "/html/body/div/div[2]/div/form/div[7]/div/input"
    data_zlozenia_wniosku_od: str = "/html/body/div/div[2]/div/form/div[8]/div/input[1]"   # RRRR-MM-DD
    data_zlozenia_wniosku_do: str = "/html/body/div/div[2]/div/form/div[8]/div/input[2]"   # RRRR-MM-DD
    data_wydania_decyzji_od: str = "/html/body/div/div[2]/div/form/div[9]/div/input[1]"
    data_wydania_decyzji_do: str = "/html/body/div/div[2]/div/form/div[9]/div/input[2]"
    wojewodztwo_1: str = "/html/body/div/div[2]/div/form/div[11]/div/select/option[1]" #/html/body/div/div[2]/div/form/div[11]/div/select/option[17]
    organ_administracji: str = "/html/body/div/div[2]/div/form/div[12]/div/select/option[1]" #/html/body/div/div[2]/div/form/div[12]/div/select/option[446]
    wojewodztwo_2: str = "/html/body/div/div[2]/div/form/div[14]/div/select/option[1]" #/html/body/div/div[2]/div/form/div[14]/div/select/option[18]
    miejscowosc: str = "/html/body/div/div[2]/div/form/div[15]/div/input"
    ulica: str = "/html/body/div/div[2]/div/form/div[16]/div/input"
    numer_domu: str = "/html/body/div/div[2]/div/form/div[17]/div/input"
    nr_dzialki_ew: str = "/html/body/div/div[2]/div/form/div[18]/div/div/input"
    obreb_ew: str = "/html/body/div/div[2]/div/form/div[19]/div[2]/input"
    arkusz_mapy: str = "/html/body/div/div[2]/div/form/div[20]/div/input"
    rodzaj_zamierzenia_budowlanego: str = "/html/body/div/div[2]/div/form/div[22]/div/select/option[1]" #/html/body/div/div[2]/div/form/div[22]/div/select/option[7]
    kategoria_obiektu: str = "/html/body/div/div[2]/div/form/div[23]/div[1]/select/option[1]" #/html/body/div/div[2]/div/form/div[23]/div[1]/select/option[31]
    nazwa_zamierzenia: str = "/html/body/div/div[2]/div/form/div[24]/div/input"
    captcha_img_src: str = "/html/body/div/div[2]/div/form/div[26]/div[1]/img"
    captcha_img_inp: str = "/html/body/div/div[2]/div/form/div[26]/div[1]/input"
    search: str = "/html/body/div/div[2]/div/form/div[27]/button"

@dataclass
class OutXPathModel_1:
    data_wplywu: str = "/html/body/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]"          #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[1]
    inwestor: str = "/html/body/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]"             #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[2]
    nazwa_zamieszkania: str = "/html/body/div/div[2]/div/div[3]/table/tbody/tr[1]/td[3]"   #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[3]
    stan_prawny: str = "/html/body/div/div[2]/div/div[3]/table/tbody/tr[1]/td[4]/span[2]"  #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[4]
    data_wydania_decyzji: str = "/html/body/div/div[2]/div/div[3]/table/tbody/tr[1]/td[5]" #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[5]
    url: str = "/html/body/div/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/a"                #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[6]/a




#https://wyszukiwarka.gunb.gov.pl/wyniki/?document_type=rwd&rwd_document_type=Decyzja+pozytywna&request_number=&decision_number=&date_min=2023-01-01&date_max=2024-07-19&decision_date_min=2024-01-01&decision_date_max=&organ_region=8&org=all&region=8&city=&street=&house_nr=&ew_parcel=&ew_organ=&ew_sheet=&invest_purpose=1&invest=2&intention_name=&page=1
#https://wyszukiwarka.gunb.gov.pl/wyniki/?document_type=rwd&rwd_document_type=Decyzja+pozytywna&request_number=&decision_number=&date_min=2023-01-01&date_max=2024-07-19&decision_date_min=2024-01-01&decision_date_max=&organ_region=8&org=all&region=8&city=&street=&house_nr=&ew_parcel=&ew_organ=&ew_sheet=&invest_purpose=1&invest=2&intention_name=&page=2
#https://wyszukiwarka.gunb.gov.pl/wyniki/?document_type=rwd&rwd_document_type=Decyzja+pozytywna&request_number=&decision_number=&date_min=2023-01-01&date_max=2024-07-19&decision_date_min=2024-01-01&decision_date_max=&organ_region=8&org=all&region=8&city=&street=&house_nr=&ew_parcel=&ew_organ=&ew_sheet=&invest_purpose=1&invest=2&intention_name=&page=9
    # captcha_img_src: str = "/html/body/div/div[2]/div/form/div[1]/div[1]/img"
    # captcha_img_inp: str = "/html/body/div/div[2]/div/form/div[1]/div[1]/input[1]"
    # search: str = "/html/body/div/div[2]/div/form/div[2]/button"

@dataclass
class OutXPathModel_2:
    url: str = ""
    szczegoly_wniosku_nr: str = "/html/body/div/div[2]/div/div[1]/h2/small/b"  #
    stan_prawny: str = "/html/body/div/div[2]/div/div[2]/div[1]/div[2]/p/b"  #
    #INFORMACJE DOTYCZĄCE OBIEKTU BUDOWLANEGO
    wojewodztwo: str = "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/p/b"  #
    kod_pocztowy: str = "/html/body/div/div[2]/div/div[2]/div[3]/div[2]/p/b"  #
    poczta: str = "/html/body/div/div[2]/div/div[2]/div[4]/div[2]/p/b"  #
    miejscowosc: str = "/html/body/div/div[2]/div/div[2]/div[5]/div[2]/p/b"  #
    ulica: str = "/html/body/div/div[2]/div/div[2]/div[6]/div[2]/p/b"  #
    numer_domu: str = "/html/body/div/div[2]/div/div[2]/div[7]/div[2]/p/b"  #
    numer_lokalu: str = "/html/body/div/div[2]/div/div[2]/div[8]/div[2]/p/b"  #
    #INFORMACJE DOTYCZĄCE DZIAŁKI BUDOWLANEJ
    nr_dzialki_ew: str = "/html/body/div/div[2]/div/div[2]/div[9]/div[2]/p"  #
    obreb_ew: str = "/html/body/div/div[2]/div/div[2]/div[10]/div[2]/p"  #
    jednostka_ew: str = "/html/body/div/div[2]/div/div[2]/div[11]/div[2]/p"  #
    #INFORMACJE DOTYCZĄCE ZAMIERZENIA BUDOWLANEGO
    rodzaj_obiektu: str = "/html/body/div/div[2]/div/div[2]/div[12]/div[2]/p"  #
    kategoria_obiektu: str = "/html/body/div/div[2]/div/div[2]/div[13]/div[2]/p"
    kubatura_budynku: str = "/html/body/div/div[2]/div/div[2]/div[14]/div[2]/p"
    nazwa_zamierzenia_budowlanego: str = "/html/body/div/div[2]/div/div[2]/div[15]/div[2]/p/b"
    rodzaj_zamierzenia_budowlanego: str = "/html/body/div/div[2]/div/div[2]/div[16]/div[2]/p"
    #DANE INWESTORA
    nazwisko_inwestora: str = "/html/body/div/div[2]/div/div[2]/div[17]/div[2]/p/b"
    imie_inwestora: str = "/html/body/div/div[2]/div/div[2]/div[18]/div[2]/p/b"
    #DANE DOTYCZĄCE PROJEKTANTA
    nazwisko_pojektanta: str = "/html/body/div/div[2]/div/div[2]/div[19]/div[2]/p"
    imie_pojektanta: str = "/html/body/div/div[2]/div/div[2]/div[20]/div[2]/p"
    numer_uprawnien_budowlanych_pojektanta: str = "/html/body/div/div[2]/div/div[2]/div[21]/div[2]/p"
    pozostali_projektanci_pojektanta: str = "/html/body/div/div[2]/div/div[2]/div[22]/div[2]/p"
    #NAZWA I ADRES ORGANU ADMINISTRACJI ARCHITEKTOWNICZNO-BUDOWLANEJ
    nazwa_organu: str = "/html/body/div/div[2]/div/div[2]/div[23]/div[2]/p/b"
    adres_organu: str = "/html/body/div/div[2]/div/div[2]/div[24]/div[2]/p/b"
    #NUMERY EWIDENCYJNE WNIOSKU, DATA WPŁYWU I REJESTRACJI
    numer_ewidencyjny_wniosku_nadawany_w_urzedzie: str = "/html/body/div/div[2]/div/div[2]/div[25]/div[2]/p/b"
    data_wplywu_wniosku_do_urzedu: str = "/html/body/div/div[2]/div/div[2]/div[26]/div[2]/p"
    data_rejestracji_w_systemie_komputerowym: str = "/html/body/div/div[2]/div/div[2]/div[27]/div[2]/p"
    #NUMER I DATA WYDANIA DECYZJI
    numer_ewidencyjny_decyzji_nadawany_w_urzedzie: str = "/html/body/div/div[2]/div/div[2]/div[28]/div[2]/p/b"
    data_wydania_decyzji: str = "/html/body/div/div[2]/div/div[2]/div[29]/div[2]/p"
    decyzja: str = "/html/body/div/div[2]/div/div[2]/div[30]/div[2]/p[2]/b"
    #BRAKI FORMALNE WNIOSKU
    czy_inwestor_byl_wezwany_do_uzupelnienia_brakow_formalnych: str = "/html/body/div/div[2]/div/div[2]/div[31]/div[2]/p"
    data_wyslania_wezwania_do_uzupelnienia_brakow_formalnych: str = "/html/body/div/div[2]/div/div[2]/div[32]/div[2]/p"
    data_uzupelnienia_brakow_formalnych: str = "/html/body/div/div[2]/div/div[2]/div[33]/div[2]/p"
    #WYCOFANIE WNIOSKU, PRZEKAZANIE ZGODNIE Z WŁAŚCIWOŚCIĄ, POZOSTAWIENIE BEZ ROZPOZNANIA
    wniosek_wycofany_przez_inwestora: str = "/html/body/div/div[2]/div/div[2]/div[34]/div[2]/p"
    data_wycofania_wniosku: str = "/html/body/div/div[2]/div/div[2]/div[35]/div[2]/p"
    wniosek_bez_rozpoznania: str = "/html/body/div/div[2]/div/div[2]/div[36]/div[2]/p"
    wniosek_przekazany_zgodnie_z_wlasciwoscia: str = "/html/body/div/div[2]/div/div[2]/div[37]/div[2]/p"
    #UZUPEŁNIENIE DOKUMENTACJI (art. 35 ust. 3 Prawa budowlanego)
    Czy_inwestor_byl_wezwany_do_uzupelnienia_dokumentacji: str = "/html/body/div/div[2]/div/div[2]/div[38]/div[2]/p"
    Data_wyslania_postanowienia: str = "/html/body/div/div[2]/div/div[2]/div[39]/div[2]/p"
    Data_otrzymania_uzupelnienia_dokumentacji_uplyw_terminu_na_uzupelnienie: str = "/html/body/div/div[2]/div/div[2]/div[40]/div[2]/p"
    #UZGODNIENIA Z KONSERWATOREM ZABYTKÓW
    Czy_wniosek_wymagal_uzgodnien_z_wojewodzkim_konserwatorem_zabytkow: str = "/html/body/div/div[2]/div/div[2]/div[41]/div[2]/p"
    Data_wyslania_dokumentow_do_konserwatora: str = "/html/body/div/div[2]/div/div[2]/div[42]/div[2]/p"
    Data_otrzymania_uzgodnien_z_konserwatorem: str = "/html/body/div/div[2]/div/div[2]/div[43]/div[2]/p"
    #ZAWIESZENIE POSTĘPOWANIA
    Zawieszenie_postepowania: str = "/html/body/div/div[2]/div/div[2]/div[44]/div[2]/p"
    Data_zawieszenia_postepowania: str = "/html/body/div/div[2]/div/div[2]/div[45]/div[2]/p"
    Data_podjecia_postepowania: str = "/html/body/div/div[2]/div/div[2]/div[46]/div[2]/p"
    #INNE PRZYCZYNY WYDŁUŻENIA TERMINU WYDANIA DECYZJI
    Czy_zaistnialy_inne_przyczyny_wydluzenia_ustawowego_czasu_wydania_decyzji: str = "/html/body/div/div[2]/div/div[2]/div[47]/div[2]/p"
    #POŁOŻENIE NA MAPIE
    polozenie_na_mapie: str = "/html/body/div/div[2]/div/div[2]/div[48]/div[1]/div[3]/div/div[1]/div[2]"

@dataclass
class DataModel:
    url_start: str = "https://wyszukiwarka.gunb.gov.pl/"
    screenshot_location: str = r"C:\Users\pkubo\Pictures\Screenshots"
    data_files_location: str = r"C:\devops_sandbox\git\GUNB-bot"



obj_list_path = "data/obj_list.json"
obj_path = "data/obj.json"


def load_list_OutXPathModel_1() -> list[OutXPathModel_1]:
    with open(obj_list_path, "r", encoding="utf-8") as f:
        list_of_users = json.load(f)
        list_of_users = [OutXPathModel_1(**item) for item in list_of_users]
        for a in list_of_users:
            a.creation_date = datetime.strptime(str(a.creation_date), "%Y-%m-%d %H:%M:%S")
            a.actualization_date = datetime.strptime(str(a.actualization_date), "%Y-%m-%d %H:%M:%S")
    return list_of_users


def load_OutXPathModel_1() -> OutXPathModel_1:
    with open(obj_path, "r", encoding="utf-8") as f:
        item = json.load(f)
        model = OutXPathModel_1(**item)
        model.creation_date = datetime.strptime(str(model.creation_date), "%Y-%m-%d %H:%M:%S")
        model.actualization_date = datetime.strptime(str(model.actualization_date), "%Y-%m-%d %H:%M:%S")
    return model


def save_list_OutXPathModel_1(news_list: list[OutXPathModel_1]):
    with open(obj_list_path, "w", encoding="utf-8") as f:
        json.dump([item.__dict__ for item in news_list], f, indent=4, default=str)


def save_OutXPathModel_1(news: OutXPathModel_1):
    with open(obj_path, "w", encoding="utf-8") as f:
        json.dump(news.__dict__, f, indent=4, default=str)




def load_list_OutXPathModel_2() -> list[OutXPathModel_2]:
    with open(obj_list_path, "r", encoding="utf-8") as f:
        list_of_users = json.load(f)
        list_of_users = [OutXPathModel_2(**item) for item in list_of_users]
        for a in list_of_users:
            a.creation_date = datetime.strptime(str(a.creation_date), "%Y-%m-%d %H:%M:%S")
            a.actualization_date = datetime.strptime(str(a.actualization_date), "%Y-%m-%d %H:%M:%S")
    return list_of_users


def load_OutXPathModel_2() -> OutXPathModel_2:
    with open(obj_path, "r", encoding="utf-8") as f:
        item = json.load(f)
        model = OutXPathModel_2(**item)
        model.creation_date = datetime.strptime(str(model.creation_date), "%Y-%m-%d %H:%M:%S")
        model.actualization_date = datetime.strptime(str(model.actualization_date), "%Y-%m-%d %H:%M:%S")
    return model


def save_list_OutXPathModel_2(news_list: list[OutXPathModel_2]):
    with open(obj_list_path, "w", encoding="utf-8") as f:
        json.dump([item.__dict__ for item in news_list], f, indent=4, default=str)


def save_OutXPathModel_2(news: OutXPathModel_2):
    with open(obj_path, "w", encoding="utf-8") as f:
        json.dump(news.__dict__, f, indent=4, default=str)
