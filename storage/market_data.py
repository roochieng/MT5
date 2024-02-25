from config import app, db, bcrypt


class MarketData(db.Model):
    """
    Represents market data for a trading instrument.

    Each instance of this class represents a single set of market data (e.g., OHLC prices, volume)
    for a specific trading instrument at a particular timestamp. Market data is stored in the 
    'market_data' table of the database.

    Attributes:
        id (int): The unique identifier for the market data record.
        symbol (str): The trading symbol or instrument identifier.
        timestamp (datetime): The timestamp at which the market data was recorded.
        open_price (float): The opening price of the trading instrument.
        high_price (float): The highest price reached during the recorded period.
        low_price (float): The lowest price reached during the recorded period.
        close_price (float): The closing price of the trading instrument.
        volume (int): The trading volume during the recorded period.
    """

    __tablename__ = 'market_data'
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime)
    open_price = db.Column(db.Float)
    high_price = db.Column(db.Float)
    low_price = db.Column(db.Float)
    close_price = db.Column(db.Float)
    volume = db.Column(db.Integer)
