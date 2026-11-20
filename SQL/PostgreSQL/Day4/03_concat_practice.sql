SELECT
	LEFT(first_name, 1) || '.' || RIGHT(last_name, 1)
FROM
	customer;