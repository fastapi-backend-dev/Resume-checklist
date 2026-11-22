-- Challenge 1
SELECT
	*,
	(SELECT SUM(amount) FROM payment p2 WHERE p1.customer_id = p2.customer_id),
	(SELECT COUNT(*) FROM payment p3 WHERE p1.customer_id = p3.customer_id)
FROM
	payment p1
ORDER BY customer_id;


-- Challenge 2
SELECT
	title, film_id, replacement_cost, rating,
	(SELECT MAX(replacement_cost) FROM film f2 WHERE f1.rating = f2.rating),
	(SELECT AVG(replacement_cost) FROM film f3 WHERE f1.rating = f3.rating)
FROM
	film f1
ORDER BY title;


-- Challenge 3 (Without payment id)
SELECT
	first_name,
	(SELECT MAX(amount) FROM payment p2 WHERE p1.customer_id = p2.customer_id)
FROM
	customer c
		JOIN
	payment p1 ON c.customer_id = p1.customer_id;


-- Challenge 3 (With payment id)
SELECT
	first_name,
	(SELECT MAX(amount) FROM payment p2 WHERE p1.customer_id = p2.customer_id),
	p1.payment_id
FROM
	customer c
		JOIN
	payment p1 ON c.customer_id = p1.customer_id;