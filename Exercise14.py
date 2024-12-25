user_input = input("Please enter a string: ")

width = 30

space = (width - len(user_input)) // 2

print('*' * width)

print('*' + ' ' * space + user_input + ' ' * (width - len(user_input) - space - 2) + '*')

print('*' * width)