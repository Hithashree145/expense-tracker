import csv
import json
import os
from datetime import datetime

CSV_FILE = "expenses.csv"
JSON_FILE = "expenses.json"


def add_expense():
    print("\n----- Add Expense -----")

    category = input("Enter Category: ")
    description = input("Enter Description: ")

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    date = datetime.now().strftime("%d-%m-%Y")

    # Generate ID
    expense_id = 1
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", newline="") as file:
            rows = list(csv.reader(file))
            if len(rows) > 1:
                expense_id = int(rows[-1][0]) + 1

    # Save to CSV
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([expense_id, date, category, description, amount])

    # Save to JSON
    expense = {
        "id": expense_id,
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    data = []

    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            try:
                data = json.load(file)
            except:
                data = []

    data.append(expense)

    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("\nExpense Added Successfully!")


def view_expenses():
    print("\n----- Expense List -----")

    if not os.path.exists(CSV_FILE):
        print("No expenses found.")
        return

    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) <= 1:
            print("No expenses found.")
            return

        for row in rows:
            print("{:<5} {:<12} {:<15} {:<20} {}".format(*row))


def delete_expense():
    def delete_expense():
    print("\n----- Delete Expense -----")

    try:
        delete_id = int(input("Enter Expense ID to Delete: "))
    except ValueError:
        print("Invalid ID!")
        return

    rows = []

    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses found.")
        return

    new_rows = [rows[0]]
    found = False

    for row in rows[1:]:
        if int(row[0]) != delete_id:
            new_rows.append(row)
        else:
            found = True

    if not found:
        print("Expense ID not found.")
        return

    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(new_rows)

    # Update JSON
    with open(JSON_FILE, "r") as file:
        data = json.load(file)

    data = [expense for expense in data if expense["id"] != delete_id]

    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("Expense Deleted Successfully!")

def search_expense():
    def search_expense():
    print("\n----- Search Expense -----")

    category = input("Enter Category: ").lower()

    found = False

    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\nMatching Expenses\n")

        for row in reader:
            if row[2].lower() == category:
                print(row)
                found = True

    if not found:
        print("No matching expense found.")
