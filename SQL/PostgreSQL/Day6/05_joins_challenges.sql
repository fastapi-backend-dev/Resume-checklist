SELECT
	first_name,
	last_name,
	phone,
	district
FROM
	customer c
		INNER JOIN
	address a ON c.address_id = a.address_id
WHERE
	district = 'Texas';


SELECT
	a.address_id,
	address
FROM
	customer c
		RIGHT JOIN
	address a ON c.address_id = a.address_id
WHERE c.address_id IS NULL;