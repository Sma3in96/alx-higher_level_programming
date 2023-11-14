-- adv task2
-- select city, avg order
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city
ORDER BY avg_temp DESC;
