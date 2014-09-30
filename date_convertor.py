#Month Exercise
date = float(input("Please enter date as DD/MM/YYYY")

date_length = len(date)
day = date[:3] 

if day == 01:
    print("1st")

elif day == 2:
    print("2nd")

elif day == 3:
    print("3rd")

elif day >= 4 and day <= 30:
    print("{0}th".format(day))



