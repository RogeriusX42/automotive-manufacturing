import mysql.connector 

cn = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="AlanTuring@2025", 
    database="automotive_manufacturing", 
    port=3306
)

print("Connected: ", cn.is_connected())

cursor = cn.cursor()
cursor.execute("SELECT * FROM batch")
rows = cursor.fetchall()
print("\nBatches: ")
for row in rows:
    print(row)
cursor.close()

cursor = cn.cursor()
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()
print("\nProducts: ")
for row in rows:
    print(row)
cursor.close()


cn.close()