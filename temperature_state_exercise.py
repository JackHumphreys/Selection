#Temperature State Exercise
#Jack Humphreys

temp = int(input("Please enter temperature in centigrade: "))

if temp <= 0:
    print("Frozen")

elif temp >= 100:
    print("Boiling")

elif temp > 0 and temp < 100:
    print("Niether")
        
else:
    print("N/A")
