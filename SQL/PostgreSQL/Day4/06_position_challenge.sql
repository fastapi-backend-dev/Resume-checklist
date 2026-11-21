SELECT
	last_name || ', ' || LEFT(email, POSITION('.' IN email)-1)
FROM
	customer;