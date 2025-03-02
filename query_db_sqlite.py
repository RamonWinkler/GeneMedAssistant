import sqlite3
import pandas as pd

def query_gene(symbol):
    conn = sqlite3.connect("genes.db")
    query = "SELECT * FROM gene_info WHERE Symbol = ? LIMIT 1;"
    df = pd.read_sql_query(query, conn, params=(symbol,))
    conn.close()
    return df.to_dict(orient="records")

# example
#gene_data = query_gene("TP53")
#print(gene_data)