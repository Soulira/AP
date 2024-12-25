numbers = [1,2,3,4,5,6]

while True:
      index = int(input("Enter index (-1 to quit):"))-1
      if index not in range(len(numbers)) :
         print("Invalid value")
      else:
        value = int(input(" Enter new value: "))   
        numbers[index] = value
        print(numbers)
      if index == -1:
        break

    