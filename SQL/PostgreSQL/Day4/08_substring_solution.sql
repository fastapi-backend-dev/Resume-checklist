-- Challenge 1
SELECT
	email,
	SUBSTRING(email FROM 1 FOR 1) || '***.' || SUBSTRING(email FROM POSITION('.' IN email)+1 FOR 1)
	|| '***' || SUBSTRING(email FROM POSITION('@' IN email))
FROM
	customer;

-- Challenge 2
SELECT
	email,
	'***' || SUBSTRING(email FROM POSITION('.' IN email)-1 FOR 1) || '.' || SUBSTRING(email FROM POSITION('.' IN email)+1 FOR 1)
	|| '***' || SUBSTRING(email FROM POSITION('@' IN email))
FROM
	customer;