--Script to display all entries in a table
--Query to list all entries in the second_table where the name matches the specified value.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
