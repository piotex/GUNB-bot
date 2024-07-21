import time
import selenium_gunb
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        return render_template("search.html")
        # user = request.args.get('nm')
        # return redirect(url_for('success', name=user))


if __name__ == "__main__":
    app.run()

    # selenium_gunb.main()




