import serial
import json
import threading
from datetime import datetime
import mysql.connector

# --- Config ---
SERIAL_PORT = "COM3"     # Change as needed
BAUD = 9600
DB = dict(
    host="localhost",
    user="root",
    password="AlanTuring@2025",
    database="automotive_manufacturing"
)

# --- DB setup ---
cn = mysql.connector.connect(**DB)
cur = cn.cursor()
sql = "INSERT INTO batch(Product_ID, Quality, timeframe) VALUES (%s, %s, %s)"

# --- Serial reader ---
def read_serial():
    ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)
    while True:
        line = ser.readline().decode("utf-8", errors="ignore").strip().split(",")
        if len(line) < 2:
            continue
        product_id, quality = line[0], line[1]
        ts = datetime.now()

        # Log to JSON file
        data = {"timeframe": ts.strftime('%Y-%m-%d %H:%M:%S'),
                "ProductID": product_id,
                "Quality": quality}
        print(json.dumps(data, indent=2))
        with open("production_cars_v2.json", "a") as f:
            f.write(json.dumps(data) + ",\n")

        # Insert into MySQL
        try:
            cur.execute(sql, (product_id, float(quality), ts))
            cn.commit()
        except Exception as e:
            print("DB error:", e)

# --- Start thread ---
thread = threading.Thread(target=read_serial, daemon=True)
thread.start()

while True:
    pass