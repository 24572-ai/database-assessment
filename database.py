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

def print_all_aircraft_by_speed():
    #prints all aircraft data sorted by speed
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from airnzaircraft order by cruising_speed desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"{'Name':<20}"f"{'passengers':<15}"f"{'Range':<15}"f"{'Speed':<12}"f"{'Max weight':<12}"f"{'takeoff speed':<15}"f"{'land speed':<12}"f"{'no of planes':<12}")
    for airnzaircraft in results:
        print(f"{airnzaircraft[1]:<20}"f"{airnzaircraft[2]:<15}"f"{airnzaircraft[3]:<15}"f"{airnzaircraft[4]:<12}"f"{airnzaircraft[5]:<12}"f"{airnzaircraft[6]:<15}"f"{airnzaircraft[7]:<12}"f"{airnzaircraft[8]:<12}")
    db.close()

def print_all_aircraft_by_number():
    #prints all aircraft data sorted by speed
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "select * from airnzaircraft order by no_of_aircraft desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(f"{'Name':<20}"f"{'passengers':<15}"f"{'Range':<15}"f"{'Speed':<12}"f"{'Max weight':<12}"f"{'takeoff speed':<15}"f"{'land speed':<12}"f"{'no of planes':<12}")
    for airnzaircraft in results:
        print(f"{airnzaircraft[1]:<20}"f"{airnzaircraft[2]:<15}"f"{airnzaircraft[3]:<15}"f"{airnzaircraft[4]:<12}"f"{airnzaircraft[5]:<12}"f"{airnzaircraft[6]:<15}"f"{airnzaircraft[7]:<12}"f"{airnzaircraft[8]:<12}")
    db.close()



data = input("What would you like to learn about Air NZ planes?\n1. print all aircraft\n2. print aircraft by speed\n3. print all aircraft by the highest amount in the fleet\n4. help\n5. leave\n")
if data == "1":
    print_all_aircraft()
elif data == "2":
    print_all_aircraft_by_speed()
elif data == "3":
    print_all_aircraft_by_number()
elif data == "4":
    print('Name - Name of aircraft\n pax_capacity - how many passenger the aircraft can hold defined by the amount of seats\n range - aircrafts range in kilometers\n cruising_speed - the speed the aircraft usually flies at in knots at cruising altitude\n max_takeoff_weight - the maximum weight the aircraft can be when taking off in kg\n takeoff_speed - the speed the aircraft needs to reach to take off in knots\n landing_speed - minimum speed to lands in knots\n no_of_aircraft - how many of this type of plane are in the airnz fleet')
elif data == "5":
    print("goodbye")






