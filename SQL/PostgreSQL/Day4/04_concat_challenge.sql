SELECT
	LEFT(email, 1) || '***' || RIGHT(email, 19)
FROM
	customer;