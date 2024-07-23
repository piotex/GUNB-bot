from dataclasses import dataclass


@dataclass
class XPathModel3:
    szczegoly_wniosku_nr: str = "-"
    stan_prawny: str = "Stan prawny"
    #INFORMACJE DOTYCZĄCE OBIEKTU BUDOWLANEGO
    wojewodztwo: str = "Województwo"
    kod_pocztowy: str = "Kod pocztowy"
    poczta: str = "Poczta"
    miejscowosc: str = "Miejscowość"
    ulica: str = "Ulica"
    numer_domu: str = "Numer domu"
    numer_lokalu: str = "Numer lokalu"
    #INFORMACJE DOTYCZĄCE DZIAŁKI BUDOWLANEJ
    nr_dzialki_ew: str = "Nr działki ew."
    obreb_ew: str = "Obręb ew."
    jednostka_ew: str = "Jednostka ew."
    #INFORMACJE DOTYCZĄCE ZAMIERZENIA BUDOWLANEGO
    rodzaj_obiektu: str = "Rodzaj obiektu"
    kategoria_obiektu: str = "Kategoria obiektu"
    kubatura_budynku: str = "Kubatura budynku"
    nazwa_zamierzenia_budowlanego: str = "Nazwa zamierzenia budowlanego"
    rodzaj_zamierzenia_budowlanego: str = "Rodzaj zamierzenia budowlanego"
    #DANE INWESTORA
    nazwisko_inwestora: str = "Nazwisko"
    imie_inwestora: str = "Imię"
    #DANE DOTYCZĄCE PROJEKTANTA
    nazwisko_pojektanta: str = "Nazwisko"
    imie_pojektanta: str = "Imię"
    numer_uprawnien_budowlanych_pojektanta: str = "Numer uprawnień budowlanych"
    pozostali_projektanci_pojektanta: str = "Pozostali projektanci"
    #NAZWA I ADRES ORGANU ADMINISTRACJI ARCHITEKTOWNICZNO-BUDOWLANEJ
    nazwa_organu: str = "Nazwa organu"
    adres_organu: str = "Adres organu"
    #NUMERY EWIDENCYJNE WNIOSKU, DATA WPŁYWU I REJESTRACJI
    numer_ewidencyjny_wniosku_nadawany_w_urzedzie: str = "Numer ewidencyjny wniosku nadawany w urzędzie"
    data_wplywu_wniosku_do_urzedu: str = "Data wpływu wniosku do urzędu"
    data_rejestracji_w_systemie_komputerowym: str = "Data rejestracji w systemie komputerowym"
    #NUMER I DATA WYDANIA DECYZJI
    numer_ewidencyjny_decyzji_nadawany_w_urzedzie: str = "Numer ewidencyjny decyzji nadawany w urzędzie"
    data_wydania_decyzji: str = "Data wydania decyzji"
    decyzja: str = "Decyzja"
    #BRAKI FORMALNE WNIOSKU
    czy_inwestor_byl_wezwany_do_uzupelnienia_brakow_formalnych: str = "Czy inwestor był wezwany do uzupełnienia braków formalnych (art. 64 § 2 kpa)"
    data_wyslania_wezwania_do_uzupelnienia_brakow_formalnych: str = "Data wysłania wezwania do uzupełnienia braków formalnych"
    data_uzupelnienia_brakow_formalnych: str = "Data uzupełnienia braków formalnych"
    #WYCOFANIE WNIOSKU, PRZEKAZANIE ZGODNIE Z WŁAŚCIWOŚCIĄ, POZOSTAWIENIE BEZ ROZPOZNANIA
    wniosek_wycofany_przez_inwestora: str = "Wniosek wycofany przez inwestora"
    data_wycofania_wniosku: str = "Data wycofania wniosku"
    wniosek_bez_rozpoznania: str = "Wniosek bez rozpoznania"
    wniosek_przekazany_zgodnie_z_wlasciwoscia: str = "Wniosek przekazany zgodnie z właściwością"
    #UZUPEŁNIENIE DOKUMENTACJI (art. 35 ust. 3 Prawa budowlanego)
    czy_inwestor_byl_wezwany_do_uzupelnienia_dokumentacji: str = "Czy inwestor był wezwany do uzupełnienia dokumentacji"
    data_wyslania_postanowienia: str = "Data wysłania postanowienia"
    data_otrzymania_uzupelnienia_dokumentacji_uplyw_terminu_na_uzupelnienie: str = "Data otrzymania uzupełnienia dokumentacji/upływ terminu na uzupełnienie"
    liczba_dni: str = "Liczba dni"
    #UZGODNIENIA Z KONSERWATOREM ZABYTKÓW
    czy_wniosek_wymagal_uzgodnien_z_wojewodzkim_konserwatorem_zabytkow: str = "Czy wniosek wymagał uzgodnień z wojewódzkim konserwatorem zabytków"
    data_wyslania_dokumentow_do_konserwatora: str = "Data wysłania dokumentów do konserwatora"
    data_otrzymania_uzgodnien_z_konserwatorem: str = "Data otrzymania uzgodnień z konserwatorem"
    #ZAWIESZENIE POSTĘPOWANIA
    zawieszenie_postepowania: str = "Zawieszenie postępowania"
    data_zawieszenia_postepowania: str = "Data zawieszenia postępowania"
    data_podjecia_postepowania: str = "Data podjęcia postępowania"
    #INNE PRZYCZYNY WYDŁUŻENIA TERMINU WYDANIA DECYZJI
    czy_zaistnialy_inne_przyczyny_wydluzenia_ustawowego_czasu_wydania_decyzji: str = "Czy zaistniały inne przyczyny wydłużenia ustawowego czasu wydania decyzji"
    #POŁOŻENIE NA MAPIE
    polozenie_na_mapie: str = "/html/body/div/div[2]/div/div[2]/div[48]/div[1]/div[3]/div/div[1]/div[2]"



    # szczegoly_wniosku_nr: str = "/html/body/div/div[2]/div/div[1]/h2/small/b"  #
    # stan_prawny: str = "/html/body/div/div[2]/div/div[2]/div[1]/div[2]/p/b"  #
    # #INFORMACJE DOTYCZĄCE OBIEKTU BUDOWLANEGO
    # wojewodztwo: str = "/html/body/div/div[2]/div/div[2]/div[2]/div[2]/p/b"  #
    # kod_pocztowy: str = "/html/body/div/div[2]/div/div[2]/div[3]/div[2]/p/b"  #
    # poczta: str = "/html/body/div/div[2]/div/div[2]/div[4]/div[2]/p/b"  #
    # miejscowosc: str = "/html/body/div/div[2]/div/div[2]/div[5]/div[2]/p/b"  #
    # ulica: str = "/html/body/div/div[2]/div/div[2]/div[6]/div[2]/p/b"  #
    # numer_domu: str = "/html/body/div/div[2]/div/div[2]/div[7]/div[2]/p/b"  #
    # numer_lokalu: str = "/html/body/div/div[2]/div/div[2]/div[8]/div[2]/p/b"  #
    # #INFORMACJE DOTYCZĄCE DZIAŁKI BUDOWLANEJ
    # nr_dzialki_ew: str = "/html/body/div/div[2]/div/div[2]/div[9]/div[2]/p"  #
    # obreb_ew: str = "/html/body/div/div[2]/div/div[2]/div[10]/div[2]/p"  #
    # jednostka_ew: str = "/html/body/div/div[2]/div/div[2]/div[11]/div[2]/p"  #
    # #INFORMACJE DOTYCZĄCE ZAMIERZENIA BUDOWLANEGO
    # rodzaj_obiektu: str = "/html/body/div/div[2]/div/div[2]/div[12]/div[2]/p"  #
    # kategoria_obiektu: str = "/html/body/div/div[2]/div/div[2]/div[13]/div[2]/p"
    # kubatura_budynku: str = "/html/body/div/div[2]/div/div[2]/div[14]/div[2]/p"
    # nazwa_zamierzenia_budowlanego: str = "/html/body/div/div[2]/div/div[2]/div[15]/div[2]/p/b"
    # rodzaj_zamierzenia_budowlanego: str = "/html/body/div/div[2]/div/div[2]/div[16]/div[2]/p"
    # #DANE INWESTORA
    # nazwisko_inwestora: str = "/html/body/div/div[2]/div/div[2]/div[17]/div[2]/p/b"
    # imie_inwestora: str = "/html/body/div/div[2]/div/div[2]/div[18]/div[2]/p/b"
    # #DANE DOTYCZĄCE PROJEKTANTA
    # nazwisko_pojektanta: str = "/html/body/div/div[2]/div/div[2]/div[19]/div[2]/p"
    # imie_pojektanta: str = "/html/body/div/div[2]/div/div[2]/div[20]/div[2]/p"
    # numer_uprawnien_budowlanych_pojektanta: str = "/html/body/div/div[2]/div/div[2]/div[21]/div[2]/p"
    # pozostali_projektanci_pojektanta: str = "/html/body/div/div[2]/div/div[2]/div[22]/div[2]/p"
    # #NAZWA I ADRES ORGANU ADMINISTRACJI ARCHITEKTOWNICZNO-BUDOWLANEJ
    # nazwa_organu: str = "/html/body/div/div[2]/div/div[2]/div[23]/div[2]/p/b"
    # adres_organu: str = "/html/body/div/div[2]/div/div[2]/div[24]/div[2]/p/b"
    # #NUMERY EWIDENCYJNE WNIOSKU, DATA WPŁYWU I REJESTRACJI
    # numer_ewidencyjny_wniosku_nadawany_w_urzedzie: str = "/html/body/div/div[2]/div/div[2]/div[25]/div[2]/p/b"
    # data_wplywu_wniosku_do_urzedu: str = "/html/body/div/div[2]/div/div[2]/div[26]/div[2]/p"
    # data_rejestracji_w_systemie_komputerowym: str = "/html/body/div/div[2]/div/div[2]/div[27]/div[2]/p"
    # #NUMER I DATA WYDANIA DECYZJI
    # numer_ewidencyjny_decyzji_nadawany_w_urzedzie: str = "/html/body/div/div[2]/div/div[2]/div[28]/div[2]/p/b"
    # data_wydania_decyzji: str = "/html/body/div/div[2]/div/div[2]/div[29]/div[2]/p"
    # decyzja: str = "/html/body/div/div[2]/div/div[2]/div[30]/div[2]/p[2]/b"
    # #BRAKI FORMALNE WNIOSKU
    # czy_inwestor_byl_wezwany_do_uzupelnienia_brakow_formalnych: str = "/html/body/div/div[2]/div/div[2]/div[31]/div[2]/p"
    # data_wyslania_wezwania_do_uzupelnienia_brakow_formalnych: str = "/html/body/div/div[2]/div/div[2]/div[32]/div[2]/p"
    # data_uzupelnienia_brakow_formalnych: str = "/html/body/div/div[2]/div/div[2]/div[33]/div[2]/p"
    # #WYCOFANIE WNIOSKU, PRZEKAZANIE ZGODNIE Z WŁAŚCIWOŚCIĄ, POZOSTAWIENIE BEZ ROZPOZNANIA
    # wniosek_wycofany_przez_inwestora: str = "/html/body/div/div[2]/div/div[2]/div[34]/div[2]/p"
    # data_wycofania_wniosku: str = "/html/body/div/div[2]/div/div[2]/div[35]/div[2]/p"
    # wniosek_bez_rozpoznania: str = "/html/body/div/div[2]/div/div[2]/div[36]/div[2]/p"
    # wniosek_przekazany_zgodnie_z_wlasciwoscia: str = "/html/body/div/div[2]/div/div[2]/div[37]/div[2]/p"
    # #UZUPEŁNIENIE DOKUMENTACJI (art. 35 ust. 3 Prawa budowlanego)
    # czy_inwestor_byl_wezwany_do_uzupelnienia_dokumentacji: str = "/html/body/div/div[2]/div/div[2]/div[38]/div[2]/p"
    # data_wyslania_postanowienia: str = "/html/body/div/div[2]/div/div[2]/div[39]/div[2]/p"
    # data_otrzymania_uzupelnienia_dokumentacji_uplyw_terminu_na_uzupelnienie: str = "/html/body/div/div[2]/div/div[2]/div[40]/div[2]/p"
    # liczba_dni: str = "/html/body/div/div[2]/div/div[2]/div[41]/div[2]/p"
    # #UZGODNIENIA Z KONSERWATOREM ZABYTKÓW
    # czy_wniosek_wymagal_uzgodnien_z_wojewodzkim_konserwatorem_zabytkow: str = "/html/body/div/div[2]/div/div[2]/div[41]/div[2]/p"
    # data_wyslania_dokumentow_do_konserwatora: str = "/html/body/div/div[2]/div/div[2]/div[42]/div[2]/p"
    # data_otrzymania_uzgodnien_z_konserwatorem: str = "/html/body/div/div[2]/div/div[2]/div[43]/div[2]/p"
    # #ZAWIESZENIE POSTĘPOWANIA
    # zawieszenie_postepowania: str = "/html/body/div/div[2]/div/div[2]/div[44]/div[2]/p"
    # data_zawieszenia_postepowania: str = "/html/body/div/div[2]/div/div[2]/div[45]/div[2]/p"
    # data_podjecia_postepowania: str = "/html/body/div/div[2]/div/div[2]/div[46]/div[2]/p"
    # #INNE PRZYCZYNY WYDŁUŻENIA TERMINU WYDANIA DECYZJI
    # czy_zaistnialy_inne_przyczyny_wydluzenia_ustawowego_czasu_wydania_decyzji: str = "/html/body/div/div[2]/div/div[2]/div[47]/div[2]/p"
    # #POŁOŻENIE NA MAPIE
    # polozenie_na_mapie: str = "/html/body/div/div[2]/div/div[2]/div[48]/div[1]/div[3]/div/div[1]/div[2]"