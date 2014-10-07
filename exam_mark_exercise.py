#Exam mark exercise
#Jack Humphreys

mark = int(input("Please enter mark: "))

if 0 <= mark <= 40:
    print("Grade U")

elif 41 <= mark <= 50:
    print("Grade E")

elif 51 <= mark <= 60:
    print("Grade D")

elif 61 <= mark <= 70:
    print("Grade C")

elif 71 <= mark <= 80:
    print("Grade B")

elif 81 <= mark <= 100:
    print("Grade A")

else:
    print("This is not a mark")


