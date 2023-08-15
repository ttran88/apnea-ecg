import wfdb
import sqlite3
import os

# Determine the path to the source directory
source_dir = os.path.dirname(os.path.abspath(__file__))
recordname = os.path.join(source_dir, "apnea-ecg-database-1.0.0/b01")

# Load the waveforms
record = wfdb.rdsamp(recordname)
signal = record[0]
annotation = wfdb.rdann(recordname, 'atr')

# Connect to SQLite database (it will create 'ecg_data.db' if it doesn't exist)
conn = sqlite3.connect('ecg_data.db')
cursor = conn.cursor()

# Create a table for the ECG signals
cursor.execute('''
CREATE TABLE IF NOT EXISTS ecg_signals (
    id INTEGER PRIMARY KEY,
    time_index INTEGER,
    amplitude REAL
)
''')

# Insert the ECG signal data into the ecg_signals table
signal_data = [(index, value[0]) for index, value in enumerate(signal)]
cursor.executemany('INSERT INTO ecg_signals (time_index, amplitude) VALUES (?, ?)', signal_data)

# Create a table for the annotations
cursor.execute('''
CREATE TABLE IF NOT EXISTS annotations (
    id INTEGER PRIMARY KEY,
    annotation_index INTEGER,
    symbol TEXT
)
''')

# Insert the annotation data into the annotations table
annotation_data = list(zip(annotation.sample, annotation.symbol))
cursor.executemany('INSERT INTO annotations (annotation_index, symbol) VALUES (?, ?)', annotation_data)

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Data has been successfully ingested into SQLite database.")
