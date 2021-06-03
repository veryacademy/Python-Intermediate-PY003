# Introducing Python Intermediate
A lambda function is a small anonymous function.

## Topics:

* Lambda functions

### Code Examples
---
```python
x = lambda y : y + 100
print(x(100))
```
```python
x = lambda y, z : y + z
print(x(100, 100))
```
```python
new = lambda x, y, z : x + y + z
print(new(100, 100, 100))
```




```python
# Interpreter - anonymous
(lambda x: x + 1)(2)
```

```python
# Using with Map
items = [1,2,3]
x = list(map(lambda x: x, items))
print(x)
```

```python
# Using with Map compared to for
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

print(squared)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

print(squared)
```



## 001 Code Challenges
---
Use the previous code examples to help you complete the code challenges

### **Challenge 1 - x**


### Solutions
---

```Python
```