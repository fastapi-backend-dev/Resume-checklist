SELECT
	email,
	RIGHT(email, 5)
FROM
	customer;


SELECT
	email,
	LEFT(RIGHT(email, 4), 1)
FROM
	customer;
