-- Write a SQL script that creates a function SafeDiv that
-- divides (and returns) the first by the second number or
-- returns 0 if the second number is equal to 0.

-- Requirements:

-- You must create a function
-- The function SafeDiv takes 2 arguments:
-- a, INT
-- b, INT
-- And returns a / b or 0 if b == 0
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 2)
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN CAST(a AS DECIMAL(10, 2)) / CAST(b AS DECIMAL(10, 2));
    END IF;
END;
//
DELIMITER ;