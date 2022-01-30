from dash import html
import dash_bootstrap_components as dbc

from app.utils.constants import home_location, new_contact_location


def get_layout() -> html.Div:
    return html.Div(
        id='sidebar-container', className='sidebar',
        children=[
            dbc.Nav(
                [
                    dbc.NavLink("Home", href=home_location, active="exact"),
                    dbc.NavLink("New", href=new_contact_location, active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
        ]
    )
