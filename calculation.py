import tkinter as tk
from tkinter import simpledialog

# Create a dictionary to store jurisdiction prices
jurisdiction_prices = {
    "FCC/US/GV": 5244,
"Canada": 228,
"Puerto Rico": 152,
"Alabama": 38,
"Alaska": 114,
"Arizona": 76,
"Arkansas": 38,
"California": 1292,
"Colorado": 342,
"Connecticut": 152,
"DC": 114,
"Delaware": 0,
"Florida": 114,
"Georgia": 152,
"Hawaii": 76,
"Idaho": 114,
"Illinois": 152,
"Indiana": 114,
"Iowa": 38,
"Kansas": 152,
"Kentucky": 152,
"Louisiana": 76,
"Maine": 76,
"Maryland": 76,
"Massachusetts": 38,
"Michigan": 114,
"Minnesota": 114,
"Mississippi": 38,
"Missouri": 152,
"Montana": 38,
"Nebraska": 304,
"Nevada": 190,
"New Hampshire": 0,
"New Jersey": 0,
"New Mexico": 152,
"New York": 114,
"North Carolina": 38,
"North Dakota": 0,
"Ohio": 152,
"Oklahoma": 114,
"Oregon": 190,
"Pennsylvania": 228,
"Rhode Island": 0,
"South Carolina": 76,
"South Dakota": 0,
"Tennessee": 38,
"Texas": 190,
"Utah": 152,
"Vermont": 38,
"Virginia": 152,
"Washington": 152,
"West Virginia": 114,
"Wisconsin": 38,
"Wyoming": 76
}

# Function to calculate the total price
def calculate_price():
    # Get selected jurisdictions
    selected_jurisdictions = [jurisdiction for jurisdiction, var in jurisdictions_var.items() if var.get()]

    # Get carrier type from user
    carrier_type = simpledialog.askstring("Input", "Enter carrier type (Local, Wireless, VoIP, IXC, Inmate): ")

    # Get number of users from user
    num_users = simpledialog.askinteger("Input", "Enter number of users: ")

    # Calculate the total price based on selected jurisdictions
    total_price = sum(jurisdiction_prices[j] for j in selected_jurisdictions)

    # Modify the total price based on carrier type
    if carrier_type == "Local":
        pass  # No change for Local
    elif carrier_type == "Wireless":
        total_price *= 0.75
    elif carrier_type == "VoIP":
        total_price *= 0.70
    elif carrier_type == "IXC":
        total_price *= 0.50
    elif carrier_type == "Inmate":
        total_price *= 0.37

    # Apply additional pricing based on the number of users
    if num_users == 1:
        total_price += 0
    elif 2 <= num_users <= 5:
        total_price += (num_users - 1) * 600
    else:
        total_price += (5 * 600) + ((num_users - 5) * 300)

    # Display the calculated total price
    result_label.config(text=f"Total Annual Price: ${total_price:.2f}")

# Function to select all jurisdictions
def select_all():
    for jurisdiction in jurisdictions_var.values():
        jurisdiction.set(True)

# Function to deselect all jurisdictions
def deselect_all():
    for jurisdiction in jurisdictions_var.values():
        jurisdiction.set(False)

# Create the main application window
root = tk.Tk()
root.title("Price Calculator")

# Create a Frame for the checkboxes
checkbox_frame = tk.Frame(root)
checkbox_frame.pack()

# Create checkboxes for jurisdictions
jurisdictions_var = {}
columns = 3  # Number of columns for jurisdictions
row_num = 0
col_num = 0

for jurisdiction in jurisdiction_prices:
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(checkbox_frame, text=jurisdiction, variable=var, onvalue=True, offvalue=False)
    checkbox.grid(row=row_num, column=col_num, sticky="w", padx=5, pady=5)
    jurisdictions_var[jurisdiction] = var
    col_num += 1
    if col_num >= columns:
        col_num = 0
        row_num += 1

# Create a "Select All" button
select_all_button = tk.Button(root, text="Select All", command=select_all)
select_all_button.pack()

# Create a "Deselect All" button
deselect_all_button = tk.Button(root, text="Deselect All", command=deselect_all)
deselect_all_button.pack()

# Create a button to calculate the price
calculate_button = tk.Button(root, text="Calculate Price", command=calculate_price)
calculate_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()