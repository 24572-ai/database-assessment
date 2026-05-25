import sqlite3

db = sqlite3.connect('airnzairplanes.db')
cursor = db.cursor()
sql = "SELECT * FROM airnzaircraft"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()