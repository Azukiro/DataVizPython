
import pandas as pd
from consts import *
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



def readData():
    return pd.read_csv(CSV_DATA_PATH, sep=';', low_memory=False, encoding="UTF-8", usecols=CSV_DATA_HEADERS)

def createDict(data, keys, values):
    return { 
        tuple(
            df[key][i] 
            for key in keys
        )
            :
        {
            val : df[val][i]
            for val in values
        } 
        for i in range(len(data)) 
    };






if __name__ == '__main__':
	app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
	df = pd.read_csv(CSV_DATA_PATH, sep=';', low_memory=False, encoding="UTF-8", usecols=CSV_DATA_HEADERS)

	fig = fig = px.histogram(df, x="puiss_max",  nbins=1000)

	app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
	])
    app.run_server(debug=True)

