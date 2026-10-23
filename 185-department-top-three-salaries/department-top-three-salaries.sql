
SELECT department, employee, salary
FROM (
    SELECT
        d.name AS department,
        e.name AS employee,
        e.salary,
        DENSE_RANK() OVER (
            PARTITION BY d.id
            ORDER BY e.salary DESC
        ) AS rnk
    FROM Employee AS e
    LEFT JOIN Department AS d
        ON e.departmentId = d.id
) AS ranked_employees
WHERE rnk <= 3;
