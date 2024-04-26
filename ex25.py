import random
# użycie metody random.choice
def select_random_item(lst):
    return random.choice(lst)

# Test:
my_list = [1, 2, 3, 4, 5]
random_item = select_random_item(my_list)

print("Randomly selected item:", random_item)
