-- cities by state joinned
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE states.id = cities.state_id 
