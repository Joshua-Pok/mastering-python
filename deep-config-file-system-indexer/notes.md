<!--markdownlint-disable-->


# __init__.py

Tells python this directory is a package and that we can import from it, if not it is not importable


# Defensive I/O

Do not use a bare except or except Exception 

It hides bugs because we dont know what Exception
It slwallows system signals, if we ctrl c t o terminate, it interrupts our kill signal

**Always trap exactly what we expect to fail**

# .exteed()


adds items from one list one by one into another, so we dont end up with a list with other lists


# Naive Indexing


## File Reading

```python

with open(file_path, "r") as file:

    entire_contents = file.read()

    print()
```


with statement creates a context manager, it gurantees file will be closed automatically when we are done

.read() takes a single byte and dunps in to a string variable in ram


## UnicodeDecodeError


If we try to read a non text file, with text encoding(utf--8), python wont know how to translate errors and will throw a **UnicodeDecodeError**



# JSON Serialization and Deserialization


Python has a inbuilt json module for this

**json.dump()** saves our data to the file 


```Python

with open("index.json", "w") as f:
    json.dump(data, f)
```


we can also specify such that it has human readable indentation


```Python
json.dump(data, f, indent=2)
```


**json.load()** loads our data from the file


```Python

with open("index.json", "r") as f:
    data = json.load(f)
```




pickle is for serializing and deserializing into/from raw bytes


# ArgParse Library


Argparse is a library that allows us to take cli arguments. Argparse takes that list and organizes it into a neat, easily accessible object

## 3 Steps to using argparse

1) Initialize the parser
```Python

parser = argparse.ArgumentParser(description="A tool to do blah blah")
```


2) Define arguments

```Python

parser.add_argument("--input_file", help="the image file to process")

```


3) call parser.parse_args() to generate the args object


we can then access the arguments with args.<argumentname>


3) Optional: Add SubParsers

```Python

subparsers = parser.add_subparsers(dest="command", required = True)
# creates the switchboard, tells argparse to store name of command user picked inside args.command

parser_init = subparsers.add_parser('init', ...)
# create new parser to handle init 

# we can then add arguments to parser_init as per normal

```


arguments that start with "--" are treated as optional and we can provide default="" to provide a default value



