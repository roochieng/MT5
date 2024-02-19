import MetaTrader5 as mt5
import os
from dotenv import load_dotenv

load_dotenv()

# Load login credentials from environment variables
my_login = os.environ.get('LOGIN')
my_password = os.environ.get('PASSWORD')
my_server = os.environ.get('SERVER')

# Initialize MetaTrader 5 connection
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()
print(mt5.account_info())

