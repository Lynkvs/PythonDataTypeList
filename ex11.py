def has_common_member(list1, list2):
#stworzenie 2 list
    # Konwertuje obie listy na zbiory i sprawdza, czy nie są niepuste.
    return bool(set(list1) & set(list2))


# Test:
list1 = [5, 3, 3, 5, 5]
list2 = [5, 6, 7, 4, 9]
print("Do the lists have at least one common member?", has_common_member(list1, list2))
