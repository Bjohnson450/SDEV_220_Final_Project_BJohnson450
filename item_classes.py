class Location:
    def __init__(self, department, aisle, shelf):
        self.department = department
        self.aisle = aisle
        self.shelf = shelf

    def display_location(self):
        return f"Location: Department {self.department}, Aisle {self.aisle}, Shelf {self.shelf}"
    
    def __str__(self):
        return f"\nDepartment: {self.department} \nAisle: {self.aisle} \nShelf: {self.shelf}"

class Item:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        return f"Item: {self.name} \nLocation \n-----------------{self.location}"

class Soup(Item):
    def __init__(self, name, soup_type, size, location):
        super().__init__(name, location)
        self.soup_type = soup_type
        self.size = size

    def display_info(self):
        return f"{super().display_info()}\nFlavor: {self.soup_type}\nSize: {self.size}ml"

class Fruit(Item):
    def __init__(self, name, location):
        super().__init__(name, location)

    def display_info(self):
        return super().display_info()

class Vegetable(Item):
    def __init__(self, name, location):
        super().__init__(name, location)

    def display_info(self):
        return super().display_info()

class Juice(Item):
    def __init__(self, name, flavor, location):
        super().__init__(name, location)
        self.flavor = flavor

    def display_info(self):
        return f"{super().display_info()}\nFlavor: {self.flavor}"

class BakingSupplies(Item):
    def __init__(self, name, type_of_supply, brand, location):
        super().__init__(name, location)
        self.type_of_supply = type_of_supply
        self.brand = brand

    def display_info(self):
        return f"{super().display_info()}\nType: {self.type_of_supply}\nBrand: {self.brand}"

class ChipsAndSnacks(Item):
    def __init__(self, name, flavor, size, location):
        super().__init__(name, location)
        self.flavor = flavor
        self.size = size

    def display_info(self):
        return f"{super().display_info()}\nFlavor: {self.flavor}\nSize: {self.size}oz"

class Dairy(Item):
    def __init__(self, name, fat_content, location):
        super().__init__(name, location)
        self.fat_content = fat_content

    def display_info(self):
        return f"{super().display_info()}\nFat Content: {self.fat_content}"
