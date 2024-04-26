def list_to_string(char_list):
    # Użycie metody join(), aby połączyć wszystkie znaki w string
    return ''.join(char_list)


# Test:
char_list = ['s', 'a', 'm', 'o', 'l', 'o', 't']
result_string = list_to_string(char_list)

print("Resulting string:", result_string)
