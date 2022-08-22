-- Lists all record in the table second_table witha score >= in my SQL SERVER.
-- Records are ordered by descending score.
SELECT 'score', 'name'
FROM 'second_table'
WHERE 'score' >= 10
ORDER BY 'score' DESC;
