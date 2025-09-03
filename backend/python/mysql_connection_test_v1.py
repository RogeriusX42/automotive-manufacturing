import mysql.connector 

cn = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="AlanTuring@2025", 
    database="automotive_manufacturing", 
    port=3306
)

cn.close()