word = input("Enter your word: ")


i = 0
is_p = True

while i < len(word) // 2 and is_p:
    if word[i] != word[len(word) - 1 - i]:  
        is_p = False
    i += 1  


if is_p:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")