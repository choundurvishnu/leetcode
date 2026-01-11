# Write your MySQL query statement below
SELECT p.product_name, s.year,s.price from Product p join Sales s on p.product_id = s.product_id