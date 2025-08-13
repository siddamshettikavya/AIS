def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
print(count_vowels("hello"))   
print(count_vowels("OpenAI"))  
print(count_vowels("sky"))     