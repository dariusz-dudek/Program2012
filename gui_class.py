import tkinter as tk
from os import getenv
from tkinter import ttk
from dotenv import load_dotenv
from tkinter.messagebox import showinfo

load_dotenv()


class Gui_class(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Centre window on thr screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (int(getenv('WINDOW_WIDTH')) / 2)
        y = (screen_height / 2) - (int(getenv('WINDOW_HEIGHT')) / 2)
        self.geometry(f"{int(getenv('WINDOW_WIDTH'))}x{int(getenv('WINDOW_HEIGHT'))}+{int(x)}+{int(y)}")

        container = ttk.Frame(self, width=400, height=400)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # In brackets add another window class
        for window in (
                Main_menu, Lst_page, Add_employee, Export_data, Delete_employee, Edit_employee, Additional_function):
            frame = window(container, self)
            self.frames[window] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(Main_menu)

    def show_frame(self, count):
        frame = self.frames[count]
        frame.tkraise()


class Main_menu(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Main menu', font=getenv('LARGE_FONT'))
        label.pack(pady=10, padx=10)

        button_list_page = tk.Button(self, text='Show all employees', font=getenv('MEDIUM_FONT'),
                                     command=lambda: controller.show_frame(Lst_page))
        button_list_page.pack(pady=10, padx=10)

        button_add_employee = tk.Button(self, text='Adding a new employee', font=getenv('MEDIUM_FONT'),
                                        command=lambda: controller.show_frame(Add_employee))
        button_add_employee.pack(pady=10, padx=10)

        button_export_data = tk.Button(self, text='Export data', font=getenv('MEDIUM_FONT'),
                                       command=lambda: controller.show_frame(Export_data))
        button_export_data.pack(pady=10, padx=10)

        button_delete_employee = tk.Button(self, text='Delete employee', font=getenv('MEDIUM_FONT'),
                                           command=lambda: controller.show_frame(Delete_employee))
        button_delete_employee.pack(pady=10, padx=10)

        button_edit_employee = tk.Button(self, text='Employee data editing', font=getenv('MEDIUM_FONT'),
                                         command=lambda: controller.show_frame(Edit_employee))
        button_edit_employee.pack(pady=10, padx=10)

        button_additional_function = tk.Button(self, text='Additional function', font=getenv('MEDIUM_FONT'),
                                               command=lambda: controller.show_frame(Additional_function))
        button_additional_function.pack(pady=10, padx=10)

        button_exit_program = tk.Button(self, text='Exit program', font=getenv('MEDIUM_FONT'),
                                        command=self.quit)
        button_exit_program.pack(pady=10, padx=10)


class Lst_page(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Show all employees', font=getenv('LARGE_FONT'))
        label.grid(pady=10, padx=10)

        button = tk.Button(self, text='Main menu', font=getenv('MEDIUM_FONT'),
                           command=lambda: controller.show_frame(Main_menu))
        button.grid()


class Add_employee(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        title_label = ttk.Label(self, text='Add a new employee', font=getenv('LARGE_FONT'))
        title_label.grid(pady=getenv('PADY_LABEL_TITLE'), padx=getenv('PADX_LABEL_TITLE'), row=0, column=0,
                         columnspan=3)

        # Adding labels
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'sex': 'Sex',
            'department_number': 'Department number',
            'salary': 'Salary',
            'age': 'Age',
            'children': 'Children',
            'marital_status': 'Marital status'
        }
        for count, key in enumerate(labels):
            exec(f"{key}_label = ttk.Label(self, text='{labels[key]}', font=getenv('MEDIUM_FONT'))")
            exec(f"{key}_label.grid(pady=getenv('PADY_LABEL'), padx=getenv('PADX_LABEL'), row={count + 1}, column=0)")

        # Create text boxes
        first_name = ttk.Entry(self, width=getenv('TEXT_BOX-WIDTH'), font=getenv('MEDIUM_FONT'))
        first_name.grid(row=1, column=1, columnspan=3)

        last_name = ttk.Entry(self, width=getenv('TEXT_BOX-WIDTH'), font=getenv('MEDIUM_FONT'))
        last_name.grid(row=2, column=1, columnspan=2)

        sex = tk.StringVar(self)
        sex.set('W')

        ttk.Radiobutton(self, text='Woman', variable=sex, value='W', command=lambda: sex.set('W')).grid(row=3,
                                                                                                        column=1)
        ttk.Radiobutton(self, text='Man', variable=sex, value='M', command=lambda: sex.set('M')).grid(row=3,
                                                                                                      column=2)

        department_number = tk.IntVar(self)
        department_number.set(1)

        ttk.OptionMenu(self, department_number, *range(1, 11)).grid(row=4, column=1, columnspan=2)

        salary = ttk.Entry(self, width=getenv('TEXT_BOX-WIDTH'), font=getenv('MEDIUM_FONT'))
        salary.grid(row=5, column=1, columnspan=2)

        age = tk.IntVar(self)
        age.set(18)
        ttk.OptionMenu(self, age, *range(18, 66)).grid(row=6, column=1, columnspan=2)

        children = tk.IntVar(self)
        children.set(0)
        ttk.OptionMenu(self, children, *range(0, 21)).grid(row=7, column=1, columnspan=2)

        marital_status = tk.StringVar(self)
        marital_status.set('Y')

        ttk.Radiobutton(self, text='Married', variable=marital_status, value='Y',
                        command=lambda: marital_status.set('Y')).grid(row=8, column=1)
        ttk.Radiobutton(self, text='No married', variable=marital_status, value='N',
                        command=lambda: marital_status.set('N')).grid(row=8, column=2)

        # Adding button
        button = tk.Button(self, text='Main menu', font=getenv('MEDIUM_FONT'),
                           command=lambda: controller.show_frame(Main_menu))
        button.grid(row=9, column=0, columnspan=3)


class Export_data(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Export data', font=getenv('LARGE_FONT'))
        label.grid(pady=10, padx=10)

        button = tk.Button(self, text='Main menu', font=getenv('MEDIUM_FONT'),
                           command=lambda: controller.show_frame(Main_menu))
        button.grid()


class Delete_employee(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Delete employee', font=getenv('LARGE_FONT'))
        label.grid(pady=10, padx=10)

        button = tk.Button(self, text='Main menu', font=getenv('MEDIUM_FONT'),
                           command=lambda: controller.show_frame(Main_menu))
        button.grid()


class Edit_employee(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text='Edit employee', font=getenv('LARGE_FONT'))
        label.grid(pady=10, padx=10)

        button = tk.Button(self, text='Main menu', font=getenv('MEDIUM_FONT'),
                           command=lambda: controller.show_frame(Main_menu))
        button.grid()


class Additional_function(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Additional function', font=getenv('LARGE_FONT'))
        label.grid(pady=10, padx=10)

        button = tk.Button(self, text='Main menu', font=getenv('MEDIUM_FONT'),
                           command=lambda: controller.show_frame(Main_menu))
        button.grid()


app = Gui_class()
app.mainloop()

# class Gui(Tk):
#     def __init__(self):
#         super().__init__()
#
#         # configure the root window
#         self.title('My app')
#         self.geometry('400x400')
#
#         # label
#         self.label = Label(self, text='Hello tkinter')
#         self.label.grid(pady=5, padx=5)
#
#         # tk.Button
#         self.tk.Button = tk.Button(self, text='Click me', font=('OpenSans', 15), width=20, pady=5)
#         self.tk.Button['command'] = self.tk.Button_clicked
#         self.tk.Button.grid(pady=5, padx=5)
#
#     def tk.Button_clicked(self):
#         showinfo(title='Information', message='Hello, Tkinter')
#
#
# gui = Gui()
#
# gui.mainloop()

#
#
#
