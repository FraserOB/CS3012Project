from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    username = request.form['username']
    r = requests.get('http://api.github.com/users/FraserOB')
    json_object = r.text
    return render_template('data.html', userData=json_object)

if __name__ == '__main__':
    app.run(debug=True)
