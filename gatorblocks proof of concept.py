##Property of Daniel Todd
##run this file 
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
w=0
day_off =[]
for offDay in dayOff:#from list of days off in day of year format, converts to day of school year    
    if dayOff[w] >246:
        day_off += [dayOff[w]-247]
    else:
        day_off += [dayOff[w]+120]
    w+=1
def before():
    dayOfYear=day_of_year-247#converts current day to day of school year
    rotation =1
    b=0#a counter for total days that have been ran through the loop
    for day in range(421):
        rotation+=1
        if rotation ==-1:
            continue
        if rotation ==5:
            rotation = -2
            continue
        if day in day_off:
            day+=1
            continue
        b+=1
        dayz = (b%8)-1
        x = masterlist[dayz] 
        if day== dayOfYear:
            print(weekDay[week])
            print()
            for i in range(4):
                y = x[i]
                p = classes[y]
                print(p)
    
def after():
    dayOfYear=day_of_year+120#converts current day to day of school year
    rotation =-1
    b=-1#a counter for total days that have been ran through the loop
    for day in range(421):
        rotation+=1
        if rotation ==-1:
            continue
        if rotation ==5:
            rotation = -2
            continue
        if day in day_off:
            day+=1
            continue
        b+=1
        dayz = (b%8)-1
        x = masterlist[dayz] 
        if day== dayOfYear:
            print(weekDay[week])
            print()
            for i in range(4):
                y = x[i]
                p = classes[y]
                print(p)
#used for testing
if day_of_year>=246:
    before()
else:
    after()
    
    
