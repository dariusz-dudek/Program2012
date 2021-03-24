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
    print(f"{key}_label = ttk.Label(self, text='{labels[key]}', font=getenv('MEDIUM_FONT'))")
    print(f"{key}_label.grid(pady=getenv('PADY_LABEL'), padx=getenv('PADX_LABEL'), row={count + 1}, column=0)")

