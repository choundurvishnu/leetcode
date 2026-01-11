# Write your MySQL query statement below
SELECT Max(num) AS NUM FROM MyNumbers where NUM NOT IN (SELECT num from MyNumbers group by num having count(*)>1)