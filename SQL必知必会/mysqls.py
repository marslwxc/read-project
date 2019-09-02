import mysql.connector


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1', #'1205014235zhe',
    database='learning', #'sql learning',
    auth_plugin='mysql_native_password'
)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("MySQL版本：{}".format(data))
cursor.close()
db.close()