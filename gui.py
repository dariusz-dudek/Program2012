from tkinter import *
from program import *
from tkinter import messagebox
from employee import *
# from os import getenv
from database import *
from dotenv import load_dotenv

load_dotenv()

# Variables
width_button = 20
font_button = ('OpenSans', 15)
pady_button = 5
pady_button_grid = 5
padx_button_grid = 5
global first_name
global last_name
global sex
global department_number
global salary
global age
global children
global marital_status
global sex_clicked
global employee_window
global list_window


def center_window(window_name, app_width, app_height):
    screen_width = window_name.winfo_screenwidth()
    screen_height = window_name.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    window_name.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


def main_menu():
    root = Tk()
    center_window(root, 400, 400)

    button_employee_show_all = Button(root, text='Show all employees', width=width_button, font=font_button,
                                      pady=pady_button, command=show_all_employees_striped_gui())
    button_employee_show_all.grid(row=2, column=0, pady=pady_button_grid, padx=padx_button_grid)
    button_employee_add = Button(root, text='Adding a new employee', width=width_button, font=font_button,
                                 pady=pady_button, command=employee)
    button_employee_add.grid(row=3, column=0, pady=pady_button_grid, padx=padx_button_grid)
    button_employee_export = Button(root, text='Export data', width=width_button, font=font_button, pady=pady_button)
    button_employee_export.grid(row=4, column=0, pady=pady_button_grid, padx=padx_button_grid)
    button_employee_delete = Button(root, text='Delete employee', width=width_button, font=font_button,
                                    pady=pady_button)
    button_employee_delete.grid(row=5, column=0, pady=pady_button_grid, padx=padx_button_grid)
    button_employee_edit = Button(root, text='Employee data edit', width=width_button, font=font_button,
                                  pady=pady_button)
    button_employee_edit.grid(row=6, column=0, pady=pady_button_grid, padx=padx_button_grid)
    button_additional_function = Button(root, text='Additional function', width=width_button, font=font_button,
                                        pady=pady_button)
    button_additional_function.grid(row=7, column=0, pady=pady_button_grid, padx=padx_button_grid)
    button_program_information = Button(root, text='Program information', width=width_button, font=font_button,
                                        pady=pady_button)
    button_program_information.grid(row=8, column=0, pady=pady_button_grid, padx=padx_button_grid)
    button_exit_program = Button(root, text='Exit program', width=width_button, font=font_button, pady=pady_button,
                                 command=root.quit)
    button_exit_program.grid(row=9, column=0, pady=pady_button_grid, padx=padx_button_grid)

    root.mainloop()


# Window with adding or editing employee

def employee():
    # Create global variables for text box names
    global first_name
    global last_name
    global sex
    global department_number
    global salary
    global age
    global children
    global marital_status
    global sex_clicked
    global employee_window

    employee_window = Tk()
    center_window(employee_window, 450, 400)

    # Create text box labels
    first_name_label = Label(employee_window, text='First name', font=font_button)
    first_name_label.grid(row=0, column=0)
    last_name_label = Label(employee_window, text='Last name', font=font_button)
    last_name_label.grid(row=1, column=0)
    sex_label = Label(employee_window, text='Sex', font=font_button)
    sex_label.grid(row=2, column=0)
    department_number_label = Label(employee_window, text='Department number', font=font_button)
    department_number_label.grid(row=3, column=0)
    salary_label = Label(employee_window, text='Salary', font=font_button)
    salary_label.grid(row=4, column=0)
    age_label = Label(employee_window, text='Age', font=font_button)
    age_label.grid(row=5, column=0)
    children_label = Label(employee_window, text='Number of children', font=font_button)
    children_label.grid(row=6, column=0)
    marital_status_label = Label(employee_window, text='Marital status (Y/N)', font=font_button)
    marital_status_label.grid(row=7, column=0)

    # Create text boxes
    first_name = Entry(employee_window, width=30, font=font_button)
    first_name.grid(row=0, column=1, columnspan=2)

    last_name = Entry(employee_window, width=30, font=font_button)
    last_name.grid(row=1, column=1, columnspan=2)
    sex = StringVar(employee_window)
    sex.set('W')

    Radiobutton(employee_window, text='Woman', variable=sex, value='W', command=lambda: sex.set('W')).grid(row=2,
                                                                                                           column=1)
    Radiobutton(employee_window, text='Man', variable=sex, value='M', command=lambda: sex.set('M')).grid(row=2,
                                                                                                         column=2)

    department_number = IntVar(employee_window)
    department_number.set(1)

    OptionMenu(employee_window, department_number, *range(1, 11)).grid(row=3, column=1, columnspan=2)

    salary = Entry(employee_window, width=30, font=font_button)
    salary.grid(row=4, column=1, columnspan=2)

    age = IntVar(employee_window)
    age.set(18)
    OptionMenu(employee_window, age, *range(18, 66)).grid(row=5, column=1, columnspan=2)

    children = IntVar(employee_window)
    children.set(0)
    OptionMenu(employee_window, children, *range(0, 21)).grid(row=6, column=1, columnspan=2)

    marital_status = StringVar(employee_window)
    marital_status.set('Y')

    Radiobutton(employee_window, text='Married', variable=marital_status, value='Y',
                command=lambda: marital_status.set('Y')).grid(row=7, column=1)
    Radiobutton(employee_window, text='No married', variable=marital_status, value='N',
                command=lambda: marital_status.set('N')).grid(row=7, column=2)

    # Create add button

    add_employee_button = Button(employee_window, text='Add employee', font=font_button,
                                 command=lambda: add_new_employee_to_database_gui())
    add_employee_button.grid(row=8, column=1)
    cleaning_fields_button = Button(employee_window, text='Reset', font=font_button,
                                    command=lambda: cleaning_fields())
    cleaning_fields_button.grid(row=8, column=0)
    back_to_main_menu_button = Button(employee_window, text='Back to main menu', font=font_button,
                                      command=lambda: employee_window.destroy())
    back_to_main_menu_button.grid(row=8, column=2)


