# Write your MySQL query statement below
/*
WITH Act2 AS(
    SELECT player_id,event_date, LEAD(event_date,1) OVER (partition by player_id order by event_date) AS Lead_date FROM Activity 
),
Act3 AS(
    SELECT player_id,event_date,Lead_date from Act2 WHERE event_date = (
        SELECT MIN(event_date)
        FROM Activity a
        WHERE a.player_id = Act2.player_id
    )
)
SELECT
    ROUND(
        SUM(
            CASE
                WHEN DATEDIFF(lead_date, event_date) = 1 THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS fraction
FROM Act3;
*/


SELECT
    ROUND(
        COUNT(DISTINCT a.player_id) /
        COUNT(DISTINCT f.player_id),
        2
    ) AS fraction
FROM (
    SELECT
        player_id,
        MIN(event_date) AS first_day
    FROM Activity
    GROUP BY player_id
) f
LEFT JOIN Activity a
    ON f.player_id = a.player_id
   AND a.event_date = DATE_ADD(f.first_day, INTERVAL 1 DAY);
