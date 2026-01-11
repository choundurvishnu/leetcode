# Write your MySQL query statement below
SELECT s.name FROM SALESPERSON s WHERE NOT EXISTS (
    SELECT 1 FROM Company c JOIN Orders o on c.com_id = o.com_id where c.name='RED' 
    AND o.sales_id = s.sales_id
)


