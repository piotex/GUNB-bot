import json
import requests
import webbrowser
from threading import Timer
from bs4 import BeautifulSoup
from flask import Flask, redirect, url_for, request, render_template
from utils_app import filter_data, app_delete_filter, app_add_filter, app_add_header_filter

app = Flask(__name__)


@app.route('/add_header_filter')
def add_header_filter():
    app_add_header_filter(request.args)
    return generate_report()


@app.route('/add_filter')
def add_filter():
    app_add_filter(request.args)
    return generate_report()


@app.route('/delete_filter')
def delete_filter():
    app_delete_filter(request.args)
    return generate_report()


@app.route('/generate_report')
def generate_report():
    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)

    header_filters = filters["header_filters"]
    logical_filters = filters["logical_filters"]

    with open('result.json', encoding='utf-8') as f:
        gunb_data = json.load(f)

    table_headers = [key for key in gunb_data[0]]

    gunb_data = filter_data(gunb_data, logical_filters, header_filters)

    return render_template("index.html",
                           view="generate_report.html",
                           table_headers=table_headers,
                           header_filters=header_filters,
                           logical_filters=logical_filters,
                           table_items=gunb_data)


@app.route('/save_download_data')
def save_download_data():
    # with open('data.json', 'w', encoding='utf-8') as f:
    #     json.dump(data, f)

    pass


@app.route('/download_data')
def download_data():
    data_args = request.args

    with open('posible_data_from_gunb.json', encoding='utf-8') as f:
        posible_data = json.load(f)

    if len(data_args) > 0:
        checked_data = {}
        for key in data_args:
            if data_args[key] not in checked_data:
                checked_data[data_args[key]] = []
            checked_data[data_args[key]].append(key)

        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(checked_data, f)

    with open('data.json', encoding='utf-8') as f:
        checked_data = json.load(f)



    r = requests.get("https://wyszukiwarka.gunb.gov.pl/")
    r.encoding = r.apparent_encoding
    selects = BeautifulSoup(r.text).find_all('select')
    options_wojewodztwo = {}
    for op in selects[2].findAll('option'):
        options_wojewodztwo[op.text.strip()] = op['value']
    organ = {}
    for woj in checked_data["Województwo"]:
        organ[woj] = []
        r = requests.get(f"https://wyszukiwarka.gunb.gov.pl/json/Search/getOrgsByRegion/?region={options_wojewodztwo[woj.lower()]}")
        r.encoding = r.apparent_encoding
        data_json = json.loads(r.text)
        for item in data_json["data"]:
            organ[woj].append(item["name"])




    return render_template("index.html",
                           view="download_data.html",
                           checked_data=checked_data,
                           posible_data=posible_data)

    # import gspread
    # email = ""
    # gc = gspread.service_account(filename='../secrets/gunb-bot-project-credentials.json')
    # sh = gc.create("gunb-sierpien")
    # spreadsheet_url = "https://docs.google.com/spreadsheets/d/%s" % sh.id
    #
    # worksheet = sh.add_worksheet(title="gunb-worksheet-1", rows="100", cols="20")
    #
    # with open('filters.json', encoding='utf-8') as f:
    #     filters = json.load(f)
    # with open('result.json', encoding='utf-8') as f:
    #     gunb_data = json.load(f)
    #
    # keyword_categories = [key for key in gunb_data[0]]
    # for i, key in enumerate(keyword_categories, start=0):
    #     worksheet.update_acell(f'{string.ascii_uppercase[i]}1', key)
    #
    # gunb_data = filter_data(gunb_data, filters)
    # for i, item in enumerate(gunb_data, start=2):
    #     for j, key in enumerate(item, start=0):
    #         worksheet.update_acell(f'{string.ascii_uppercase[j]}{i}', item[key])
    #
    # sh.share(email, perm_type='user', role='writer')
    # print(spreadsheet_url)
    # return redirect(spreadsheet_url, code=302)
    # return render_template("index.html", view="download_data.html")


@app.route('/home')
def home():
    return index()


@app.route('/')
def index():
    return render_template("index.html", view="home.html")


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == "__main__":
    r = requests.get("https://wyszukiwarka.gunb.gov.pl/")
    r.encoding = r.apparent_encoding
    selects = BeautifulSoup(r.text).find_all('select')
    options_typ_dokumentu = [op.text.strip() for op in selects[0].findAll('option')]
    options_wojewodztwo = [op.text.strip() for op in selects[2].findAll('option')]
    options_organ_administracji = [op.text.strip() for op in selects[3].findAll('option')]
    options_rodzaj_zamierzenia_budowlanego = [op.text.strip() for op in selects[5].findAll('option')]
    options_kategoria_obiektu = [op.text.strip() for op in selects[6].findAll('option')]
    posible_data = {
        "Typ dokumentu (Rejestr Wniosków i Decyzji)": options_typ_dokumentu,
        "Rodzaj zamierzenia budowlanego": options_rodzaj_zamierzenia_budowlanego,
        "Kategoria obiektu": options_kategoria_obiektu,
        "Województwo": options_wojewodztwo,
        "Organ administracji": options_organ_administracji,
    }
    with open('posible_data_from_gunb.json', 'w', encoding='utf-8') as f:
        json.dump(posible_data, f)

    Timer(1, open_browser).start()
    app.run(port=5000)

    # selenium_gunb.main()
