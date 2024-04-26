def multiply_list(lst):
    #Funkcja do mnożenia wszystkich wartości z listy
    result = 1
    for num in lst: #przejście przez każdą pozycje w liscie
        result *= num #mnożenie pozycji z listy
    return result

# Test
my_list = [1, 2, 3, 4, 5]
print("Product of list items:", multiply_list(my_list))
