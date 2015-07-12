-- SELECT COUNT(image) AS no_of_image, category_id
-- FROM ship_list
-- GROUP BY category_id
-- ORDER BY no_of_image

-- UPDATE ship_list SET category_id = 5
-- WHERE category_id IN (137,140,141,142,143,144,257,145,182)

-- UPDATE ship_list SET category_id = 101
-- WHERE category_id IN (SELECT id FROM ship_categories
-- WHERE name LIKE '%General cargo%'
-- ORDER BY id)

-- UPDATE ship_list SET category_id = 4
-- WHERE category_id IN (SELECT id FROM ship_categories
-- WHERE name LIKE 'Containerships%'
-- ORDER BY id)


-- UPDATE ship_list SET category_id = 265
-- WHERE category_id IN (SELECT id FROM ship_categories
-- WHERE name LIKE 'Gas Tankers%'
-- ORDER BY id)
