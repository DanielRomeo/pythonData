import sqlite3
import random
from faker import Faker

# Define connection string (replace with your database filename if different)
conn = sqlite3.connect('mydatabase.sqlite')
cursor = conn.cursor()

# Initialize Faker
fake = Faker()

# Generate fake data for 10 voters
for _ in range(10):
  # Generate voter data
  firstname = fake.first_name()
  lastname = fake.last_name()
  idnumber = f"{random.randint(10000000, 99999999)}-{random.randint(100, 999)}"  # Sample ID format
  address_id = random.randint(1, 10)  # Assuming 10 pre-populated addresses
  vote_id = random.randint(1, 10)  # Assuming 10 pre-populated votes
  ethnicity_id = random.randint(1, 5)  # Assuming 5 pre-populated ethnicities

  # Generate address data (assuming separate script populates Address table)
  # province = fake.address().province()
  # district = fake.address().district()

  # Generate vote data (assuming separate script populates Vote table)
  # national = "Party X"  # Replace with your choices
  # provincial = "Party Y"
  # regional = "Party Z"

  # Insert data into Voter table
  cursor.execute("""
    INSERT INTO Voter (firstname, lastname, idnumber, address_id, vote_id, ethnicity_id)
    VALUES (?, ?, ?, ?, ?, ?)
  """, (firstname, lastname, idnumber, address_id, vote_id, ethnicity_id))

# Save changes (commit)
conn.commit()

# Close the connection
conn.close()

print("10 Voters added successfully!")
