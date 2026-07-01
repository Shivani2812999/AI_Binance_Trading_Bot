# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot that interacts with the **Binance Futures Testnet (USDT-M)**. It allows users to place **MARKET** and **LIMIT** orders through a command-line interface while following a clean, modular architecture with logging, input validation, and exception handling.

This project was developed as part of the **Primetrade.ai Python Developer Application Task**.

---

## Features

* Place **MARKET** orders
* Place **LIMIT** orders
* Supports both **BUY** and **SELL** orders
* Command Line Interface (CLI) using `argparse`
* Input validation
* Modular project structure
* Logging of API requests, responses, and errors
* Exception handling for invalid input, API errors, and network failures
* Uses Binance Futures Testnet (USDT-M)

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── .env
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Prerequisites

* Python 3.10 or later
* Binance Futures Testnet account
* Binance Futures Testnet API Key and Secret

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd trading_bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_SECRET_KEY=YOUR_SECRET_KEY
```

The application connects to the Binance Futures Testnet endpoint.

---

## Running the Application

### Place a MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Sample Output

```text
========== ORDER SUMMARY ==========
Symbol          : BTCUSDT
Order ID        : 18239658194
Side            : BUY
Order Type      : MARKET
Status          : FILLED
Original Qty    : 0.0010
Executed Qty    : 0.0010
Price           : 0.00
Average Price   : 58374.500000

✅ Order placed successfully!
```

---

## Logging

The application records all important events in:

```text
logs/trading.log
```

The log file contains:

* API request details
* API response details
* Exceptions and error messages
* Timestamps for all operations

---

## Validation

The application validates:

* Symbol is provided
* Order side must be `BUY` or `SELL`
* Order type must be `MARKET` or `LIMIT`
* Quantity must be greater than zero
* Price is mandatory for LIMIT orders

---

## Error Handling

The application handles:

* Invalid user input
* Binance API exceptions
* Network-related exceptions
* Unexpected runtime errors

All errors are logged to the log file.

---

## Assumptions

* Only **USDT-M Futures** are supported.
* Only **MARKET** and **LIMIT** order types are implemented.
* API credentials are stored securely using a `.env` file.
* The application is intended for the **Binance Futures Testnet** environment.

---

## Technologies Used

* Python 3
* python-binance
* argparse
* python-dotenv
* logging

---

## Future Improvements

* Interactive CLI using Typer or Click
* Additional order types (Stop-Limit, OCO)
* Order cancellation support
* Position monitoring
* Streamlit or Flask web interface
* Unit tests

---

## Author

**Shivani Hadapad**

GitHub: https://github.com/Shivani2812999

LinkedIn: https://www.linkedin.com/in/Shivani-hadapad-1a838717a/
