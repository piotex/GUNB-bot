from flask import Flask, redirect, url_for, request, render_template
from input_data_model import InputDataModel
from gunb_browser import DataModel
import webbrowser
from threading import Timer

app = Flask(__name__)


@app.route('/search_input')
def search_input():
    model = InputDataModel()
    model.rodzaj_wyszukiwania = ["Wyszukiwanie pozwoleń na budowę",
                                 "(not working) Wyszukiwanie zgłoszeń zamierzenia budowlanego"]
    model.typ_dokumentu = ["Dowolny", "W trakcie rozpatrywania", "Wycofany przez inwestora", "Bez rozpatrzenia",
                           "Decyzja pozytywna", "Decyzja odmowna", "Decyzja umarzająca"]
    # model.typ_dokumentu = ["Dowolny","Sprawa w toku","Brak sprzeciwu","Decyzja o sprzeciwie"]
    model.wojewodztwo = ["Cała Polska", "dolnośląskie", "kujawsko-pomorskie", "łódzkie", "lubelskie", "lubuskie",
                           "małopolskie", "mazowieckie", "opolskie", "podkarpackie", "podlaskie", "pomorskie",
                           "śląskie", "świętokrzyskie", "warmińsko-mazurskie", "wielkopolskie", "zachodniopomorskie"]
    model.organ_administracji = ["Dowolny"]
    model.wojewodztwo_2 = ["Cała Polska", "polski obszar morski", "dolnośląskie", "kujawsko-pomorskie", "łódzkie",
                           "lubelskie", "lubuskie", "małopolskie", "mazowieckie", "opolskie", "podkarpackie",
                           "podlaskie", "pomorskie", "śląskie", "świętokrzyskie", "warmińsko-mazurskie",
                           "wielkopolskie", "zachodniopomorskie"]
    model.rodzaj_zamierzenia_budowlanego = ["Dowolne", "budowa nowego/nowych obiektów budowlanych",
                                            "rozbudowa istniejącego/istniejących obiektów budowlanych",
                                            "nadbudowa istniejącego/istniejących obiektów budowlanych",
                                            "odbudowa istniejącego/istniejących obiektów budowlanych",
                                            "rozbiórka istniejącego obiektu budowlanego",
                                            "wykonanie robót budowlanych innych niż wymienione powyżej"]
    model.kategoria_obiektu = ["Dowolna", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]

    return render_template("search_input.html", model=model)


@app.route('/search_process', methods=['GET'])
def search_process():
    # keyword = request.form
    keyword = dict(request.args)
    keyword["data_wydania_decyzji"] += "&" + keyword.pop('data_wydania_decyzji_do', None)
    keyword["data_zlozenia_wniosku"] += "&" + keyword.pop('data_zlozenia_wniosku_do', None)
    keyword["wojewodztwo"] += "&" + keyword.pop('wojewodztwo_2', None)

    model = InputDataModel(**keyword)
    browser = DataModel()
    browser.init_driver()
    browser.set_inputs(model)
    table_result = browser.get_data_from_table(model)

    import json
    with open('data.json', 'w') as f:
        json.dump(table_result, f)

    with open('data.json') as f:
        d = json.load(f)
    aa = d
    return keyword




@app.route('/')
def index():
    return search_input()


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(port=5000)

    # selenium_gunb.main()
