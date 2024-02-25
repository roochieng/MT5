import MetaTrader5 as mt5
import os
from dotenv import load_dotenv
import time

load_dotenv()

# Load login credentials from environment variables
my_login = os.environ.get('AVATRADE_LOGIN')
my_password = os.environ.get('AVATRADE_PASSWORD')
my_server = os.environ.get('AVATRADE_SERVER')

# Initialize MetaTrader 5 connection
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()
# Main loop for scalping
while True:
    # Fetch real-time market data
    symbol_info = mt5.symbol_info("EURUSD")
    if symbol_info is None:
        print("Failed to get symbol info, error code =", mt5.last_error())
        continue

    # Apply scalping strategy
    if symbol_info.bid > symbol_info.ask:
        # Place buy order
        result = mt5.order_send(
            symbol="EURUSD",
            action=mt5.ORDER_BUY,
            volume=1.0,
            type=mt5.ORDER_TYPE_MARKET,
            price=0.0,  # For market orders, price is usually set to 0
            sl=0.0,     # Optional stop-loss level
            tp=0.0,     # Optional take-profit level
            magic=0     # Optional magic number
        )
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("Failed to place buy order, error code =", result.retcode)
    elif symbol_info.bid < symbol_info.ask:
        # Place sell order
        result = mt5.order_send(
            symbol="EURUSD",
            action=mt5.ORDER_BUY,
            volume=1.0,
            type=mt5.ORDER_TYPE_MARKET,
            price=0.0,  # For market orders, price is usually set to 0
            sl=0.0,     # Optional stop-loss level
            tp=0.0,     # Optional take-profit level
            magic=0     # Optional magic number
        )
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("Failed to place sell order, error code =", result.retcode)

    # Sleep for some time before the next iteration
    time.sleep(1)

# Shutdown MetaTrader 5 connection after use
mt5.shutdown()