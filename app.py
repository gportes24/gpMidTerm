import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'Fatalities by country based on attacks(terrorist groups)'
myheading1 = 'The Armed Conflict Location & Event Data Project (ACLED) is a disaggregated conflict analysis and crisis mapping project'
myheading2 = 'Bringing clarity to crisis!'
image1 = 'acled_Dashboard.jpg'
image2 = 'midterm.png'
textbody = 'The graph depicts fatalities groupby countries and attacks- focused on those attributed to terrorism.'
sourceurl = 'https://www.acleddata.com'
githublink = 'https://github.com/gportes24/gpMidTerm'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.H2(myheading2),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '75%', 'height': '80%'})
        ],className='three columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image2), style={'width': '120%', 'height': '150'}),
        ],className='three columns'),
        html.Div([
            html.Div(textbody, style={
                'padding': '12px',
                'font-size': '15px',
                'width': '180px',
                'height': '90px',
                'border': 'thin blue solid',
                'color': 'rgb(159, 78, 78)',
                'backgroundColor': 'rgb(46, 45, 45)',
                'textAlign': 'right',
                }),
        ],className='six columns'),
    ],className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
