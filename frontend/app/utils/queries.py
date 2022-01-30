CREATE_CONTACTS_TABLE = """
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    job VARCHAR(50),
    email VARCHAR(40) NOT NULL
)
"""

GET_ALL_CONTACTS = '''
SELECT id, name, job, email
FROM contacts
'''

INSERT_CONTACTS = '''
INSERT INTO contacts (name, job, email) values (%s, %s, %s)
'''
