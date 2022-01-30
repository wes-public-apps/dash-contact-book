import logging
import os
from time import sleep

from dash import Dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app.layout import layout
from app.pages import contact_list_view
from app.pages import new_contact
from app.utils import queries
from app.utils.constants import home_location, new_contact_location
from app.utils.databases import TimescaleInterface


def initialize_db() -> bool:

    db_interface = TimescaleInterface.instance()
    if db_interface is None:
        return False

    if not db_interface.execute_query(queries.CREATE_CONTACTS_TABLE):
        return False

    return True


def launch_app() -> None:
    app = Dash(name="Contacts App")
    app.layout = layout.get_layout()

    @app.callback(
        Output("page-content", "children"),
        Input("url", "pathname")
    )
    def render_page_content(pathname):
        if pathname == home_location:
            return contact_list_view.create_layout()
        elif pathname == new_contact_location:
            return new_contact.create_layout()

        # If the user tries to reach a different page, return a 404 message
        return dbc.Jumbotron(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ]
        )

    app.run_server(
        host=os.environ['HOST'],
        port=os.environ['PORT'],
        debug=os.environ['DEBUG'],
        dev_tools_props_check=os.environ['DEV_TOOLS_PROPS_CHECK']
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Starting social media app!")
    initialize_db()
    logging.info("DB initialization complete.")
    launch_app()
    logging.info("Frontend initialized.")
    while True:
        sleep(60)
