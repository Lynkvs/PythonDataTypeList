def are_circularly_identical(list1, list2):
    # sprawdzenie czy dł. oby list jest taka sama
    if len(list1) != len(list2):
        return False
    concatenated_list1 = list1 + list1
    if ''.join(map(str, list2)) in ''.join(map(str, concatenated_list1)):
        return True
    else:
        return False
# Test
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 1, 2, 3]
result = are_circularly_identical(list1, list2)

if result:
    print("The lists are circularly identical.")
else:
    print("The lists are not circularly identical.")
