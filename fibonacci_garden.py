"""Fibonacci Garden Growth Simulator.

Asks for a target day and reports how many flowers bloom on that day,
following the Fibonacci sequence (1, 1, 2, 3, 5, 8, ...).
"""


def flowers_on_day(target_day: int) -> int:
    """Return the Fibonacci flower count for a given day (1-indexed)."""
    if target_day < 1:
        raise ValueError("target_day must be 1 or greater")

    current_flowers = 1
    next_flowers = 1

    for _ in range(target_day - 1):
        current_flowers, next_flowers = next_flowers, current_flowers + next_flowers

    return current_flowers


def read_target_day() -> int:
    """Ask until the user enters a whole number of 1 or greater."""
    while True:
        try:
            target_day = int(input("How many days should the garden grow? "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if target_day < 1:
            print("Please enter a number 1 or greater.")
            continue

        return target_day


def main() -> None:
    target_day = read_target_day()
    result = flowers_on_day(target_day)
    print(f"On day {target_day}: {result} flowers bloomed!")


if __name__ == "__main__":
    main()