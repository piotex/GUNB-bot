import json

from flask import Flask, redirect, url_for, request, render_template
import webbrowser
from threading import Timer

app = Flask(__name__)


@app.route('/filter')
def filter():
    with open('result.json', encoding='utf-8') as f:
        result = json.load(f)
    return render_template("filter.html", result=result)


@app.route('/')
def index():
    return filter()


def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(port=5000)

    # selenium_gunb.main()
