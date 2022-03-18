def translate(phrase):
    result = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": #or letter.lower() in "aeiou"
            if letter.isupper():
                result += "G"
            else:
                result += "g"
        else:
            result += letter
    return result

print(translate(input("Enter a phrase: ")))