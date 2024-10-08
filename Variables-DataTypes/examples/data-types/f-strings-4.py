# Define our data
fruit1 = "Apple"
price1 = 0.50
fruit2 = "Banana"
price2 = 0.75
fruit3 = "Cherry"
price3 = 1.00

# Print header
print(f"{'Fruit':<10} | {'Price':>10}")
print(f"{'-'*10} | {'-'*10}")

# Print rows
print(f"{fruit1:<10} | ${price1:>9.2f}") 
print(f"{fruit2:<10} | ${price2:>9.2f}") 
print(f"{fruit3:<10} | ${price3:>9.2f}") 