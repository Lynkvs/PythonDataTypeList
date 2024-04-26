
drinks = ['cola', 'fanta', 'sprite']

print("Original List: ", drinks)

drinks = [v for elt in drinks for v in ('zero', elt)]
print("Updated List: ", drinks)
