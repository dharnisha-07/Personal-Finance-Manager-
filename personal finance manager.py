import pandas as pd
import matplotlib.pyplot as plt

def input_income_sources():
    print("Enter your income sources for the month (Enter 'done' when finished):")
    income_sources = {}
    while True:
        source = input("Source: ").capitalize()
        if source == "Done":
            break
        amount = float(input("Amount (₹): "))
        income_sources[source] = amount
    return income_sources

def calculate_total_income(income_sources):
    return sum(income_sources.values())

def input_expenses():
    total_expenses = 0
    expenses = {}
    print("\nEnter your expenses for the month (Enter 'done' when finished):")
    while True:
        category = input("Expense category: ").capitalize()
        if category == "Done":
            break
        amount = float(input(f"Enter your {category} expenses for the month (₹): "))
        expenses[category] = amount
        total_expenses += amount
    return total_expenses, expenses

def input_goals():
    goals = float(input("\nEnter your financial goals for the month (₹): "))
    return goals

def generate_report(income, expenses, goals):
    net_savings = income - expenses
    if net_savings < 0:
        net_savings = 0
    print("\n------ Financial Report ------")
    print(f"Total Income: ₹{income}")
    print(f"Total Expenses: ₹{expenses}")
    print(f"Savings: ₹{net_savings}")
    if net_savings >= goals:
        print("Congratulations! You've met your financial goal for the month.")
    else:
        print("You're short of your financial goal for the month. Keep saving!")

def visualize_income_expenses(income, expenses):
    plt.figure(figsize=(10, 6))
    plt.pie([income, expenses], labels=["Income", "Expenses"], autopct='%1.1f%%', colors=['lightgreen', 'salmon'])
    plt.title("Income vs. Expenses")
    plt.axis('equal')
    plt.show()

def visualize_expenses(expenses_df):
    plt.figure(figsize=(10, 6))
    plt.bar(expenses_df['Category'], expenses_df['Amount'], color='skyblue')
    plt.xlabel('Expense Category')
    plt.ylabel('Amount (₹)')
    plt.title('Monthly Expenses Breakdown')
    plt.xticks(rotation=45)
    plt.show()

def calculate_total_expenses(expenses):
    return sum(expenses.values())

def calculate_savings(income, expenses):
    savings = income - expenses
    if savings < 0:
        return 0  # Adjust savings to zero if expenses exceed income
    return savings

def track_single_month():
    print("\n------ Monthly Finance Tracker ------")
    income_sources = input_income_sources()
    total_income = sum(income_sources.values())
    print(f"\nTotal income for the month: ₹{total_income}")

    total_expenses, expenses = input_expenses()
    goals = input_goals()
    generate_report(total_income, total_expenses, goals)
    visualize_income_expenses(total_income, total_expenses)

    expenses_df = pd.DataFrame(list(expenses.items()), columns=['Category', 'Amount'])
    visualize_expenses(expenses_df)

    savings_month = calculate_savings(total_income, total_expenses)
    if total_expenses > total_income:
        print("Your expenses exceed your income. Consider reducing expenses or increasing income.")
    else:
        print(f"You have ₹{savings_month} left after expenses. Consider saving some of it.")

def main():
    print("Welcome to the Personal Finance Management Tool!")
    track_single_month()

    track_multiple_months = input("\nDo you want to track expenses over multiple months? (yes/no): ").lower()
    if track_multiple_months == 'yes':
        while True:
            track_single_month()
            choice = input("Enter 'y' to input expenses for another month, or 'n' to exit: ").lower()
            if choice != 'y':
                break

if __name__ == "__main__":
    main()
