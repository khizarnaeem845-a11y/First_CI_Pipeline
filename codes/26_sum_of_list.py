def sum_of_list(numbers):
    """Return the total of all numbers; an empty list returns 0."""
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == "__main__":
    print(sum_of_list([1, 2, 3, 4]))
