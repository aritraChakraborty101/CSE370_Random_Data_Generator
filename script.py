
from random import randint
domains = ['gmail.com', 'outlook.com', 'yahoo.com', 'aol.com']
names = open('names.txt') #need to put random number of names in a the /names.txt file
output = open("output.txt", "w") #the output will show required format in /output.txt file
data = []
for i in range(1, 21):
    emp = f"EMP{i:03d}"
    first, last = names.readline().split()
    email = f'{first.lower()}.{last.lower()}@{domains[randint(0, 3)]}'
    phone = f"+1({randint(100, 999)}){randint(1000000, 9999999)}"
    hire_date = f'{randint(2021, 2023)}-{randint(1, 12):02d}-{randint(1, 30):02d}'
    job_id = f'JOB00{randint(1, 9)}'
    salary = randint(10, 60) * 1000
    commission = randint(10, 50) + randint(0, 999) / 1000
    manager = f"MNG00{randint(1, 7)}"
    department = f"DPT00{randint(1, 9)}"
    data.append((emp, first, last, email, phone, hire_date, job_id, salary, commission, manager, department))

for i in range(20):
    if i == 19:
        output.writelines(f"{data[i]};\n")
        break
    output.writelines(f"{data[i]},\n")

