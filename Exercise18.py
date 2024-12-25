

numbers = [1, 2, 3, 4, 5]

while True:
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Quit")
    print("Please choose an option (1-5):")

    operation = input()

    if operation == '1':
        try:
            element = int(input("Enter value: "))
            numbers.append(element)
            print("Updated list:", numbers)
        except ValueError:
            print("Enter an integer please")     
            
    elif operation == "2":
        try:
            index = int(input("Enter the index (0 to {}): ".format(len(numbers))))
            if index not in range(len(numbers) + 1):  # Allow inserting at the end
                print("Index out of range! Please enter a valid index.")
                continue 
            element = int(input("Enter value to insert: "))  # Prompt for value to insert
            numbers.insert(index, element)
            print("Updated list:", numbers)
        except ValueError:
            print("Invalid input! Please enter integers only.")

    elif operation == "3":
        try:
            popped_element = numbers.pop()  # Pop the last element
            print(f"Popped element: {popped_element}")
            print("Updated list:", numbers)
        except IndexError:
            print("The list is already empty!")

    elif operation == '4':
        try: 
            element = int(input("Enter the integer to remove: "))
            numbers.remove(element)  # Remove the first occurrence of the value
            print("Updated list:", numbers)
        except ValueError:
            print("Element not found") 

    elif operation == '5':
        print("End of the program")
        break

    else:
        print("Invalid choice! Please select a valid option.")