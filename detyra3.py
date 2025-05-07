# Detyra 3

# Exercise 1: Unique Characters
def unique_characters():
    user_input = input("Enter a string: ")
    unique_chars = {}
    for ch in user_input:
        unique_chars[ch] = True
    print(f"Number of unique characters: {len(unique_chars)}")

# Exercise 2: Remove Outliers
def remove_outliers(data, n):
    if len(data) < 2 * n:
        return None
    sorted_data = sorted(data)
    for _ in range(n):
        sorted_data.pop()       # remove largest
        sorted_data.pop(0)      # remove smallest
    return sorted_data

def main_outliers():
    values = []
    while True:
        line = input("Enter a number (blank to stop): ")
        if line == "":
            break
        try:
            num = float(line)
            values.append(num)
        except:
            print("Invalid number.")
    if len(values) < 4:
        print("Error: Need at least 4 values.")
    else:
        filtered = remove_outliers(values, 2)
        print("With outliers removed:", filtered)
        print("Original list:", values)

# Exercise 3: Anagrams
def character_counts(s):
    counts = {}
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

def main_anagrams():
    s1 = input("Enter first word: ")
    s2 = input("Enter second word: ")
    if character_counts(s1) == character_counts(s2):
        print("They are anagrams.")
    else:
        print("They are not anagrams.")

if __name__ == "__main__":
    unique_characters()
    main_outliers()
    main_anagrams()
