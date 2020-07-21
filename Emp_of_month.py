#tuple 
work_hours = [('abby',100),('billy',300),('kasi',600)]

maxsalary = 0
emp_of_month =''
#fn to find employee of the month

def emp(work_hours):
	for employee,hours in work_hours:
		if hours > maxsalary:
			maxsalary =  hours
			emp_of_month = employee
		else:
			pass
	return (emp_of_month,maxsalary)