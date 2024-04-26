def remove_duplicates(lst):
    seen = set()  # Śledzenie elementów
    result = []  # Lista do przechowywania elementów bez duplikatów
    for item in lst:
        if item not in seen:  # jeśli element nie był widziany
            result.append(item)  # dodaj do listy
            seen.add(item)  # oznacz jako widziany
    return result
# Test:
my_list = [3, 4, 2, 3, 4, 4, 8]
print("List with duplicates removed:", remove_duplicates(my_list))
