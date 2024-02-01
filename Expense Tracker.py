class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def view_expenses(self):
        print("Expense Tracker:")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")

# Example usage
tracker = ExpenseTracker()

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        tracker.add_expense(category, amount)
        print("Expense added successfully!")

    elif choice == '2':
        tracker.view_expenses()

    elif choice == '3':
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")