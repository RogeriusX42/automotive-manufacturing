USE automotive_manufacturing; 

SHOW TABLES; 

SHOW COLUMNS FROM batch; 
SHOW COLUMNS FROM products; 

SELECT * FROM products; 
SELECT * FROM batch; 

SELECT b.Batch_ID, p.Product_ID, p.product_name as Product_Name, b.Quality 
FROM batch as b 
INNER JOIN products as p 
ON b.Product_ID = p.product_ID 
#ORDER BY p.product_name DESC
#ORDER BY b.Batch_ID 
#ORDER BY b.Batch_ID DESC
#ORDER BY b.Quality 
#ORDER BY b.Quality DESC 