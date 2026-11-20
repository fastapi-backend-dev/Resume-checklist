SELECT
	fare_conditions,
	COUNT(*)
FROM
	seats s
		JOIN
	flights f ON s.aircraft_code = f.aircraft_code
		JOIN
	boarding_passes bp ON f.flight_id = bp.flight_id
GROUP BY fare_conditions
ORDER BY 2 DESC;