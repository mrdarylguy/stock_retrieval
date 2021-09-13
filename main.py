import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from datetime import datetime


def main():

    def stock_retrieval(stock_list):

        today = datetime.today()
        today = today.strftime("%B %d, %Y")
        timePeriod = "5d" #1d, 5d, 1mo, 3mo, 1y, 2y, ytd, max
        timeInterval = "15m" #1m, 2m, 5m, 15m, 1h, 1d, 1wk, 1mo, 3mo

        #Instantiate
        fig, ax = plt.subplots(1, len(stock_list))
        fig.subplots_adjust(wspace=0.3); fig.set_figwidth(15)

        #color function; Green or Red
        def color(data):
            if data[0] - data[1] > 0:
                return "green"

            elif data[0] - data[1] < 0:
                return "red"

        #Percentage change function; %? 
        def percentage_change(data):
            absolute_change =  data[0] - data[1]
            percentage = 100 * (data[0] - data[1])/data[1]
            percentage = round(percentage, 2)
            return percentage

        # Sign function; Positive or Negative
        def percentage_sign(data):
            if data[0] - data[1] > 0:
                return "+"

            elif data[0] - data[1] < 0:
                return "-"


        #Iterate across each stock in the list above
        for stock in stock_list:
            data = yf.download(stock, period="5d", interval="15m")

            #Discard other columns aside from closing price
            data = data["Close"]
            
            #Round most recent price to 2 decimal places 
            current_price = round(data[0], 2)

            plt.plot(data, color=color(data), linewidth='2.5')
            plt.grid()
            plt.title(label="{}{}%".format(percentage_sign(data), 
                                   percentage_change(data)), 
                     fontsize=16, 
                     color=color(data))
    
            plt.ylabel("Price ($)", fontsize=12)
            plt.xlabel("{} intervals".format(timeInterval), fontsize=12)
            plt.legend(["{}: $%.2f".format(stock)%current_price],fontsize=14)

            #Populate subplot
            plt.subplot(1, len(stock_list), stock_list.index(stock)+1) 
    
        plt.suptitle("Past 5 trading days, up til {}".format(today), fontsize=15)
        plt.show()

    stock_retrieval()

if __name__ == '__main__':
    stock_list = ["NIO", "XPEV", "F", "TSLA"]
    stock_retrieval(stock_list)
    