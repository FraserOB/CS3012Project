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
    return json_object
    #return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)
