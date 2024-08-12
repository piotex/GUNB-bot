import json
import os
import threading
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
from os import listdir
from os.path import isfile, join
import logging

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
    with open('data_json/default_settings.json', encoding='utf-8') as f:
        default_settings = json.load(f)
    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)
    with open('data_json/result.json', encoding='utf-8') as f:
        gunb_data = json.load(f)

    table_headers = [key for key in gunb_data[0]] if len(gunb_data) > 0 else []
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
    with open('data_json/result.json', encoding='utf-8') as f:
        gunb_data = json.load(f)

    gunb_data = filter_data(gunb_data, filters["logical_filters"], filters["header_filters"])
    sheet_data = get_sheet_data(gunb_data)
    spreadsheet_url = app_send_generate_report(sheet_data)
    return redirect(spreadsheet_url, code=302)






@app.route('/download_data_run')
def download_data_run():
    start_time = time.time()
    with open('data_json/checked_data.json', encoding='utf-8') as f:
        checked_data = json.load(f)
    download_records(checked_data)
    logging.info(f"download_data_run {datetime.datetime.now()} time: {get_time(start_time)}")
    return render_template("index.html", view="home.html")


@app.route('/download_data_add_queue')
def download_data_add_queue():
    argsss = request.args
    datee = argsss['download_data_add_queue_date']
    timee = argsss['download_data_add_queue_time'].replace(":","-")

    with open('data_json/checked_data.json', encoding='utf-8') as f:
        checked_data = json.load(f)
    with open(f'queue/{datee} {timee}.json', 'w', encoding='utf-8') as f:
        json.dump(checked_data, f)
    return download_data()
@app.route('/download_data_delete_queue')
def download_data_delete_queue():
    argsss = request.args
    date_time = argsss['download_data_add_queue_date_time']
    os.remove(fr"queue/{date_time}")
    return download_data()


@app.route('/download_data')
def download_data():
    queue_list = [f for f in listdir("queue") if isfile(join("queue", f))]
    return render_template("index.html", view="download_data.html", queue_list=queue_list)


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

    with open('data_json/checked_data.json', 'w', encoding='utf-8') as f:
        json.dump(checked_data, f)

def update_possible_data():
    with open('data_json/posible_data_from_gunb.json', encoding='utf-8') as f:
        posible_data = json.load(f)
    with open('data_json/checked_data.json', encoding='utf-8') as f:
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

    with open('data_json/posible_data_from_gunb.json', 'w', encoding='utf-8') as f:
        json.dump(posible_data, f)

@app.route('/save_downloading_settings')
def save_downloading_settings():
    update_checked_data(request.args)
    update_possible_data()
    update_possible_data()
    return downloading_settings()

@app.route('/downloading_settings')
def downloading_settings():
    with open('data_json/posible_data_from_gunb.json', encoding='utf-8') as f:
        posible_data = json.load(f)
    with open('data_json/checked_data.json', encoding='utf-8') as f:
        checked_data = json.load(f)
    total = 1
    for key in checked_data:
        total *= len(checked_data[key])

    return render_template("index.html",
                           view="downloading_settings.html",
                           checked_data=checked_data,
                           posible_data=posible_data,
                           total=total)



@app.route('/default_settings')
def default_settings():
    with open('data_json/default_settings.json', encoding='utf-8') as f:
        default_settings = json.load(f)

    default_settings["email"] = "pkubon2@gmial.com"
    default_settings["captcha_tries"] = "5"

    with open('data_json/default_settings.json', 'w', encoding='utf-8') as f:
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
    path = r"data_json/default_settings.json"
    if not os.path.isfile(path):
        raise Exception("=== Nie ma pliku konfiguracyjnego! ===")

    path = r"data_json/checked_data.json"
    if not os.path.isfile(path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({
              "Data złożenia\nwniosku / zgłoszenia": [],
              "Typ dokumentu (Rejestr Wniosków i Decyzji)": [],
              "Rodzaj zamierzenia budowlanego": [],
              "Kategoria obiektu": [],
              "Województwo": [],
              "Organ administracji": []
            }, f)

    path = r"data_json/result.json"
    if not os.path.isfile(path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump([], f)

    path = r"data_json/posible_data_from_gunb.json"
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


def queue_runner():
    while True:
        with open('data_json/default_settings.json', encoding='utf-8') as f:
            default_settings = json.load(f)
        time.sleep(int(default_settings["queue_sleep_time_s"]))

        queue_list = [f for f in listdir("queue") if isfile(join("queue", f))]
        for elem in queue_list:
            datee = elem.split(" ")[0].split("-")
            timee = elem.split(" ")[1].split(".")[0].split("-")
            q_datetime = datetime.datetime(year=int(datee[0]), month=int(datee[1]), day=int(datee[2]), hour=int(timee[0]), minute=int(timee[1]))
            a_datetime = datetime.datetime.now()
            if a_datetime > q_datetime:
                logging.info(f'Start downloading data from {elem}')
                with open('data_json/checked_data.json', encoding='utf-8') as f:
                    checked_data = json.load(f)
                download_records(checked_data)
                logging.info(f'End downloading data from {elem}')
                os.remove(fr"queue/{elem}")


if __name__ == "__main__":
    with open('data_json/default_settings.json', encoding='utf-8') as f:
        default_settings = json.load(f)

    log_level_info = {'DEBUG': logging.DEBUG,
                      'INFO': logging.INFO,
                      'WARNING': logging.WARNING,
                      'ERROR': logging.ERROR}
    logging.basicConfig(filename=rf"logs/log-{time.strftime("%Y-%m-%d")}.txt",
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=log_level_info[default_settings["log_level"]])
    init_files()

    t = threading.Thread(target=queue_runner,name='queue_runner-1')
    t.daemon = True
    t.start()

    Timer(1, open_browser).start()
    app.run(port=5000)



    # selenium_gunb.main()
