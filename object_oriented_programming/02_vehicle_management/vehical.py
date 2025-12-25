class Vehicle:
    '''Parent class'''
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        '''Display Vehical information'''
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year : {self.year}")
        print(f"Price : {self.price}")

    def start_engine(self):
        '''Engine started form Vehical class'''
        print("Engine started...")
# ------------------------------ || -------------------------------


class Car(Vehicle):
    '''Child class inherits from Vehicle'''
    def __init__(self, brand:str, model:str, year:int, price:int, num_doors:int)-> str:
        super().__init__(brand, model, year, price)

        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors : {self.num_doors}")

    def start_engine(self):
        super().start_engine()
        print("Car engine started with key...")
# ------------------------------ || -------------------------------

class Motorcycle(Vehicle):
    '''Child class for Motorcycle management inherits from vehicle'''
    def __init__(self, brand:str, model:str, year:int, price:int, has_sidecar:str):
        super().__init__(brand, model, year, price)

        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"Has side car : {self.has_sidecar}")

    def start_engine(self):
        super().start_engine()
        print("Motorcycle engine started with button...")
# ------------------------------ || -------------------------------

class Truck(Vehicle):
    """Child class for Truck management inherits from vehicle"""
    def __init__(self, brand, model, year, price, cargo_cpct):
        super().__init__(brand, model, year, price)

        self.cargo_capacity = cargo_cpct

    def display_info(self):
        super().display_info()
        print(f"Cargo capacity is: {self.cargo_capacity} Tuns!")

    def start_engine(self):
        super().start_engine()
        print("Truck engine started with ignition")

# ------------------------------ || -------------------------------

class Showroom():
    '''Manages all avaliable vehicles'''
    def __init__(self):
        self.vehicals = [] # List of vehicals

    def add_vehicle(self, vehicle:str):
        '''Adds vehicle to showroom'''
        self.vehicals.append(vehicle)

    def display_vehicle(self):
        '''Display all vehicles'''
        if not self.vehicals:
            print("\nNo vehicle found: ")
            return
        
        else:
            print(f"\n{'='*30}")
            print(f"Total Vehicles: {len(self.vehicals)}")
            print(f"{'='*30}")
            
            for i, vehicle in enumerate(self.vehicals, 1):
                print(f"\nVehicle {i}:")
                print("-" * 30)
                vehicle.display_info()
                vehicle.start_engine()
                print("-" * 30)
# ------------------------------ || -------------------------------

class Vehicle_System:
    '''Interaction and menu'''

    def __init__(self, showroom):
        self.showroom = showroom
        self.menu = {
            1: "Add Car",
            2: "Add Motorcycle",
            3: "Add Truck",
            4: "Display All Vehicles",
            5: "Exit"
        }

    def add_car_flow(self):
        '''Handels car adding and related task'''
        # brand, model, year, price, num_doors
        print("\n ------ ADD NEW CAR ------\n")
        try:
            brand = input("Enter car brand: ")
            model = input("Enter car model: ")
            year = int(input("Enter year (Ex: 2024): "))
            price = int(input("Enter car price (Ex: 2000000): "))
            no_doors = int(input("Number of door car have? (Ex: 4): "))

            # Creating car object
            car = Car(brand, model, year, price, no_doors)

            # Add to showroom 
            showroom.add_vehicle(car)
            
            # Messsage of car added
            print("Your car added to showroom sucessfully!")

        except ValueError:
            print("Invalid input. Try again!")


    def add_Motorcycle_flow(self):
        '''Handels motorcycle adding and related tasks'''

        # Adding message to show 
        print("\n ------ ADD NEW MOTORCYCLE ------\n")

        try:
            brand = input("Enter Brand: ")
            model = input("Enter model: ")
            year = int(input("Enter year (Ex; 2025): "))
            price = int(input("Enter price (Ex: 200000): "))
            has_side_car = input("Has side car? (Y/N): ")

            # Create motorcycle object
            motorcycle = Motorcycle(brand, model, year, price, has_side_car)

            # Add to showroom 
            showroom.add_vehicle(motorcycle)
            # Messsage of car added
            print("Your car added to showroom sucessfully!")

        except ValueError:
            print("Invalid input. Try again!")

    def add_truck_flow(self):
        '''Handels truck flow and releted tasks'''

        # Adding message to show 
        print("\n ------ ADD NEW TRUCK ------\n")

        try:
            brand = input("Enter Brand: ")
            model = input("Enter Model: ")
            year = int(input("Enter year (Ex; 2025): "))
            price = int(input("Enter price (Ex: 200000): "))
            cargo_cpct = int(input("Enter cargo capacity(Ex; 3, 5): "))
        
            truck = Truck(brand, model, year, price, cargo_cpct)

            showroom.add_vehicle(truck)

        except ValueError:
            print("Invalid input. Try again!")



    def show_menu(self):
        """Display menu options"""
        print("\n" + "="*30)
        print("    VEHICLE MANAGEMENT SYSTEM")
        print("="*30)
        for key, value in self.menu.items():
            print(f"{key}. {value}")
        print("="*30)


    def run(self):
        '''Main program loop'''
        while True:
            self.show_menu()

            try:
                choise = int(input("Enter your choise: "))
            except ValueError:
                print("Invalid input. Try again...")
                continue

            if choise == 1:
                self.add_car_flow()
            elif choise == 2:
                self.add_Motorcycle_flow()
            elif choise == 3:
                self.add_truck_flow()
            elif choise == 4:
                showroom.display_vehicle()
            elif choise == 5:
                print("\nThank you for choosing our showroom. Visit again!")
                break
            else:
                print("\n ------ Please Choose valid input ------\n!")
                continue


if __name__ == "__main__":
    # object for showroom class
    showroom = Showroom()

    # object for vehical_system with showroom
    system = Vehicle_System(showroom)

    # Running main program loop 
    system.run()