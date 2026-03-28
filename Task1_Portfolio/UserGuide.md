# User Guide: Personal US Stock Portfolio Management System

This document provides instructions on how to run and interact with the application developed for **Task 1**.

## System Requirements
* Python 3.6 or above.
* No external libraries (e.g., pandas, yfinance) are required to ensure the code runs flawlessly out-of-the-box for assessment purposes.

## How to Run the Application
1. Open your terminal or command prompt.
2. Navigate to the `Task1_Portfolio` directory where the source code is located.
3. Execute the following command:
   `python main.py`

## Operating Instructions
Upon launching, the system will ask you to enter a name to create a new account. You will start with a default balance of `$10,000.00`. 

The system operates via an interactive Command-Line Interface (CLI). You can select actions by entering the corresponding number:

* **[1] View Portfolio Dashboard**: Generates a real-time table showing your available cash, owned stocks, average costs, current market values, and unrealized Profit & Loss (P&L).
* **[2] Buy Stock**: Prompts you to enter a stock ticker (e.g., AAPL) and a quantity. It will fetch the simulated live price, calculate the cost, and automatically deduct from your cash balance upon confirmation. Supports fractional shares (e.g., 0.5 shares).
* **[3] Sell Stock**: Prompts you to sell a stock you currently own. Ensures you cannot sell more shares than you hold.
* **[4] Deposit Funds**: Allows you to add more cash to your account balance.
* **[5] Exit Application**: Safely terminates the program.
