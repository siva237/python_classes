import psycopg2 as pg2

con = pg2.connect(dbname = 'userdb', user = 'postgres',
                  password = 'siva123',host = 'localhost',port='5432')
print("connection established sucessfully",con)

row = [(102,'siva','banglore'),(103,'krishna','tpty')]

cur = con.cursor()

cur.executemany("insert into emp(eno,ename,loc) values (%s,%s,%s)",row)

cur.execute("select * from emp")

data = cur.fetchall()

con.commit()

print(data)

