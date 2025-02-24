import os
from item_classes import Location, Soup, Fruit, Vegetable, Juice, BakingSupplies, ChipsAndSnacks, Dairy

def get_location_input():
    aisle = input("Enter aisle name or number: ")
    shelf = input("Enter shelf: ")
    section = input("Enter section(right side, left side, or front facing): ")
    return Location(aisle, shelf, section)

def get_item_input():
    print("\nChoose the item type: ")
    print("1. Soup")
    print("2. Fruit")
    print("3. Vegetable")
    print("4. Juice")
    print("5. Baking Supplies")
    print("6. Chips and Snacks")
    print("7. Dairy")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":  # Soup
        name = input("Enter item name: ")
        soup_type = input("Enter soup flavor: ")
        size = input("Enter size in ml: ")
        location = get_location_input()
        return Soup(name, soup_type, size, location)
    
    elif choice == "2":  # Fruit
        name = input("Enter item name: ")
        location = get_location_input()
        return Fruit(name, location)
    
    elif choice == "3":  # Vegetable
        name = input("Enter item name: ")
        location = get_location_input()
        return Vegetable(name, location)
    
    elif choice == "4":  # Juice
        name = input("Enter item name: ")
        flavor = input("Enter juice flavor: ")
        location = get_location_input()
        return Juice(name, flavor, location)
    
    elif choice == "5":  # Baking Supplies
        name = input("Enter item name: ")
        type_of_supply = input("Enter type of baking supply: ")
        brand = input("Enter brand: ")
        location = get_location_input()
        return BakingSupplies(name, type_of_supply, brand, location)
    
    elif choice == "6":  # Chips and Snacks
        name = input("Enter item name: ")
        flavor = input("Enter snack flavor: ")
        size = input("Enter size: ")
        location = get_location_input()
        return ChipsAndSnacks(name, flavor, size, location)
    
    elif choice == "7":  # Dairy
        name = input("Enter item name: ")
        fat_content = input("Enter fat content (percentage): ")
        location = get_location_input()
        return Dairy(name, fat_content, location)

    else:
        print("Invalid choice. Please try again.")
        return None


def sanitize_filename(item_name):
    sanitized_name = item_name.replace(" ", "_")
    sanitized_name = ''.join(e for e in sanitized_name if e.isalnum() or e == '_')
    return sanitized_name

def save_to_file(items):
    base_path = r"C:\Users\User\Desktop\Python projects\Final Project\Item_locations"  # Base directory to save items

    os.makedirs(base_path, exist_ok=True)

    for item in items:
        item_name = item.name
        sanitized_name = sanitize_filename(item_name)

        item_file_path = os.path.join(base_path, f"{sanitized_name}.txt")

        with open(item_file_path, "w") as file:
            file.write(f"{item.display_info()}\n\n")

def main():
    items = []
    while True:
        item = get_item_input()
        if item:
            items.append(item)
        
        another = input("\nDo you want to enter another item? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    save_to_file(items)
    print("\nItems have been saved")

if __name__ == "__main__":
    main()