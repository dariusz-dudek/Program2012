import csv
import random
from employee import *


def random_employee():
    first_name = random_first_name()
    last_name = random_last_name()
    if (last_name[-3:] in ['ski', 'cki'] and last_name[-3:] == 'dzki') and first_name[-1] == 'a':
        last_name = last_name[:-1] + 'a'
    sex = 'W' if first_name[-1] == 'a' else 'M'
    department_number = random.randint(1, 10)
    salary = round(random.uniform(3000, 100000), 2)
    age = random.randint(18, 65)
    children = random.randint(0, 8)
    marital_status = random.choice([True, False])

    return Employee(first_name, last_name, sex, department_number, salary, age, children, marital_status)


def random_first_name():
    try:
        with open('first_names.csv', 'r', encoding='utf-8') as first_names_file:
            csv_reader = csv.DictReader(first_names_file)

            first_names = []

            for row in csv_reader:
                first_names.append(row['imie'])
        return random.choice(first_names)
    except IOError:
        print('Something went wrong.')


def random_last_name():
    try:
        with open('last_names.csv', 'r', encoding='utf-8') as last_name_file:
            csv_reader = csv.DictReader(last_name_file)

            last_names = []

            for row in csv_reader:
                last_names.append(row['Nazwisko aktualne'].capitalize())
        return random.choice(last_names)
    except IOError:
        print('Something went wrong.')



