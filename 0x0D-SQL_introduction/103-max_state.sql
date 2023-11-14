-- adv task 103
-- max function with select
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
