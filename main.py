
import pandas as pd
from consts import *
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from collections import Counter

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
    }


def countOperator(data):
    return Counter(df["n_operateur"])

def pandaSeriesForOperator():
    df2 = pd.Series(countOperator(df)).to_frame('new_col').reset_index()
    df2.columns = ['Opérateur', 'Nombre de bornes']
    return df2

if __name__ == '__main__':
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    # Open the main dataframe from our ressource file
    df = readData()

    #Create histogram about the number of prises
    fig = px.histogram(df, x="nbre_pdc", log_y=True )
    fig.update_traces(
                  marker=dict( line=dict(color='#000000', width=2)))
    fig.update_layout(
    title="Nombre de prise par borne",
    xaxis_title="Nombre de prises",
    yaxis_title="Nombre de bornes",
    legend_title="Nombre de prises par bornes",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
        )
    )

    #Get dataframe for the counter of operator
    df2 = pandaSeriesForOperator()
    #Create the pie
    fig2 = px.pie(df2, values='Nombre de bornes', names='Opérateur')
   
    fig2.update_layout(
    title="Pourcentae de présence des opérateurs",
    legend_title="Nom des opérateur",
    font=dict(
        family="Courier New, monospace",
        size=11,
        color="RebeccaPurple"
        )
    )
    
    #Contruct Html Page
    app.layout = html.Div(
        children=[
            html.H1(children='Statistique borne électrique'), 
            html.Div(children='''Graphiques'''),
            dcc.Graph(id='tot', figure=fig),
            dcc.Graph(id='example-graph',figure=fig2)	
        ])

    #Run server
    app.run_server(debug=True)


    

