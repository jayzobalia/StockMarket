import TickerSearch
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
import os

load_dotenv()


def get_df(symbol, size):
    # symbol = TickerSearch.get_symbol()
    app = TimeSeries(os.getenv("API_KEY"), output_format='pandas')
    df = app.get_daily_adjusted(symbol, outputsize=size)
    df = df[0]
    df.to_csv("DataBaseInsertion\\Stock CSVs\\xx.csv")
