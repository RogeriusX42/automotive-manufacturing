import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=ROGERIO\\SQLEXPRESS,1433;DATABASE=automotive_manufacturing;Trusted_Connection=yes'
    )
    print("✅ Connected successfully.")
    conn.close()
except Exception as e:
    print("❌ Connection failed.")
    print(e)