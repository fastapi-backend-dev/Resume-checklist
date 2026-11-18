SELECT
	*
FROM
	boarding_passes bp
		FULL OUTER JOIN
	tickets t ON bp.ticket_no = t.ticket_no
WHERE
 	t.ticket_no IS NULL;