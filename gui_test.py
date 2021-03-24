import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry('480x480')

photo = Image.open('image.jpg')
photo = photo.resize((150, 100), Image.ANTIALIAS)

icon = ImageTk.PhotoImage(photo)
tkinter.Label(root, image=icon).pack()

canvas = tkinter.Canvas(root, width=300, height=300, bg='blue')
canvas.pack()
canvas.create_image(30, 15,anchor=tkinter.NW, image=icon)


# main_menu = tkinter.Menu()
# root.config(menu=main_menu)
#
# file_menu = tkinter.Menu(main_menu)
#
# main_menu.add_cascade(label='File', menu=file_menu)
#
# file_menu.add_command(label='New file')
# file_menu.add_command(label='Open')
# file_menu.add_separator()
# file_menu.add_command(label='Open module')
# file_menu.add_command(label='Save')
#
# edit_menu = tkinter.Menu(main_menu)
#
# main_menu.add_cascade(label='Edit', menu=edit_menu)
#
# edit_menu.add_command(label='Cut')
# edit_menu.add_command(label='Copy')
# edit_menu.add_separator()
# edit_menu.add_command(label='Add')
# edit_menu.add_command(label='Remove')
#
# under_menu = tkinter.Menu(edit_menu)
#
# edit_menu.add_cascade(label='Small', menu=under_menu)
#
# under_menu.add_command(label='Option1')
# under_menu.add_command(label='Option2')
# under_menu.add_separator()
# under_menu.add_command(label='Option3')
# under_menu.add_command(label='Option4')
# def function_button1():
#     print('Pressed button 1')
#
#
# def function_button2(event):
#     print('Pressed button 2')
#
#
# def function_button3(event):
#     print('Pressed button 3')
#
#
# def function_window(event):
#     print('Pressed window')


# button = tkinter.Button(root, text='Button 1', command=function_button1)
# button.pack()
# button2 = tkinter.Button(root, text='Button 2')
# button2.pack()
# button2.bind('<Button-1>', function_button2)
# button3 = tkinter.Button(root, text='Button 3')
# button3.pack()
# button3.bind('<Button-3>', function_button3)
#
# root.bind('<Button-1>', function_window)

# tkinter.Label(root, text='Login').grid(row=0, column=0, padx=2, pady=2)
# tkinter.Entry(root).grid(row=0, column=1, padx=2, pady=2)
#
# tkinter.Label(root, text='Password').grid(row=1, column=0, padx=2, pady=2)
# tkinter.Entry(root).grid(row=1, column=1, padx=2, pady=2)
#
# tkinter.Button(root, text='Send').grid(row=3, column=1, padx=2, pady=2)


# label = tkinter.Label(root, text='Program 2012')
# label.pack()
#
# canvas = tkinter.Canvas(root, height=300, width=350, bg='yellow')
# canvas.pack()
#
# for i in range(5):
# 	canvas.create_line(0, 50 * i, 350, 50 * i, width=5)
#
# canvas.create_oval(30, 30, 150, 150, fill='red')
# canvas.create_rectangle(20, 200, 100, 400, fill='blue')


# def button_function():
#     print('Pressed button')
#
#
# button1 = tkinter.Button(root, text='Button1', width=10, bg='red', fg='blue', command=button_function)
# button2 = tkinter.Button(root, text='Button2', command=button_function)
# button3 = tkinter.Button(root, text='Button3', command=button_function)
# button1.pack(side=tkinter.RIGHT)
# button2.pack(side=tkinter.BOTTOM)
# button3.place(x=0, y=0)

root.mainloop()
