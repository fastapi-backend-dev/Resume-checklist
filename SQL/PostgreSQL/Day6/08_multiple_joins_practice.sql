SELECT
	passenger_name,
	scheduled_arrival
FROM
	tickets t
		JOIN
	ticket_flights tf ON t.ticket_no = tf.ticket_no
		JOIN
	flights f ON tf.flight_id = f.flight_id;