#docsting - this is code to extract data from a database of airnzaircraft made by daniel gasson



import sqlite3
DATABASE = 'airnzairplanes.db'

def print_all_aircraft():
    #prints all aircraft data in a readable way
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from airnzaircraft;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for airnzaircraft in results:
        print(airnzaircraft)
    db.close()



print_all_aircraft()




