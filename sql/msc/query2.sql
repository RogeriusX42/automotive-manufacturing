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
