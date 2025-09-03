USE automotive_manufacturing; 

SHOW TABLES; 
SHOW COLUMNS FROM batch; 
SHOW COLUMNS FROM products;
SHOW COLUMNS FROM refined_batch; 

SELECT * FROM products; 
SELECT * FROM batch; 

CREATE TABLE refined_batch( 
	refined_batch_id INTEGER AUTO_INCREMENT PRIMARY KEY, 
    original_batch_id INTEGER, 
    product_id INTEGER, 
    product_name VARCHAR(255), 
    quality INTEGER, 
    batch_status VARCHAR(255), 
    tier VARCHAR(255)
); 

SHOW TABLES; 
SHOW COLUMNS FROM refined_batch; 
SELECT * FROM refined_batch; 

INSERT INTO refined_batch(original_batch_id, product_id, product_name, quality, batch_status, tier) 
SELECT 
	b.batch_id as 'Batch_ID' , 
    p.product_id as 'Product_ID', 
    p.product_name as 'Product Name', 
    #CONCAT(quality, '%') as 'Quality', 
    b.Quality,
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
