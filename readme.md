# Expense Tracker (CSV/JSON)

## Internship Project

### Project Title
Expense Tracker using Python

## Description
Expense Tracker is a Python command-line application that helps users manage their daily expenses. It allows users to add, view, search, and delete expenses while storing data in both CSV and JSON formats. The application also generates monthly and category-wise reports to help users analyse their spending.

## Features
- Add new expenses
- View all expenses
- Delete expenses
- Search expenses by category
- Generate monthly report
- Generate category-wise report
- Store data in CSV format
- Store data in JSON format
- Simple menu-driven interface

## Technologies Used
- Python 3
- CSV
- JSON
- Datetime
- OS Module

## Project Structure

```
Expense_Tracker/
│
├── main.py
├── expense.py
├── file_handler.py
├── reports.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── expenses.csv
│   └── expenses.json
│
└── screenshots/
```

## How to Run

1. Install Python 3.
2. Download or clone this project.
3. Open the project folder.
4. Run the following command:

```bash
python main.py
```

## Example Menu

```
==============================
      EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Delete Expense
4. Search Expense
5. Monthly Report
6. Category Report
7. Exit
```

## Output Files

### CSV

```
ID,Date,Category,Description,Amount
1,25-07-2026,Food,Lunch,250
```

### JSON

```json
[
  {
    "id": 1,
    "date": "25-07-2026",
    "category": "Food",
    "description": "Lunch",
    "amount": 250
  }
]
```

## Future Enhancements

- GUI using Tkinter
- SQLite Database Integration
- Budget Alerts
- Graphical Reports
- User Login System

## Author

**Name:** Your Name

**Internship Domain:** Python Development

**Project:** Expense Tracker (CSV/JSON)

## License

This project is developed for educational and internship purposes.