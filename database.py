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
        print(f"{airnzaircraft[1]:<20}"f"{airnzaircraft[2]:<8}"f"{airnzaircraft[3]:<8}"f"{airnzaircraft[4]:<8}"f"{airnzaircraft[5]:<8}"f"{airnzaircraft[6]:<5}"f"{airnzaircraft[7]:<5}"f"{airnzaircraft[8]:<5}")
    db.close()



print_all_aircraft()




