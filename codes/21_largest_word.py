import string

def largest_word(sentence):
    """Return the longest word; ignore punctuation at word ends.
    If tied, return the first. If no words, return an empty string.
    """
    largest = ""
    for word in sentence.split():
        clean = word.strip(string.punctuation)
        if len(clean) > len(largest):
            largest = clean
    return largest

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Largest word:", largest_word(text))
