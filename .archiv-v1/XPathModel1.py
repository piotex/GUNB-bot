from dataclasses import dataclass

@dataclass
class XPathModel1:
    url: str = "https://wyszukiwarka.gunb.gov.pl/"
    rodzaj_wyszukiwania: str = "/html/body/div/div[2]/div/form/div[1]/div[1]/label/input"     #   /html/body/div/div[2]/div/form/div[1]/div[2]/label/input
    typ_dokumentu: str = "/html/body/div/div[2]/div/form/div[3]/div/select" #/html/body/div/div[2]/div/form/div[3]/div/select/option[7] # od 1 do 7
    numer_ewidencyjny_wniosku: str = "/html/body/div/div[2]/div/form/div[5]/div/input"
    numer_ewidencyjny_decyzji: str = "/html/body/div/div[2]/div/form/div[7]/div/input"
    data_zlozenia_wniosku_od: str = "/html/body/div/div[2]/div/form/div[8]/div/input[1]"   # RRRR-MM-DD
    data_zlozenia_wniosku_do: str = "/html/body/div/div[2]/div/form/div[8]/div/input[2]"   # RRRR-MM-DD
    data_wydania_decyzji_od: str = "/html/body/div/div[2]/div/form/div[9]/div/input[1]"
    data_wydania_decyzji_do: str = "/html/body/div/div[2]/div/form/div[9]/div/input[2]"
    wojewodztwo_1: str = "/html/body/div/div[2]/div/form/div[11]/div/select" #/html/body/div/div[2]/div/form/div[11]/div/select/option[17]
    organ_administracji: str = "/html/body/div/div[2]/div/form/div[12]/div/select" #/html/body/div/div[2]/div/form/div[12]/div/select/option[446]
    wojewodztwo_2: str = "/html/body/div/div[2]/div/form/div[14]/div/select" #/html/body/div/div[2]/div/form/div[14]/div/select/option[18]
    miejscowosc: str = "/html/body/div/div[2]/div/form/div[15]/div/input"
    ulica: str = "/html/body/div/div[2]/div/form/div[16]/div/input"
    numer_domu: str = "/html/body/div/div[2]/div/form/div[17]/div/input"
    nr_dzialki_ew: str = "/html/body/div/div[2]/div/form/div[18]/div/div/input"
    obreb_ew: str = "/html/body/div/div[2]/div/form/div[19]/div[2]/input"
    arkusz_mapy: str = "/html/body/div/div[2]/div/form/div[20]/div/input"
    rodzaj_zamierzenia_budowlanego: str = "/html/body/div/div[2]/div/form/div[22]/div/select" #/html/body/div/div[2]/div/form/div[22]/div/select/option[7]
    kategoria_obiektu: str = "/html/body/div/div[2]/div/form/div[23]/div[1]/select" #/html/body/div/div[2]/div/form/div[23]/div[1]/select/option[31]
    nazwa_zamierzenia: str = "/html/body/div/div[2]/div/form/div[24]/div/input"
    captcha_img_src: str = "/html/body/div/div[2]/div/form/div[26]/div[1]/img"
    captcha_img_inp: str = "/html/body/div/div[2]/div/form/div[26]/div[1]/input"
    search: str = "/html/body/div/div[2]/div/form/div[27]/button"

    def __init__(self):
        pass