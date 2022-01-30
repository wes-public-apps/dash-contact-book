
import dash_html_components as html
import dash_core_components as dcc

from app.layout import sidebar


def get_layout():
    content = html.Div(id="page-content")
    return html.Div([dcc.Location(id="url"), sidebar.get_layout(), content])
