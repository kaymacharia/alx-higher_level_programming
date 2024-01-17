--Script for displaying all the cities in California recorded in the database.
--Query to enumerate all the cities belonging to California.

SELECT id, name 
FROM cities
WHERE state_id = ( -- Query to get the id of California
      SELECT id
      FROM states
      WHERE name = "California");
