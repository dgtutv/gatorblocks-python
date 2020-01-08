import datetime
import calendar
from datetime import datetime
from gatorblocksclasses import classes
from gatorblocks_days_off import dayOff
day_of_year = datetime.now().timetuple().tm_yday#day of year from date
now = datetime.now()#current date
week = calendar.weekday(now.year, now.month, now.day)#get day of week
day1 = [0,1,2,3]
day2 = [4,5,6,7]
day3 = [2,3,0,1]
day4 = [6,7,4,5]
day5 = [1,0,3,2]
day6 = [5,4,7,6]
day7 = [3,2,1,0]
day8 = [7,6,5,4]
weekDay = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
masterlist = [day1,day2,day3,day4,day5,day6,day7,day8]
#247, first day of scool
#176, days in school year
#120 between start end year
#421 in my sceduale
day_off =[]
w=0

#detect first day



day_of_year=12#used for testing
for offDay in dayOff:#from list of days off in day of year format, converts to day of school year 
    
    if dayOff[w] >246:
        day_off += [dayOff[w]-246]
    else:
        day_off += [dayOff[w]+121]
    w+=1
if day_of_year>246:#converts current day to day of school year
    dayOfYear=day_of_year-246
else:
    dayOfYear=day_of_year+121


rotation =-1
b=-1#a counter for total days that have been ran through the loop
for day in range(421):
##    print(b)
    rotation+=1
    if rotation ==-1:
##        print("weekend")
        continue
##    print(b)
    if rotation ==5:
        rotation = -2
##        print("weekend")
        continue
##    print(b)
    if day in day_off:
##        print("run")
        day+=1
        continue
    b+=1
    dayz = (b%8)-1
    x = masterlist[dayz]
##    print(day)
##    if day == dayOfYear:
##        break   
    if day== dayOfYear:
        print(weekDay[week])
        print()
        for i in range(4):
            y = x[i]
            p = classes[y]
            print(p)
    
    
