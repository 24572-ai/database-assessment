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
    print(f"{'Name':<20}"f"{'passengers':<15}"f"{'Range':<15}"f"{'Speed':<12}"f"{'Max weight':<12}"f"{'takeoff speed':<15}"f"{'land speed':<12}"f"{'no of planes':<12}")
    for airnzaircraft in results:
        print(f"{airnzaircraft[1]:<20}"f"{airnzaircraft[2]:<15}"f"{airnzaircraft[3]:<15}"f"{airnzaircraft[4]:<12}"f"{airnzaircraft[5]:<12}"f"{airnzaircraft[6]:<15}"f"{airnzaircraft[7]:<12}"f"{airnzaircraft[8]:<12}")
    db.close()



print_all_aircraft()




