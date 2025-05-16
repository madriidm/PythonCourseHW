# Exercise 1 – Reverse Lookup

def reverseLookup(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys

def main():
    french_dict = {
        "le": "the",
        "la": "the",
        "pomme": "apple",
        "chat": "cat"
    }

    print("The French words for 'the' are:", reverseLookup(french_dict, "the"))
    print("Expected: ['le', 'la']")
    print()

    print("The French word for 'apple' is:", reverseLookup(french_dict, "apple"))
    print("Expected: ['pomme']")
    print()

    print("The French word for 'asdf' is:", reverseLookup(french_dict, "asdf"))
    print("Expected: []")



# Exercise 2 – Sum a List of Numbers

def main():
    total = 0.0
    while True:
        line = input("Enter a number (or blank to quit): ").strip()
        if line == "":
            break
        try:
            number = float(line)
            total += number
            print("Current total:", total)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print("Final total:", total)

    # Exercise 3 – Does a String Represent an Integer?

def isInteger(s):
    s = s.strip()
    if s == "":
        return False
    if s[0] in "+-":
        return s[1:].isdigit() and len(s) > 1
    return s.isdigit()

def main():
    s = input("Enter a string to check if it's an integer: ")
    if isInteger(s):
        print("That is a valid integer.")
    else:
        print("That is NOT a valid integer.")


