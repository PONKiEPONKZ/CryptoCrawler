"""
This code defines a Flask application that serves an index page at the root route and a JSON representation of processed data at the '/data' route.
"""
from flask import Flask, jsonify, render_template
from data import collect_and_process_data
from utils.logger import logger

app = Flask(__name__)


@app.route("/")
def index():
    """
    Renders the index.html template for the root route.

    Returns:
        str: The rendered HTML template.
    """
    logger.info("Handling index route")
    return render_template("index.html")


@app.route("/data")
def get_data():
    """
    Collects and processes data from the data source, and returns it as JSON.

    Returns:
        str: The JSON representation of the processed data.
    """
    logger.info("Handling data route")
    df = collect_and_process_data()
    if df is None:
        logger.warning("Data collection and processing failed")
        return jsonify([])
    df_dict = df.rename(columns={
        'CryptoSymbol': 'CryptoSymbol',
        'Cryptocurrency': 'Cryptocurrency',
        'Last Price': 'Last Price',
        'High Price': 'High Price',
        'Low Price': 'Low Price',
        'market_cap': 'Market Cap',
        'Volume': 'Volume'
    }).to_dict(orient="records")
    logger.info("Data collection and processing completed successfully")
    print(df_dict)
    return jsonify(df_dict)


if __name__ == "__main__":
    logger.info("Starting application")
    app.run()