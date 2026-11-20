SELECT
	seat_no,
	ROUND(AVG(amount), 2) AS avg_price
FROM
	ticket_flights tf
		JOIN
	boarding_passes bp ON tf.ticket_no = bp.ticket_no AND tf.flight_id = bp.flight_id
GROUP BY seat_no
ORDER BY avg_price DESC;