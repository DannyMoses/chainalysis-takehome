from flask import Flask, request, jsonify, render_template
import requests

from config import config

app = Flask(__name__)

def getFromBlockchain(symbol):
    r = requests.get(config["blockchain"][1] + config["blockchain"][-1](symbol, "usd"))
    return r.json()[config["blockchain"][2]]

def getFromGemini(symbol):
    r = requests.get(config["gemini"][1]  + config["gemini"][-1](symbol, "usd"))
    return r.json()[config["gemini"][2]]

def getPrice(exchange, symbol="BTC", fiat="USD"):
    r = requests.get(config[exchange][1] + config[exchange][-1](symbol, fiat))
    return r.json()[config[exchange][2]]

@app.route('/')
def home():
    return render_template('index.html',cryptos=config["CRYPTOS"], exchanges=config["EXCHANGES"])

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
    # return {"Blockchain" : float(getFromBlockchain(crypto)), "Gemini" : float(getFromGemini(crypto))}
    ret = {}
    for e in config["EXCHANGES"]:
        ret[e[0]] = getPrice(e[0], crypto)
    return ret
