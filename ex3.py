def find_largest(lst):
    if not lst:  # jeśli lista pusta nie zwracaj nic
        return None
    largest = lst[0]  # Przyjmij, że pierwsza liczba jest największa
    for num in lst:  # Iteruj przez każdą liczbę w tablicy
        if num > largest:  # Jeśli bieżąca liczba jest większa niż największa do tej pory
            largest = num  # zaktualizuj największą liczbę
    return largest

# Test:
my_list = [30, 5, 60, 8, 15]
print("Largest number in the list:", find_largest(my_list))
