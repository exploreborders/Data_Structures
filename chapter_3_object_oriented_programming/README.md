# Chapter 3: Object-Oriented Programming - Modeling Real-World Concepts

This chapter introduces object-oriented programming (OOP) as a powerful paradigm for organizing code around real-world concepts. OOP allows you to model complex systems by breaking them into objects that interact with each other, making code more modular, reusable, and easier to understand.

## Why Object-Oriented Programming?

### The Problem with Procedural Programming
Traditional procedural programming organizes code around functions that operate on data. This can lead to:
- **Scattered logic**: Related operations spread across multiple functions
- **Global state**: Data accessible everywhere, leading to bugs
- **Tight coupling**: Functions depend heavily on specific data structures
- **Poor reusability**: Hard to reuse code in different contexts

### OOP Solution: Organizing Around Objects
OOP addresses these issues by:
- **Encapsulating** related data and behavior together
- **Hiding complexity** behind clean interfaces
- **Promoting modularity** through independent objects
- **Enabling reuse** through inheritance and composition

## Classes and Objects: The Building Blocks

### Understanding Classes as Blueprints
**Classes** are templates that define what objects will look like and how they'll behave. Think of a class as an architectural blueprint for a house - it specifies the structure and capabilities, but isn't a house itself.

**Key Components of a Class:**
- **Attributes**: Data that objects will store (like properties)
- **Methods**: Functions that define object behavior
- **Constructor**: Special method that creates new objects

### The `self` Parameter: Object Identity
Every method receives `self` as its first parameter, which refers to the specific object being operated on. This allows objects to maintain their own state and behave independently.

**Example:**
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name        # Each dog has its own name
        self.breed = breed      # Each dog has its own breed
        self.energy = 100       # Each dog has its own energy level

    def bark(self):
        return f"{self.name} says woof!"  # Uses this dog's name

# Create different objects with different states
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

print(dog1.bark())  # "Buddy says woof!"
print(dog2.bark())  # "Max says woof!"
```

### Instance vs Class Attributes
```python
class Dog:
    # Class attribute - shared by all dogs
    species = "Canis familiaris"

    def __init__(self, name):
        # Instance attributes - unique to each dog
        self.name = name
        self.tricks = []  # Each dog has its own list

    def learn_trick(self, trick):
        self.tricks.append(trick)  # Modifies this dog's tricks

dog1 = Dog("Buddy")
dog2 = Dog("Max")

dog1.learn_trick("sit")
dog2.learn_trick("roll over")

print(Dog.species)     # "Canis familiaris" (class attribute)
print(dog1.tricks)     # ["sit"] (instance attribute)
print(dog2.tricks)     # ["roll over"] (instance attribute)
```

## Encapsulation: Protecting Internal State

### The Public Interface Contract
Encapsulation is about defining clear boundaries between what users of your class need to know and what they don't. The **public interface** is your contract with users - it defines how they can interact with your objects safely.

### Private Attributes: Implementation Details
Python uses naming conventions to indicate privacy:
- `_attribute`: Protected (internal use, but accessible)
- `__attribute`: Private (name mangling makes it harder to access)

**Example of Good Encapsulation:**
```python
class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance  # Protected attribute
        self._transactions = []          # Protected attribute

    def deposit(self, amount):
        """Public method - safe interface for users."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        if amount > 10000:  # Business rule
            raise ValueError("Deposit amount too large")

        self._balance += amount
        self._transactions.append(f"Deposit: +{amount}")
        return self._balance

    def withdraw(self, amount):
        """Public method - validates and updates balance."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount
        self._transactions.append(f"Withdrawal: -{amount}")
        return self._balance

    def get_balance(self):
        """Public method - controlled access to balance."""
        return self._balance

# Good usage
account = BankAccount(1000)
account.deposit(500)      # ✓ Validates and updates safely
balance = account.get_balance()  # ✓ Controlled access

# Bad usage (breaks encapsulation)
# account._balance = -1000  # ✗ Bypasses validation
```

### Benefits of Encapsulation
1. **Data Integrity**: Internal state stays valid
2. **API Stability**: Users don't depend on implementation details
3. **Maintainability**: Internal changes don't break users
4. **Safety**: Prevents accidental corruption of object state

## Inheritance: "Is A" Relationships

### Understanding Inheritance Hierarchies
Inheritance creates family trees of classes where child classes inherit behavior from parent classes. This models "is a" relationships in the real world.

**When to Use Inheritance:**
- ✅ `Triangle` inherits from `Polygon` (Triangle IS A Polygon)
- ✅ `Car` inherits from `Vehicle` (Car IS A Vehicle)
- ❌ `Engine` inherits from `Car` (Engine is NOT a type of Car)

### Method Overriding and Extension
Child classes can modify inherited behavior:
```python
class Animal:
    def speak(self):
        return "Some generic animal sound"

    def move(self):
        return "Moves in some way"

