import json
from collections import defaultdict
import os
from core.storage import load_expenses, save_expenses

def add_expense(expenses):
    try:
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount (₹): "))
        print("Select a category:")
        categories = ["🍔 Food", "🏠 Home", "💻 Work", "🎉 Fun", "✨ Misc"]
        for i, category in enumerate(categories, start=1):
            print(f"{i}. {category}")
        cat_choice = int(input("Enter a category number: "))
        if 1 <= cat_choice <= len(categories):
            category = categories[cat_choice - 1].split(' ', 1)[1]
        else:
            print("❌ Invalid category choice.")
            return

        date = input("Enter date (YYYY-MM-DD): ")

        expense = {
            "name": name,
            "amount": amount,
            "category": category,
            "date": date
        }
        expenses.append(expense)
        save_expenses(expenses)
        print(f"\n✅ Added '{name}' (₹{amount:.2f}) to {category} on {date}.\n")
    except ValueError:
        print("\n❌ Invalid input. Please enter correct values.\n")

def view_expenses(expenses):
    if not expenses:
        print("\n⚠️ No expenses to display.\n")
        return
    print("\n📋 All Expenses:")
    print(f"{'Index':<6} {'Date':<12} {'Category':<10} {'Amount':<8} {'Name'}")
    print("-" * 60)
    for idx, e in enumerate(expenses):
        print(f"{idx:<6} {e['date']:<12} {e['category']:<10} ₹{e['amount']:<8.2f} {e['name']}")
    print()

def view_summary(expenses, monthly_budget=15000.0):
    if not expenses:
        print("\n⚠️ No expenses to summarize.\n")
        return
    print("\n📊 Expenses by Category:")
    print("-" * 30)
    category_totals = defaultdict(float)
    total_spent = 0.0

    for e in expenses:
        category_totals[e['category']] += e['amount']
        total_spent += e['amount']

    for cat, amt in category_totals.items():
        print(f"{cat}: ₹{amt:.2f}")

    print(f"\n💰 Total Spent: ₹{total_spent:.2f}")
    remaining = monthly_budget - total_spent
    print(f"💵 Budget Left: ₹{remaining:.2f}")
    print(f"📅 Per Day: ₹{remaining / 30:.2f}\n")

def export_to_csv(expenses):
    import csv
    filename = input("Enter filename to export (e.g., expenses.csv): ")
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['date', 'category', 'amount', 'name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for e in expenses:
                writer.writerow(e)
        print(f"\n✅ Exported expenses to '{filename}'.\n")
    except PermissionError:
        print(f"\n❌ Permission denied. Please close '{filename}' if it's open elsewhere and try again.\n")
    except Exception as e:
        print(f"\n⚠️ Failed to export expenses: {e}\n")

def update_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        idx = int(input("Enter the index of the expense to update: "))
        if 0 <= idx < len(expenses):
            expense = expenses[idx]
            print(f"Updating expense: {expense}")
            expense['name'] = input(f"Enter new name (or press Enter to keep '{expense['name']}'): ") or expense['name']
            amount_input = input(f"Enter new amount (₹) (or press Enter to keep '{expense['amount']}'): ")
            if amount_input:
                expense['amount'] = float(amount_input)
            expense['category'] = input(f"Enter new category (or press Enter to keep '{expense['category']}'): ") or expense['category']
            expense['date'] = input(f"Enter new date (YYYY-MM-DD) (or press Enter to keep '{expense['date']}'): ") or expense['date']
            save_expenses(expenses)
            print("\n✅ Expense updated successfully.\n")
        else:
            print("\n❌ Invalid index.\n")
    except ValueError:
        print("\n❌ Invalid input. Please enter correct values.\n")

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        idx = int(input("Enter the index of the expense to delete: "))
        if 0 <= idx < len(expenses):
            deleted = expenses.pop(idx)
            save_expenses(expenses)
            print(f"\n✅ Deleted expense: {deleted}\n")
        else:
            print("\n❌ Invalid index.\n")
    except ValueError:
        print("\n❌ Invalid input. Please enter a number.\n")

def search_expenses(expenses):
    keyword = input("Enter keyword to search (name or category): ").lower()
    results = [e for e in expenses if keyword in e['name'].lower() or keyword in e['category'].lower()]
    if results:
        print("\n🔍 Search Results:")
        print(f"{'Date':<12} {'Category':<10} {'Amount':<8} {'Name'}")
        print("-" * 50)
        for e in results:
            print(f"{e['date']:<12} {e['category']:<10} ₹{e['amount']:<8.2f} {e['name']}")
        print()
    else:
        print("\n⚠️ No matching expenses found.\n")
