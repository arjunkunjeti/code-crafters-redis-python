# write a query to group dates by week and then check if the dircu is trending down
# if it is, then we can assume that the user is not active

# create a table to store the results
CREATE TABLE IF NOT EXISTS test (
    week_start DATE,
    DIRCU DOUBLE,
    active BOOLEAN
);

# insert the results into the table
INSERT INTO test
SELECT
    week_start,
    DIRCU,
    CASE
        WHEN DIRCU < LAG(DIRCU) OVER (ORDER BY week_start) THEN FALSE
        ELSE TRUE
    END AS active
    # lag over a percentage of the previous week
    # WHEN DIRCU < LAG(DIRCU) OVER (ORDER BY week_start) * 0.9 THEN FALSE
FROM (
    SELECT
        DATE_TRUNC('week', date) AS week_start,
        AVG(dircu) AS DIRCU
    FROM (
        SELECT
            date,
            dircu
        FROM
            test
        WHERE
            date > '2019-01-01'
    ) AS t
    GROUP BY
        week_start
) AS t;



WITH weekly_stats AS (
SELECT
    system,
    CONCAT(YEAR(date), '-', WEEK(date)) AS week,
    AVG(dircu) AS dircu
FROM
    test
WHERE system = 'test'
GROUP BY
    system,
    week
), weekly_change AS (
SELECT
    system,
    week,
    dircu,
    LAG(dircu) OVER (PARTITION BY system ORDER BY week) AS prev_dircu
FROM weekly_stats
)

SELECT
    system,
    week,
    dircu,
    prev_dircu,
    BOOL_OR((prev_dircu - dircu)/prev_dircu < 0.5) AS active
FROM weekly_change
GROUP BY 1