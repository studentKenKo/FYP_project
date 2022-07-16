import threading
import time
#  connect Database
import psycopg2

# Update connection string information
host = "localhost"
dbname = ""
user = "admin"
password = "12345678"
sslmode = "allow"

conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)

# conn = psycopg2.connect("dbname=test user=postgres")
cur = conn.cursor()
cur.execute("select * from information_schema.tables where table_name=%s", ('inventory',))
if not bool(cur.rowcount):
  cur.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
  print("Finished creating table")
# Insert some data into the table
cur.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))


# 子執行緒的工作函數
def job():
  for i in range(5000):
    # print("Child thread:", i)
    # Insert some data into the table
    cur.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", i))
    # time.sleep(1)

# 建立一個子執行緒
t = threading.Thread(target = job)
# 執行該子執行緒
t.start()
# 等待 t 這個子執行緒結束
t.join()

# Clean up
conn.commit()
cur.close()
conn.close()

print("Done.")