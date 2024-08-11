# Create a list of tuples with friends' names and the length of each name
friends = ["riya", "maya", "jaya", "siya","piya"]
friends_tuples = [(name, len(name)) for name in friends]
for friend in friends_tuples:
    print(friend)

# Part 2: Track and compare trip expenses
# Your expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Your partner's expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

# Print the total expenses
print("\nTotal expenses:")
print(f"Your total expenses: ${your_total}")
print(f"Partner's total expenses: ${partner_total}")

# Determine who spent more
if your_total > partner_total:
    print("\nYou spent more money overall.")
elif your_total < partner_total:
    print("\nYour partner spent more money overall.")
else:
    print("\nBoth spent the same amount.")

# Find the expense category with the significant difference
print("\nExpense categories with significant differences:")
for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > 100:  # Considering a difference > $100 as significant
        print(f"Category: {category}, Difference: ${difference}")
