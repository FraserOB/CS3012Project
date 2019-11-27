from flask import Flask, render_template, request
import requests
#import graph.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    username1 = request.form['username1']
    username2 = request.form['username2']
    r1 = requests.get('http://api.github.com/users/'+username1+'')
    r2 = requests.get('http://api.github.com/users/'+username2+'')
    json_object = r1.text + "\n" + r2.text
    return render_template('data.html', userData=json_object)

if __name__ == '__main__':
    app.run(debug=True)
