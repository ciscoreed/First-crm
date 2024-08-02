import MySQLdb

dataBase = MySQLdb.connect(
    host='localhost',
    user='root',
    password='password123'
    
)

cursor = dataBase.cursor()
cursor.execute("CREATE DATABASE cisco")
print("All Done!")

cursor.close()
dataBase.close()
