from program import *


def main_menu():
    while True:
        print('Main menu')
        print('Choice one option:\n'
              '[1] - Show all employees\n'
              '[2] - Adding a new employee\n'
              '[3] - Export data\n'
              '[4] - Delete employee\n'
              '[5] - Employee data editing\n'
              '[6] - Additional functions\n'
              '[7] - End program\n')

        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                show_all_employees_stripped()
            elif choice == 2:
                add_new_employee_to_database(add_new_employee())
            elif choice == 3:
                export_data()
            elif choice == 4:
                delete_employee()
            elif choice == 5:
                employee_data_edit()
            elif choice == 6:
                additional_functions()
            elif choice == 7:
                break
            else:
                print('Wrong choice. Try one more time.')
        except ValueError:
            print('Wrong choice. Try one more time.')


def additional_functions():
    while True:
        print('Additional menu\n'
              '[a] - Calculation of the number of employees with a salary of not less than ...\n'
              '[b] - Calculate of the average salary in the department\n'
              '[c] - Display the highest salaries of all women and all men\n'
              '[d] - View all departments\n'
              '[e] - Display the ratio of the average wage of the women to the average wage of men\n'
              '[f] - Percentage increasing the salary of all employees\n'
              '[g] - Quota increasing the salary of all employees\n'
              '[h] - Sort employees by last name\n'
              '[i] - Sort employees according to their salaries\n'
              '[j] - Adding to database random employees\n'
              '[k] - Return to main manu')

        choice = input('Enter the choice: ').lower()

        if choice == 'a':
            print(f'The number of employees with a salary of not less than is {salary_les_then(enter_value("salary"))}')
        elif choice == 'b':
            print(f"The average salary in selected department is {average_salary_in_the_department(enter_department_number()):,.2f}")
        elif choice == 'c':
            biggest_salary_man_and_woman()
        elif choice == 'd':
            show_all_departments()
        elif choice == 'e':
            ratio_average_salary_woman_man()
        elif choice == 'f':
            raising_present_salary(enter_present())
        elif choice == 'g':
            result = raising_value_salary(enter_value("raise"))
            print('Ratio of increases for women and men is {:,.2f} to {:,.2f}'.format(result[0], result[1]))
        elif choice == 'h':
            print('Sort employees by last name')
        elif choice == 'i':
            print('Sort employees according to their salaries')
        elif choice == 'j':
            adding_random_employees()
        elif choice == 'k':
            break
        else:
            print('Wrong choice. Try one more time.')


def edit_employ_menu():
    while True:
        print('What field do you want edit?\n'
              '[1] Last name\n'
              '[2] Department number\n'
              '[3] Salary\n'
              '[4] Age\n'
              '[5] Number of children\n'
              '[6] Marital status\n'
              '[7] Return to main menu')
        try:
            return int(input('Enter your choice: '))
        except ValueError:
            print('Wrong choice. Try one more time.')
