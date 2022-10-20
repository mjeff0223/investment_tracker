import yfinance as yf
import json





def add_to_portfolio(portfolio):
    ticker = input("What is the ticker of the stock you bought? ")
    num_shares = int(input("How many shares did you buy? "))
    price = int(input("What was the price of the shares? "))
    purchase_amount = price * num_shares
    portfolio[ticker] = {}
    portfolio[ticker]["value"]= purchase_amount
    portfolio[ticker]["avg_cost"]= purchase_amount/num_shares
    portfolio[ticker]["shares"]= num_shares
    return "New portfolio: ", portfolio
    
    


ticker = None



portfolio = {
    f"{ticker}":{
        "value": 0,
        "avg_cost": 0,
        "shares": 0

    }
}



print(add_to_portfolio(portfolio))