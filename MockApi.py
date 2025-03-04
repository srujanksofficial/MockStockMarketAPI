from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# List of sample stocks
stocks = {
    "AAPL": "Apple Inc.",
    "GOOGL": "Alphabet Inc.",
    "MSFT": "Microsoft Corporation",
    "AMZN": "Amazon.com, Inc.",
    "TSLA": "Tesla, Inc."
}

@app.route('/api/stocks', methods=['GET'])
def get_stocks():
    # Generate random stock prices and create the desired response structure
    stock_data = [
        {
            "stock_name": name,
            "symbol": symbol,
            "date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z"),
            "price": round(random.uniform(100, 1500), 2)
        }
        for symbol, name in stocks.items()
    ]
    return jsonify({"stocks": stock_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
