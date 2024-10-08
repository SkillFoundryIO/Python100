x = 5
y = 3

print(f"Is {x} greater than {y}? {x > y}")
print(f"Is {x} less than {y}? {x < y}")

age = 25
is_citizen = True

# using the and operator to combine two expressions
print(f"Eligible to vote? {age >= 18 and is_citizen == True}")
# for boolean values, we do not need to specify == True. A boolean is true/false
print(f"Eligible to vote? {age >= 18 and is_citizen}")

temp_celcius = 8.25
is_raining = False

# using the or operator to combine two expressions
print(f"Should we wear a coat? {temp_celcius < 10 or is_raining}")

# using not to reverse a boolean value
is_workday = True

print(f"Should we sleep in? {not is_workday}")

print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False


# transactions only allowed if the account is open 
# and the remaining balance is positive or overdraft
# is allowed
balance = 500.25
transaction = -250
status = "Open"
allow_overdraft = True

print(f"Allow Transaction? {((balance + transaction > 0) or (allow_overdraft)) and (status == "Open")}")

is_open = status == "Open"
available_balance = balance + transaction > 0

print(f"Allow Transaction? {is_open and (available_balance or allow_overdraft)}")