from pathlib import Path
import sqlite3

from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)
app.secret_key = "expense-tracker-local"
DB_PATH = Path(__file__).with_name("expense.db")


def connect_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db


def init_db():
    with connect_db() as db:
        db.execute("""CREATE TABLE IF NOT EXISTS budget_settings (
            id INTEGER PRIMARY KEY, budget INTEGER NOT NULL, new_budget INTEGER
        )""")
        db.execute("""CREATE TABLE IF NOT EXISTS expense_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT, expense INTEGER NOT NULL
        )""")
        columns = {row["name"] for row in db.execute("PRAGMA table_info(budget_settings)")}
        if "new_budget" not in columns:
            db.execute("ALTER TABLE budget_settings ADD COLUMN new_budget INTEGER")


def get_summary():
    with connect_db() as db:
        settings = db.execute("SELECT budget, new_budget FROM budget_settings WHERE id = 1").fetchone()
        expenses = db.execute("SELECT id, expense FROM expense_records ORDER BY id DESC").fetchall()
    total = sum(row["expense"] for row in expenses)
    return settings, expenses, total


@app.route("/", methods=["GET"])
def home():
    settings, expenses, total = get_summary()
    return render_template("index.html", settings=settings, expenses=expenses, total=total)


@app.post("/budget")
def set_budget():
    field = request.form.get("kind")
    value = parse_amount(request.form.get("amount"), "Budget")
    if value is None:
        return redirect(url_for("home"))
    if field not in ("original", "new"):
        flash("Invalid budget type.", "error")
        return redirect(url_for("home"))
    with connect_db() as db:
        settings = db.execute("SELECT id FROM budget_settings WHERE id = 1").fetchone()
        if settings:
            column = "budget" if field == "original" else "new_budget"
            db.execute(f"UPDATE budget_settings SET {column} = ? WHERE id = 1", (value,))
        else:
            db.execute("INSERT INTO budget_settings (id, budget, new_budget) VALUES (1, ?, ?)",
                       (value, None if field == "original" else value))
    flash("Budget saved.", "success")
    return redirect(url_for("home"))


def parse_amount(raw, label):
    try:
        amount = int(raw)
        if amount <= 0:
            raise ValueError
        return amount
    except (TypeError, ValueError):
        flash(f"{label} must be a whole number greater than zero.", "error")
        return None


@app.post("/expenses")
def add_expense():
    amount = parse_amount(request.form.get("amount"), "Expense")
    if amount is not None:
        with connect_db() as db:
            db.execute("INSERT INTO expense_records (expense) VALUES (?)", (amount,))
        flash("Expense added.", "success")
    return redirect(url_for("home"))


@app.post("/expenses/<int:expense_id>/delete")
def delete_expense(expense_id):
    with connect_db() as db:
        db.execute("DELETE FROM expense_records WHERE id = ?", (expense_id,))
    flash("Expense deleted.", "success")
    return redirect(url_for("home"))


init_db()

if __name__ == "__main__":
    app.run(debug=True)
