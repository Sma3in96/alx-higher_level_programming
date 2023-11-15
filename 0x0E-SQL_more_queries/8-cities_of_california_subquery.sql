-- select id and name for state.name
SELECT cities.id , cities.name 
FROM cities , states 
WHERE states.name = "California" AND states.id = cities.state_id;
