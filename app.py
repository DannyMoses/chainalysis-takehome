from flask import Flask, request, jsonify, render_template
import requests

from config import config

app = Flask(__name__)

# get ticker from Blockchain.com
# returns:
# { symbol : str, price_24h : float, volume_24_h : float, last_trade_price : float }
def getFromBlockchain(symbol):
    r = requests.get(config["blockchain"][1] + symbol)
    return r.json()[config["blockchain"][2]]

def getFromGemini(symbol):
    r = requests.get(config["gemini"][1]  + symbol)
    return r.json()[config["gemini"][2]]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/exchanges', methods=['GET'])
def getExhanges():
    return { "data" : config["EXCHANGES"] }

@app.route('/ticker', methods=["GET"])
def getTicker():
   exchange = request.args.get('exchange')
   currency = request.args.get('currency')

   print(exchange, currency)
   return 200

@app.route("/update/<crypto>", methods=["GET"])
def update(crypto="BTC"):
    if (crypto == "BTC"):
        return {"blockchain" : float(getFromBlockchain("BTC-USD")), "gemini" : float(getFromGemini("btcusd"))}
    elif (crypto == "ETH"):
        return {"blockchain" : float(getFromBlockchain("ETH-USD")), "gemini" : float(getFromGemini("ethusd"))}
