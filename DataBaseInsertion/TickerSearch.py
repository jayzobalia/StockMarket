import requests
from dotenv import load_dotenv
import os
from DataBaseInsertion import utils

load_dotenv()

def get_symbol():
    keyword = input("Enter a stock that you want to search: ")
    data = {
        "function": "SYMBOL_SEARCH",
        "keywords": keyword,
        "apikey": os.getenv("API_KEY")
    }

    r = requests.get(os.getenv("URL"), data)
    rep = r.json()
    results = rep["bestMatches"]
    stock_dict = {}
    for i in range(len(results)):
        cmp = results[i]
        name = cmp["2. name"]
        symb = cmp["1. symbol"]

        stock_dict.update({name: symb})

    if len(stock_dict) <= 0:
        stock_dict = {}

    if stock_dict:
        print("List of Potential Matches: ", stock_dict)
        y = input("Select one option from the given list of matches. i.e. Select a number: ")
        name = utils.get_nth_key(stock_dict, int(y) - 1)
        symbol = stock_dict.get(name)
        return symbol



