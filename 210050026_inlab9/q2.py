import sqlite3
import csv
import sys

try:
    query_state = sys.argv[1]               # taking command line arguement
    sqliteConnection = sqlite3.connect('zipcodesDB.db')     # creating Database
    create_zipcodes_table = '''CREATE TABLE zipcodesInfo(
                                zip_code TEXT PRIMARY KEY,
                                latitude REAL NOT NULL,
                                longitude REAL NOT NULL,
                                city TEXT NOT NULL,
                                state TEXT NOT NULL,
                                country TEXT NOT NULL);'''                 
    cursor = sqliteConnection.cursor()
    cursor.execute(create_zipcodes_table)   # creating table

    file = open('zipcodes.csv')     # inserting data into table created
    filecontents = csv.reader(file)
    insert_data = "INSERT INTO zipcodesInfo(zip_code, latitude, longitude, city, state, country) VALUES(?, ?, ?, ?, ?, ?)"
    cursor.executemany(insert_data, filecontents)

    filter_states = "SELECT * from zipcodesInfo WHERE state=? ORDER BY latitude"       # filtering states
    zipCodes_state = cursor.execute(filter_states,(query_state,)).fetchall()
    if len(zipCodes_state) == 0:
        print("NOT FOUND")
        exit(1)
    max_latitude_city = zipCodes_state[len(zipCodes_state)-1][3]
    northernCities = list()         # list to store wanted cities
    for i in zipCodes_state:
        if i[3] == max_latitude_city:
            northernCities.append(i[0])
    northernCities.sort()
    for northernCity in northernCities[0:-1]:
        print(northernCity,end=",")
    print(northernCities[-1])
    
    sqliteConnection.commit()
    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()