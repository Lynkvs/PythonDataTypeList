def find_long_words(words, n):
    # Użycie listy, aby odfiltrować słowa dłuższe niż n
    return [word for word in words if len(word) > n]

# Test:
word_list = ["samolot", "rower", "samochód", "deska", "rolki"]
threshold = 5
long_words = find_long_words(word_list, threshold)

print(f"Words longer than {threshold} characters:", long_words)
