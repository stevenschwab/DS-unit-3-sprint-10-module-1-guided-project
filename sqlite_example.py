import sqlite3
import queries as q
# step 1
# connect to the database
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2
cursor = connection.cursor()

# step 3 - write a query
# (See the queries.py file)

# step 4 - execute the query on the cursor and fetch the results
# 'pulling the results" from the cursor
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])