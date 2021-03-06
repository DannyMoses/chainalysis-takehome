config = {
    "PORT" : 3000,
    "EXCHANGES" : [("Blockchain", "blockchain.com"), ("Gemini", "gemini.com")],
    "site" : 0,
    "api" : 1,
    "last_price" : 2,
    "CRYPTOS" : [("BTC", "Bitcoin"), ("ETH", "Ethereum")],
    "FIATS" : ["USD"],
    "INTERVAL" : 1,
    "Blockchain" : ["blockchain.com", "https://api.blockchain.com/v3/exchange/tickers/", "last_trade_price", "error",
        lambda crypto, fiat: f"{crypto.upper()}-{fiat.upper()}" ],
    "Gemini" : ["gemini.com", "https://api.gemini.com/v1/pubticker/", "last", "result",
        lambda crypto, fiat: f"{crypto.lower()}{fiat.lower()}"]
}
