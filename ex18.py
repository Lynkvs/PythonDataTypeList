from itertools import permutations #zaimportowanie permutacji z biblioteki
def generate_permutations(lst):
    # Użyj funkcji permutacji z itertools, aby wygenerować wszystkie permutacje
    return list(permutations(lst))

# Example usage:
my_list = [1, 2, 3]
all_permutations = generate_permutations(my_list)

print("All permutations of the list:", all_permutations)
