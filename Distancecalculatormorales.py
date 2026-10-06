#Distance calculator
##ask for desired number of kilometers and input of the conversion.
kilometers = float(input("Enter distance in kilometers: "))
conversion = 0.621371
#calculate for miles in number
miles = kilometers * conversion
print("Distance in miles: ",miles)
#ask if they want to retake the program
question = input("do you want to convert anoher distance?(yes/no)")
##justify their answer
if question == "yes":
    kilometers2 = float(input("Enter distance in kilometers: "))
    miles2 = kilometers2 * conversion
    print("Distance in miles: ",miles2)
else:
    print("program ended.")
