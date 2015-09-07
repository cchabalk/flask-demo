from flask import render_template, redirect, request
from app import app
from bokeh.plotting import figure
    
from bokeh.charts import TimeSeries
from bokeh.resources import CDN
from bokeh.embed import file_html, components

import pandas as pd
import json
import requests
import datetime

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index(): 
        return render_template('index.html')


@app.route('/graph', methods=['GET', 'POST'])
def graph():

    #get POST data
    tickerSymbol = request.form['ticker'].upper()
    features = request.form.getlist('features')

    #get stock data from Quandl WIKI
    quandleKey = 'Hss7TYkWM9KUsB5wfvRb'
    quandleRequest = 'https://www.quandl.com/api/v3/datasets/WIKI/' + tickerSymbol + '.json?api_key=' + quandleKey
    r = requests.get(quandleRequest)

    #bad ticker
    if (r.status_code != 200):
        return render_template('errorPage.html')

    #convert to dataframe
    df = pd.DataFrame(r.json()['dataset']['data'],columns = r.json()['dataset']['column_names'])
    df['Date'] = pd.to_datetime(df['Date'])
    df.rename(columns=lambda x: tickerSymbol + ': ' + x, inplace=True)

    #handle no features
    if len(features)==0:
        p = figure(x_axis_type = "datetime",title='Data from Quandl WIKI set')
    else:
        #pre-pend ticker name to column names
        columns = ['Date']+features
        tickerText = tickerSymbol+': '
        columns = [tickerText + s for s in columns]
        p = TimeSeries(df[columns],legend=True,index=tickerText + 'Date',title='Data from Quandl WIKI set',xlabel='date',width=600, height=600)

    #generate html plot
    htmlPlot = file_html(p,CDN,"my plot")

    return render_template('graph.html',
				tickerSymbol = tickerSymbol,
				features = features,
                                plottingData = htmlPlot)


