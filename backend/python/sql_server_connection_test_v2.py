import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ROGERIO\SQLEXPRESS;"
    "DATABASE=AdventureWorksDW2020;"
    "UID=sa;"
    "PWD=AlanTuring@2025"
)

cursor = conn.cursor()
cursor.execute("SELECT TOP 10 ProductKey, EnglishProductName FROM DimProduct")

result = cursor.fetchall() 

print('\n--- RAW RESULT ---') 
print(result) 

print('\n--- PROCESSED RESULT ---') 
for row in result:
    print(f"ProductKey: {row.ProductKey}, EnglishProductName: {row.EnglishProductName}")