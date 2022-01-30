from dataclasses import dataclass
import logging

from typing import List, Any

from app.utils.databases import TimescaleInterface
from app.utils import queries


@dataclass
class Contact:
    id: int
    name: str
    email: str
    job: str

    @classmethod
    def get_contact(cls, id) -> Any:
        raise NotImplementedError()


class Contacts:

    @classmethod
    def get_contacts(cls) -> List[Contact]:
        db_interface: TimescaleInterface = TimescaleInterface.instance()
        records = db_interface.get_records(queries.GET_ALL_CONTACTS)
        logging.debug(records)
        contacts = [
            Contact(record[0], record[1], record[3], record[2])
            for record in records
        ]
        logging.debug(contacts)
        return contacts

    @classmethod
    def add_contact(cls, contact: Contact) -> bool:
        db_interface: TimescaleInterface = TimescaleInterface.instance()
        return db_interface.insert_records(
            queries.INSERT_CONTACTS,
            [(contact.name, contact.job, contact.email)]
        )
