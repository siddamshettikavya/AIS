def word_frequency(text):
    freq = {}
    words = text.split()
    for word in words:
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
    return freq

# Example usage:
text = input("Enter a sentence: ")
print(word_frequency(text))