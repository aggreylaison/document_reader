import psycopg2
import os

conn=psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password=os.environ.get("DB_PASSWORD")

)

cur=conn.cursor()

cur.execute("insert into emp (names) values ('aggrey')")

cur.execute("select id,names from emp")

rows=cur.fetchall()

print(rows)

conn.commit()
cur.close()
conn.close()