SELECT
	*
FROM
	payment
WHERE
	customer_id IN (
	SELECT
		customer_id
	FROM
		customer
	WHERE first_name LIKE 'A%'
	);