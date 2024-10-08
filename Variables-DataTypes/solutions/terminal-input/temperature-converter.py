fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9 # Need parenthesis for order of operations.

print(f"{fahrenheit:.1f}F is equal to {celsius:.1f}C.")