import MetaTrader5 as mt5

# Connect to MetaTrader 5 server
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# Define the symbol and timeframe
symbol = "EURUSD"
timeframe = mt5.TIMEFRAME_M1  # Use M1 (1-minute) timeframe for scalping

# Define initial stop-loss distance (in pips) and take-profit distance (in pips)
initial_stop_loss_pips = 20
initial_take_profit_pips = 20

# Request historical prices
rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, 5)  # Get last 5 bars

if rates is None:
    print("Failed to retrieve historical prices.")
    mt5.shutdown()
    quit()

# Calculate the pivot point (PP) and support/resistance levels
high = max(rate['high'] for rate in rates)
low = min(rate['low'] for rate in rates)
close = rates[-1]['close']
pivot_point = (high + low + close) / 3
support1 = (2 * pivot_point) - high
resistance1 = (2 * pivot_point) - low

# Define initial stop-loss and take-profit levels
stop_loss = close - initial_stop_loss_pips * mt5.symbol_info(symbol).point
take_profit = close + initial_take_profit_pips * mt5.symbol_info(symbol).point

# Print initial stop-loss and take-profit levels
print("Initial Stop Loss:", stop_loss)
print("Initial Take Profit:", take_profit)

# Main loop for monitoring trade
while True:
    # Get the current bid price for the symbol
    current_price = mt5.symbol_info_tick(symbol).bid  # Use bid price for buying and ask price for selling
    
    # Update stop-loss and take-profit levels based on current price
    if current_price - stop_loss > initial_stop_loss_pips * mt5.symbol_info(symbol).point:
        stop_loss = current_price - initial_stop_loss_pips * mt5.symbol_info(symbol).point
    if take_profit - current_price > initial_take_profit_pips * mt5.symbol_info(symbol).point:
        take_profit = current_price + initial_take_profit_pips * mt5.symbol_info(symbol).point

    # Print updated stop-loss and take-profit levels
    print("Updated Stop Loss:", stop_loss)
    print("Updated Take Profit:", take_profit)

    # Exit the loop if the trade hits the take-profit level
    if current_price >= take_profit:
        print("Take Profit hit. Exiting trade.")
        break

# Shutdown MetaTrader 5 connection
mt5.shutdown()
