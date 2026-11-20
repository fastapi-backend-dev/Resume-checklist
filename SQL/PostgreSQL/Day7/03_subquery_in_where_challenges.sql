-- Challenge 1
SELECT
	*
FROM
	film
WHERE
	length > (
	SELECT
		AVG(length)
	FROM
		film
	);



-- Challenge 2
SELECT * FROM film
WHERE
film_id IN (SELECT film_id FROM inventory WHERE store_id = 2 GROUP BY film_id HAVING COUNT(*) > 3);