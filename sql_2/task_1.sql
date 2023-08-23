-- write a query in SQL to display the first name, last name, department number, and department name for each employee
SELECT first_name, last_name, employees.department_id, department_name FROM employees
JOIN department
ON employees.department_id = department.department_id

-- write a query in SQL to display the first and last name, department, city, and state province for each employee
SELECT first_name, last_name, department_name, city, state_province FROM employees
JOIN department
ON employees.department_id = department.department_id
JOIN locations
ON department.location_id = locations.location_id

-- write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
SELECT first_name, last_name, employees.department_id, department_name FROM employees 
JOIN department
ON employees.department_id = department.department_id
WHERE employees.department_id = 80 OR employees.department_id = 80

-- write a query in SQL to display all departments including those where does not have any employee
SELECT * from departments

-- write a query in SQL to display the first name of all employees including the first name of their manager
-- there is no managers table
SELECT first_name, manager_id FROM employees

-- write a query in SQL to display the job title, full name (first and last name ) of the employee, and the difference between the maximum salary for the job and the salary of the employee
SELECT CONCAT(first_name, " ", last_name) as 'Full name', job_title, salary, max_salary - salary as 'Difference' from jobs
JOIN employees
ON employees.job_id = jobs.job_id

-- write a query in SQL to display the job title and the average salary of employees
SELECT job_title, (min_salary + max_salary)/2 as 'Average salary' from jobs

-- write a query in SQL to display the full name (first and last name), and salary of those employees who work in any department located in London
SELECT first_name, last_name, salary, city from employees
JOIN departments
ON employees.department_id = departments.department_id
JOIN locations
ON departments.location_id = locations.location_id
WHERE locations.city = 'Seattle';

-- write a query in SQL to display the department name and the number of employees in each department
SELECT depart_name, COUNT(employees.department_id) as Count FROM employees
JOIN departments
ON employees.department_id = departments.department_id
GROUP BY employees.department_id

 