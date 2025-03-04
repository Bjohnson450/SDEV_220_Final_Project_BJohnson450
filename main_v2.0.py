import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from item_classes import Location, Soup, Fruit, Vegetable, Juice, BakingSupplies, ChipsAndSnacks, Dairy

# Function to sanitize filenames
def sanitize_filename(item_name):
    sanitized_name = item_name.replace(" ", "_")
    sanitized_name = ''.join(e for e in sanitized_name if e.isalnum() or e == '_')
    return sanitized_name

# Function to save item details to a file
def save_to_file(items):
    base_path = r"C:\Users\User\Desktop\Python projects\Final Project\Item_locations"  # Base directory to save items. Chancge Path as necessary
    os.makedirs(base_path, exist_ok=True)
    for item in items:
        item_name = item.name
        sanitized_name = sanitize_filename(item_name)
        item_file_path = os.path.join(base_path, f"{sanitized_name}.txt")
        with open(item_file_path, "w") as file:
            file.write(f"{item.display_info()}\n\n")

# Function to get location input from the user
def get_location_input():
    aisle = aisle_entry.get()
    shelf = shelf_entry.get()
    section = section_var.get()
    return Location(aisle, shelf, section)

# Function to get the item input based on the selected item type
def get_item_input():
    choice = item_type_var.get()
    name = name_entry.get()
    location = get_location_input()

    if choice == "Soup":
        soup_type = soup_type_entry.get()
        size = size_entry.get()
        return Soup(name, soup_type, size, location)
    
    elif choice == "Fruit":
        return Fruit(name, location)
    
    elif choice == "Vegetable":
        return Vegetable(name, location)
    
    elif choice == "Juice":
        flavor = flavor_entry.get()
        return Juice(name, flavor, location)
    
    elif choice == "Baking Supplies":
        type_of_supply = type_of_supply_entry.get()
        brand = brand_entry.get()
        return BakingSupplies(name, type_of_supply, brand, location)
    
    elif choice == "Chips and Snacks":
        flavor = flavor_entry.get()
        size = size_entry.get()
        return ChipsAndSnacks(name, flavor, size, location)
    
    elif choice == "Dairy":
        fat_content = fat_content_entry.get()
        return Dairy(name, fat_content, location)

# Function to handle the form submission
def submit_item():
    item = get_item_input()
    if item:
        items.append(item)
        messagebox.showinfo("Success", "Item added successfully!")

# Function to save all items
def save_items():
    save_to_file(items)
    messagebox.showinfo("Saved", "Items have been saved to files!")

# Function to update the visible fields based on the selected item type
def update_fields(event=None):
    choice = item_type_var.get()

    soup_type_label.grid_forget()
    soup_type_entry.grid_forget()
    flavor_label.grid_forget()
    flavor_entry.grid_forget()
    size_label.grid_forget()
    size_entry.grid_forget()
    type_of_supply_label.grid_forget()
    type_of_supply_entry.grid_forget()
    brand_label.grid_forget()
    brand_entry.grid_forget()
    fat_content_label.grid_forget()
    fat_content_entry.grid_forget()

    # Show fields based on the selected item type
    if choice == "Soup":
        soup_type_label.grid(row=2, column=0, padx=10, pady=5)
        soup_type_entry.grid(row=2, column=1, padx=10, pady=5)
        size_label.grid(row=3, column=0, padx=10, pady=5)
        size_entry.grid(row=3, column=1, padx=10, pady=5)
    
    elif choice in ["Juice", "Chips and Snacks"]:
        flavor_label.grid(row=2, column=0, padx=10, pady=5)
        flavor_entry.grid(row=2, column=1, padx=10, pady=5)
        size_label.grid(row=3, column=0, padx=10, pady=5)
        size_entry.grid(row=3, column=1, padx=10, pady=5)

    elif choice == "Baking Supplies":
        type_of_supply_label.grid(row=2, column=0, padx=10, pady=5)
        type_of_supply_entry.grid(row=2, column=1, padx=10, pady=5)
        brand_label.grid(row=3, column=0, padx=10, pady=5)
        brand_entry.grid(row=3, column=1, padx=10, pady=5)

    elif choice == "Dairy":
        fat_content_label.grid(row=2, column=0, padx=10, pady=5)
        fat_content_entry.grid(row=2, column=1, padx=10, pady=5)

root = tk.Tk()
root.title("Item Entry Form")

# List to store items
items = []

# Item Type Selection
item_type_var = tk.StringVar()
item_type_var.set("Soup")

item_type_label = tk.Label(root, text="Select Item Type:")
item_type_label.grid(row=0, column=0, padx=10, pady=5)

item_type_options = ["Soup", "Fruit", "Vegetable", "Juice", "Baking Supplies", "Chips and Snacks", "Dairy"]
item_type_menu = ttk.Combobox(root, textvariable=item_type_var, values=item_type_options)
item_type_menu.grid(row=0, column=1, padx=10, pady=5)
item_type_menu.bind("<<ComboboxSelected>>", update_fields)

# Entry fields for item details
name_label = tk.Label(root, text="Item Name:")
name_label.grid(row=1, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

# Labels and entry fields that will be used later
soup_type_label = tk.Label(root, text="Soup Type:")
soup_type_entry = tk.Entry(root)

flavor_label = tk.Label(root, text="Flavor:")
flavor_entry = tk.Entry(root)

size_label = tk.Label(root, text="Size:")
size_entry = tk.Entry(root)

type_of_supply_label = tk.Label(root, text="Baking Supply Type:")
type_of_supply_entry = tk.Entry(root)

brand_label = tk.Label(root, text="Brand:")
brand_entry = tk.Entry(root)

fat_content_label = tk.Label(root, text="Fat Content:")
fat_content_entry = tk.Entry(root)

# Location Inputs
aisle_label = tk.Label(root, text="Aisle:")
aisle_label.grid(row=8, column=0, padx=10, pady=5)
aisle_entry = tk.Entry(root)
aisle_entry.grid(row=8, column=1, padx=10, pady=5)

shelf_label = tk.Label(root, text="Shelf:")
shelf_label.grid(row=9, column=0, padx=10, pady=5)
shelf_entry = tk.Entry(root)
shelf_entry.grid(row=9, column=1, padx=10, pady=5)

section_label = tk.Label(root, text="Section:")
section_label.grid(row=10, column=0, padx=10, pady=5)
section_var = tk.StringVar()
section_var.set("right")
section_right = tk.Radiobutton(root, text="Right", variable=section_var, value="right")
section_right.grid(row=10, column=1, padx=10, pady=5, sticky="w")
section_left = tk.Radiobutton(root, text="Left", variable=section_var, value="left")
section_left.grid(row=10, column=2, padx=10, pady=5, sticky="w")
section_front = tk.Radiobutton(root, text="Front", variable=section_var, value="front")
section_front.grid(row=10, column=3, padx=10, pady=5, sticky="w")

# Submit button
submit_button = tk.Button(root, text="Add Item", command=submit_item)
submit_button.grid(row=11, column=0, columnspan=2, pady=20)

# Save Button
save_button = tk.Button(root, text="Save Items", command=save_items)
save_button.grid(row=12, column=0, columnspan=2, pady=20)

# Initial call to update the fields
update_fields()

# Start the Tkinter event loop
root.mainloop()
save_to_file(items)
