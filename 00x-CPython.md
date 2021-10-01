# CPython
Introducing how Python is compiled

C:\> python -m py_complie x.py
 
Here we are calling the Python compiler with the  -m option. -m represents module and the module name is py_compile. This module generates the .pyc file for .py file. *.pyc file contains the byte code of the Python program. One can open and see the byte code representation of the python program. To convert byte code into machine code/output use:

```
C:\> python <nameofpycfile>.pyc
```

Here Python would skip the step of byte code generation and would convert byte code directly to machine code.

```
import dis # "dis" - Disassembler of Python byte code into mnemonics.
dis.dis('print("Hello, World!")')
```