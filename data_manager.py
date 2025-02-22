import csv
import os
from datetime import datetime

DATA_FILE = "transactions.csv"

def initialize_data():
    """Initialize the CSV file if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "Description", "Category", "Amount"])

def add_transaction(date, description, category, amount):
    """Append a new transaction to the CSV file."""
    with open(DATA_FILE, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date, description, category, amount])

def get_transactions():
    """Retrieve all transactions from the CSV file."""
    transactions = []
    try:
        with open(DATA_FILE, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        initialize_data()
        return []
    return transactions

def delete_transaction(index):
    """Delete a transaction by its index."""
    transactions = get_transactions()
    if 0 <= index < len(transactions):
        del transactions[index]
        with open(DATA_FILE, "w", newline="") as csvfile:
            fieldnames = ["Date", "Description", "Category", "Amount"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transactions)
    else:
        print("Invalid index")

def edit_transaction(index, date, description, category, amount):
    """Edit an existing transaction identified by its index."""
    transactions = get_transactions()
    if 0 <= index < len(transactions):
        transactions[index]["Date"] = date
        transactions[index]["Description"] = description
        transactions[index]["Category"] = category
        transactions[index]["Amount"] = amount
        with open(DATA_FILE, "w", newline="") as csvfile:
            fieldnames = ["Date", "Description", "Category", "Amount"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transactions)
    else:
        print("Invalid index")
