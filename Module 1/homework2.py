# Exercise 1: Palindrome
text = input("Enter a string: ").lower()
is_palindrome = True
for i in range(len(text) // 2):
    if text[i] != text[-(i + 1)]:
        is_palindrome = False
        break
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# Exercise 2: Greatest Common Divisor
n = int(input("Enter the first positive integer: "))
m = int(input("Enter the second positive integer: "))
d = min(n, m)
while n % d != 0 or m % d != 0:
    d -= 1
print("The greatest common divisor is:", d)


# Exercise 3: Area of a Room
length = float(input("Enter the length of the room (m): "))
width = float(input("Enter the width of the room (m): "))
area = length * width
print(f"The area of the room is {area} square meters.")


# Exercise 4: Admission Price
BABY_LIMIT = 2
CHILD_LIMIT = 12
ADULT_LIMIT = 64
CHILD_PRICE = 14.00
SENIOR_PRICE = 18.00
ADULT_PRICE = 23.00

total = 0.0
while True:
    age_input = input("Enter guest age (blank to finish): ")
    if age_input == "":
        break
    age = int(age_input)
    if age <= BABY_LIMIT:
        cost = 0.00
    elif age <= CHILD_LIMIT:
        cost = CHILD_PRICE
    elif age > ADULT_LIMIT:
        cost = SENIOR_PRICE
    else:
        cost = ADULT_PRICE
    total += cost
print(f"The total admission cost is ${total:.2f}")


# Exercise 5: Avoiding Duplicates
words = []
while True:
    word = input("Enter a word (blank to finish): ").lower()
    if word == "":
        break
    if word not in words:
        words.append(word)
for w in words:
    print(w)
