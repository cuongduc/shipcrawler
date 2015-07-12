-- UPDATE ship_categories
-- SET name = 'Bulkers' WHERE
-- name LIKE 'Bulkers%'

-- DELETE FROM ship_categories
-- WHERE name = 'Bulkers' AND id != 5
-- 
-- SELECT * FROM ship_categories
-- ORDER BY id;

-- UPDATE ship_categories
-- SET name = 'General Cargo' WHERE
-- name LIKE 'General cargo ships%'

-- DELETE FROM ship_categories
-- WHERE id != 101 AND id IN (
-- SELECT id FROM ship_categories
-- WHERE name = 'General Cargo'

-- SELECT id FROM ship_categories
-- WHERE name LIKE '%General cargo%'
-- ORDER BY id

-- DELETE FROM ship_categories
-- WHERE id != 101 AND id IN (SELECT id FROM ship_categories
-- WHERE name LIKE '%General cargo%'
-- ORDER BY id)

-- UPDATE ship_categories SET name = 'General Cargo Ship'
-- WHERE name LIKE 'General cargo%'

-- SELECT id FROM ship_categories
-- WHERE name LIKE 'Containerships%'

-- DELETE FROM ship_categories
--        WHERE id != 4 AND id IN (
-- 	  SELECT id FROM ship_categories
-- 	  WHERE name LIKE 'Containerships%' 
-- 	  ORDER BY id
-- 	)

-- SELECT id FROM ship_categories
-- WHERE name LIKE '%Cruise Ships%'
-- ORDER BY id

-- DELETE FROM ship_categories
--        WHERE id != 13 AND id IN (
-- 	  SELECT id FROM ship_categories
-- 	  WHERE name LIKE '%Cruise Ships%' 
-- 	  ORDER BY id
-- 	)

-- SELECT id FROM ship_categories
-- WHERE name LIKE 'Gas Tankers%';

-- DELETE FROM ship_categories
--        WHERE id != 13 AND id IN (
-- 	  SELECT id FROM ship_categories
-- 	  WHERE name LIKE '%Cruise Ships%' 
-- 	  ORDER BY id
-- 	)

-- DELETE FROM ship_categories
--        WHERE id != 265 AND id IN (
-- 	  SELECT id FROM ship_categories
-- 	  WHERE name LIKE '%Cruise Ships%' 
-- 	  ORDER BY id
-- 	)
