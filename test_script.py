from string_tools import formatting, analysis

text = "   hello world    "
print("Original: ", repr(text))
print("Capitalized: ", formatting.capitalize_words(text))
print("Trimmed:", formatting.remove_whitespace(text))

print("-" * 30)

sample = "Radar"
print(f"Text: {sample}")
print("Is palindrome?", analysis.is_palindrome(sample))
print("Number of vowels: ", analysis.count_vowels(sample))