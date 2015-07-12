-- SELECT * FROM ship_list
-- WHERE category_id NOT IN (SELECT id FROM ship_categories)

-- SELECT * from ship_categories
-- WHERE name LIKE '%Heavy Lift%'

-- UPDATE ship_list
-- SET category_id = 51
-- WHERE category_id = 1

-- CREATE TABLE train_ship (
-- 	image CHARACTER VARYING(100) NOT NULL,
-- 	category_id SMALLINT
-- )

-- CREATE INDEX train_image_idx ON train_ship USING btree (image)
-- CREATE INDEX train_image_hash_idx ON train_ship USING hash (category_id)

-- INSERT INTO train_ship
-- SELECT image, category_id FROM ship_list
-- WHERE image IS NOT NULL
-- AND category_id IS NOT NULL

-- INSERT INTO val(image, category_id)
-- SELECT image, category_id FROM ship_list OFFSET random()*180900 LIMIT 40000;

-- CREATE TABLE val (
--  image CHARACTER VARYING(255),
--  category_id SMALLINT
-- )

-- DELETE FROM train_ship WHERE image IN (SELECT image FROM val)
-- CREATE TABLE train1(
-- image CHARACTER VARYING(255)
-- );
-- 
-- CREATE TABLE val2(
-- image CHARACTER VARYING(255)
-- )

-- SELECT t.image, ts.category_id
-- FROM train_ship ts, train1 t
-- WHERE t.image = ts.image
-- ORDER BY ts.category_id

-- SELECT COUNT(sub.img) count_img, sub.id
-- FROM (SELECT v.image img, ts.category_id id
-- FROM ship_list ts, val2 v
-- WHERE v.image = ts.image
-- ORDER BY ts.category_id) sub
-- GROUP BY sub.id
-- ORDER BY count_img

SELECT v.image, ts.category_id
FROM ship_list ts, train1 v
WHERE v.image = ts.image
ORDER BY ts.category_id