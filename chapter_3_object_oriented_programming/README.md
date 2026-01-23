# Chapter 3: Object-Oriented Programming

This chapter covers the fundamentals of object-oriented programming in Python: classes, objects, methods, encapsulation, inheritance, composition, and duck typing.

## Key Concepts

### Classes and Objects: The Building Blocks
- **Classes**: Blueprints or templates for creating objects. Define what data and behavior objects will have.
- **Objects**: Instances of classes - the actual "things" you work with. Created by calling the class like a function.
- **Methods**: Functions defined inside classes that operate on objects.
- **`__init__`**: Special method called when creating new objects. Sets up initial state.

### Encapsulation: Hiding Complexity
- **Public Interface**: Methods and attributes users should interact with. The "controls" you expose.
- **Private Attributes**: Internal data marked with `_` prefix. Implementation details users shouldn't touch.
- **Data Hiding**: Protect internal state from accidental modification. Like keeping engine parts inside a car.

### Inheritance: "Is A" Relationships
- **Parent/Child Classes**: Child classes inherit behavior from parents but can add/modify functionality.
- **"Is A" Rule**: Only use inheritance when the relationship makes sense (e.g., Triangle IS A Polygon).
- **Method Resolution Order**: How Python finds which method to call when there are multiple options.
- **Super()**: Call parent class methods from child classes.

### Composition: "Has A" Relationships
- **"Has A" Rule**: Build complex objects by combining simpler ones (e.g., Car HAS A Engine).
- **Flexibility**: Easier to change than inheritance. Like Lego blocks vs fixed sculptures.
- **Delegation**: One object forwards work to contained objects.

### Duck Typing: Behavior Over Type
- **"If it walks like a duck..."**: Accept any object that behaves correctly, regardless of its class.
- **Polymorphism**: Same interface, different implementations. Like USB ports accepting different devices.
- **Python's Flexibility**: No need for complex inheritance hierarchies for simple behavior matching.

### Magic Methods: Operator Overloading
- **Special Methods**: Methods starting/ending with `__` that give classes special powers.
- **`__str__`**: Controls how objects display as strings (used by `print()`).
- **`__add__`**: Defines `+` behavior for objects.
- **Common Magics**: `__eq__` (==), `__len__` ([]), `__getitem__` (indexing), etc.

## Examples with Detailed Explanations

### Vector Class (Basic OOP)
```python
class Vector:
    def __init__(self, x, y):  # Constructor - sets up new vectors
        self.x = x  # Instance attributes - data unique to each vector
        self.y = y

    def norm(self):  # Method - behavior for vectors
        return (self.x**2 + self.y**2)**0.5

    def __add__(self, other):  # Magic method - defines +
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):  # Magic method - defines string representation
        return f"({self.x}, {self.y})"

u = Vector(3, 4)  # Create object/instance
v = u + Vector(1, 2)  # Uses __add__ and creates new vector
print(v)  # Uses __str__
```

### Polygon Hierarchy (Inheritance)
```python
class Polygon:
    def __init__(self, sides, points):
        self._sides = sides  # Protected attribute
        self._points = points

    def sides(self):  # Public method
        return self._sides

class Triangle(Polygon):  # Inherits from Polygon
    def __init__(self, points):
        super().__init__(3, points)  # Call parent constructor

    def __str__(self):
        return "I'm a triangle."
```

### MyLimitedList (Composition)
```python
class MyLimitedList:
    def __init__(self):
        self._L = []  # Has a list - composition

    def append(self, item):
        self._L.append(item)  # Delegate to contained list

    def __getitem__(self, index):
        return self._L[index]  # More delegation
```

### Duck Typing Example
```python
def add_to_collection(collection, item):
    if hasattr(item, 'sides'):  # Duck typing - check behavior
        collection.add(item)

# Works with Triangle, Square, or any object with 'sides' method
fake_triangle = type('Fake', (), {'sides': lambda self: 3})()
add_to_collection(my_collection, fake_triangle)  # Works!
```