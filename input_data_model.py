from dataclasses import dataclass


@dataclass
class InputDataModel:
    # url: str = "https://wyszukiwarka.gunb.gov.pl/"
    rodzaj_wyszukiwania: str = "Rodzaj wyszukiwania"                            # "/html/body/div/div[2]/div/form/div[1]/div[1]/label/input"  #   /html/body/div/div[2]/div/form/div[1]/div[2]/label/input
    typ_dokumentu: str = "Typ dokumentu (Rejestr Wniosków i Decyzji)"           # "/html/body/div/div[2]/div/form/div[3]/div/select"  #/html/body/div/div[2]/div/form/div[3]/div/select/option[7] # od 1 do 7
    numer_ewidencyjny_wniosku: str = "Numer ewidencyjny wniosku"                # "/html/body/div/div[2]/div/form/div[5]/div/input"
    numer_ewidencyjny_decyzji: str = "Numer ewidencyjny decyzji"                # "/html/body/div/div[2]/div/form/div[7]/div/input"
    data_zlozenia_wniosku_od: str = "Data złożenia\nwniosku / zgłoszenia"   # "/html/body/div/div[2]/div/form/div[8]/div/input[1]"  # RRRR-MM-DD
    data_zlozenia_wniosku_do: str = "Data złożenia wniosku / zgłoszenia (do)"   # "/html/body/div/div[2]/div/form/div[8]/div/input[2]"  # RRRR-MM-DD
    data_wydania_decyzji_od: str = "Data wydania decyzji"                  # "/html/body/div/div[2]/div/form/div[9]/div/input[1]"
    data_wydania_decyzji_do: str = "Data wydania decyzji (do)"                  # "/html/body/div/div[2]/div/form/div[9]/div/input[2]"
    wojewodztwo_1: str = "Województwo"                                          # "/html/body/div/div[2]/div/form/div[11]/div/select"           #/html/body/div/div[2]/div/form/div[11]/div/select/option[17]
    organ_administracji: str = "Organ administracji"                            # "/html/body/div/div[2]/div/form/div[12]/div/select"  #/html/body/div/div[2]/div/form/div[12]/div/select/option[446]
    wojewodztwo_2: str = "Województwo"                                          # "/html/body/div/div[2]/div/form/div[14]/div/select"  #/html/body/div/div[2]/div/form/div[14]/div/select/option[18]
    miejscowosc: str = "Miejscowość"                                            # "/html/body/div/div[2]/div/form/div[15]/div/input"
    ulica: str = "Ulica"                                                        # "/html/body/div/div[2]/div/form/div[16]/div/input"
    numer_domu: str = "Numer domu"                                              # "/html/body/div/div[2]/div/form/div[17]/div/input"
    nr_dzialki_ew: str = "Nr działki ew."                                       # "/html/body/div/div[2]/div/form/div[18]/div/div/input"
    obreb_ew: str = "Obręb ew."                                                 # "/html/body/div/div[2]/div/form/div[19]/div[2]/input"
    arkusz_mapy: str = "Arkusz mapy"                                            # "/html/body/div/div[2]/div/form/div[20]/div/input"
    rodzaj_zamierzenia_budowlanego: str = "Rodzaj zamierzenia budowlanego"      # "/html/body/div/div[2]/div/form/div[22]/div/select"  #/html/body/div/div[2]/div/form/div[22]/div/select/option[7]
    kategoria_obiektu: str = "Kategoria obiektu"                                # "/html/body/div/div[2]/div/form/div[23]/div[1]/select"  #/html/body/div/div[2]/div/form/div[23]/div[1]/select/option[31]
    nazwa_zamierzenia: str = "Nazwa zamierzenia"                                # "/html/body/div/div[2]/div/form/div[24]/div/input"
    captcha_img_src: str = ""                           # "/html/body/div/div[2]/div/form/div[26]/div[1]/img"
    captcha_img_inp: str = "Wpisz kod znajdujący się na obrazku poniżej:"       # "/html/body/div/div[2]/div/form/div[26]/div[1]/input"
    search: str = ""                                    # "/html/body/div/div[2]/div/form/div[27]/button"

