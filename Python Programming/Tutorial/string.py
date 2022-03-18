# Working with strings


phrase = "Giraffe Academy"
print("Giraffe\nAcademy") #\n is a new line
print(phrase.upper() + " is cool!")

new_phrase = phrase.upper() #UPPER CASE
print(new_phrase.isupper())
print(phrase.lower())

word = "car"
print(word.upper().isupper())
print(word.capitalize())
print(len(word))
print(word[0])

new_word = "banana academy"
print(new_word.index("academy"))
print(new_word.replace("banana", "giraffe"))