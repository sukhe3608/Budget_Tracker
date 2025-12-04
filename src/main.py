from manager import add_income, add_expense, get_month_summary, export_csv
from utils import log, validate_amount

def main_menu():
    while True:
        print("\n==== Budget Tracker ==== ")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Monthly Summary")
        print("4. Export Monthly Summary to CSV")
        print("5. Exit")
        print("=========================")
        choice = input("Select an option: ")
        if choice == '1':
            amount = validate_amount(input("Enter amount: "))
            if not amount:
                print("Invalid amount. Please try again.")
                continue
            category = input("Enter category: ")
            add_income(amount, category)
            print("Income added successfully.")

        elif choice == '2':
            amount = validate_amount(input("Enter amount: "))
            if not amount:
                print("Invalid amount. Please try again.")
                continue
            category = input("Enter category: ")
            add_expense(amount, category)
            print("Expense added successfully.")

        elif choice == '3':
            month = input("Enter month (YYYY-MM): ")
            summary = get_month_summary(month)
            if summary:
                print(f"\n--- Summary for {month} ---")
                print(f"Total Income: {summary['income']}")
                print(f"Total Expense: {summary['expense']}")
                print(f"Savings: {summary['savings']}")
                print("-------------------------")
            else:
                print("Failed to retrieve summary.")
        
        elif choice == '4':
            month = input("Enter month (YYYY-MM): ")
            export_csv(month)
            print("CSV exported successfully.")

        elif choice == '5':
            print("Exiting Budget Tracker. Goodbye!")
            break

if __name__ == "__main__":
    main_menu()