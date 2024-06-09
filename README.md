## Python Data

Tools used:
- Python3
- Django
- ReactJs
- Numpy
- Pandas
- SqlLite

### How to use:
- Downlad and install `sqllitebrowser`
- In the terminal, run `sqlitebrowser` to start the application.
- Proceed to connect to the mydatabase.sqlite database via the application.
  

### SQLITE CHEATSHEET:
Show all tables in the database:
```sql
SELECT name FROM sqlite_master WHERE type='table';
```

Delete a table from the database:
```sql
DROP table Voter
```

Get the schema of a table in the database:
`.schma Voter`