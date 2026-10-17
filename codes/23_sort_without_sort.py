def bubble_sort(numbers):
    """Return a new list in ascending order without changing the input list."""
    result = numbers.copy()
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result

if __name__ == "__main__":
    print(bubble_sort([5, 2, 9, 1]))
