station_N = int(input(" Enter the number of charging  stations: "))
x=1

if station_N <= 1:
    print("Please enter a valid number of charging  stations.")

    while station_N <= 1:

        station_N = int(input(" Enter the number of charging  stations: "))

#
kwr_station_N = int(input("Enter the kw rating of the charging station: "))
if kwr_station_N == 7: 
    ppM= 0 
elif kwr_station_N == 22:
    ppM= 0.005
else:
    ppM = 0.01

if x == 1:
    startmillage = int(input("Enter the starting mileage at previous charging station: "))
  
else:
    currentmillage = int(input("Enter the current mileage: "))
    milesTravelled = int(input("Enter the miles travelled since last charge: "))
    print( " current millage") 
    print (" milesTravelled since last charge")
    currentmillage = currentmillage + milesTravelled  
    print( "Current mileage is: ", currentmillage) 

    station=1
 
                  