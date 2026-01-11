# Write your MySQL query statement below
SELECT name from Customer where ifnull(referee_id,0) != 2