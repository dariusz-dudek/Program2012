# from os import getenv
from os import *
import menu
import string
from database import *
from random_employee import *


def press_enter():
    input("Press enter to continue")
    print()


def create_tables():
    try:
        database = Database(getenv('DB_NAME'))
        database.create_table('employee', 'first_name text', 'last_name text', 'sex text', 'department_number integer',
                              'salary real', 'age integer', 'children integer', 'marital_status text')
    except sqlite3.OperationalError:
        pass


def show_all_employees_stripped():
    database = Database(getenv('DB_NAME'))
    result = database.show_all('employee', 'rowid', 'first_name', 'last_name', 'salary')

    print(f"+{'-' * 92}+")
    print('| {:5} | {:32} | {:32} | {:12} |'.format('ID', 'First Name', 'Last Name', 'Salary'))
    print(f"+{'-' * 92}+")
    for row in result:
        print('| {:5} | {:32} | {:32} | {:>12,.2f} |'.format(row[0], row[1], row[2], row[3]))
    print(f"+{'-' * 92}+")


def add_new_employee_to_database(employee):
    database = Database(getenv('DB_NAME'))
    try:
        database.insert('employee', employee.first_name, employee.last_name, employee.sex, employee.department_number,
                        employee.salary, employee.age, employee.children, employee.marital_status)
        return True, 'Employee added'
    except AttributeError:
        return False, 'No employee was add'


def add_new_employee():
    return Employee(enter_first_name(), enter_last_name(), enter_sex(), enter_department_number(),
                    enter_value('salary'), enter_age(), enter_children(), enter_marital_status())


def show_all_employees():
    database = Database(getenv('DB_NAME'))
    result = database.show_all('employee', 'rowid', 'first_name', 'last_name', 'sex', 'department_number', 'salary',
                               'age', 'children', 'marital_status')

    print(f"+{'-' * 154}+")
    print(
        '| {:5} | {:32} | {:32} | {:5} | {:17} | {:12} | {:3} | {:8} | {:14} |'.format('ID', 'First Name', 'Last Name',
                                                                                       'Sex', 'Department number',
                                                                                       'Salary', 'Age', 'Children',
                                                                                       'Marital status'))
    print(f"+{'-' * 154}+")

    for row in result:
        print('| {:5} | {:32} | {:32} |'.format(row[0], row[1], row[2]), end='')
        if row[3] == 'M':
            print(' {:5} |'.format('man'), end='')
        else:
            print(' {:5} |'.format('woman'), end='')
        print(' {:17} | {:12} | {:3} | {:8} |'.format(row[4], row[5], row[6], row[7]), end='')
        if row[8] == '1':
            print(' {:14} |'.format('yes'))
        else:
            print(' {:14} |'.format('no'))
    print(f"+{'-' * 154}+")


def show_all_employees_special():
    database = Database(getenv('DB_NAME'))
    result = database.show_all('employee', 'rowid', 'first_name', 'last_name')

    for row in result:
        print(f'ID: {row[0]}\tFirst name: {row[1].upper()}\tLast name: {row[2].upper()}')


def delete_employee():
    while True:
        try:
            show_all_employees_special()
            database = Database(getenv('DB_NAME'))
            rows_deleted = database.delete('employee', int(input('Enter the ID of the employee you want to delete')))

            if rows_deleted == 0:
                print('This ID does not exist. Try one more time.')
            else:
                print('The employee was deleted')
                break
        except ValueError:
            print('Wrong answer, it is not integer. Tty one more time')


def salary_les_then(given_salary):
    database = Database(getenv('DB_NAME'))
    result = database.choice_with_condition('employee', 'salary', '>=', given_salary)
    return len(result)


def biggest_salary_man_and_woman():
    database = Database(getenv('DB_NAME'))
    result = database.show_all('employee', 'sex', 'salary')
    biggest_salary_man = 0
    biggest_salary_woman = 0
    for row in result:
        if row[0] == 'W' and row[1] > biggest_salary_woman:
            biggest_salary_woman = row[1]
        if row[0] == 'M' and row[1] > biggest_salary_man:
            biggest_salary_man = row[1]
    print(f'Biggest salary for man is {biggest_salary_man} and biggest salary woman is {biggest_salary_woman}')


def average_salary_in_the_department(given_department):
    database = Database(getenv('DB_NAME'))
    result = database.choice_with_condition('employee', 'department_number', '=', given_department)
    sum_of_salaries = 0
    for salary in result:
        sum_of_salaries += salary[4]
    return round(sum_of_salaries / len(result), 2)


