SELECT
	email,
	LEFT(email, POSITION(last_name IN email)-2)
FROM
	customer;