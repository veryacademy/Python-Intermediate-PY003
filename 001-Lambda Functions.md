# Introducing Python Intermediate
A lambda function is a small anonymous function.

## Topics:

* Anonymous and function comparison
* Named functions
* Multiple bound arguments
* Map, Filter, Reduce

### Code Examples
---
```python
# ex1.0.1 Anonymous and function comparison
# def is short for "define"
def name(x):
    y = x + 1
    return y
print (name(2))

(lambda x: x + 1)(2)
```
```python
# ex1.0.2 Named function
x = lambda y : y + 100
print(x(100))
```
```python
# ex1.0.3 Multiple bound arguments
x = lambda y, z : y + z
print(x(100, 100))

new = lambda x, y, z : x + y + z
print(new(100, 100, 100))
```
```python
# ex1.0.4 Arguments
## Positional
## Named
## Variable list of arguments
## Variable list of keyword arguments
x = lambda x, y, z: x + y + z
print(x(1,2,3))

x = lambda x, y, z=1: x + y + z
print(x(3,2))

x = lambda x, y, z=3: x + y + z
print(x(1,y=2))

x = lambda *args: sum(args)
print(x(1,2,3,4,5,6))

x = lambda **kwargs: sum(kwargs.values())
print(x(a=1, b=2, c=3))
```
```python 
# ex1.0.4 Lambda with map()
items = [1,2,3]

def square(number):
    return number ** 2

squared = map(square, items)

print(list(squared))


items = [1,2,3]
x = list(map(lambda x: x**2, items))
print(x)
```
```python
# ex1.0.5 Lambda with map() 
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

print(squared)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

print(squared)
```
```python
# ex1.0.5 filter()
items = [1, 2, 3, 4, 5, 6, 7,8]
x = list(filter(lambda x: x % 2 == 0, items))
print(x)
```
```python 
import functools
# ex1.0.6 reduce
x = functools.reduce(lambda x, y: x+y, range(1,11))
print(x)
```
```python 
import functools

items = [1002,48,981,305,20]
x = functools.reduce(lambda a,b: a if (a > b) else b, items)

print(x)
```

## 001 Code Challenges
---
x

### **Challenge 1 - x**

### Solutions
---
```Python
```