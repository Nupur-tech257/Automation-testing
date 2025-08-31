import mysql.connector as conn
import re

# connect to DB
mydb = conn.connect(
    host="db",
    user="testuser",
    password="testpass",
    database="testdb"   # add this if you want to target a specific DB
)
cursor = mydb.cursor()

#cursor.execute("create table if not exists users(id int(11) PRIMARY KEY NOT NULL,name varchar(255) NOT NULL,email varchar(255) NOT NULL,location varchar(255));")
#cursor.execute("INSERT INTO users VALUES ( 2,'hi','hi@gmail.com','delhi');")

# read SQL file
with open("/usr/src/app/migrations/Table.sql", "r") as f:
    sql_script = f.read()

# remove block comments
sql_cleaned = re.sub(r"/\*.*?\*/", "", sql_script, flags=re.DOTALL)

# execute statements one by one
for statement in sql_cleaned.split(";"):
    if statement.strip():
        cursor.execute(statement)
        
# ✅ commit + close connection object
mydb.commit()
cursor.close()
mydb.close()
print('done')
