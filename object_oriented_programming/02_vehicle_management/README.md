# 🚗 Vehicle Management System

A Python-based vehicle showroom management system demonstrating **Object-Oriented Programming** principles including **Inheritance** and **Polymorphism**. This project showcases the transition from basic OOP concepts to advanced class hierarchies and method overriding.

**Part of:** [Raw Python Logic Building Series](https://github.com/pradip-pawar1/Raw-python-Logic_building)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technical Highlights](#technical-highlights)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Class Architecture](#class-architecture)
- [OOP Concepts Demonstrated](#oop-concepts-demonstrated)
- [Code Examples](#code-examples)
- [What I Learned](#what-i-learned)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

---

## Overview

This console-based application manages a vehicle showroom inventory, allowing users to add different types of vehicles (Cars, Motorcycles, Trucks) and view the complete inventory. The system demonstrates how inheritance hierarchies work in real-world applications.

**Key Achievement:** Successfully implemented polymorphism where the same method (`start_engine()`) exhibits different behavior across vehicle types—a core principle used in production-level software design.

---

## Features

### Vehicle Management
- **Add Multiple Vehicle Types**
  - Cars with door count
  - Motorcycles with sidecar option
  - Trucks with cargo capacity
  
- **Inventory Display**
  - View all vehicles with complete specifications
  - See vehicle-specific attributes
  - Demonstrate polymorphic behavior in action

### User Experience
- Interactive menu-driven interface
- Input validation and error handling
- Clear success messages and feedback
- Clean, organized output formatting

---

## Technical Highlights

- **Pure Python Implementation** - No external dependencies
- **Class Hierarchy Design** - One parent class, three specialized child classes
- **Polymorphic Behavior** - Method overriding for vehicle-specific operations
- **Clean Code Principles** - Single Responsibility, DRY (Don't Repeat Yourself)
- **Error Handling** - Try-except blocks for robust input validation
- **Type Safety** - Boolean conversion for yes/no inputs

---

## Project Structure
```
02_vehicle_management/
├── vehicle.py          # Main application file
└── README.md           # Project documentation
```

**File Organization:**
```python
vehicle.py
├── Vehicle (Parent Class)
├── Car (Child Class)
├── Motorcycle (Child Class)
├── Truck (Child Class)
├── Showroom (Management Class)
├── Vehicle_System (UI Class)
└── Main Execution Block
```

---

## Installation

### Prerequisites
- Python 3.7 or higher
- No external libraries required

### Setup

1. Clone the repository:
```bash
git clone https://github.com/pradip-pawar1/Raw-python-Logic_building.git
cd object_oriented_programming/02_vehicle_management
```

2. Run the application:
```bash
python vehicle.py
```

---

## Usage

### Starting the Application
```bash
python vehicle.py
```

### Main Menu
```
==============================
    VEHICLE MANAGEMENT SYSTEM
==============================
1. Add Car
2. Add Motorcycle
3. Add Truck
4. Display All Vehicles
5. Exit
==============================
```

### Example Workflow

**Adding a Car:**
```
------ ADD NEW CAR ------

Enter car brand: Toyota
Enter car model: Fortuner
Enter year (Ex: 2024): 2024
Enter car price (Ex: 2000000): 3500000
Number of doors (Ex: 4): 4

Toyota Fortuner added to showroom successfully!
```

**Adding a Motorcycle:**
```
------ ADD NEW MOTORCYCLE ------

Enter Brand: Royal Enfield
Enter model: Classic 350
Enter year (Ex: 2025): 2024
Enter price (Ex: 200000): 185000
Has sidecar? (Y/N): n

Royal Enfield Classic 350 added to showroom successfully!
```

**Viewing All Vehicles:**
```
==============================
Total Vehicles: 2
==============================

Vehicle 1:
------------------------------
Brand: Toyota
Model: Fortuner
Year: 2024
Price: 3500000
Number of doors: 4
Car engine started with key
------------------------------

Vehicle 2:
------------------------------
Brand: Royal Enfield
Model: Classic 350
Year: 2024
Price: 185000
Has sidecar: No
Motorcycle engine started with button
------------------------------
```

---

## Class Architecture

### 1. Vehicle (Parent Class)

**Purpose:** Base class defining common attributes and behaviors for all vehicles

**Attributes:**
- `brand` (str): Vehicle manufacturer
- `model` (str): Vehicle model name
- `year` (int): Manufacturing year
- `price` (int): Vehicle price

**Methods:**
- `display_info()`: Shows vehicle details
- `start_engine()`: Generic engine start behavior (overridden by children)

---

### 2. Car (Child Class)

**Inherits from:** Vehicle

**Additional Attributes:**
- `num_doors` (int): Number of doors (2, 4, etc.)

**Overridden Methods:**
- `display_info()`: Calls parent method + displays door count
- `start_engine()`: "Car engine started with key"

---

### 3. Motorcycle (Child Class)

**Inherits from:** Vehicle

**Additional Attributes:**
- `has_sidecar` (bool): Whether motorcycle has a sidecar

**Overridden Methods:**
- `display_info()`: Calls parent method + displays sidecar status
- `start_engine()`: "Motorcycle engine started with button"

---

### 4. Truck (Child Class)

**Inherits from:** Vehicle

**Additional Attributes:**
- `cargo_capacity` (int): Cargo capacity in tons

**Overridden Methods:**
- `display_info()`: Calls parent method + displays cargo capacity
- `start_engine()`: "Truck engine started with ignition"

---

### 5. Showroom (Management Class)

**Purpose:** Manages collection of all vehicles

**Attributes:**
- `vehicles` (list): Stores all Vehicle objects

**Methods:**
- `add_vehicle(vehicle)`: Adds vehicle to inventory
- `display_vehicle()`: Shows all vehicles with their details

---

### 6. Vehicle_System (UI Class)

**Purpose:** Handles user interaction and application flow

**Attributes:**
- `showroom` (Showroom): Reference to showroom object
- `menu` (dict): Menu options

**Methods:**
- `add_car_flow()`: Handle car addition
- `add_Motorcycle_flow()`: Handle motorcycle addition
- `add_truck_flow()`: Handle truck addition
- `show_menu()`: Display menu
- `run()`: Main program loop

---

## OOP Concepts Demonstrated

### 1. Inheritance (Parent-Child Relationship)
```python
class Vehicle:  # Parent
    def __init__(self, brand, model, year, price):
        self.brand = brand
        # ... other attributes

class Car(Vehicle):  # Child inherits from Vehicle
    def __init__(self, brand, model, year, price, num_doors):
        super().__init__(brand, model, year, price)  # Call parent constructor
        self.num_doors = num_doors
```

**Why it matters:** Eliminates code duplication. Common vehicle properties (brand, model, year, price) are defined once in the parent and inherited by all children.

---

### 2. Polymorphism (Same Method, Different Behavior)
```python
# Vehicle class
def start_engine(self):
    print("Engine started...")

# Car class
def start_engine(self):
    print("Car engine started with key")

# Motorcycle class
def start_engine(self):
    print("Motorcycle engine started with button")

# Truck class
def start_engine(self):
    print("Truck engine started with ignition")
```

**Why it matters:** Same method name (`start_engine`) produces different output based on object type. This is how real-world frameworks like Django and Flask handle different request types with the same interface.

---

### 3. Method Overriding

Child classes override parent methods to provide specialized behavior while maintaining the same interface.
```python
# Parent method
def display_info(self):
    print(f"Brand: {self.brand}")
    # ... other info

# Child method (Car)
def display_info(self):
    super().display_info()  # Call parent version first
    print(f"Number of doors: {self.num_doors}")  # Add child-specific info
```

---

### 4. Encapsulation

Each class bundles related data and operations together:
- Vehicle objects contain vehicle data AND vehicle operations
- Showroom contains vehicle collection AND inventory operations
- Vehicle_System contains UI logic AND menu operations

---

### 5. Abstraction

Users interact with simple interfaces without needing to know implementation details:
```python
showroom.add_vehicle(car)  # Simple interface
# User doesn't need to know how list.append() works internally
```

---

### Demonstrating Polymorphism
```python
vehicles = [car, motorcycle, truck]

for vehicle in vehicles:
    vehicle.start_engine()  # Same method call, different output
```

**Output:**
```
Car engine started with key
Motorcycle engine started with button
Truck engine started with ignition
```

---

## What I Learned

### OOP Principles
- **Inheritance enables code reuse** - Wrote vehicle properties once, used them three times
- **Polymorphism provides flexibility** - Same interface, different implementations
- **Method overriding customizes behavior** - Child classes specialize parent functionality
- **`super()` maintains parent-child connection** - Calls parent methods from child classes

### Software Design
- **Class hierarchies model real-world relationships** - Vehicles naturally form a hierarchy
- **Separation of concerns improves maintainability** - UI, business logic, and data management are separated
- **Composition over inheritance** - Vehicle_System HAS a Showroom (composition), doesn't inherit from it

### Python Skills
- **Boolean conversion** - Converting user input ("Y"/"N") to True/False
- **enumerate() for indexed loops** - Numbering vehicles in display
- **List comprehension alternative** - Using simple loops when clarity matters more
- **Exception handling patterns** - Using try-except for user input validation

### Real-World Application
- **Understanding class hierarchies** - How frameworks like Django use model inheritance
- **Polymorphic design patterns** - How different object types respond to same method calls
- **Menu-driven applications** - Building interactive CLI tools

---

## Future Enhancements

### Planned Features
- [ ] **Data Persistence** - Save vehicles to JSON file
- [ ] **Vehicle Search** - Search by brand, model, or price range
- [ ] **Price Filtering** - Filter vehicles by price budget
- [ ] **Vehicle Comparison** - Compare specifications of two vehicles
- [ ] **Sold Vehicles Tracking** - Mark vehicles as sold and track sales
- [ ] **Discount Management** - Apply discounts based on vehicle type
- [ ] **Test Drive Scheduling** - Book test drives for vehicles

### Technical Improvements
- [ ] **Unit Tests** - Add pytest for automated testing
- [ ] **Abstract Base Class** - Use ABC module for stricter inheritance
- [ ] **Property Decorators** - Add validation for price, year, etc.
- [ ] **Custom Exceptions** - Create VehicleNotFoundError, InvalidPriceError
- [ ] **Logging** - Add logging for operations tracking
- [ ] **Configuration File** - Move menu options to config.json

---

## Project Metrics

| Metric | Value |
|--------|-------|
| Lines of Code | ~200 |
| Classes | 6 |
| Methods | 15+ |
| Inheritance Levels | 2 (Vehicle → Car/Motorcycle/Truck) |
| Polymorphic Methods | 2 (display_info, start_engine) |
| Development Time | 3 days |

---

## Related Projects

|Sr. No | Project Name              | Link                                            |
| ---- | ------------------------- | ----------------------------------------------- |
| 1 | Word Guess Game           | [View Project](../../procedural_programming/01_word_guess_game/)           |
| 2 | ATM Simulation            | [View Project](../../procedural_programming/02_atm_simulation/)            |
| 3 | Library Management System | [View Project](../../procedural_programming/03_library_management/) |
| 4 | Student report card system | [View Project](../../procedural_programming/04_student_report_card_system/) |
| 5 | Number analyser | [View Project](../../procedural_programming/05_number_analyzer/) |
| 6 | Bank Management System | [View Project](../../object_oriented_programming/01_bank_management/)

Check out the complete series: [Raw Python Logic Building](https://github.com/pradip-pawar1/Raw-python-Logic_building)

---

## 👨‍💻 Author

**Pradip Pawar**

Civil Engineering Student | Self-Taught Python Developer | Aspiring AI/ML Engineer

- **GitHub:** [@pradip-pawar1](https://github.com/pradip-pawar1)
- **LinkedIn:** [@pradip-pawar1](https://www.linkedin.com/in/pradip-pawar1/)
- **Email:** pradip.codelabplus@gmail.com

---

## 🙏 Acknowledgments

- Built as part of learning Object-Oriented Programming in Python
- Focuses on mastering the four pillars: Encapsulation, Abstraction, Inheritance, Polymorphism
- Part of my transition journey from Civil Engineering to Software Development

---

## 📄 License

This project is open source and available under the [MIT License](../../LICENSE).

---

## 📊 Key Takeaways

> **From this project, I learned that inheritance isn't just about code reuse—it's about modeling real-world relationships in code. When a Car IS-A Vehicle, inheritance makes logical sense. When a Showroom HAS vehicles, composition (not inheritance) is the right choice.**

> **Polymorphism showed me how professional frameworks work: one interface (`start_engine()`), multiple implementations. This is the foundation of plugin systems, API design, and framework extensibility.**

---

**⭐ If you found this project helpful or interesting, please consider giving it a star!**

**🔄 Fork it, improve it, and share your learnings!**

---

*Last Updated: December 2024*
```

---

## **Why This README is Recruiter-Focused:**

✅ **Demonstrates technical depth** - Explains not just WHAT but WHY
✅ **Shows learning progression** - Clear "What I Learned" section
✅ **Professional formatting** - Tables, code blocks, proper structure
✅ **Real-world connections** - Links concepts to industry practices (Django, frameworks)
✅ **Metrics included** - Lines of code, development time, complexity
✅ **Future thinking** - Shows you understand what production code needs
✅ **Clear communication** - Technical concepts explained simply
✅ **Portfolio ready** - Can be shared directly with recruiters

---

## **Next Steps:**

1. Copy this entire markdown into your `README.md` file
2. Adjust any links if needed
3. Take a screenshot of your running program (optional but impressive)
4. Push to GitHub
5. Update your main repository README to link to this project

**LinkedIn Post Template:**
```
Just completed my second OOP project: Vehicle Management System 🚗

This project took my understanding from basic OOP to advanced concepts:

✅ Inheritance - One parent class (Vehicle), three specialized children (Car, Motorcycle, Truck)
✅ Polymorphism - Same method (start_engine), different behavior for each vehicle type
✅ Method Overriding - Child classes customize parent behavior
✅ Clean class hierarchies - Modeling real-world relationships in code

Key insight: Learned the difference between IS-A (inheritance) and HAS-A (composition) relationships. A Car IS-A Vehicle (inheritance), but a Showroom HAS vehicles (composition).

This is how frameworks like Django handle different model types with the same interface—powerful concept.

Project 1: Bank Management (Encapsulation) ✅
Project 2: Vehicle Management (Inheritance) ✅
Project 3: Library Management (Coming next)

GitHub: [link]

#Python #OOP #Programming #SoftwareDevelopment #Learning