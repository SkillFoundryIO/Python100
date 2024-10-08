# We can convert the string input in the same line if we choose.
# This is called method chaining.
bill_amount = float(input("Enter the total bill amount: $"))
tip_percentage = float(input("Enter the tip percentage: "))

tip = bill_amount * (tip_percentage / 100)
total_bill = bill_amount + tip

print(f"For a bill of ${bill_amount:.2f} with a {tip_percentage:.1f}% tip, the tip is ${tip:.2f} for a total of ${total_bill:.2f}.")