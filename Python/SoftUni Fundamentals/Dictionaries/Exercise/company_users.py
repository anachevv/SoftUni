dct_employees_and_ids = {}
command = input()

while command != "End":
    company_name, employee_id = command.split(' -> ')

    if company_name not in dct_employees_and_ids:
        dct_employees_and_ids[company_name] = []
        if employee_id not in dct_employees_and_ids[company_name]:
            dct_employees_and_ids[company_name].append(employee_id)
    if employee_id not in dct_employees_and_ids[company_name]:
        dct_employees_and_ids[company_name].append(employee_id)

    command = input()

for company, id in dct_employees_and_ids.items():
    print(company, end='\n-- ')
    print(f"\n-- ".join(id))
