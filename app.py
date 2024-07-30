import csv

def display_menu():
    print("\nBudget Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Save Data")
    print("5. Load Data")
    print("6. Exit")


def add_income(income_list):
    amount = float(input("Enter income amount: "))
    category = input("Enter income category: ")
    income_list.append((amount, category))
    print("Income added successfully.")


def add_expense(expense_list):
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    expense_list.append((amount, category))
    print("Expense added successfully.")


def view_summary(income_list, expense_list):
    total_income = sum(amount for amount, _ in income_list)
    total_expenses = sum(amount for amount, _ in expense_list)
    balance = total_income - total_expenses

    print("\nSummary")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")

    print("\nIncome by Category:")
    income_by_category = {}
    for amount, category in income_list:
        if category in income_by_category:
            income_by_category[category] += amount
        else:
            income_by_category[category] = amount
    for category, amount in income_by_category.items():
        print(f"{category}: ${amount:.2f}")

    print("\nExpenses by Category:")
    expenses_by_category = {}
    for amount, category in expense_list:
        if category in expenses_by_category:
            expenses_by_category[category] += amount
        else:
            expenses_by_category[category] = amount
    for category, amount in expenses_by_category.items():
        print(f"{category}: ${amount:.2f}")


def save_data(income_list, expense_list):
    with open("budget_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Amount", "Category"])
        for amount, category in income_list:
            writer.writerow(["Income", amount, category])
        for amount, category in expense_list:
            writer.writerow(["Expense", amount, category])
    print("Data saved successfully.")


def load_data(income_list, expense_list):
    try:
        with open("budget_data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == "Income":
                    income_list.append((float(row[1]), row[2]))
                elif row[0] == "Expense":
                    expense_list.append((float(row[1]), row[2]))
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved data found.")


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
            save_data(income_list, expense_list)
        elif choice == "5":
            load_data(income_list, expense_list)
        elif choice == "6":
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
