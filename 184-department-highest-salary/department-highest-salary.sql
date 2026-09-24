# Write your MySQL query statement below
select d.name as department, e.name as employee, e.salary as salary from employee e
right join department d
on e.departmentId = d.id
where (e.departmentId, e.salary) IN (
select departmentId, max(salary)
from employee
group by departmentId
);