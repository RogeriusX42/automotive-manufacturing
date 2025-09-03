import mysql.connector 

cn = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="AlanTuring@2025", 
    database="automotive_manufacturing", 
    port=3306
)

print("Connected: ", cn.is_connected())

cur = cn.cursor()

sql = """
INSERT INTO products (product_name)
VALUES (%s)
"""

data = [
    ('Polo Highline 2024',), ('Onix 2025',), ('Fit 2015',), ('Palio 2012',)
    ]

cur.executemany(sql, data)
cn.commit()

print(cur.rowcount, "rows inserted.")
cn.close()








#1st test - Didn't pass 

#cars = ['Polo Highline', 'Onix', 'Fit', 'Palio']
#cursor = cn.cursor()
#insert_query = f"INSERT INTO products(name) VALUES ('{cars[0]}'), ('{cars[1]}'), ('{cars[2]}'), ('{cars[3]}')" 
#cursor.executemany(insert_query)
#cn.commit()

#print(cursor.rowcount, "rows inserted")
#cursor.close()

#cn.close()