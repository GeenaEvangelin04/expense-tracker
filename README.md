# 📒 Expense Tracker (CLI Version)

A command-line application to **track, manage, and analyze personal expenses**. This tool helps you stay on top of your spending habits and budget, right from the terminal!

---

## ✨ Features

✅ **Add Expense** – Record new expenses with name, category, amount, and date  
✅ **View All Expenses** – See a list of all your expenses  
✅ **View Summary** – Get total spending by category and overall budget summary  
✅ **Export to CSV** – Export your expenses for backup or analysis  
✅ **Update Expense** – Edit an existing expense  
✅ **Delete Expense** – Remove an expense  
✅ **Search Expenses** – Search by name or category  
✅ **Data Persistence** – Expenses stored in a local JSON file  
✅ **Modular Codebase** – Easy to extend or integrate with a GUI later

---

## 📂 Project Structure

│
├── core/
│ ├── expense_manager.py # Core expense management logic
│ └── storage.py # Load and save expenses
│
├── data/
│ └── expenses.json # Local data storage (JSON file)
│
├── utils/
│ └── helpers.py # Helper functions (if any)
│
├── gui/
│ └── app.py # Placeholder for future GUI implementation
│
├── main.py # Entry point for the CLI app
│
├── requirements.txt # List of dependencies
│
└── README.md # This file