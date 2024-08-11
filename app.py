import json
import os
import time
import datetime
import requests
import webbrowser
from threading import Timer
from bs4 import BeautifulSoup
from download_records import download_records
from flask import Flask, redirect, request, render_template
from utils_app import filter_data, app_delete_filter, app_add_filter, app_add_header_filter, get_time, \
    app_save_generate_report, get_sheet_data, app_send_generate_report

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


@app.route('/save_generate_report')
def save_generate_report():
    app_save_generate_report(request.args)
    return generate_report()

@app.route('/generate_report')
def generate_report():
    with open('default_settings.json', encoding='utf-8') as f:
        default_settings = json.load(f)
    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)
    with open('result.json', encoding='utf-8') as f:
        gunb_data = json.load(f)

    table_headers = [key for key in gunb_data[0]]
    gunb_data = filter_data(gunb_data, filters["logical_filters"], filters["header_filters"])

    return render_template("index.html",
                           view="generate_report.html",
                           table_headers=table_headers,
                           header_filters=filters["header_filters"],
                           logical_filters=filters["logical_filters"],
                           table_items=gunb_data,
                           default_settings=default_settings)



@app.route('/send_generate_report')
def send_generate_report():
    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)
    with open('result.json', encoding='utf-8') as f:
        gunb_data = json.load(f)

    gunb_data = filter_data(gunb_data, filters["logical_filters"], filters["header_filters"])
    sheet_data = get_sheet_data(gunb_data)
    spreadsheet_url = app_send_generate_report(sheet_data)
    return redirect(spreadsheet_url, code=302)






@app.route('/download_data_run')
def download_data_run():
    start_time = time.time()
    download_records()
    print("===")
    print(f"download_data_run {datetime.datetime.now()} time: {get_time(start_time)}")
    return render_template("index.html", view="home.html")
@app.route('/download_data')
def download_data():
    return render_template("index.html", view="download_data.html")


def update_checked_data(args):
    data_args = {}
    for key in args:
        data_args[key] = args[key]

    checked_data = {}
    checked_data["Data złożenia\nwniosku / zgłoszenia"] = [data_args.pop("Data złożenia wniosku / zgłoszenia", "2024-01-01")]

    for key in data_args:
        if data_args[key] not in checked_data:
            checked_data[data_args[key]] = []
        checked_data[data_args[key]].append(key)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(checked_data, f)

def update_possible_data():
    with open('posible_data_from_gunb.json', encoding='utf-8') as f:
        posible_data = json.load(f)
    with open('data.json', encoding='utf-8') as f:
        checked_data = json.load(f)

    if "Województwo" in checked_data:
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
                if item["name"] != "Dowolny":
                    organ[woj].append(item["name"])
        posible_data["Organ administracji"] = organ

    with open('posible_data_from_gunb.json', 'w', encoding='utf-8') as f:
        json.dump(posible_data, f)

@app.route('/save_downloading_settings')
def save_downloading_settings():
    update_checked_data(request.args)
    update_possible_data()
    return downloading_settings()

@app.route('/downloading_settings')
def downloading_settings():
    with open('posible_data_from_gunb.json', encoding='utf-8') as f:
        posible_data = json.load(f)
    with open('data.json', encoding='utf-8') as f:
        checked_data = json.load(f)

    return render_template("index.html",
                           view="downloading_settings.html",
                           checked_data=checked_data,
                           posible_data=posible_data)



@app.route('/default_settings')
def default_settings():

    with open('default_settings.json', encoding='utf-8') as f:
        default_settings = json.load(f)

    default_settings["email"] = "pkubon2@gmial.com"
    default_settings["captcha_tries"] = "5"

    with open('default_settings.json', 'w', encoding='utf-8') as f:
        json.dump(default_settings, f)

@app.route('/home')
def home():
    return index()


@app.route('/')
def index():
    return render_template("index.html", view="home.html")


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


def init_files():
    path = r"data.json"
    if not os.path.isfile(path):
        a = 0

    path = r"posible_data_from_gunb.json"
    if not os.path.isfile(path):
        r = requests.get("https://wyszukiwarka.gunb.gov.pl/")
        r.encoding = r.apparent_encoding
        selects = BeautifulSoup(r.text).find_all('select')
        options_typ_dokumentu = [op.text.strip() for op in selects[0].findAll('option') if op.text.strip() != 'Dowolny']
        options_rodzaj_zamierzenia_budowlanego = [op.text.strip() for op in selects[5].findAll('option') if op.text.strip() != 'Dowolne']
        options_kategoria_obiektu = [op.text.strip() for op in selects[6].findAll('option') if op.text.strip() != 'Dowolna']
        options_wojewodztwo = [op.text.strip() for op in selects[2].findAll('option') if op.text.strip() != 'Cała Polska']
        posible_data = {
            "Data złożenia\nwniosku / zgłoszenia": ["2024-01-01"],
            "Typ dokumentu (Rejestr Wniosków i Decyzji)": options_typ_dokumentu,
            "Rodzaj zamierzenia budowlanego": options_rodzaj_zamierzenia_budowlanego,
            "Kategoria obiektu": options_kategoria_obiektu,
            "Województwo": options_wojewodztwo,
        }
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(posible_data, f)



if __name__ == "__main__":


    init_files()
    Timer(1, open_browser).start()
    app.run(port=5000)

    # selenium_gunb.main()
