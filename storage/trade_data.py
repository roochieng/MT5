from config import app, db, bcrypt


class Trade(db.Model):
    """
    Represents a trade in a trading application.

    Each instance of this class represents a single trade executed within the trading application. 
    Trades are stored in the 'trades' table of the database.

    Attributes:
        id (int): The unique identifier for the trade.
        entry_price (float): The price at which the trade was entered.
        exit_price (float): The price at which the trade was exited.
        stop_loss (float): The stop-loss level for the trade.
        take_profit (float): The take-profit level for the trade.
        profit (float): The profit or loss incurred from the trade.
    """
    __tablename__ = 'trades'
    id = db.Column(db.Integer, primary_key=True)
    entry_price = db.Column(db.Float)
    exit_price = db.Column(db.Float)
    stop_loss = db.Column(db.Float)
    take_profit = db.Column(db.Float)
    profit = db.Column(db.Float)
