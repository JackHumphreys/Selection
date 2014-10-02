#Month Exercise
date = str(input("Please enter date as DD/MM/YYYY: "))

date.split("/")
day,month,year = date.split("/")


if day == 1:
    print("1st")

elif day == 2:
    print("2nd")

elif day == 3:
    print("3rd")

elif day == 4:
    print("{0}th".format(day))





