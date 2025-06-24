electronics_customers = {"Alex", "Maria", "John"}
clothing_customers = {"John", "Sophia", "Maria", "Mike"}

all_customers = electronics_customers.union(clothing_customers)

# Also, you could use:
# all_customers = electronics_customers | clothing_customers

print(all_customers) # {"Maria", "Alex", "Mike", "John", "Sophia"}



regular_customers = electronics_customers.intersection(clothing_customers)

# Also, we could use:
# regular_customers = electronics_customers & clothing_customers

print(regular_customers) # {"John", "Maria"}



exclusive_electronics_customers = electronics_customers.difference(clothing_customers)

# Also, we could use:
# exclusive_electronics_customers = electronics_customers - clothing_customers

print(exclusive_electronics_customers) # {"Alex"}




unique_customers = electronics_customers.symmetric_difference(clothing_customers)

# Also, we could use:
# unique_customers = electronics_customers ^ clothing_customers

print(unique_customers)  # {"Alex", "Mike", "Sophia"}
