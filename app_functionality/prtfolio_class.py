from operator import add
import yfinance as yf

portfolio = {}





def add_to_portfolio(portfolio):


    
    ticker = input("What is the ticker of the stock you bought? ").upper()
    num_shares = int(input("How many shares did you buy? "))
    price = int(input("What was the price of the shares? "))
    purchase_amount = price * num_shares
    portfolio[ticker] = {}
    portfolio[ticker]["value"]= purchase_amount
    portfolio[ticker]["avg_cost"]= purchase_amount/num_shares
    portfolio[ticker]["shares"]= num_shares
    return "New portfolio: ", portfolio





def save_portfolio(portfolio):
    global saved_portfolio
    saved_portfolio = []
    if saved_portfolio != []:
        saved_portfolio.pop()
        saved_portfolio.append(portfolio)
    else:
        saved_portfolio.append(portfolio)
    return saved_portfolio

def show_portfolio(portfolio):
    print(saved_portfolio)

save_portfolio(portfolio)




   






