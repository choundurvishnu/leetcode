# Write your MySQL query statement below
WITH daily_activity AS(
    SELECT 
        activity_date, user_id,
        ROW_NUMBER() OVER (PARTITION by activity_date, USER_id order by activity_date )
        AS rn
        from Activity where activity_date BETWEEN DATE('2019-07-27') - INTERVAL 29 DAY AND DATE('2019-07-27')
)
SELECT
    activity_date AS day,
    COUNT(user_id) AS active_users
FROM daily_activity
WHERE rn = 1
GROUP BY activity_date;


/*
SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE('2019-07-27') - INTERVAL 29 DAY
                        AND DATE('2019-07-27')
GROUP BY activity_date;





*/
