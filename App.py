import pandas as pd

# Load data
df = pd.read_csv("sample_data.csv")

print("\n--- Expense Summary ---\n")

# Total spending
total = df["Amount"].sum()
print(f"Total Spending: ₹{total}")

# Category-wise spending
category = df.groupby("Category")["Amount"].sum()
print("\nSpending by Category:\n")
print(category)

# Highest expense category
top_category = category.idxmax()
print(f"\nHighest Spending Category: {top_category}")

# Simple AI-like suggestion
if top_category == "Food":
    print("\nSuggestion: Try reducing food delivery expenses.")
elif top_category == "Shopping":
    print("\nSuggestion: Limit unnecessary shopping.")
else:
    print("\nSuggestion: Review your top expenses to optimize savings.")
