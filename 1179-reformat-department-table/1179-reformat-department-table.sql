# Write your MySQL query statement below
SELECT
    id,
    SUM(CASE WHEN month = 'Jan' THEN revenue ELSE null END) AS Jan_Revenue,
    SUM(CASE WHEN month = 'Feb' THEN revenue ELSE null END) AS Feb_Revenue,
    SUM(CASE WHEN month = 'Mar' THEN revenue ELSE null END) AS Mar_Revenue,
    SUM(CASE WHEN month = 'Apr' THEN revenue ELSE null END) AS Apr_Revenue,
    SUM(CASE WHEN month = 'May' THEN revenue ELSE null END) AS May_Revenue,
    SUM(CASE WHEN month = 'Jun' THEN revenue ELSE null END) AS Jun_Revenue,
    SUM(CASE WHEN month = 'Jul' THEN revenue ELSE null END) AS Jul_Revenue,
    SUM(CASE WHEN month = 'Aug' THEN revenue ELSE null END) AS Aug_Revenue,
    SUM(CASE WHEN month = 'Sep' THEN revenue ELSE null END) AS Sep_Revenue,
    SUM(CASE WHEN month = 'Oct' THEN revenue ELSE null END) AS Oct_Revenue,
    SUM(CASE WHEN month = 'Nov' THEN revenue ELSE null END) AS Nov_Revenue,
    SUM(CASE WHEN month = 'Dec' THEN revenue ELSE null END) AS Dec_Revenue
FROM department
GROUP BY
    id
ORDER BY
    id;
    

# Table was created as follows-
# Create table If Not Exists Department (id int, revenue int, month varchar(5))
# Truncate table Department
# insert into Department (id, revenue, month) values ('1', '8000', 'Jan')
# insert into Department (id, revenue, month) values ('2', '9000', 'Jan')
# insert into Department (id, revenue, month) values ('3', '10000', 'Feb')
# insert into Department (id, revenue, month) values ('1', '7000', 'Feb')
# insert into Department (id, revenue, month) values ('1', '6000', 'Mar')