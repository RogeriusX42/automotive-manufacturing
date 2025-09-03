CREATE DATABASE automotive_manufacturing; 
USE automotive_manufacturing; 

CREATE TABLE products( 
	Product_ID INTEGER AUTO_INCREMENT PRIMARY KEY, 
	product_name VARCHAR(255)
); 

CREATE TABLE batch(
	Batch_ID INTEGER AUTO_INCREMENT PRIMARY KEY, 
    Product_ID INTEGER, 
    Quality INTEGER 
);

INSERT INTO products (product_name) VALUES ('Civic'), ('Corolla'), ('City'), ('Argo'), ('Polo'), ('T-Cross'); 
INSERT INTO products (product_name) VALUES ('Cronos');
SELECT product_name from products; 
SELECT Product_ID from products; 
SELECT product_name, product_ID from products; 
SELECT * from products; 

INSERT INTO batch (Product_ID, Quality) VALUES (1, 90), (2, 80), (3, 86), (4, 85), (5, 84), (6, 92), (7, 99); 

SELECT Batch_ID from batch; 
SELECT Product_ID from batch; 

SELECT DISTINCT COUNT(Product_ID) from batch; 
SELECT COUNT( DISTINCT Product_ID) from batch; 

SELECT b.batch_id, p.product_name FROM batch AS b INNER join products AS p ON b.product_id = p.product_id; 

SELECT b.batch_id as 'Batch' , p.product_name as 'Product Name', CONCAT(quality, '%') as 'Quality'
FROM batch as b 
INNER JOIN products AS p 
ON b.product_id = p.product_id; 


SELECT 
	b.batch_id as 'Batch' , 
    p.product_name as 'Product Name', 
    CONCAT(quality, '%') as 'Quality', 
    IF(quality >= 85, 'approved', 'rejected') as 'Status'
FROM batch as b 
INNER JOIN products AS p 
ON b.product_id = p.product_id;


SELECT 
	b.batch_id as 'Batch' , 
    p.product_name as 'Product Name', 
    CONCAT(quality, '%') as 'Quality', 
    IF(quality >= 85, 'approved', 'rejected') as 'Status',
    CASE
		WHEN quality >= 99 THEN 'S'
        WHEN quality >= 90 THEN 'A'
        WHEN quality >= 85 THEN 'B'
        WHEN quality >= 80 THEN 'C'
        WHEN quality < 80 THEN 'D'
    END AS Tier 
FROM batch as b 
INNER JOIN products AS p 
ON b.product_id = p.product_id;







# SELECT FROM INNER JOIN ON 
