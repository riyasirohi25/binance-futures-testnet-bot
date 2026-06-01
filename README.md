# Binance Futures Testnet Trading Bot

## Overview

A Python CLI application that places Market and Limit orders on Binance Futures Testnet (USDT-M).

## Features

* Place MARKET orders
* Place LIMIT orders
* BUY and SELL support
* Input validation
* Error handling
* Logging of requests and responses
* CLI interface using Click

## Project Structure

trading_bot/
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ └── logging_config.py
├── logs/
│ └── trading.log
├── cli.py
├── requirements.txt
└── README.md

## Installation

Create virtual environment:

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Environment Variables

Create a .env file:

API_KEY=your_api_key
API_SECRET=your_api_secret

## Usage

Market Order:

python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001

Limit Order:

python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 120000

## Logging

Logs are stored in:

logs/trading.log

## Assumptions

* User has a Binance Futures Testnet account.
* API credentials are valid.
* Testnet funds are available.
