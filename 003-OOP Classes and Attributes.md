# Introducing Python OOP 1
# Create classes and instantiate objects

- https://www.programiz.com/python-programming/object-oriented-programming
- https://amir.rachum.com/blog/2016/10/03/understanding-python-class-instantiation/
- https://realpython.com/python3-object-oriented-programming/
- https://stackoverflow.com/questions/38857446/how-to-convert-class-diagram-association-relation-to-code

## An Object
- Python is a multi-paradigm programming language. It supports different programming approaches
- One of the popular approaches to solve a programming problem is by creating objects
- This is known as Object-Oriented Programming (OOP)
- An object has two characteristics, attributes and behavior
- Formally, an object is a collection of data and associated behaviors.
- An object is a collection of data with associated behaviors

A student for example:

- Name, age, height (attributes)
- Walk, run, write (behavior)

## How to Define a Class
- Class is a blueprint for the object
- All class definitions start with the class keyword
- followed by the name of the class and a colon
- Name of the class starts with a Capital or PEP8 - CapWords notation
- Any code that is indented below the class definition is considered part of the class’s body
- It must start with a letter or underscore

## Pass
- the pass keyword. 
- pass is often used as a placeholder indicating where code will eventually go. 
- It allows you to run this code without Python throwing an error.

## Class Attribute / Instance Attribute
### Class Attribute
- Class attributes are the variables defined directly in the class that are shared by all objects of the class
- They have the same value for every instance.
### Instance Attribute
- Instance attributes are attributes or properties attached to an instance of a class
- Instance attributes are unique to each object

## Instantiating
- Instantiating a class is creating a copy of the class which inherits all class variables and methods.
- Instantiating a class in Python is simple. 
- To instantiate a class, we simply call the class as if it were a function.
- Remember: A class is a blueprint for how something should be defined 
- ... an instance is an object that is built from a class and contains real data.

## \_\_init__()

 - Built-in __init__() function
 - All classes have a function called __init__(), which is always executed when the class is being initiated.
 - The __init__() function is called automatically every time a new object is created, .__init__() sets the initial state of the object by assigning the values of the object’s properties.
 - Give .__init__() any number of parameters, but the first parameter will always be a variable called self.
 - When a new class instance is created, the instance is automatically passed to the self parameter in .__init__() so that new attributes can be defined on the object.

 ## Self
 - The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
 - It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

 ## Instance Methods / Behaviors
 - Instance methods are functions that are defined inside a class
 - Can only be called from an instance of that class
 - Just like .__init__(), an instance method’s first parameter is always self.

### Code Examples
---
```python
# ex1.0.1 
# >>> python -i Car()
# >>> help(Car)
"""
A class is a blueprint for the object with docstrings
"""
class Car:
    """
    Represents a car
    """
    pass

```

```python
# ex1.0.2 
"""
An object (instance) is an instantiation of a class.
Instantiating a class is creating a copy of the class which inherits all class variables and methods.
"""
class Car:
    pass

obj = Car()
print(Car())
# <__main__.Car object at 0x000001D3DD3FDFA0> Memory Address
```

```python
# ex1.0.3 
"""
Instantiating an object (highlighting the point that each instance is different)
"""
class Car:
    pass

obj1 = Car()
obj2 = Car()
x = obj1 == obj2
print(x)
print(obj1 is obj2)

```

```python
# ex1.0.4
"""
Adding attributes
"""
class Student:
    pass

obj1 = Student()
obj2 = Student()

obj1.x = 10
obj1.y = 20 

obj2.x = 40
obj2.y = 50

print(obj1.x, obj1.y)
print(obj2.x, obj2.y)

```

```python
"""
Class initialization method
"""
class Car:
  """
  Represents a car
  """
  smell = "good"

  def __init__(self, color, weight):
    self.color = color
    self.weight = weight

car1 = Car("red", 100)
car2 = Car("blue", 200)

print(car1.color, car1.weight)
print(car2.color, car2.weight)
```

```python
# ex1.0.5
"""
Class methods
Question: What if we forget self?
"""
class Car:
    def details(self):
        self.wheels = 4
        self.doors = 1

x = Car()
x.details()
print(x.wheels, x.doors)

```

```python
# ex1.0.5
"""
Passing arguments to a method
"""
class Car:
    def details(self, wheels: int, doors: int):
        self.wheels = wheels
        self.doors = doors

x = Car()
x.details(4,4)
print(x.wheels, x.doors)

```

```python
# ex1.0.6
"""
Class initialization method
"""
class Student:
    """
    Represents an instance of a student
    """
    
    # class attribute
    school = "Very Academy"

    # instance attribute
    def __init__(self, name, age, course):
        """
        Example
        """
        self.name = name
        self.age = age
        self.course = course

x = Student("Mike", 21, "Python")

print(x.school)
print(F"Student name: {x.name} age: {x.age}")
print(F"Current Course: {x.course}")

```

```python
# ex1.0.6
"""
Instance methods
"""
class Customer:
    """
    Represents an instance of a student
    """

    # instance attribute
    def __init__(self, customerName, address, email):
        self.name = customerName
        self.address = address
        self.email = email

    def customer_details(self):
        return f"{self.name}, {self.address}, {self.email}"

    def customer_payment(self, paymentCardNumber):
        return f"{self.name}, {paymentCardNumber}"


x = Customer("Mike", "1 new road", "m@m.com")
y = x.customer_payment("123124124124")
print(x.customer_details())
print(y)

```

```python
# ex1.0.7
"""
Outputting using the instance method __str__
"""
class Customer:

    # instance attribute
    def __init__(self, customerName, address, email):
        self.name = customerName
        self.address = address
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.address}, {self.email}"

x = Customer("Mike", "1 new road", "m@m.com")
print(x)

```
```python
# ex1.0.8

class Car:
  """
  Represents a blueprint for a car
  """

  def __init__(self, make: str, model: str, year: int, max_speed: int) -> None:
    """ Initialize car attributes """
    self.make = make
    self.model = model
    self.year = year
    self.max_speed = max_speed

    self.fuel_level = 0
    self.fuel_capacity = 100

  def __str__(self) -> str:
    return f"{self.make} {self.model} {self.year}"

  def drive_car(self) -> str:
    """ Control the cars movement """
    return f"The car is now moving"

  def calculate_fuel(self, distance: int) -> str:
    """ Calculate the current fuel based on distance travelled """
    return f"Current fuel: {self.fuel_level}"

  def add_fuel(self, amount: int) -> str:
    """ Add fuel to car """
    fuel_level = self.fuel_level + amount
    
    if fuel_level > self.fuel_capacity:
      return f"Fuel capacity reached"

    return f"New fuel level: {fuel_level}"
    

car1 = Car("audi", "A1", 2021, 160)
```
