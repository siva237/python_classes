import csv
import psycopg2 as pg2
connection = pg2.connect(dbname='userdb', user='postgres', password='siva123', host='localhost', port='5432')
cur = connection.cursor()
with open('S:/file operations/sss3.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        cur.execute("insert into employee values(%s, %s, %s, %s, %s)", row)

connection.commit()
