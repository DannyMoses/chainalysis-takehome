from flask import Flask, request, jsonify
import requests

from config import config

app = Flask(__name__)

# get ticker from Blockchain.com
# returns:
# { symbol : str, price_24h : float, volume_24_h : float, last_trade_price : float }
def getFromBlockchain(symbol):
    r = requests.get('https://api.blockchain.com/v3/exchange/tickers/' + symbol)
    return r.json()

def getFromGemini(symbol):
    r = requests.get('https://api.gemini.com/v1/pubticker/' + symbol)
    return r.json()


exchanges = { "blockchain.com" : ["BTC-USD", "ETH-USD"], "gemini.com" : ["btcusd", "ethusd"] }

@app.route('/exchanges', methods=['GET'])
def getExhanges():
    return { "data" : config["EXCHANGES"] }

@app.route('/ticker', methods=["GET"])
def getTicker():
   exchange = request.args.get('exchange')
   currency = request.args.get('currency')

   print(exchange, currency)
   return 200


