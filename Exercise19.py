words = set()
nb_words = 0

while True:
    word = input("Enter a word: ").strip()  
    if not word:  
        break
    nb_words += 1  
    
   
    if word in words:
        print("You already entered this unique word.")
        break
    
   
    words.add(word)


print("\nUnique words:")
for word in sorted(words):
    print(word)
