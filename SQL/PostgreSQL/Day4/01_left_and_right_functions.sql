SELECT
	last_name,
	RIGHT(LEFT(last_name, 3), 1)
FROM
	customer;