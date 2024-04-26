def list_difference(list1, list2): # zdefiniowanie 2 list

    # Konwertuje obie listy na zbiory i znajduje różnicę zbiorów
    return list(set(list1) - set(list2))

# Example usage:
list1 = [8, 5, 6, 4, 5]
list2 = [3, 2, 5, 6, 7]
difference = list_difference(list1, list2)

print("Difference between the two lists:", difference)
