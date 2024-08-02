import MySQLdb

dataBase = MySQLdb.connect(
    host='localhost',
    user='root',
    password='Password@123'
    
)

cursor = dataBase.cursor()
cursor.execute("CREATE DATABASE cisco")
print("All Done!")

cursor.close()
dataBase.close()
