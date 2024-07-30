import csv
from datetime import datetime

def display_menu():
    print("\nBudget Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Set Budget Limit")
    print("5. Save Data")
    print("6. Load Data")
    print("7. Exit")


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_date_input(prompt):
    while True:
        try:
            date_str = input(prompt)
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")


def add_income(income_list):
    amount = get_float_input("Enter income amount: ")
    category = input("Enter income category: ")
    date = get_date_input("Enter date (YYYY-MM-DD): ")
    income_list.append((amount, category, date))
    print("Income added successfully.")


def add_expense(expense_list):
    amount = get_float_input("Enter expense amount: ")
    category = input("Enter expense category: ")
    date = get_date_input("Enter date (YYYY-MM-DD): ")
    expense_list.append((amount, category, date))
    print("Expense added successfully.")


def view_summary(income_list, expense_list):
    total_income = sum(amount for amount, _, _ in income_list)
    total_expenses = sum(amount for amount, _, _ in expense_list)
    balance = total_income - total_expenses

    print("\nSummary")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")

    print("\nIncome by Category:")
    income_by_category = {}
    for amount, category, _ in income_list:
        if category in income_by_category:
            income_by_category[category] += amount
        else:
            income_by_category[category] = amount
    for category, amount in income_by_category.items():
        print(f"{category}: ${amount:.2f}")

    print("\nExpenses by Category:")
    expenses_by_category = {}
    for amount, category, _ in expense_list:
        if category in expenses_by_category:
            expenses_by_category[category] += amount
        else:
            expenses_by_category[category] = amount
    for category, amount in expenses_by_category.items():
        print(f"{category}: ${amount:.2f}")

    print("\nMonthly Summary:")
    income_by_month = {}
    for amount, category, date in income_list:
        month = date.strftime("%Y-%m")
        if month in income_by_month:
            income_by_month[month] += amount
        else:
            income_by_month[month] = amount
    for month, amount in income_by_month.items():
        print(f"Income for {month}: ${amount:.2f}")

    expenses_by_month = {}
    for amount, category, date in expense_list:
        month = date.strftime("%Y-%m")
        if month in expenses_by_month:
            expenses_by_month[month] += amount
        else:
            expenses_by_month[month] = amount
    for month, amount in expenses_by_month.items():
        print(f"Expenses for {month}: ${amount:.2f}")

    if income_list:
        max_income = max(income_list, key=lambda x: x[0])
        print(
            f"\nHighest Income: ${max_income[0]:.2f} in category {max_income[1]} on {max_income[2].strftime('%Y-%m-%d')}"
        )

    if expense_list:
        max_expense = max(expense_list, key=lambda x: x[0])
        print(
            f"Highest Expense: ${max_expense[0]:.2f} in category {max_expense[1]} on {max_expense[2].strftime('%Y-%m-%d')}"
        )


def set_budget_limit(budget_limits):
    category = input("Enter category to set budget limit: ")
    limit = get_float_input("Enter budget limit: ")
    budget_limits[category] = limit
    print("Budget limit set successfully.")


def check_budget(expense_list, budget_limits):
    expenses_by_category = {}
    for amount, category, _ in expense_list:
        if category in expenses_by_category:
            expenses_by_category[category] += amount
        else:
            expenses_by_category[category] = amount

    for category, limit in budget_limits.items():
        if category in expenses_by_category and expenses_by_category[category] > limit:
            print(f"Alert: You have exceeded the budget limit for {category}!")


def save_data(income_list, expense_list, budget_limits):
    try:
        with open("budget_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Amount", "Category", "Date"])
            for amount, category, date in income_list:
                writer.writerow(["Income", amount, category, date.strftime("%Y-%m-%d")])
            for amount, category, date in expense_list:
                writer.writerow(
                    ["Expense", amount, category, date.strftime("%Y-%m-%d")]
                )
        with open("budget_limits.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Limit"])
            for category, limit in budget_limits.items():
                writer.writerow([category, limit])
        print("Data saved successfully.")
    except IOError as e:
        print(f"An error occurred while saving data: {e}")


def load_data(income_list, expense_list, budget_limits):
    try:
        with open("budget_data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == "Income":
                    income_list.append(
                        (float(row[1]), row[2], datetime.strptime(row[3], "%Y-%m-%d"))
                    )
                elif row[0] == "Expense":
                    expense_list.append(
                        (float(row[1]), row[2], datetime.strptime(row[3], "%Y-%m-%d"))
                    )
        with open("budget_limits.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                budget_limits[row[0]] = float(row[1])
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved data found.")
    except IOError as e:
        print(f"An error occurred while loading data: {e}")
    except ValueError as e:
        print(f"Data format error: {e}")


def main():
    income_list = []
    expense_list = []
    budget_limits = {}

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_income(income_list)
        elif choice == "2":
            add_expense(expense_list)
        elif choice == "3":
            view_summary(income_list, expense_list)
            check_budget(expense_list, budget_limits)
        elif choice == "4":
            set_budget_limit(budget_limits)
        elif choice == "5":
            save_data(income_list, expense_list, budget_limits)
        elif choice == "6":
            load_data(income_list, expense_list, budget_limits)
        elif choice == "7":
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
