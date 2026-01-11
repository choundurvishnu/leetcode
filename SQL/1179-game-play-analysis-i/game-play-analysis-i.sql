# Write your MySQL query statement below
With Ranked AS(
    Select player_id, event_date, Row_number() over(partition by player_id order by event_date) AS rn from Activity
)
SELECT
    player_id,
    event_date AS first_login
FROM ranked
WHERE rn = 1;

/*
SELECT
    player_id,
    min(event_date) AS first_login
FROM Activity
group by player_id;
*/
