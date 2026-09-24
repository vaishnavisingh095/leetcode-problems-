# Write your MySQL query statement below
select e1.name as employee
from employee e1
join employee e2 
ON e1.managerId = e2.Id
where e1.salary>e2.salary;
