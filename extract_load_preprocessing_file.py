import sqlite3
import pandas as pd
import gzip

# Define columns from gene_info
column_names = [
    "#tax_id", "GeneID", "Symbol", "LocusTag", "Synonyms", "dbXrefs", 
    "chromosome", "map_location", "description", "type_of_gene",
    "Symbol_from_nomenclature_authority", "Full_name_from_nomenclature_authority",
    "Nomenclature_status", "Other_designations", "Modification_date", "Feature_type"
]

# Read the gzipped file
file_path = "gene_info.gz"

with gzip.open(file_path, 'rt') as f:
    df = pd.read_csv(f, sep="\t", comment="#", names=column_names, dtype=str)

# Create SQLite database and connection
conn = sqlite3.connect('genes.db')  # Corrected line
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS gene_info (
    tax_id TEXT,
    GeneID TEXT,
    Symbol TEXT,
    LocusTag TEXT,
    Synonyms TEXT,
    dbXrefs TEXT,
    chromosome TEXT,
    map_location TEXT,
    description TEXT,
    type_of_gene TEXT,
    Symbol_from_nomenclature_authority TEXT,
    Full_name_from_nomenclature_authority TEXT,
    Nomenclature_status TEXT,
    Other_designations TEXT,
    Modification_date TEXT,
    Feature_type TEXT
)
''')

# Insert data into the table
df.to_sql('gene_info', conn, if_exists='replace', index=False)

# Commit and close the connection
conn.commit()
conn.close()

print("Data successfully loaded into SQLite.")
