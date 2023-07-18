-- lists all records of the table second_table of the database hbtn_0c_0 in MySQL server.
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
-- database name will be passed as an argument to the mysql command
SELECT score, name FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
