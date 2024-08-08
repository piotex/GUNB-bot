import json
import string

from flask import Flask, redirect, url_for, request, render_template
import webbrowser
from threading import Timer

from utils_app import filter_data, app_delete_filter, app_add_filter

app = Flask(__name__)


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
    with open('result.json', encoding='utf-8') as f:
        gunb_data = json.load(f)

    keyword_categories = [key for key in gunb_data[0]]

    gunb_data = filter_data(gunb_data, filters)

    # if len(gunb_data) < 1:
    #     gunb_data = [{}]
    #     for key in keyword_categories:
    #         gunb_data[0][key] = ""

    table_headers = keyword_categories

    return render_template("index.html", view="generate_report.html",
                           table_headers=table_headers,
                           table_items=gunb_data, old_filters_keywords=filters)


@app.route('/download_data')
def download_data():
    import gspread
    email = ""
    gc = gspread.service_account(filename='../secrets/gunb-bot-project-credentials.json')
    sh = gc.create("gunb-sierpien")
    spreadsheet_url = "https://docs.google.com/spreadsheets/d/%s" % sh.id

    worksheet = sh.add_worksheet(title="gunb-worksheet-1", rows="100", cols="20")

    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)
    with open('result.json', encoding='utf-8') as f:
        gunb_data = json.load(f)

    keyword_categories = [key for key in gunb_data[0]]
    for i, key in enumerate(keyword_categories, start=0):
        worksheet.update_acell(f'{string.ascii_uppercase[i]}1', key)

    gunb_data = filter_data(gunb_data, filters)
    for i, item in enumerate(gunb_data, start=2):
        for j, key in enumerate(item, start=0):
            worksheet.update_acell(f'{string.ascii_uppercase[j]}{i}', item[key])

    sh.share(email, perm_type='user', role='writer')
    print(spreadsheet_url)
    return redirect(spreadsheet_url, code=302)
    return render_template("index.html", view="download_data.html")


@app.route('/home')
def home():
    return index()


@app.route('/')
def index():
    return render_template("index.html", view="home.html")


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(port=5000)

    # selenium_gunb.main()
