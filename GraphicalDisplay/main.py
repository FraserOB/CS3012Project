from flask import Flask, render_template, request
import requests
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/graph', methods=['POST'])
def graph():
        username1 = request.form['username1']
        username2 = request.form['username2']
        bar = create_plot(username1, username2)
        return render_template('graph.html', plot=bar)

compared_data=['followers', 'followings', 'number of repos']

def get_data(j_obj):
    username = j_obj['login']
    followers = j_obj['followers']
    followings = j_obj['following']
    repos = j_obj['public_repos']
    userdata = [followers, followings, repos]
    return userdata

def create_plot(name1, name2):


    r1 = requests.get('http://api.github.com/users/'+name1+'')
    r2 = requests.get('http://api.github.com/users/'+name2+'')
    j_obj1 = r1.json()
    username1 = j_obj1['login']
    userdata1 = get_data(j_obj1)
    j_obj2 = r2.json()
    username2 = j_obj2['login']
    userdata2 = get_data(j_obj2)

    data = [
        go.Bar(name= username1, x=compared_data, y=userdata1),
        go.Bar(name= username2, x=compared_data, y=userdata2)
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

if __name__ == '__main__':
    app.run(debug=True)
