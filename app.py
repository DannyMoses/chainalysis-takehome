from flask import Flask, request, jsonify, render_template
import requests
import threading
import time

from config import config

def getFromBlockchain(symbol):
    r = requests.get(config["blockchain"][1] + config["blockchain"][-1](symbol, "usd"))
    return r.json()[config["blockchain"][2]]

def getFromGemini(symbol):
    r = requests.get(config["gemini"][1]  + config["gemini"][-1](symbol, "usd"))
    return r.json()[config["gemini"][2]]

def getPrice(exchange, symbol="BTC", fiat="USD"):
    r = requests.get(config[exchange][1] + config[exchange][-1](symbol, fiat))
    if config[exchange][3] in r.json():
        return -1.0
    else:
        return r.json()[config[exchange][2]]

workerLock = threading.Lock()
prices = {}
def workerThread():
    while True:
        workerLock.acquire()
        for coin in config["CRYPTOS"]:
            for exchange in config["EXCHANGES"]:
                prices[exchange[0]][coin[0]] = float(getPrice(exchange[0], coin[0]))
        workerLock.release()
        time.sleep(config["INTERVAL"])

def create_app():
    app = Flask(__name__)
    for exchange in config["EXCHANGES"]:
        prices[exchange[0]] = {crypto[0] : 0.0 for crypto in config["CRYPTOS"]}
    worker = threading.Thread(target=workerThread, name="price-updater", daemon=True)
    worker.start()

    return app

app = create_app()

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
    ret = {}
    #for e in config["EXCHANGES"]:
    #    ret[e[0]] = getPrice(e[0], crypto)
    workerLock.acquire()
    for e in config["EXCHANGES"]:
        ret[e[0]] = prices[e[0]][crypto]
    workerLock.release()
    return ret

if __name__ == "__main__":
    app.run(port=config["PORT"])
