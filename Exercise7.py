year = input("Please type in a year:")

if int(year)%4 == 0 :
    print("That year is a leap year")
else:
    if  int(year)%100 == 0 and int(year)%400 == 0:
        print("hat year is a leap year")
    else :
        print("That year is not a leap year.")
    