def export_data():
    database = Database(getenv('DB_NAME'))
    result = database.show_all('employee', 'first_name', 'last_name', 'sex', 'department_number', 'salary', 'age',
                               'children')
    try:
        while True:
            file_name = input(
                'Enter the name of the file to which you want to save the data using only ascii letters: ')
            if file_name.isalpha():
                break
            else:
                print('this is not ascii letters name. Try one more time.')

        with open(f'{file_name}.txt', 'w') as file:
            if file.writable():
                for row in result:
                    file.write(f'{row[1]} {row[0]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}\n')
        print(f'Data saved to file {file_name}.txt')
    except (IOError, ValueError):
        print('Something went wrong.')


def employee_data_edit():
    while True:

        try:
            show_all_employees()
            choice_id = int(input('Enter the employee ID to edit: '))
            database = Database(getenv('DB_NAME'))

            answer = menu.edit_employ_menu()

            if answer == 1:
                if not database.choice_with_condition('employee', 'rowid', '=', choice_id)[0][2] == 'W':
                    print('Last name can only be changed for a woman')
                else:
                    database.edit_by_rowid('employee', 'last_name', enter_last_name(), choice_id)
                    break
            elif answer == 2:
                database.edit_by_rowid('employee', 'department_number', enter_department_number(), choice_id)
                break
            elif answer == 3:
                database.edit_by_rowid('employee', 'salary', enter_value('salary'), choice_id)
                break
            elif answer == 4:
                database.edit_by_rowid('employee', 'age', enter_age(), choice_id)
                break
            elif answer == 5:
                database.edit_by_rowid('employee', 'children', enter_children(), choice_id)
                break
            elif answer == 6:
                database.edit_by_rowid('employee', 'marital_status', enter_marital_status(), choice_id)
                break
            elif answer == 7:
                break
            else:
                print('Wrong answer. Tty one more time')
        except (ValueError, sqlite3.ProgrammingError):
            print('Wrong answer, it is not integer. Tty one more time')


def enter_first_name():
    while True:
        first_name = input('Enter first name: ').capitalize()
        answer = enter_name_conditions(first_name)
        if answer[0]:
            return first_name
        else:
            print(answer[1])


def enter_name_conditions(entered_name):
    if len(entered_name) < 3:
        return False, 'Name too short. Try one more time.'
    elif len(entered_name) > 30:
        return False, 'Name too long. Try one more time.'
    elif set(entered_name).difference(string.ascii_letters):
        return False, 'You have to use only asci letters. Try one more time.'
    else:
        return True, 'OK'


def enter_last_name():
    while True:
        last_name = input('Enter the last name: ').capitalize()
        answer = enter_name_conditions(last_name)
        if answer[0]:
            return last_name
        else:
            print(answer[1])


def enter_sex():
    while True:
        sex = input('Enter the sex [\'W\' for woman and \'M\' for man]: ').upper()
        answer = enter_sex_conditions(sex)
        if answer[0]:
            return sex
        else:
            print(answer[1])


def enter_sex_conditions(sex):
    if sex == 'M' or sex == 'W':
        return True, 'OK'
    else:
        return False, 'Wrong character. Try one more time.'


def enter_department_number():
    while True:
        department_number = input('Enter the department number from 1 to 10: ')
        answer = enter_department_number_condition(department_number)
        if type(answer[0]) == bool:
            if answer[0]:
                return int(department_number)
            else:
                print(answer[1])
        else:
            print(answer)


def enter_department_number_condition(department_number):
    try:
        if 1 <= int(department_number) <= 10:
            return True, 'OK'
        else:
            return False, 'Out of range number. Try one more time.'
    except ValueError:
        return 'Wrong answer, it is not integer. Tty one more time'


def enter_value(parameter):
    while True:
        value = input(f'Enter the {parameter}: ')
        answer = enter_value_condition(value, parameter)
        if type(answer[0]) == bool:
            if answer[0]:
                return float(value)
            else:
                print(answer[1])
        else:
            print(answer)


def enter_value_condition(value, parameter):
    try:
        if float(value) < 0:
            return False, f'The {parameter} can not be len then zero. Try one more time.'
        elif float(value) > 100000:
            return False, 'I think it is too much. Try one more time.'
        else:
            return True, 'OK'
    except ValueError:
        return 'It is not number. Tty one more time'


