-- Challenge 1
SELECT title, film_id, replacement_cost, rating
FROM film f1
WHERE replacement_cost = (SELECT MIN(replacement_cost)
						  FROM film f2
						  WHERE f1.rating = f2.rating)
ORDER BY f1.title;


-- Challenge 2
SELECT title, film_id, length, rating
FROM film f1
WHERE length = (SELECT MAX(length)
						  FROM film f2
						  WHERE f1.rating = f2.rating)
ORDER BY f1.title;