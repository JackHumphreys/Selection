#Date Exercise
date = input("Please enter date as DD/MM/YY: ")
day_input = int(date[:2])
month_input = int(date[3:5])
year_input = int(date[6:8])

if day_input == 1:
    day = ("1st")

elif day_input == 2:
    day = ("2nd")

elif day_input == 3:
    day = ("3rd")

elif day_input >= 4 and day_input <=30:
    day = ("{0}th".format(day_input))
    

else:
    day = ("N/A")





if month_input == 1:
    month = ("January")

elif month_input == 2:
    month = ("February")

elif month_input == 3:
    month = ("March")

elif month_input == 4:
    month = ("April")

elif month_input == 5:
    month = ("May")

elif month_input == 6:
    month = ("June")

elif month_input == 7:
    month = ("July")

elif month_input == 8:
    month = ("August")

elif month_input == 9:
    month = ("September")

elif month_input == 10:
    month = ("October")

elif month_input == 11:
    month = ("November")
    
elif month_input == 12:
    month = ("December")

else:
    month = ("N/A")



if year_input >= 30:
    year = ("19{0}".format(year_input))

elif year_input <= 30:
    year = ("20{0}".format(year_input))







print(day, month, year)
