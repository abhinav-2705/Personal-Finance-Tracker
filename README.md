# Personal Finance Tracker

A Python-based command-line application to track personal finances, including income, expenses, and category-wise spending, with interactive visualizations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Features

-   Transaction Management:
    -      Add, edit, and delete financial transactions (date, description, category, amount).
-   Financial Calculations:
    -      Calculate overall balance.
    -      Calculate category-wise spending.
-   Data Visualization:
    -      Generate pie charts to visualize category spending using `matplotlib`.
-   Data Persistence:
    -      Stores transaction data in a CSV file.
-   Command-Line Interface (CLI):
    -   User friendly menu driven interface.

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd personal-finance-tracker
    ```

2.  Install dependencies:

    ```bash
    pip install matplotlib
    ```

## Usage

1.  Run the application:

    ```bash
    python main.py
    ```

2.  Follow the menu prompts:

    -      Choose options to add transactions, view transactions, calculate balance, visualize spending, etc.

3.  Data storage:

    -   Transaction data is stored in `transactions.csv`.

## Dependencies

-   Python 3.x
-   matplotlib (for visualizations)
-   csv (built-in)
-   datetime (built-in)

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to report bugs or suggest new features.
