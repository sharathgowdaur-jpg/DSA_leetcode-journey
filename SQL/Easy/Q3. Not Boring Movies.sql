# Write your MySQL query statement below
SELECT * FROM CinemA
WHERE id % 2 != 0 AND description != "boring"
ORDER BY rating DESC