class Dog(Animal):
    def speak(self):  # Override parent's method
        return "Woof!"

    def fetch(self):  # Add new method
        return "Fetches the ball"

class Cat(Animal):
    def speak(self):  # Override parent's method
        return "Meow!"

# Usage
dog = Dog()
cat = Cat()

print(dog.speak())   # "Woof!" (overridden)
print(dog.move())    # "Moves in some way" (inherited)
print(dog.fetch())   # "Fetches the ball" (added)

print(cat.speak())   # "Meow!" (overridden)
print(cat.move())    # "Moves in some way" (inherited)
```

### The `super()` Function: Calling Parent Methods
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}"

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)  # Call parent's __init__
        self.salary = salary

    def introduce(self):
        # Call parent's method and extend it
        basic_intro = super().introduce()
        return f"{basic_intro} and I earn ${self.salary}"

employee = Employee("Alice", 30, 50000)
print(employee.introduce())
# "Hi, I'm Alice and I earn $50000"
```

### Multiple Inheritance and Method Resolution Order (MRO)
Python supports multiple inheritance, but it can be complex. The MRO determines which method gets called when multiple parents define the same method.

```python
class A:
    def method(self): return "A"

class B:
    def method(self): return "B"

class C(A, B):  # C inherits from both A and B
    pass

c = C()
print(c.method())  # "A" (A comes first in MRO)
print(C.__mro__)   # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
```

## Composition: "Has A" Relationships

### Building Objects from Components
Composition assembles complex objects from simpler parts. Instead of inheriting behavior, objects contain other objects that provide functionality.

**"Has A" vs "Is A":**
- **Inheritance**: "A Car IS A Vehicle" (inheritance)
- **Composition**: "A Car HAS AN Engine" (composition)

### Composition Example
```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower} HP started"

    def stop(self):
        return "Engine stopped"

class Wheels:
    def __init__(self, count=4):
        self.count = count

    def rotate(self):
        return f"All {self.count} wheels rotating"

class Car:
    def __init__(self, make, model, hp):
        self.make = make
        self.model = model
        self.engine = Engine(hp)      # Car HAS AN Engine
        self.wheels = Wheels()        # Car HAS Wheels

    def start(self):
        engine_msg = self.engine.start()
        wheels_msg = self.wheels.rotate()
        return f"{self.make} {self.model}: {engine_msg}, {wheels_msg}"

    def drive(self):
        return f"{self.make} {self.model} is driving"

# Usage
car = Car("Toyota", "Camry", 200)
print(car.start())   # "Toyota Camry: Engine with 200 HP started, All 4 wheels rotating"
print(car.drive())   # "Toyota Camry is driving"
```

### Advantages of Composition
1. **Flexibility**: Easy to swap components (change engine type)
2. **Loose Coupling**: Components can be developed independently
3. **Testability**: Individual components can be tested in isolation
4. **Reusability**: Components can be used in different contexts

### Delegation Pattern
Objects forward method calls to their components:
```python
class Playlist:
    def __init__(self):
        self._songs = []  # Composition

    def add_song(self, song):
        self._songs.append(song)  # Delegate to list

    def remove_song(self, song):
        self._songs.remove(song)  # Delegate to list

    def __len__(self):
        return len(self._songs)    # Delegate to list

    def __getitem__(self, index):
        return self._songs[index]  # Delegate to list
```

## Duck Typing: Behavior Over Type

### The Duck Test
"If it walks like a duck and quacks like a duck, then it is a duck."

In programming: If an object behaves the way you expect, use it regardless of its class.

### Duck Typing in Practice
```python
# Traditional approach (type checking)
def process_data(data):
    if isinstance(data, list):
        return sum(data)
    elif isinstance(data, dict):
        return sum(data.values())
    else:
        raise TypeError("Unsupported data type")

# Duck typing approach (behavior checking)
def process_data(data):
    try:
        return sum(data)  # Works if data is iterable and contains numbers
    except TypeError:
        raise TypeError("Data must be iterable and contain numbers")

# Even more flexible
def process_data(data):
    if hasattr(data, '__iter__'):  # Check if iterable
        return sum(data)
    else:
        return float(data)  # Try to convert single number

# Usage
print(process_data([1, 2, 3]))        # 6
print(process_data({1, 2, 3}))        # 6 (set is iterable)
print(process_data((1, 2, 3)))        # 6 (tuple is iterable)
print(process_data(42))               # 42.0 (single number)
```

### Benefits of Duck Typing
1. **Flexibility**: Accept any object that behaves correctly
2. **Extensibility**: New types work automatically if they implement the expected interface
3. **Loose Coupling**: Functions don't depend on specific class hierarchies
4. **Pythonic**: Emphasizes capabilities over inheritance relationships

## Magic Methods: Operator Overloading

### Special Methods for Custom Behavior
Magic methods (dunder methods) give your classes special powers by defining how they interact with Python's built-in operations.

