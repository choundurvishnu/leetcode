# Write your MySQL query statement below
SELECT DISTINCT email
FROM (
    SELECT email, COUNT(*) OVER (PARTITION BY email) AS cnt
    FROM Person
) t
WHERE cnt > 1;

