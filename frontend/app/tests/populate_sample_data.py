from app.utils.databases import TimescaleInterface

db_interface: TimescaleInterface = TimescaleInterface.instance()
values = [
    ("Wes", "Software Developer", "murraywj@yahoo.com"),
    ("Wes", "Software Developer", "murraywj@yahoo.com"),
    ("Bob", "UX", "bobux@yahoo.com"),
]
records = ", ".join(["%s"] * len(values))
query = f'''
INSERT INTO contacts (name, job, email) VALUES ({records})
'''
db_interface.insert_records(query, values)
