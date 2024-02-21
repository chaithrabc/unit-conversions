import tkinter as tk

def cm_to_feet():
    try:
        cm = float(cm_entry.get())
        feet = cm / 30.48
        result_label1.config(text=f"{feet:.2f} feet")
    except ValueError:
        result_label1.config(text="Invalid input")

def feet_to_inches():
    try:
        feet = float(feet_entry.get())
        inches = feet * 12
        result_label2.config(text=f"{inches:.2f} inches")
    except ValueError:
        result_label2.config(text="Invalid input")

def sqft_to_sqm():
    try:
        sqft = float(sqft_entry.get())
        sqm = sqft / 10.764
        result_label3.config(text=f"{sqm:.2f} square meters")
    except ValueError:
        result_label3.config(text="Invalid input")

def sqft_to_hectare_acres():
    try:
        sqft = float(sqft_to_ha_entry.get())
        hectares = sqft / 107639.104
        acres = sqft / 43560
        result_label4.config(text=f"{hectares:.2f} hectares\n{acres:.2f} acres")
    except ValueError:
        result_label4.config(text="Invalid input")


root = tk.Tk()
root.title("Unit Conversion")


root.configure(bg="pale turquoise")

tk.Label(root, text="Centimeter to Feet:", bg="pale turquoise").grid(row=0, column=0, padx=5, pady=5)
cm_entry = tk.Entry(root)
cm_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=cm_to_feet, bg="azure4", fg="white").grid(row=0, column=2, padx=5, pady=5)
result_label1 = tk.Label(root, text="", bg="pale turquoise")
result_label1.grid(row=0, column=3, padx=5, pady=5)

tk.Label(root, text="Feet to Inches:", bg="pale turquoise").grid(row=1, column=0, padx=5, pady=5)
feet_entry = tk.Entry(root)
feet_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=feet_to_inches, bg="azure4", fg="white").grid(row=1, column=2, padx=5, pady=5)
result_label2 = tk.Label(root, text="", bg="pale turquoise")
result_label2.grid(row=1, column=3, padx=5, pady=5)

tk.Label(root, text="Sqft to Sqm:", bg="pale turquoise").grid(row=2, column=0, padx=5, pady=5)
sqft_entry = tk.Entry(root)
sqft_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=sqft_to_sqm, bg="azure4", fg="white").grid(row=2, column=2, padx=5, pady=5)
result_label3 = tk.Label(root, text="", bg="pale turquoise")
result_label3.grid(row=2, column=3, padx=5, pady=5)

tk.Label(root, text="Sqft to Hectare/Acres:", bg="pale turquoise").grid(row=3, column=0, padx=5, pady=5)
sqft_to_ha_entry = tk.Entry(root)
sqft_to_ha_entry.grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Convert", command=sqft_to_hectare_acres, bg="azure4", fg="white").grid(row=3, column=2, padx=5, pady=5)
result_label4 = tk.Label(root, text="", bg="pale turquoise")
result_label4.grid(row=3, column=3, padx=5, pady=5)

root.mainloop()
