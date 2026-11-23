SELECT
	CURRENT_TIMESTAMP,
	TO_CHAR(return_date - rental_date, 'Dy, MI')
FROM
	rental;