# core/storage.py

import json
import os

# Path to the data file
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'expenses.json')

def load_expenses():
    """Load expenses from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_expenses(expenses):
    """Save expenses to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)
