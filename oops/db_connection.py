import psycopg2 as pg2

# Establishing the connection with db

conn = pg2.connect(dbname = "",port = "5432",
                   host = "localhost",
                   user = "postgres",password="")

# entry into db

cursor = conn.cursor()

# executing the sql queries

cursor.execute("select * from emp")

data = cursor.fetchall()

print(data)
