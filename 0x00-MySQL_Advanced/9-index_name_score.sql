-- Title: Index on name and score
-- Desc: Create an index on the first letter of the
-- name column and the score column
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score);