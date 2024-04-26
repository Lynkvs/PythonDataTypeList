def find_smallest(lst):
    if not lst:  # jeśli lista pusta nie zwracaj nic
        return None
    smallest = lst[0]  # Przyjmij, że pierwsza liczba jest najmniejsza
    for num in lst:  # Iteruj przez każdą liczbę z tablicy
        if num < smallest:  # Jeśli aktualna liczba jest mniejsza niż najmniejsza dotychczasowa
            smallest = num  # zaktualizuj najmniejszą liczbę
    return smallest

# Test:
my_list = [13, 4, 1, 8, 15]
print("Smallest number in the list:", find_smallest(my_list))
