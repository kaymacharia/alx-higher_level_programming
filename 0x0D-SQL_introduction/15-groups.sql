--Counts the occurrences of records with identical scores.
SELECT score, COUNT(score) AS number FROM second_table
    GROUP BY score
    ORDER BY score DESC;
