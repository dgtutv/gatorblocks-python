import json
import datetime
print("Please enter the first day of school in; Day, Month, Year format")
year= int(input('Year: '))
month= int(input('Month: '))
day= int(input('Day: '))
date1=datetime.date(year, month, day)
day_of_year = date1.timetuple().tm_yday
beginning=day_of_year
with open('referenceBegin.txt', 'w') as filehandle:
    json.dump(beginning, filehandle)
print("Please enter the last day of school in; Day, Month, Year format")
year= int(input('Year: '))
month= int(input('Month: '))
day= int(input('Day: '))
date1=datetime.date(year, month, day)
day_of_year = date1.timetuple().tm_yday
Final=day_of_year
with open('referenceFinal.txt', 'w') as filehandle:
    json.dump(Final, filehandle)
print("If there is a weekend between the new year and first day of school after the winter break, enter 2. Otherwise enter 0")
end=int(input())
with open('referenceEnd.txt', 'w') as filehandle:
    json.dump(end, filehandle)
