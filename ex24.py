def append_list(list1, list2):
    # Użycie metody extend(), aby dołączyć wszystkie elementy z listy2 do listy1.
    list1.extend(list2)
    return list1

# Test:
first_list = [6, 7, 8]
second_list = [9, 10, 11]
result_list = append_list(first_list, second_list)

print("Resulting list after appending:", result_list)
