def clone_list(lst):

    return lst[:]  # Używanie wycinania listy do tworzenia kopii

# Test:
original_list = [3, 2, 4, 1, 6]
cloned_list = clone_list(original_list)

print("Original list:", original_list)
print("Cloned list:", cloned_list)
