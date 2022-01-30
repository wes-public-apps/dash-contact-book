import dash_table

from app.models.contacts import Contacts


def create_layout() -> dash_table.DataTable:
    return dash_table.DataTable(
        id="contacts",
        columns=[{'name': v, 'id': v} for v in ['id', 'name', 'job', 'email']],
        data=[
            {'id': contact.id, 'name': contact.name, 'job': contact.job, 'email': contact.email}
            for contact in Contacts.get_contacts()
        ]
    )
