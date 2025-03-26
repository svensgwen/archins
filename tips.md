# Tips for Python Pro Coding

The line
```py
def function(self) -> None:
```
- Defines a method named function, which belongs to a class (since it has self as the first parameter).
- None → This is a type hint that indicates the function does not return any value.

## @staticmethod
@staticmethod in Python
The @staticmethod decorator is used in Python to define a method inside a class that does not require access to instance (self) or class (cls) variables.

🚀 Key Features of @staticmethod:

✅ No self or cls required (does not access instance or class attributes).

✅ Can be called directly on the class without creating an instance.

✅ Behaves like a regular function but inside a class (used for utility/helper functions).