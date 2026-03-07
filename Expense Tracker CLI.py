import csv
from datetime import datetime

file_name = "expenses.csv"

def add_record():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    entry_type = input("Enter type (income/expense): ")

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, entry_type])

    print("Record added successfully")


def view_records():
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            print("\nDate        Category     Amount     Type")
            print("---------------------------------------------")

            for row in reader:
                print(f"{row[0]:<12}{row[1]:<12}{row[2]:<12}{row[3]}")

    except:
        print("No records found")


def total_balance():
    income = 0
    expense = 0

    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[3] == "income":
                    income += float(row[2])
                else:
                    expense += float(row[2])

        print("Total Income:", income)
        print("Total Expense:", expense)
        print("Balance:", income - expense)

    except:
        print("No records found")


while True:
    print("\nExpense Tracker")
    print("1. Add Record")
    print("2. View Records")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        view_records()
    elif choice == "3":
        total_balance()
    elif choice == "4":
        break
    else:
        print("Invalid choice")