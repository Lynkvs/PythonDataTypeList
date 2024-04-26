def sum_list(lst):
    total = 0
    for num in lst: #przejście przez każdą pozycje w liscie
        total += num #dodawanie każdej pozycji z listy
    return total

# Test:
my_list = [23, 5, 8, 11, 3]
print("Sum of list items:", sum_list(my_list))
