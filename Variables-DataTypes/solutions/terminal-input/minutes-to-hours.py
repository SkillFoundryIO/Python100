total_minutes = int(input("Enter the number of minutes: "))

# Hours should use integer division, truncating the remainder
hours = total_minutes // 60
# Remaining minutes uses modulo to only get the remainder portion with hours already accounted for.
remaining_minutes = total_minutes % 60

print(f"{total_minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes.")