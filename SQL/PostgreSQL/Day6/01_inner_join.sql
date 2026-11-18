SELECT
	p.*,
	first_name,
	last_name
FROM
	payment p
		INNER JOIN
	staff s ON p.staff_id = s.staff_id
WHERE
	p.staff_id = 1;