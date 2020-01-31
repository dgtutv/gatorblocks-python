##Property of Daniel Todd
##run this file 
import datetime
import calendar
import json
from datetime import datetime
with open('days_off.txt', 'r') as filehandle:
    dayOff=json.load(filehandle)
with open('classes.txt', 'r') as filehandle:
    classes = json.load(filehandle)
with open('referenceBegin.txt', 'r') as filehandle:
    begin = json.load(filehandle)
with open('referenceEnd.txt', 'r') as filehandle:
    end = json.load(filehandle)
with open('referenceFinal.txt', 'r') as filehandle:
    Final = json.load(filehandle)
with open('referenceLastDay.txt', 'r') as filehandle:
    LastDay = json.load(filehandle)
with open('referenceFirstDay.txt', 'r') as filehandle:
    FirstDay = json.load(filehandle)    
day_of_year = datetime.now().timetuple().tm_yday   #day of year from date
now = datetime.now()  #current date
week = calendar.weekday(now.year, now.month, now.day)   #get day of week
day1 = [0,1,2,3]
day2 = [4,5,6,7]
day3 = [2,3,0,1]
day4 = [6,7,4,5]        #These are my block rotations
day5 = [1,0,3,2]
day6 = [5,4,7,6]
day7 = [3,2,1,0]
day8 = [7,6,5,4]
weekDay = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]    #Used for assigning a number to days of the week, mostly useful for determining at which point the block rotations should start
masterlist = [day1,day2,day3,day4,day5,day6,day7,day8]     #This list is used for rotating through the block rotations
#247, first day of scool
#176, days in school year

day_of_year=153   #debugging date

w=0     #counter for running through and iterating list of days off
counter=0     #counter for the number of days running through the main for loop, not including weekends or days off
if day_of_year<Final-1:  #Final is the dev inputted number that inicates the last day of school
    day_of_year+=365
day_of_year-=begin
for offDay in dayOff:    #from list of days off in day of year format, converts to day of school year    
    if dayOff[w] < Final-1:    
        dayOff[w]+=365    #This is similar to the if statement above, just appplies to a list
    dayOff[w]-=begin
    w+=1
rotation=(weekDay.index(FirstDay)-1)
print(weekDay[week])
print()
for day in range(365):      #iterates through every day from the start of school until today, this is because we want to use modulo to tell which block rotation should be used
    #even if not a school day we still want to display day of week
    rotation+=1
    if rotation ==-1:
        continue
    if rotation ==5:        #This code skips weekends
        rotation=-2
        continue
    if day in dayOff:
        continue
    dayz=(counter%8)        #This code skips dev entered days off school
    counter+=1
    x=masterlist[dayz]
    if day == day_of_year:      #When the code reaches to todays date, it will use modulo to tell which rotation is appropiate and then will cycle through the afformentioned lists to display today's classes
        for i in range(4):
            y = x[i]
            p = classes[y]
            print(p)
print()
input("Press ENTER to end program")     #Windows will not run without this 

