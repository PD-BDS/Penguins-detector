import sqlite3
import seaborn as sns
import pandas as pd

# Load the penguins dataset
penguins = sns.load_dataset("penguins").dropna()

# Mapping islands to unique IDs
island_mapping = {name: idx + 1 for idx, name in enumerate(penguins["island"].unique())}
penguins["island_id"] = penguins["island"].map(island_mapping)

# Connect to SQLite database
conn = sqlite3.connect("penguins.db")
cursor = conn.cursor()

# Create tables
cursor.executescript("""
CREATE TABLE IF NOT EXISTS islands (
    island_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS penguins (
    animal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    species TEXT NOT NULL,
    bill_length_mm REAL NOT NULL,
    bill_depth_mm REAL NOT NULL,
    flipper_length_mm REAL NOT NULL,
    body_mass_g REAL NOT NULL,
    sex TEXT NOT NULL,
    island_id INTEGER NOT NULL,
    FOREIGN KEY (island_id) REFERENCES islands(island_id) ON DELETE CASCADE
);
""")

# Insert island data
island_df = pd.DataFrame(list(island_mapping.items()), columns=["name", "island_id"])
island_df.to_sql("islands", conn, if_exists="append", index=False)

# Insert penguin data
penguins[["species", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex", "island_id"]] \
    .to_sql("penguins", conn, if_exists="append", index=False)

# Commit and close
conn.commit()
conn.close()

print("Database created successfully.")

