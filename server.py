

from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'whatever'


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/data', methods=['POST'])
def data():
    # data = {
        session['name'] = request.form['name']
        session['locations'] = request.form['locations']
        session['languages'] = request.form['languages']
        return redirect('/result')
    # }
    # session['name']= request.form['name']


if __name__ == "__main__":
    app.run(debug=True)
