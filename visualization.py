import matplotlib.pyplot as plt
import financial_operations

def visualize_category_spending():
    """Generate a pie chart for category spending."""
    category_spending = financial_operations.calculate_category_spending()
    # Filter out categories with zero or negative spending if desired
    labels = []
    amounts = []
    for category, amount in category_spending.items():
        # For visualization, you might want to only chart expenses (negative values)
        if amount < 0:
            labels.append(category)
            amounts.append(abs(amount))
    if amounts:
        plt.figure(figsize=(8, 6))
        plt.pie(amounts, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title("Spending by Category")
        plt.axis("equal")
        plt.show()
    else:
        print("No expense data available for visualization.")
