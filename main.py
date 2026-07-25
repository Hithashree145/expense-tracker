from expense import add_expense
from expense import view_expenses
from expense import delete_expense
from expense import search_expense

from reports import monthly_report
from reports import category_report


def menu():
    while True:
        print("\n==============================")
        print("      EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Search Expense")
        print("5. Monthly Report")
        print("6. Category Report")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            delete_expense()

        elif choice == "4":
            search_expense()

        elif choice == "5":
            monthly_report()

        elif choice == "6":
            category_report()

        elif choice == "7":
            print("\nThank you for using Expense Tracker.")
            break

        else:
            print("\nInvalid Choice!")


if __name__ == "__main__":
    menu()
