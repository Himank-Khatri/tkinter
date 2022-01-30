import tkinter as tk
from tkinter import Variable, ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('600x400')
root.resizable(False,False)
root.title('Lables')


'''GRID CONFIG'''
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)


'''TEXT LABELS'''
# text_label = ttk.Label(root, text='Hello World')
# text_label.pack(side='top',expand=False)
# text_label.config(font=('Segoe UI', 60))


'''IMAGE LABELS'''
# image = Image.open("image_png.png").resize((600, 400))
# photo = ImageTk.PhotoImage(image)
# final = tk.Label(root, text='Hello World!', image=photo, compound='center')
# final.pack()


'''TEXT INPUT & SCROLL'''
# text = tk.Text(root, height=8)
# text.grid(row=0, column=0, sticky="ew")
# text.insert("1.0", "Please enter a comment...")

# text_scroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
# text_scroll.grid(row=0, column=1, sticky="ns")
# text['yscrollcommand'] = text_scroll.set


'''SEPERATORS'''
# ttk.Label(root, text='Hello, World!', padding=20).pack()
# ttk.Separator(root, orient='horizontal').pack(fill='x')
# ttk.Label(root, text='Hello, World!', padding=20).pack()


'''CHECKBOX'''
# def print_current_option():
#     print(selected_option.get())

# selected_option = tk.StringVar()
# check_button = ttk.Checkbutton(
#     root,
#     text='Check Me',
#     variable=selected_option,
#     command=print_current_option,
#     onvalue='On',
#     offvalue='Off'
# )
# check_button.pack(expand=True)


'''RADIO BUTTONS'''
# storage_variable = tk.StringVar()

# option_one = ttk.Radiobutton(root, text='Option 1', variable=storage_variable, value='First Option')
# option_one.pack()

# option_two = ttk.Radiobutton( root, text='Option 2', variable=storage_variable, value='Second Option')
# option_two.pack()

# option_three = ttk.Radiobutton( root, text='Option 3', variable=storage_variable, value='Third Option')
# option_three.pack()


'''COMBO BOXES'''
# selected_weekday = tk.StringVar()
# weekday = ttk.Combobox(root, textvariable=selected_weekday)
# weekday["values"] = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
# weekday["state"] = 'readonly' # "normal"
# weekday.pack(expand=True)

# def handle_selection(event):
#     print('Today is', selected_weekday.get())
#     print("Anyway we're gonna change it to Friday.")
#     selected_weekday.set('Friday')
#     print(weekday.current())    

# weekday.bind('<<ComboboxSelected>>', handle_selection)


'''LIST BOXES'''
# programming_langs = ('C', 'Go', 'Java', 'Perl', 'Python', 'Ruby')
# langs = tk.StringVar(value=programming_langs)
# langs_select = tk.Listbox(root, listvariable=langs, height=6, selectmode='extended')
# langs_select.pack()

# def handle_selection_change(event):
#     selected_indices = langs_select.curselection()
#     for i in selected_indices:
#         print(langs_select.get(i))

# langs_select.bind('<<ListboxSelect>>', handle_selection_change)


'''SPIN BOXES'''
# initial_value = tk.IntVar(value=20)
# values = (5,10,15,20,25,30) # optional
# spin_box = ttk.Spinbox(root, values=values, from_=0, to=30, textvariable=initial_value, wrap=True)
# spin_box.pack(expand=True)


'''SCALES'''
# def handle_scale_change(event):
#     print(scale.get())

# scale = ttk.Scale(root, orient='horizontal', from_=0, to=10, command=handle_scale_change)
# scale.pack(fill='x', expand=True)


root.mainloop()



