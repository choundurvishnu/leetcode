# Write your MySQL query statement below
UPDATE SALARY
SET SEX = 
        CASE 
            WHEN sex = 'm' THEN 'f'
            ELSE 'm'
        END;