def list_window_gui():
    global list_window
    list_window = Tk()
    center_window(list_window, 400, 400)


def show_all_employees_striped_gui():
    list_window_gui()
    database = Database(getenv('DB_NAME'))
    result = database.show_all('employee', 'rowid', 'first_name', 'last_name', 'salary')
    for count, heading in enumerate(['ID', 'First name', 'Last name', 'Salary']):
        Label(list_window, text=heading).grid(row=0, column=count)
    for count_row, row in enumerate(result):
        for count_field, field in enumerate(row):
            Label(list_window, text=row[count_field]).grid(row=count_row + 1, column=count_field, sticky=W)


def add_new_employee_to_database_gui():
    message = add_new_employee_to_database(add_employee_gui())
    if message[0]:
        Label(employee_window, text=message[1], font=font_button).grid(row=9, column=0, columnspan=3)
        cleaning_fields()
    else:
        Label(employee_window, text=message[1], font=font_button).grid(row=9, column=0, columnspan=3)


def cleaning_fields():
    first_name.delete(0, END)
    last_name.delete(0, END)
    sex.set('W')
    department_number.set(1)
    salary.delete(0, END)
    age.set(18)
    children.set(0)
    marital_status.set('Y')


def enter_first_name_gui():
    answer_first_name = enter_name_conditions(str(first_name.get()).capitalize())
    if not answer_first_name[0]:
        messagebox.showwarning('This is my popup!', f'In field First name:\n {answer_first_name[1]}')
        first_name.delete(0, END)
        return False
    else:
        return str(first_name.get()).capitalize()


def enter_last_name_gui():
    answer_last_name = enter_name_conditions(str(last_name.get()).capitalize())
    if not answer_last_name[0]:
        messagebox.showwarning('This is my popup!', f'In field First name:\n {answer_last_name[1]}')
        last_name.delete(0, END)
        return False
    else:
        return str(last_name.get()).capitalize()


def enter_sex_gui():
    answer_sex = enter_sex_conditions(sex.get())
    if not answer_sex[0]:
        messagebox.showwarning('This is my popup!', f'In field sex:\n {answer_sex[1]}')
        return False
    else:
        return sex.get()


def enter_department_number_gui():
    answer_department_number = enter_department_number_condition(department_number.get())
    if type(answer_department_number[0]) == bool:
        if answer_department_number[0]:
            return int(department_number.get())
        else:
            messagebox.showwarning('This is my popup!', f'In field department number :\n {answer_department_number[1]}')
            return False
    else:
        messagebox.showerror('This is my popup', f'In field department number:\n {answer_department_number}')
        return False


def enter_value_gui(field, description):
    answer_value = enter_value_condition(field.get(), description)
    if type(answer_value[0]) == bool:
        if answer_value[0]:
            return int(field.get())
        else:
            messagebox.showwarning('This is my popup!', f'In field salary:\n {answer_value[1]}')
            field.delete(0, END)
            return False
    else:
        messagebox.showerror('This is my popup', f'In field salary:\n {answer_value}')
        field.delete(0, END)
        return False


def enter_age_gui():
    answer_age = enter_age_condition(age.get())
    if type(answer_age[0]) == bool:
        if answer_age[0]:
            return int(age.get())
        else:
            messagebox.showwarning('This is my popup', f'In field age:\n {answer_age[1]}')
            return False
    else:
        messagebox.showerror('This is my popup', f'In filed age:\n {answer_age}')
        return False


def enter_children_gui():
    answer_children = enter_children_condition(children.get())
    if type(answer_children[0]) == bool:
        if answer_children[0]:
            return int(children.get())
        else:
            messagebox.showwarning('This is my popup', f'In field children:\n {answer_children[1]}')
            return False
    else:
        messagebox.showerror('Tis is my popup', f'In field children:\n {answer_children}')
        return False


def enter_marital_status_gui():
    answer_marital_status = enter_marital_status_conditions(str(marital_status.get()).upper())
    if answer_marital_status[0]:
        return str(marital_status.get()).upper() == 'Y'
    else:
        messagebox.showwarning('This is my popup', f'In field marital status:\n {answer_marital_status[1]}')
        return False


def add_employee_gui():
    # print(enter_first_name_gui(), enter_last_name_gui(), enter_sex_gui(),
    #       enter_department_number_gui(),
    #       enter_value_gui(salary, 'salary'), enter_age_gui(), enter_children_gui(),
    #       enter_marital_status_gui())
    while True:
        if True in [enter_first_name_gui(), enter_last_name_gui(), enter_sex_gui(), enter_department_number_gui(),
                    enter_value_gui(salary, 'salary'), enter_age_gui(), enter_children_gui(),
                    enter_marital_status_gui()]:
            return Employee(enter_first_name_gui(), enter_last_name_gui(), sex.get(),
                            enter_department_number_gui(),
                            enter_value_gui(salary, 'salary'), enter_age_gui(), enter_children_gui(),
                            enter_marital_status_gui())
        else:
            break


main_menu()
