## 3. Connecting to the Database ##

import sqlite3
conn = sqlite3.connect("jobs.db")

## 6. Creating a Cursor and Running a Query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])
query = "select major from recent_grads;"
majors = cursor.execute(query).fetchall()
print(majors[0:3])

## 8. Fetching a Specific Number of Results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
query = "select Major,Major_category from recent_grads;"
cursor.execute(query)
five_results = cursor.fetchmany(5)

## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

# connecting to database jobs.db
conn = sqlite3.connect('jobs.db')

# query as per Q2
query = '''
        SELECT Major
        FROM recent_grads
        ORDER BY 1 DESC
        '''

# results assignment as per Q3
reverse_alphabetical = conn.execute(query).fetchall()

# closing connection to jobs.db as per Q4
conn.close()

# displaying reverse_alphabetical
reverse_alphabetical[0:5]