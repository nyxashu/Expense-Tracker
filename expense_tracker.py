import json
import os

FILE_PATH = 'expenses.json'

def load_expenses():
    """Load expenses from a file."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    """Save expenses to a file."""
    with open(FILE_PATH, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(amount, category, description):
    """Add a new expense."""
    expenses = load_expenses()
    expense = {
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added: {amount} in category '{category}' with description '{description}'.")

def view_expenses():
    """View all expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
    else:
        print("Expenses:")
        for idx, expense in enumerate(expenses, 1):
            print(f"{idx}. Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

def view_expenses_by_category(category):
    """View expenses by category."""
    expenses = load_expenses()
    category_expenses = [expense for expense in expenses if expense['category'] == category]
    if not category_expenses:
        print(f"No expenses found in category '{category}'.")
    else:
        print(f"Expenses in category '{category}':")
        for idx, expense in enumerate(category_expenses, 1):
            print(f"{idx}. Amount: {expense['amount']}, Description: {expense['description']}")

def main():
    """Main function to run the application."""
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            add_expense(amount, category, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category = input("Enter the category to filter by: ")
            view_expenses_by_category(category)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
