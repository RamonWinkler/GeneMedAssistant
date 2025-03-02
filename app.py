from flask import Flask, request, jsonify
import sqlite3
import pandas as pd

app= Flask(__name__)

@app.route("/", methods=["GET"])  # Root route
def home():
    return "APP is running"

# Function to query gene by symbol
def query_gene(symbol):
    conn = sqlite3.connect("genes.db")
    query = "SELECT * FROM gene_info WHERE Symbol = ?, LIMIT 1;"
    df = pd.read_sql_query(query, conn, params=(symbol,))
    conn.close()
    return df.to_dict(orient="records")

@app.route("/gene", methods=["GET"])
def get_gene():
    # Use 'request' to get query parameters
    symbol = request.args.get("symbol")  # Corrected line
    if symbol:
        return f"Gene Symbol: {symbol}"
    else:
        return "No gene symbol provided"

if __name__ == "__main__":
    app.run(debug= True)