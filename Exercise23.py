while True:
    try:
        N = int(input("Please enter a positive integer N: "))
        if N <= 0:
            print("Invalid input! Please enter a positive integer.")
            continue
        break  
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


for i in range(-N, N + 1):
    if i != 0:
        print(i)