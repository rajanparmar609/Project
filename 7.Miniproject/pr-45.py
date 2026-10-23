
import sqlite3

db = sqlite3.connect("expense.db")

# Create budget table
db.execute("""
    CREATE TABLE IF NOT EXISTS budget_settings (
        id INTEGER PRIMARY KEY,
        budget INTEGER NOT NULL,
        new_budget INTEGER
    )
""")

# Create expenses table
db.execute("""
    CREATE TABLE IF NOT EXISTS expense_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        expense INTEGER NOT NULL
    )
""")

# Add new_budget column if the existing table doesn't have it
columns = [
    row[1] for row in
    db.execute("PRAGMA table_info(budget_settings)").fetchall()
]

if "new_budget" not in columns:
    db.execute(
        "ALTER TABLE budget_settings ADD COLUMN new_budget INTEGER"
    )

db.commit()

# Load or create original budget
result = db.execute(
    "SELECT budget, new_budget FROM budget_settings WHERE id = 1"
).fetchone()

if result is None:
    while True:
        try:
            budget = int(input("Enter your original budget: ₹"))

            if budget <= 0:
                print("Budget must be greater than zero.")
                continue

            db.execute(
                """INSERT INTO budget_settings (id, budget, new_budget)
                   VALUES (1, ?, NULL)""",
                (budget,)
            )
            db.commit()
            new_budget = None
            print("Budget saved successfully!")
            break

        except ValueError:
            print("Please enter a valid whole number.")
else:
    budget = result[0]
    new_budget = result[1]
    print("Original budget: ₹", budget)

    if new_budget is not None:
        print("Updated budget: ₹", new_budget)


# Get all expenses
def get_expenses():
    return db.execute(
        "SELECT id, expense FROM expense_records ORDER BY id"
    ).fetchall()


# Display a report for a selected budget
def view_report(report_budget, title):
    expenses = get_expenses()
    total = sum(amount for _, amount in expenses)
    remaining = report_budget - total

    print(f"\n========== {title} ==========")
    print(f"Budget: ₹{report_budget}")
    print("\n----- Expense Details -----")

    if not expenses:
        print("No expenses recorded yet.")
    else:
        for expense_id, amount in expenses:
            print(f"Expense {expense_id}: ₹{amount}")

    print("---------------------------")
    print("Number of Expenses:", len(expenses))
    print("Total Spent: ₹", total)

    if remaining >= 0:
        print("Remaining Budget: ₹", remaining)
        print("Status: Under Budget")
    else:
        print("Amount Over Budget: ₹", abs(remaining))
        print("Status: Over Budget")

    if report_budget > 0:
        percentage = (total / report_budget) * 100
        print(f"Budget Used: {percentage:.1f}%")

    print("=" * (len(title) + 22))


# Main menu
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Original Budget Report")
    print("3. Change Budget")
    print("4. View New Budget Report")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            expense = int(input("Enter expense amount: ₹"))

            if expense <= 0:
                print("Expense must be greater than zero.")
                continue

            db.execute(
                "INSERT INTO expense_records (expense) VALUES (?)",
                (expense,)
            )
            db.commit()
            print("Expense saved successfully!")

        except ValueError:
            print("Please enter a valid whole number.")

    elif choice == "2":
        view_report(budget, "ORIGINAL BUDGET REPORT")

    elif choice == "3":
        try:
            amount = int(input("Enter your new budget: ₹"))

            if amount <= 0:
                print("Budget must be greater than zero.")
                continue

            new_budget = amount

            db.execute(
                "UPDATE budget_settings SET new_budget = ? WHERE id = 1",
                (new_budget,)
            )
            db.commit()

            print("New budget saved successfully!")
            view_report(new_budget, "NEW BUDGET REPORT")

        except ValueError:
            print("Please enter a valid whole number.")

    elif choice == "4":
        if new_budget is None:
            print("You haven't set a new budget yet.")
            print("Please choose option 3 first.")
        else:
            view_report(new_budget, "NEW BUDGET REPORT")

    elif choice == "5":
        print("Expense tracker closed.")
        break


    else:
        print("Invalid choice. Please choose 1, 2, 3, 4 or 5.")

db.close()