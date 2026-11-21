-- Substring syntax: SUBSTRING(string FROM start [FOR length])
-- string -> column/string that we want to extract from
-- start -> position (where to start from?)
-- length -> (Optional) How many characters (If ommited, it will extract from start to end)
-- Example 1: SUBSTRING(email FROM 2 FOR 3)
-- Example 2: SUBSTRING(email FROM POSITION('.' in email) FOR 3)
-- Example 3: SUBSTRING(email FROM POSITION('.' in email)+1 FOR 3)

SELECT
	email,
	--SUBSTRING(email FROM POSITION('.' in email)+1 FOR LENGTH(last_name))
	--SUBSTRING(email FROM 3 FOR 2)
	SUBSTRING(email FROM POSITION('.' in email)+1 FOR POSITION('@' IN email)-POSITION('.' in email)-1)
FROM
	customer;