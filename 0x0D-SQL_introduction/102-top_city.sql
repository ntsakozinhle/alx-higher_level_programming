-- import the table dump into the hbtn_0c_0 database
-- script to display the top 3 cities' temperature during July and August

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
