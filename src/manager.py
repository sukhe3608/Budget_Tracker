from storage import load_data, save_data
from utils import log, validate_amount
from models import Transaction
import csv
from datetime import datetime

def add_income(amount, category):
    try:
        data = load_data()

        tx = Transaction(amount=amount, category=category, t_type="income")

        # Save in a single common list
        data["transactions"].append(tx.to_dict())

        save_data(data)
        log(f"Income added: {amount} in category {category}")
    except Exception as e:
        log(f"Failed to add income: {e}")


def add_expense(amount, category):
    try:
        data = load_data()

        tx = Transaction(amount=amount, category=category, t_type="expense")

        data["transactions"].append(tx.to_dict())

        save_data(data)
        log(f"Expense added: {amount} in category {category}")
    except Exception as e:
        log(f"Failed to add expense: {e}")


def get_month_summary(month: str):
    try:
        data = load_data()
        transactions = data["transactions"]

        month_records = [t for t in transactions if t["date"].startswith(month)]

        total_income = sum(t["amount"] for t in month_records if t["type"] == "income")
        total_expense = sum(t["amount"] for t in month_records if t["type"] == "expense")

        savings = total_income - total_expense

        return {
            "month": month,
            "income": total_income,
            "expense": total_expense,
            "savings": savings
        }
    except Exception as e:
        log(f"Failed to get month summary: {e}")
        return None


def export_csv(month: str):
    data = load_data()
    filename = f"budget_summary_{month}.csv"

    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount"])

            for t in data["transactions"]:
                if t["date"].startswith(month):
                    writer.writerow([t["date"], t["type"], t["category"], t["amount"]])

        log(f"CSV exported: {filename}")
    except Exception as e:
        log(f"Failed to export CSV: {e}")
