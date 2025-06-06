from core.storage import load_expenses
from core.expense_manager import (
    add_expense,
    view_expenses,
    view_summary,
    export_to_csv,
    update_expense,
    delete_expense,
    search_expenses
)


def main():
    expenses = load_expenses()
    while True:
        print("📒 Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Export to CSV")
        print("5. Update Expense")
        print("6. Delete Expense")
        print("7. Search Expenses")
        print("8. Exit")

        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                add_expense(expenses)
            elif choice == '2':
                view_expenses(expenses)
            elif choice == '3':
                view_summary(expenses)
            elif choice == '4':
                export_to_csv(expenses)
            elif choice == '5':
                update_expense(expenses)
            elif choice == '6':
                delete_expense(expenses)
            elif choice == '7':
                search_expenses(expenses)
            elif choice == '8':
                print("👋 Exiting...")
                break
            else:
                print("❌ Invalid choice. Please try again.")
        except Exception as e:
            print(f"⚠️ Error: {e}\nPlease try again.\n")

if __name__ == '__main__':
    main()
