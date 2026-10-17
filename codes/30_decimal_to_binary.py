def decimal_to_binary(number):
    """Return binary digits as a string; zero returns '0'; negatives raise ValueError."""
    if number < 0:
        raise ValueError("number must not be negative")
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number //= 2
    return binary

if __name__ == "__main__":
    print(decimal_to_binary(10))
