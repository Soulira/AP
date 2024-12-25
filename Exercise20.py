user_list = []

while True:
    number = int(input("Enter a number (-1 to quit): "))
    if number == -1:
        break
    user_list.append(number)
    print("Current List:", user_list)
    print("Sorted List:", sorted(user_list))