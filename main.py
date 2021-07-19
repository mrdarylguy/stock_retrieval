import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from datetime import datetime


def main():



    def stock_retrieval():
        stock_list = ["NIO", "XPEV", "F", "TSLA"]
        today = datetime.today()
        today = today.strftime("%B %d, %Y")

        fig, ax = plt.subplots(1, len(stock_list))
        fig.subplots_adjust(wspace=0.3); fig.set_figwidth(15)


        for stock in stock_list:
            data = yf.download(stock, period="1d", interval="15m")
    
            data = data["Close"]
    
            current_price = round(data[0], 2)

            ax[stock_list.index(stock)].plot(data)
            ax[stock_list.index(stock)].set_ylabel('Price ($)')
            ax[stock_list.index(stock)].set_xlabel('15 minute intervals')
            ax[stock_list.index(stock)].legend(["{}: $%.2f".format(stock) %current_price], fontsize=14)

        plt.suptitle("date: {}".format(today), fontsize=15)
        plt.show()

    stock_retrieval()

if __name__ == '__main__':
    main()
    