### Arithmetic Operators
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):      # +
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):      # -
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):     # *
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar): # /
        return Vector(self.x / scalar, self.y / scalar)

    def __neg__(self):             # unary -
        return Vector(-self.x, -self.y)

# Usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)  # Vector(4, 6)
print(v1 * 2)   # Vector(6, 8)
print(-v1)      # Vector(-3, -4)
```

### Comparison Operators
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):       # ==
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):       # <
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

    def __le__(self, other):       # <=
        return self < other or self == other

# Usage
v1 = Vector(3, 4)  # magnitude = 5
v2 = Vector(1, 2)  # magnitude = sqrt(5) ≈ 2.236

print(v1 == Vector(3, 4))  # True
print(v1 < v2)             # False (5 > 2.236)
print(v2 < v1)             # True
```

### String Representation
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):      # str() and print()
        return f"({self.x}, {self.y})"

    def __repr__(self):     # repr() and interactive display
        return f"Vector({self.x}, {self.y})"

# Usage
v = Vector(3, 4)
print(v)        # "(3, 4)" - uses __str__
print(repr(v))  # "Vector(3, 4)" - uses __repr__
```

### Container Methods
```python
class SimpleList:
    def __init__(self):
        self._items = []

    def __len__(self):             # len()
        return len(self._items)

    def __getitem__(self, index):  # []
        return self._items[index]

    def __setitem__(self, index, value):  # [] =
        self._items[index] = value

    def __delitem__(self, index):  # del []
        del self._items[index]

    def __iter__(self):            # iteration
        return iter(self._items)

    def __contains__(self, item):  # in
        return item in self._items

# Usage
lst = SimpleList()
lst._items = [1, 2, 3]  # Direct access for demo

print(len(lst))      # 3
print(lst[1])        # 2
lst[1] = 99
print(2 in lst)      # False (2 was changed to 99)
print(99 in lst)     # True
```

## OOP Design Principles

### SOLID Principles in Python

#### Single Responsibility Principle
A class should have only one reason to change.
```python
# Bad: One class doing too many things
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self): pass
    def save_to_database(self): pass  # Different responsibility
    def send_email(self): pass        # Different responsibility

# Good: Separate responsibilities
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class PayrollCalculator:
    def calculate_pay(self, employee): pass

class EmployeeRepository:
    def save(self, employee): pass

class EmailService:
    def send_welcome_email(self, employee): pass
```

#### Open-Closed Principle
Software entities should be open for extension but closed for modification.
```python
# Bad: Modifying existing code for new features
class ShapeCalculator:
    def area(self, shape):
        if shape.type == "circle":
            return 3.14 * shape.radius ** 2
        elif shape.type == "square":
            return shape.side ** 2
        # Adding triangle requires modifying this method

# Good: Extension through new classes
class Shape:
    def area(self): pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Adding Triangle doesn't require modifying existing code
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
```

### Choosing Between Inheritance and Composition

#### When to Use Inheritance
- Clear "is a" relationships
- Shared behavior across multiple related classes
- Polymorphism is needed
- The base class is stable and well-understood

#### When to Use Composition
- "Has a" relationships
- You want to reuse behavior from unrelated classes
- The implementation may change frequently
- You want to avoid deep inheritance hierarchies

### Common OOP Patterns in Python

#### Factory Pattern
```python
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, **params):
        if shape_type == "circle":
            return Circle(**params)
        elif shape_type == "square":
            return Square(**params)
        elif shape_type == "triangle":
            return Triangle(**params)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Usage
circle = ShapeFactory.create_shape("circle", radius=5)
square = ShapeFactory.create_shape("square", side=4)
```

#### Strategy Pattern
```python
from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortingStrategy):
    def sort(self, data):
        # Bubble sort implementation
        return sorted(data)  # Simplified

class QuickSort(SortingStrategy):
    def sort(self, data):
        # Quick sort implementation
        return sorted(data)  # Simplified

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)

# Usage
sorter = Sorter(BubbleSort())
result = sorter.sort([3, 1, 4, 1, 5])
```

## Summary: OOP Benefits and Best Practices

### Benefits of Object-Oriented Programming
1. **Modularity**: Code organized into independent, reusable units
2. **Maintainability**: Changes localized to specific classes
3. **Extensibility**: New functionality added through inheritance/composition
4. **Testability**: Individual objects can be tested in isolation
5. **Real-world Modeling**: Code structure mirrors problem domain

### Best Practices
- **Favor composition over inheritance** when possible
- **Use clear, descriptive class and method names**
- **Keep classes focused on single responsibilities**
- **Design clean public interfaces**
- **Use duck typing for flexible APIs**
- **Document your classes and methods**
- **Write tests for your classes**

This comprehensive introduction to OOP provides the foundation for understanding data structures as objects with well-defined interfaces and behaviors.