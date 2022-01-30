import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()
root.resizable(False, False)
root.title('Meter2Feet')
main = ttk.Frame(root)
main.grid(padx=20, pady=15)

meter_value = tk.StringVar()
feet_value = tk.StringVar(value='Feet shown here')
def calculate_feet(*args):
    try:
        meters = float(meter_value.get())
        feet = meters * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass

meter_label = ttk.Label(main, text="Meters:")
meter_input = ttk.Entry(main, width=15, textvariable=meter_value)

feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

meter_label.grid(row=0, column=0, padx=15, sticky='w')
meter_input.grid(row=0, column=1, padx=15, sticky='e')
meter_input.focus()

feet_label.grid(row=1, column=0, padx=15, pady=15, sticky='w')
feet_display.grid(row=1, column=1, padx=15, pady=15, sticky='w')

calc_button.grid(row=2, column=0, columnspan=2, sticky='ew')

meter_input.bind('<Return>', calculate_feet)
meter_input.bind('<KP_Enter>', calculate_feet)


root.mainloop()