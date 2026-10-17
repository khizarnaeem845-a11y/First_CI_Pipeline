def rotate_list(items, k):
    """Return a new list rotated right by k; negative k rotates left."""
    if not items:
        return []
    shift = k % len(items)
    if shift == 0:
        return items.copy()
    return items[-shift:] + items[:-shift]

if __name__ == "__main__":
    print(rotate_list([1, 2, 3, 4, 5], 2))
