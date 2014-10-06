#Jack Humphreys
#Gross Pay Exercise

hours = float(input("Please enter the hours you work in a week: "))
pay = float(input("Please enter hourly pay: "))

pay_extra = ((hours*pay)+(pay-40)*1.5)

if pay > 40:
    print("Gross pay is: {0}".format(pay_extra))

elif hours > 60:
    print("ERROR")

else:
    print("Gross pay is: {0}".format(hours*pay))

