select
Company.company_code,
Company.founder,
lead_manager_code_count,
senior_manager_code_count,
manager_code_count,
employee_code_count
from Company
left join (
    select company_code, count(distinct lead_manager_code) as lead_manager_code_count
    from Lead_Manager
    group by company_code
) Lead_Manager_query on Lead_Manager_query.company_code = Company.company_code
left join (
    select company_code, count(distinct senior_manager_code) as senior_manager_code_count
    from Senior_Manager
    group by company_code
) Senior_Manager_query on Senior_Manager_query.company_code = Company.company_code
left join (
    select company_code, count(distinct manager_code) as manager_code_count
    from Manager
    group by company_code
) Manager_query on Manager_query.company_code = Company.company_code
left join (
    select company_code, count(distinct employee_code) as employee_code_count
    from Employee
    group by company_code
) Employee_query on Employee_query.company_code = Company.company_code
order by Company.company_code