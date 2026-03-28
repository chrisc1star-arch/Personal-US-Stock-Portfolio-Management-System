# Personal US Stock Portfolio Management System

## Problem Definition
Managing a personal investment portfolio requires tracking stock positions, calculating real-time Profit and Loss (P&L), and managing account balances. This project provides an Object-Oriented Python application with an interactive command-line interface to track US stock positions and calculate current portfolio values.

## OOP Concepts Utilized
* **Encapsulation**: User account balances (`__balance`) and asset lists (`__assets`) are made private and can only be modified through specific class methods (e.g., `deposit`, `buy_stock`).
* **Inheritance**: A base `Asset` class is created, and specific types like `Stock` inherit from it.
* **Polymorphism**: Different asset types can override the `get_current_value()` method to calculate their market value differently.

## Module Structure
1. `main.py`: The entry point that runs the interactive CLI menu.
2. `models.py`: Contains the core OOP classes (`Asset`, `Stock`, `Portfolio`).
3. `utils.py`: Contains helper functions for mock data retrieval and UI formatting.

## Usage
Please refer to the `User_Guide.md` file in this directory for instructions on how to run and operate the application.
