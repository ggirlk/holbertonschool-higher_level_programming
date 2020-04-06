-- Cities of California 
SELECT * FROM cities WHERE id = (SELECT state_id FROM states WHERE name = 'California')
