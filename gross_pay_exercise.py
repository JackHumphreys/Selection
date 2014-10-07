#Jack Humphreys
#Gross Pay Exercise

hours = float(input("Please enter the hours you work in a week: "))
pay = float(input("Please enter hourly pay: "))

if hours > 60:
    print("ERROR")

elif hours > 40:
    print("Gross pay is: {0}".format((pay*40)+(hours-40)*(pay*1.5)))

else:
    print("Gross pay is: {0}".format(pay*hours))

