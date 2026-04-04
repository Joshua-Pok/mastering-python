<!--markdownlint-disable-->


# __dict__ tax (dik tax)

In python, when we create objects, python allows us to attach new data to it at any time.

To allow for this flexibility, python backs every object with a hidden dictionary called **__dict__**
__dict__ s is a hashtable, and when we have many many objects, giving each one more memory than it needs will quickly consume our applications memory


# __slots__ 

__slots__ is python's solution to the dict tax. By defining slots, we tell python "I will only ever need this many attributes, do not allocate a dict for it"
Python responds by allocating a tiny, fixed sized array in memory just large enough to hold these specific pointers


# dataclasses module


While we can write __slots__ manuall, python 3.10+ provides a @dataclass decorator. It automatically generates initialization methods and automatically configures slots based on variables


```Python
from dataclasses import dataclass

@dataclass(slots=True)
class ServerRecord:
    ip_address: str 
    metadata: dict


    node = ServerRecord(...)
```

Because we used dataclass, __init__ was automatically written for us



When we try to add a unspecified attribute,

```Python

node.last_reboot = "yesterday"
```
**Python will throw an AttributeError**


# sys.getsizeof

Python sys module provides access to variables and functions that interact strongly with the interpreter.

getsizeof() returns the size of an object in bytes


# Shallow vs Deep Memory

sys.getSizeof() calculates shallow size, meaning it completely ignores the dict attached to it


we have to do
```Python

sys.getsizeof(node) + sys.getsizeof(node.__dict__)
```

to get the accurate size of the enire obejct


# Python Data Model

Python has a philosophy: Devs should not need to learn custom vocab to interact with specific objects.

To achieve this, python uses a system called the DataModel, relying heavily on "dunder" methods __ __ methods
Think of dunder methods as universal adapters, when we write len(my_obj), python dosent actually know how to do it, instead, it looks inside your class for a method specifically called __len__


## Native Protocols

To make an object behave like a dictionary

### Container Protoccol

lets us use **in** to check for existence (__contains__)

### Sized Protocol 

lets us use **len()** to get count (__len__)

### Iterable Protoccol 

lets us use **for x in ...** to loop over it (__iter__)

### Mapping Protoccol

lets us use **[]** to get and set items (__getitem__) and (__setitem__)

## THread Safety

Assume python dicts are thread unsafe by deafult
 we need to add a lock with threading.lock()



# Yield keyword 






