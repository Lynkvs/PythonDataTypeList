def access_index(lst):
  #  Iteracja po każdym elemencie listy wraz z jego indeksem
    for index, element in enumerate(lst):
        print(f"Index: {index}, Element: {element}")


# Test:
my_list = [10, 20, 30, 40, 50]
access_index(my_list)
