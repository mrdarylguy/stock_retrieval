import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

class Retrieval:
    def __init__(self):
        self.timeInterval = None
        self.timePeriod = None
        self.date = datetime.today()
        self.num_of_rows = 1
        self.num_of_columns = 0
        self.output_path = None  

    def formatted_date(self):
        today = self.date
        today = today.strftime("%B, %d, %Y")
        return today

    def color(self, data):
        if data[0] - data[1] > 0:
            return "green"
        elif data[0] - data[1] < 0:
            return "red"
        elif data[0] == data[1]:
            return "black"

        else:
            return "grey"

    def percentage_sign(self, data):
        if data[0] - data[1] > 0:
            return "+"
        elif data[0] - data[1] < 0:
            return "-"

    def percentage_change(self, data):
        absolute_change = data[0] - data[1]
        percentage = 100 * absolute_change/data[1]
        percentage = round(percentage, 2)
        return percentage

    def plotting(self, stock):
        data=yf.download(stock, period=self.timePeriod, interval=self.timeInterval)
        data=data["Close"]
        current_price=round(data[0], 2)

        plt.plot(data, color=self.color(data), linewidth='2.5')
        plt.grid()
        plt.title(label="{}{}%".format(self.percentage_sign(data), self.percentage_change(data)),
        fontsize=16,
        color=self.color(data))

        plt.ylabel("Price ($)", fontsize=12)
        plt.xlabel("{} intervals".format(self.timeInterval), fontsize=12)
        plt.legend(["{}: $%.2f".format(stock)%current_price], fontsize=14)

        plt.subplot(1, self.num_of_columns, stock_list.index(stock)+1)

    def extract_stock_data(self, stock_list, time_interval, time_period):

        self.num_of_columns = len(stock_list)
        self.timeInterval = time_interval
        self.timePeriod = time_period

        fig, ax = plt.subplots(self.num_of_rows, self.num_of_columns)
        fig.subplots_adjust(wspace=0.3)
        fig.set_figwidth(15)

        for stock in stock_list:
            self.plotting(stock)
            
        plt.suptitle("Past 5 trading days, up til {}".format(self.formatted_date()),fontsize=15)
        plt.show()

if __name__ == '__main__':

    retrieval = Retrieval()
    stock_list = ["NIO", "XPEV", "F", "TSLA"]
    time_interval = '15m'
    time_period = '5d'
    retrieval.extract_stock_data(stock_list, time_interval, time_period)