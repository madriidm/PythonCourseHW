# Detyra 4
from random import randrange

def roll_two_dice():
    return randrange(1, 7) + randrange(1, 7)

def main():
    num_runs = 1000
    expected = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
        7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }
    counts = {i: 0 for i in range(2, 13)}
    for _ in range(num_runs):
        total = roll_two_dice()
        counts[total] += 1
    print("Total | Simulated % | Expected %")
    for total in sorted(counts.keys()):
        simulated = counts[total] / num_runs * 100
        expected_percent = expected[total] * 100
        print(f"{total:5} | {simulated:11.2f} | {expected_percent:10.2f}")

if __name__ == "__main__":
    main()
