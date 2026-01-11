# Write your MySQL query statement below
SELECT actor_id, director_id from ActorDirector group by actor_id, director_id  having count(*) >= 3
order by actor_id,director_id


