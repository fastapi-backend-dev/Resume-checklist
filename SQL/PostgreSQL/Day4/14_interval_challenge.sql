-- Challenge 1
SELECT
	customer_id,
	return_date - rental_date AS rental_duration
FROM
	rental
WHERE
	customer_id = 35;



-- Challenge 2
SELECT
	customer_id,
	AVG(return_date - rental_date) AS avg_rental_duration
FROM
	rental
GROUP BY customer_id
ORDER BY avg_rental_duration DESC;