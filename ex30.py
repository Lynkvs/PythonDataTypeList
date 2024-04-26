def get_frequency(lst):
    # Inicjalizacja pustego słownika do przechowywania częstotliwości elementów
    frequency_dict = {}
    # Iteracja przez każdy element listy wejściowej
    for item in lst:
        # Jeśli element jest już w słowniku, zwiększ jego liczbę częstotliwości.
        if item in frequency_dict:
            frequency_dict[item] += 1
        # Jeśli elementu nie ma w słowniku, dodaj go z częstotliwością 1.
        else:
            frequency_dict[item] = 1
    return frequency_dict
# Test:
my_list = [35, 2, 43, 2, 4, 56, 5, 6, 5]
frequency = get_frequency(my_list)
# Wyświetla częstotliwość wyrazów z listy
print("Frequency of elements in the list:")
for item, freq in frequency.items():
    print(f"{item}: {freq}")
