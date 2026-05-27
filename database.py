#docsting - this is code to extract data from a database of airnzaircraft made by daniel gasson



import sqlite3
DATABASE = 'airnzairplanes.db'





db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "select * from airnzaircraft;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)



db.close()