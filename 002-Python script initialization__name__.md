# Introducing Python Intermediate


## Topics:

* if \_\_name\_\_ == "\_\_main\_\_"


### Code Examples
---
```python
# ex1.0.1 Execute code at level 0 indentation

print("hello world")
```

```python
# ex1.0.2

#main
import sys
import login
print(sys.modules.keys())
print("main:module executed")

#login
import algorithms
print("login:module executed")

#algorithm
print("algorithm:library executed")
```
```python
# ex1.0.3

#main
import sys
import login
# print(sys.modules.keys())
print("main:module executed")
print(f"main-name:{__name__}")
print(globals())

#login
import algorithms
print("login:module executed")
print(f"login-name:{__name__}")

#algorithm
print("algorithm:library executed")
print(f"algorithm-name:{__name__}")
```
```python
# ex1.0.4

#main
import sys
import login

if __name__ == "__main__":
    print("# Main: Main Program")

#login
import algorithms

if __name__ == "__main__":
    print("# Login: Main Program")
else:
    print("# Login: Imported Module")

#algorithm
print("algorithm:library executed")
```

```python
# ex1.0.2 __Name__ Assignment
print(__name__)
```
```python
# ex1.0.3

print(f"{__name__}")

if __name__ == "__main__":
  print(f"Name:{__name__}")
```
```python
# ex1.0.4

def name():
  print(f"{__name__}")

if __name__ == "__main__":
  name()

# Whats the point...this works too!

def name():
  print(f"{__name__}")

name()

```
```python
# ex1.0.5

#f1
import f2

def name():
  print(f"{__name__}")

if __name__ == "__main__":
  name()

#f2
print(f"{__name__}")

```
```python
# ex1.0.6

#f1
import f2

def name():
  print(f"{__name__}")

if __name__ == "__main__":
  name()

#f2
if __name__ == "__main__":
  print(f"I am {__name__}")
else:
  print(f"I am {__name__}")
```
```python
# ex1.0.7

#f1
import f2

def main():
  print(f"f1 is the main program")
  print(f"f1:{__name__}")

if __name__ == "__main__":
  main()
else:
  print("f1 is an import")

#f2
def run_import_module():
  print(f"f2 is a importable module")
  print(f"f2:{__name__}")

def main():
  print(f"f2 is the main program")
  print(f"f2:{__name__}")

if __name__ == "__main__":
  main()
else:
  run_import_module()
```
```python
# ex1.0.8

#f1
from f2 import run_import_module

def main():
  print(f"f1 is the main program")
  print(f"f1:{__name__}")

  run_import_module()

if __name__ == "__main__":
  main()
else:
  print("f1 is an import")

#f2
def run_import_module():
  print(f"f2 is a importable module")
  print(f"f2:{__name__}")

def main():
  print(f"f2 is the main program")
  print(f"f2:{__name__}")

if __name__ == "__main__":
  main()
```