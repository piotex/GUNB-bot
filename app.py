from flask import Flask, redirect, url_for, request, render_template

from input_data_model import InputDataModel
from gunb_browser import DataModel

app = Flask(__name__)


@app.route('/input_1')
def input_1():
    model = InputDataModel()
    model.rodzaj_wyszukiwania = ["Wyszukiwanie pozwoleń na budowę", "(not working) Wyszukiwanie zgłoszeń zamierzenia budowlanego"]
    model.typ_dokumentu = ["Dowolny", "W trakcie rozpatrywania", "Wycofany przez inwestora", "Bez rozpatrzenia", "Decyzja pozytywna", "Decyzja odmowna", "Decyzja umarzająca"]
    # model.typ_dokumentu = ["Dowolny","Sprawa w toku","Brak sprzeciwu","Decyzja o sprzeciwie"]
    model.wojewodztwo_1 = ["Cała Polska", "dolnośląskie", "kujawsko-pomorskie", "łódzkie", "lubelskie", "lubuskie", "małopolskie", "mazowieckie", "opolskie", "podkarpackie", "podlaskie", "pomorskie", "śląskie", "świętokrzyskie", "warmińsko-mazurskie", "wielkopolskie", "zachodniopomorskie"]
    model.organ_administracji = ["Dowolny"]
    model.wojewodztwo_2 = ["Cała Polska", "polski obszar morski", "dolnośląskie", "kujawsko-pomorskie", "łódzkie", "lubelskie", "lubuskie", "małopolskie", "mazowieckie", "opolskie", "podkarpackie", "podlaskie", "pomorskie", "śląskie", "świętokrzyskie", "warmińsko-mazurskie", "wielkopolskie", "zachodniopomorskie"]
    model.rodzaj_zamierzenia_budowlanego = ["Dowolne", "budowa nowego/nowych obiektów budowlanych", "rozbudowa istniejącego/istniejących obiektów budowlanych", "nadbudowa istniejącego/istniejących obiektów budowlanych", "odbudowa istniejącego/istniejących obiektów budowlanych", "rozbiórka istniejącego obiektu budowlanego", "wykonanie robót budowlanych innych niż wymienione powyżej"]
    model.kategoria_obiektu = ["Dowolna", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII" ]

    return render_template("search.html", model=model)

@app.route('/search', methods=['GET'])
def search():
    # keyword = request.form
    keyword = dict(request.args)
    model = InputDataModel(**keyword)
    browser = DataModel()
    browser.init_driver()
    browser.set_inputs(model)

    return keyword

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        return render_template("search.html", data=[{'name': 'red'}, {'name': 'green'}, {'name': 'blue'}])
        # user = request.args.get('nm')
        # return redirect(url_for('success', name=user))


@app.route('/')
def index():
    return input_1()


if __name__ == "__main__":
    app.run()

    # selenium_gunb.main()
