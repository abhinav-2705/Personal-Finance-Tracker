import data_manager
import financial_operations
import visualization
from datetime import datetime

def print_menu():
    print("\nPersonal Finance Tracker")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Calculate Balance")
    print("4. Visualize Category Spending")
    print("5. Delete Transaction")
    print("6. Edit Transaction")
    print("7. Exit")

def main():
    data_manager.initialize_data()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Automatically use today's date or let user specify
            use_today = input("Use today's date? (y/n): ").strip().lower()
            if use_today == "y":
                date = datetime.now().strftime("%Y-%m-%d")
            else:
                date = input("Enter date (YYYY-MM-DD): ")
            description = input("Description: ")
            category = input("Category: ")
            try:
                amount = float(input("Amount (positive for income, negative for expense): "))
            except ValueError:
                print("Invalid amount. Transaction not added.")
                continue
            data_manager.add_transaction(date, description, category, amount)
            print("Transaction added successfully.")

        elif choice == "2":
            transactions = data_manager.get_transactions()
            if transactions:
                for i, transaction in enumerate(transactions):
                    print(f"{i}: {transaction}")
            else:
                print("No transactions found.")

        elif choice == "3":
            balance = financial_operations.calculate_balance()
            print(f"Overall Balance: {balance:.2f}")

        elif choice == "4":
            visualization.visualize_category_spending()

        elif choice == "5":
            try:
                index = int(input("Enter index of transaction to delete: "))
                data_manager.delete_transaction(index)
                print("Transaction deleted successfully.")
            except ValueError:
                print("Invalid index input.")

        elif choice == "6":
            try:
                index = int(input("Enter index of transaction to edit: "))
            except ValueError:
                print("Invalid index input.")
                continue
            date = input("Enter new date (YYYY-MM-DD): ")
            description = input("Enter new description: ")
            category = input("Enter new category: ")
            try:
                amount = float(input("Enter new amount: "))
            except ValueError:
                print("Invalid amount. Edit aborted.")
                continue
            data_manager.edit_transaction(index, date, description, category, amount)
            print("Transaction updated successfully.")

        elif choice == "7":
            print("Exiting Personal Finance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
