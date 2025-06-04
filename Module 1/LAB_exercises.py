
# LAB 2.1.12 – The print() function and its arguments
print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

print("\n" + "-"*40)

# LAB 2.1.13 – Formatting the output
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

print("\n" + "-"*40)

# LAB 2.2.6 – Python literals - strings
print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")

print("\n" + "-"*40)

# LAB 2.4.7 – Variables
john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=", ")
total_apples = john + mary + adam
print(total_apples)
print("Total number of apples:", total_apples)

print("\n" + "-"*40)

# LAB 2.4.9 – Variables - a simple converter
kilometers = 12.25
miles = 7.38
miles_to_kilometers = round(miles * 1.61, 2)
kilometers_to_miles = round(kilometers / 1.61, 2)
print(miles, "miles is", miles_to_kilometers, "kilometers")
print(kilometers, "kilometers is", kilometers_to_miles, "miles")

print("\n" + "-"*40)

# LAB 2.4.10 – Operators and expressions
x = 1  # change this to test other inputs
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

print("\n" + "-"*40)

# LAB 2.5.3 – Comments
# This program computes the number of seconds in a given number of hours
hours = 2  # number of hours
seconds = 3600  # number of seconds in 1 hour
print("Hours:", hours)  # print hours
print("Seconds in Hours:", hours * seconds)  # print total seconds
print("Goodbye!")  # end message

print("\n" + "-"*40)

# LAB 2.6.9 – Simple input and output
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("\nThat's all, folks!")

print("\n" + "-"*40)

# LAB 2.6.10 – Operators and expressions
x = float(input("Enter value for x: "))
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))
print("y =", y)

print("\n" + "-"*40)

# LAB 2.6.11 – Operators and expressions – 2
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
total_minutes = hour * 60 + mins + dura
end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60
print(f"{end_hour}:{end_minute}")
