from collections import Counter

def get_top_words(text, n=3):
    """
    Return the top-n words by frequency, breaking ties lexicographically.
    
    Args:
        text (str): Input text to analyze
        n (int): Number of top words to return (default: 3)
    
    Returns:
        list: List of tuples (word, count) sorted by frequency then lexicographically
    """
    # Normalize to lowercase and split on spaces
    words = text.lower().split()
    
    # Use Counter for efficient word counting
    word_count = Counter(words)
    
    # Sort by count (highest first), then by word (alphabetical) for tie-breaking
    # The key (-x[1], x[0]) ensures:
    # - Higher counts come first (negative count for descending order)
    # - Lexicographical order for ties (x[0] is the word)
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    # Return top n words
    return sorted_words[:n]

# Test the function with the provided sample
if __name__ == "__main__":
    text = "to be or not to be that is the question"
    print("Input:", text)
    print("Output:", get_top_words(text))
    
    # Additional test cases to verify tie-breaking
    print("\nAdditional test cases:")
    
    # Test case 1: Multiple ties
    test1 = "a a b b c c d"
    print(f"Input: {test1}")
    print(f"Output: {get_top_words(test1)}")
    
    # Test case 2: Single word
    test2 = "hello hello hello"
    print(f"Input: {test2}")
    print(f"Output: {get_top_words(test2)}")
    
    # Test case 3: All unique words
    test3 = "one two three four five"
    print(f"Input: {test3}")
    print(f"Output: {get_top_words(test3)}")
   
