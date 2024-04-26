def is_list_empty(lst):
    return len(lst) == 0


# Test:
my_list = [1, 2, 3]
if is_list_empty(my_list):
    print("The list is empty.")
else:
    print("The list is not empty.")
