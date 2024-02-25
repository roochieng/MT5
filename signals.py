import MetaTrader5 as mt5

# Connect to MetaTrader 5 server
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# Define the symbol and timeframe
symbol = "EURUSD"
timeframe = mt5.TIMEFRAME_M1  # Use M1 (1-minute) timeframe for scalping

# Request historical prices
rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 5)  # Get last 5 bars

if rates is None:
    print("Failed to retrieve historical prices.")
    mt5.shutdown()
    quit()

# Calculate the pivot point (PP)
high = max(rate['high'] for rate in rates)
low = min(rate['low'] for rate in rates)
close = rates[-1]['close']
pivot_point = (high + low + close) / 3

# Get the current price
current_price = mt5.symbol_info_tick(symbol).bid  # Use bid price for buying and ask price for selling

# Define buy and sell signals based on pivot point
buy_signal = current_price > pivot_point
sell_signal = current_price < pivot_point

# Print trading signals
print("Current Price:", current_price)
print("Pivot Point:", pivot_point)
print("Buy Signal:", buy_signal)
print("Sell Signal:", sell_signal)

# Shutdown MetaTrader 5 connection
mt5.shutdown()