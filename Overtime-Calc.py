
# If the hours worked is more than 40 than overtime is accounted for by beign multiplied by 1.5.
def weeklyPay(hours, wage):
    if hours > 40:
        return 40 * wage + (hours - 40) * wage * 1.5
    else:
        return hours * wage

# This insures that the prompt is correct and valid
def getFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("This is an invalid value. Try Again. ")

# Input statements from user
hours = getFloat('How many hours did you work? ')
wage = getFloat('What was your hourly rate? ')
pay = weeklyPay(hours, wage)

# Output statement
print(f"Total pay: ${pay:.2f} ")