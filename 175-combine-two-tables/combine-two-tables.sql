# Write your MySQL query statement below
select firstName, lastName, city,state from person p
left join address a
ON p.personId = a.personId
