def get_unique_values(lst):
    # Konwertuje listę na zestaw, aby usunąć duplikaty, a następnie konwertuje ją z powrotem na listę.
    return list(set(lst))

# Test:
my_list = [3, 5, 7, 7, 4, 2, 6, 6, 5]
unique_values = get_unique_values(my_list)

print("Unique values from the list:", unique_values)
