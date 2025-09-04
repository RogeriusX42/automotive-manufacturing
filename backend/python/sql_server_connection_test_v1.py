from sqlalchemy import create_engine, text
import urllib

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ROGERIO\\SQLEXPRESS;"
    "DATABASE=AdventureWorksDW2020;"
    "UID=sa;"
    "PWD=AlanTuring@2025"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
with engine.connect() as conn:
    result = conn.execute(text("SELECT TOP 10 * FROM DimProduct"))
    for row in result:
        print(row)