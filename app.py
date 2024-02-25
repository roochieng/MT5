# app.py
from flask import Flask, render_template, request
from config import app, db, bcrypt
from storage.trade_data import Trade
from storage.market_data import MarketData

@app.route('/')
def index():
    return 'Welcome to the trading app!'

@app.route('/insert_trade', methods=['POST'])
def insert_trade():
    entry_price = request.form['entry_price']
    exit_price = request.form['exit_price']
    stop_loss = request.form['stop_loss']
    take_profit = request.form['take_profit']
    
    new_trade = Trade(entry_price=entry_price, exit_price=exit_price, stop_loss=stop_loss, take_profit=take_profit)
    db.session.add(new_trade)
    db.session.commit()
    
    return 'Trade inserted successfully!'

@app.route('/trades')
def get_trades():
    trades = Trade.query.all()
    return render_template('trades.html', trades=trades)

if __name__ == '__main__':
    app.run(debug=True)
