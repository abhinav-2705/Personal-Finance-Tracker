import data_manager

def calculate_balance():
    """Calculate the overall balance from all transactions."""
    transactions = data_manager.get_transactions()
    balance = 0.0
    for transaction in transactions:
        try:
            balance += float(transaction["Amount"])
        except ValueError:
            continue
    return balance

def calculate_category_spending():
    """
    Calculate total spending per category.
    Expenses should be negative amounts and incomes positive;
    adjust as necessary for your use case.
    """
    transactions = data_manager.get_transactions()
    category_spending = {}
    for transaction in transactions:
        category = transaction["Category"]
        try:
            amount = float(transaction["Amount"])
        except ValueError:
            amount = 0.0
        # Summing amounts by category
        if category in category_spending:
            category_spending[category] += amount
        else:
            category_spending[category] = amount
    return category_spending
