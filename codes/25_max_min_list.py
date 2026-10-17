def find_max_min(numbers):
    """Return (maximum, minimum); raise ValueError for an empty list."""
    if not numbers:
        raise ValueError("numbers must not be empty")
    maximum = numbers[0]
    minimum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    return (maximum, minimum)

if __name__ == "__main__":
    print(find_max_min([4, 9, 1, 7]))
