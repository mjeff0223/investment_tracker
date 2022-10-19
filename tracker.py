import yfinance as yf
import json


def get_price():
    global ticker
    global price
    ticker = input("What is the ticker? ")
    ticker = ticker.upper()
    stock = yf.Ticker(ticker).info
    price = stock['regularMarketPrice']
    return price 

def get_average():
    buy_price = price
    num_shares = int(input("How many shares did you buy? "))
    average = buy_price/num_shares


def add_to_portfolio(portfolio):
    num_shares = int(input("How many shares did you buy? "))
    price = get_price()
    purchase_amount = int(input("What is the total purchase amount? "))
    portfolio[ticker] = {}
    portfolio[ticker]["value"]= purchase_amount
    portfolio[ticker]["avg_cost"]= purchase_amount/num_shares
    portfolio[ticker]["shares"]= num_shares
    print("New portfolio: ", portfolio)
    return portfolio
    




portfolio = {
    "APPL":{
        "value": 0,
        "avg_cost": 0,
        "shares": 0

    }
}



print(add_to_portfolio(portfolio))