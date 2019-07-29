import psycopg2 as pg2

# Establishing the connection with db

conn = pg2.connect(dbname="mobiledb", port="5432",
                   host="localhost",
                   user="postgres",
                   password="1234")

# entry into db

cursor = conn.cursor()

# executing the sql queries

cursor.execute("select * from samaungstore_samaungstore")

data = cursor.fetchall()

print(data)
