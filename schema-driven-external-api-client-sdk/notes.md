<!--markdownlint-disable-->


# Custom Exceptions

Domain Exceptions are custom error types we create to represent something that could go wrong within business logic

Instead of saying keyerror, which could mean alot of things, we can throw a **ExternalAPIResponseMalformed** error. This allow us to seperate the messy details of outside world from the clean logic of internal application


## How to create custom error

We creata a custom error by creating a class that inherits from python's **Exception** class. This makes our class catchable by try except

```python
class MyCustomError(Exception):
    pass
```



Good practice is to create a Base exception for our project, then have specific errors that inherit from that


## Catching and reraising

When we catch low level errors and raise them as higher level errors

```python
try:
    external_lib.fetch()
except ConnectionError as e:
    raise APIServerDownError("External service is unreachable") from err


```



# urllib.request

python's in built way of making requests

```python

response = urllib.request.urlopen("http://example.com/api/data")
raw_bytes = response.read()
text_data = raw_bytes.decode('utf-8')
```



# json
json.loads() parses a string text into a real python dictionary


payload_list = json.loads(text_data)
