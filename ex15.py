import random
def shuffle_and_print(lst):

    random.shuffle(lst)  # pomieszaj listę
    print("Shuffled list:", lst)


# Test:
my_list = [1, 2, 3, 4, 5]
shuffle_and_print(my_list)
