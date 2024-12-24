

age1 = input("Please type in the age of the first person:")
age2 = input("Please type in the age of the first person:")

if int(age1) == int(age2):
    print("Both people are the same age!")
else :
    print("The older age is:",max(int(age1),int(age2)))