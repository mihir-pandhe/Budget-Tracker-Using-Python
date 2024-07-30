def display_menu():
    print("\nBudget Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Exit")


def add_income(income_list):
    amount = float(input("Enter income amount: "))
    income_list.append(amount)
    print("Income added successfully.")


def add_expense(expense_list):
    amount = float(input("Enter expense amount: "))
    expense_list.append(amount)
    print("Expense added successfully.")


def view_summary(income_list, expense_list):
    total_income = sum(income_list)
    total_expenses = sum(expense_list)
    balance = total_income - total_expenses

    print("\nSummary")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")


def main():
    income_list = []
    expense_list = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_income(income_list)
        elif choice == "2":
            add_expense(expense_list)
        elif choice == "3":
            view_summary(income_list, expense_list)
        elif choice == "4":
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
