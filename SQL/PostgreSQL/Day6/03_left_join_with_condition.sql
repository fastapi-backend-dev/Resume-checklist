SELECT
	*
FROM
	aircrafts_data ad
		LEFT JOIN
	flights f ON ad.aircraft_code = f.aircraft_code
WHERE
	f.flight_no IS NULL;