import dash
from dash import html, dcc, callback, Input, Output


dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='This is our RADIANZAS page'),

    html.Div(children='''
        This is our RADIANZAS page content.
    '''),

])