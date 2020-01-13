import json
import datetime
#Please enter all days off school in day of year format, in this list
#DO NOT INCLUDE WEEKENDS!!
#spt20
#oct14
#oct25
#nov8
#nov11
#nov25
#dec23
#dec24
#dec25
#dec26
#dec27
#dec30
#dec31
#jan1
#jan2
#jan3
#feb14
#feb17
#mar16
#mar17
#mar18
#mar19
#mar20
#mar23
#mar24
#mar25
#mar26
#mar27
#apr10
#apr13
#may15
#may18
print("Please enter all days off school in day, month, year, format,DO NOT INCLUDE WEEKENDS!! Enter nothing to indicate all dates have been entered, enter anything to continue.")
dayOff = []
while True:
    if input()=="":
        break
    else:
        year= int(input('Year: '))
        month= int(input('Month: '))
        day= int(input('Day: '))
        date1=datetime.date(year, month, day)
        day_of_year = date1.timetuple().tm_yday
        dayOff+=[day_of_year]    
with open('days_off.txt', 'w') as filehandle:
    json.dump(dayOff, filehandle)

