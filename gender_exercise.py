first = input("Please enter your first name: ")
last = input("Please enter last name: ")
gender = str(input("Please enter m or f for your gender:"))

if gender == f:
    print("Mr {0} {1}".format(first,last))

elif gender == m:
    print("Ms {0} {1}".format(first,last))
else:
          print("Please enter an appropriate gender.")
