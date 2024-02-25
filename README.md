# Trading Strategies with MetaTrader 5 (MT5) API
This project demonstrates various trading strategies implemented in Python using the MetaTrader 5 (MT5) API. The strategies include scalping techniques based on pivot points, moving averages, and other technical indicators.

## Overview
Trading in financial markets involves buying and selling financial instruments such as stocks, currencies, or commodities with the aim of making a profit. This project focuses on implementing algorithmic trading strategies to automate the process of entering and exiting trades based on predefined rules.

## Technologies Used
- Python: The programming language used for implementing the trading strategies.
- MetaTrader 5 (MT5) API: Provides access to real-time market data, historical prices, and trading functions for trading on the MetaTrader 5 platform.
- Pandas: Python library used for data manipulation and analysis, particularly for handling financial time series data.
- Matplotlib: Python library used for creating visualizations and plots to analyze market data and trading performance.
- dotenv: Python library for loading environment variables from a .env file, used for storing sensitive information such as login credentials.

## Features
- Scalping strategies based on pivot points: Buy and sell signals are generated based on the crossing of price levels relative to pivot points, with stop-loss and take-profit levels dynamically adjusted to manage risk and maximize profits.
- Moving average crossover strategies: Buy and sell signals are generated based on the crossover of short-term and long-term moving averages, indicating potential trend reversals or continuations.
## Installation
1. Clone the repository to your local machine:
```
git clone https://github.com/roochieng/MT5.git
```
2. Install the required Python packages:
```
pip install -r requirements.txt
```
3. Set up your MetaTrader 5 account and obtain login credentials.

4. Create a .env file in the project directory and add your MetaTrader 5 login credentials:
```
LOGIN=your_mt5_login
PASSWORD=your_mt5_password
SERVER=your_mt5_server
```

## Usage
1. Run the Python scripts to execute different trading strategies.
2. Monitor the console output for trade signals, entry/exit points, and trading performance metrics.
3. Analyze the generated plots and visualizations to evaluate the effectiveness of the trading strategies.

## Contributing
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.