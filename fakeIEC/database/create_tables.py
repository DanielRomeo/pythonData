import sqlite3

""""
This file creates all the neccessary database tables and populates the default tables such as Ethnicity table
"""

# Define connection string (replace with your database filename if different)
conn = sqlite3.connect('mydatabase.sqlite')
cursor = conn.cursor()

# Create Voter table
voter_table = """
CREATE TABLE Voter (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  firstname VARCHAR(50) NOT NULL,
  lastname VARCHAR(50) NOT NULL,
  idnumber VARCHAR(20) UNIQUE NOT NULL,
  address_id INTEGER REFERENCES Address(id),
  vote_id INTEGER REFERENCES Vote(id),
  ethnicity_id INTEGER REFERENCES Ethnicity(id)
);
"""

# Create Ethnicity table
ethnicity_table = """
CREATE TABLE Ethnicity (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL,
  language_group VARCHAR(50)
);
"""

# Create Address table
address_table = """
CREATE TABLE Address (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  province VARCHAR(50) NOT NULL,
  district VARCHAR(50) NOT NULL
);
"""

# Create Vote table
vote_table = """
CREATE TABLE Vote (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  national VARCHAR(50) NOT NULL,
  provincial VARCHAR(50) NOT NULL,
  regional VARCHAR(50) NOT NULL
);
"""

# Insert values in Ethnicity table:
query_insert_into_ethnicity1 = """
INSERT INTO Ethnicity(name) Values('black');
"""
query_insert_into_ethnicity2 = """
INSERT INTO Ethnicity(name) Values('white');
"""
query_insert_into_ethnicity3 = """
INSERT INTO Ethnicity(name) Values('coloured');
"""
query_insert_into_ethnicity4 = """
INSERT INTO Ethnicity(name) Values('indian');
"""


# Check if tables exist (using a single query for efficiency)
cursor.execute("""
SELECT name FROM sqlite_master WHERE type='table' AND
  (name = 'Voter' OR name = 'Ethnicity' OR name = 'Address' OR name = 'Vote');
""")

existing_tables = [row[0] for row in cursor.fetchall()]

for table_definition in [voter_table, ethnicity_table, address_table, vote_table ]:
    if table_definition.split()[2] not in existing_tables:  # Check table name
        cursor.execute(table_definition)
        print(f"Created table: {table_definition.split()[2]}")


# commented out query to isnert values into ethnicity
cursor.execute(query_insert_into_ethnicity1)
cursor.execute(query_insert_into_ethnicity2)
cursor.execute(query_insert_into_ethnicity3)
cursor.execute(query_insert_into_ethnicity4)


# Save changes (commit)
conn.commit()

# Close the connection
conn.close()

print("Tables created successfully!")