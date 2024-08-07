import json
import string

from flask import Flask, redirect, url_for, request, render_template
import webbrowser
from threading import Timer

from utils_app import filter_data

app = Flask(__name__)


@app.route('/generate_report')
def generate_report():
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


@app.route('/add_filter')
def add_filter():
    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)

    args = request.args
    if "keyword_category" in args and "keyword" in args:
        keyword = args["keyword"]
        keyword_category = args["keyword_category"].replace('\r','')
        filters.append([keyword, keyword_category])

    with open('filters.json', 'w', encoding='utf-8') as f:
        json.dump(filters, f)

    return filter()
@app.route('/delete_filter')
def delete_filter():
    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)

    args = request.args
    if "keyword_category_to_del" in args and "keyword_to_del" in args:
        res = []
        for x in filters:
            if args["keyword_to_del"] != x[0]:
                res.append(x)
        filters = res

    with open('filters.json', 'w', encoding='utf-8') as f:
        json.dump(filters, f)

    return filter()


@app.route('/filter')
def filter():
    args = request.args

    with open('filters.json', encoding='utf-8') as f:
        filters = json.load(f)
    with open('result.json', encoding='utf-8') as f:
        gunb_data = json.load(f)

    keyword_categories = [key for key in gunb_data[0]]

    gunb_data = filter_data(gunb_data, filters)

    if len(gunb_data) < 1:
        gunb_data = [{}]
        for key in keyword_categories:
            gunb_data[0][key] = ""

    return render_template("filter.html", result=gunb_data, keyword_categories=keyword_categories, old_filters_keywords=filters)


@app.route('/')
def index():
    return filter()


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(port=5000)

    # selenium_gunb.main()