def enter_age():
    while True:
        age = input('Enter your age: ')
        answer = enter_age_condition(age)
        if type(answer[0]) == bool:
            if answer[0]:
                return int(age)
            else:
                print(answer[1])
        else:
            print(answer)


def enter_age_condition(age):
    try:
        if int(age) > 65:
            return False, 'You are too old to work in our company. Try one more time.'
        elif int(age) < 18:
            return False, 'You are too yang to work in our company. Try one more time.'
        else:
            return True, 'OK'
    except ValueError:
        return 'It is wrong date. Tty one more time'


def enter_children():
    while True:
        children = input('Enter the number of children: ')
        answer = enter_children_condition(children)
        if type(answer[0]) == bool:
            if answer[0]:
                return int(children)
            else:
                print(answer[1])
        else:
            print(answer)


def enter_children_condition(children):
    try:
        if int(children) < 0:
            return False, 'You must enter a positive value. Try one more time.'
        if int(children) >= 20:
            print()
            return False, 'I do not think it is possible'
        else:
            return True, 'OK'
    except ValueError:
        return 'It is not a number. Try one more time.'


def enter_marital_status():
    while True:
        marital_status = input('Enter the marital status [\'Y\' - married or \'N\' - not married ').upper()
        answer = enter_marital_status_conditions(marital_status)
        if answer[0]:
            return marital_status == 'Y'
        else:
            print(answer[1])


def enter_marital_status_conditions(marital_status):
    if marital_status == 'Y' or marital_status == 'N':
        return True, 'OK'
    else:
        return False, 'Wrong answer. Try one more time.'


def adding_random_employees():
    while True:
        try:
            number_of_employee = int(input('How many employees do you want to add? '))
            break
        except ValueError:
            print('This is not a integer. Try one more time')
    for _ in range(number_of_employee):
        add_new_employee_to_database(random_employee())


def show_all_departments():
    database = Database(getenv('DB_NAME'))
    for department in range(1, 11):
        result = database.choice_with_condition('employee', 'department_number', '=', department)
        woman = 0
        man = 0
        for row in result:
            if row[2] == 'W':
                woman += 1
            else:
                man += 1
        try:
            if woman > man:
                print(
                    f'In department {department} women are more then men. Average salary in this department is {average_salary_in_the_department(department)}')
            elif woman < man:
                print(
                    f'In department {department} women are less then men. Average salary in this department is {average_salary_in_the_department(department)}')
            else:
                print(
                    f'In department {department} women and men are the same. Average salary in this department is {average_salary_in_the_department(department)}')
        except ZeroDivisionError:
            pass


def ratio_average_salary_woman_man():
    database = Database(getenv('DB_NAME'))
    result = database.show_all('employee', 'sex', 'salary')
    woman_salary = 0
    woman = 0
    men_salary = 0
    men = 0
    for row in result:
        if row[0] == 'W':
            woman_salary += row[1]
            woman += 1
        else:
            men_salary += row[1]
            men += 1

    print(
        f'The ratio of the average salary of woman to the average salary of men is {(woman_salary / woman) / (woman_salary / men)}')


def raising_present_salary(raise_present):
    database = Database(getenv('DB_NAME'))
    result = database.show_all('employee', 'rowid', 'salary', 'children', 'marital_status')
    for row in result:
        raise_present_row = raise_present
        if not row[2] == 0:
            raise_present_row = raise_present_row + (row[2] * 2)
        if row[3] == '1':
            raise_present_row += 3
        database.edit_by_rowid('employee', 'salary', round(row[1] * (1 + raise_present_row / 100), 2), row[0])


def enter_present():
    while True:
        try:
            entering_present = int(input('Enter the present raise salary: '))
            if entering_present < 0:
                print('You must enter a positive value. Try one more time.')
            if entering_present > 100:
                print('I do not think it is possible')
            else:
                return entering_present
        except ValueError:
            print('It is not a number. Try one more time.')


def raising_value_salary(raise_value):
    database = Database(getenv('DB_NAME'))
    result = database.show_all('employee', 'rowid', 'salary', 'sex')
    raise_men, raise_woman = 0, 0
    for row in result:
        if row[2] == 'M':
            raise_men += raise_value
        else:
            raise_woman += raise_value
        database.edit_by_rowid('employee', 'salary', raise_value, row[0])
    print('Sum of raises is {:,.2f}'.format(raise_men + raise_woman))
    return [raise_woman, raise_men]
