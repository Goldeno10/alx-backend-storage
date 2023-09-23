-- Write a SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans

-- Requirements:

-- Import this table dump: metal_bands.sql.zip
-- Column names must be: origin and nb_fans
-- Your script can be executed on any database
-- Context: Calculate/compute something is always power intensive…
--  better to distribute the load!
--  (especially in the case of a very large table)
-- Create a temporary table to hold the ranks
CREATE TEMPORARY TABLE temp_ranked_origins AS
SELECT
    origin,
    DENSE_RANK() OVER (ORDER BY SUM(nb_fans) ASC) AS country_rank
FROM
    metal_bands
GROUP BY
    origin;

-- Retrieve the ranked country origins
SELECT
    origin,
    country_rank
FROM
    temp_ranked_origins
ORDER BY
    country_rank;