<!-- 
1. ### Difference between tuple and dictionary.
2. ### Difference between tuple and set.
3. ### Difference between map() and filter().
4. ### Difference between range() and xrange()
5. ### Difference between int() and eval().
6. ### Difference between append() and extend()
7. ### Difference between input() and raw_input() (Python 2).
8. ### Difference between `for` Loop and `while` Loop
9. ### Difference between remove() and pop().
10. ### Difference between sorted() and sort().
11. ### Difference between split() and partition().
12. ### Difference between find() and index().
13. ### Difference between upper() and capitalize().
14. ### Difference between function overloading and function overriding.
15. ### Difference between method overloading and method overriding.
16. ### Difference between normal function and lambda function.
17. ### Difference between a function and a generator.
18. ### Difference between generator and iterator.
19. ### Difference between yield and return.
20. ### Difference between static methods and class methods.
21. ### Difference between static methods and instance methods.
22. ### Difference between getattr() and setattr().
23. ### Difference between `map()` and `filter()`
24. ### Difference between `update()` and `union()` in Sets
25. ### Difference between `intersection()` and `difference()` in Sets
26. ### Difference between `frozenset` and `set`
27. ### Difference between `remove()` and `discard()` in Sets
28. ### Difference between Keyword Arguments and Positional Arguments
29. ### Difference between `*args` and `**kwargs`
30. ### Difference between Global and Local Variables
31. ### Difference between global scope and local scope.
32. ### Difference between Shallow Copy and Deep Copy
33. ### Difference Between Class Variable and Instance Variable
34. ### Difference Between Class Method and Static Method -->



1. [Difference between tuple and dictionary](#difference-between-tuple-and-dictionary)
2. [Difference between tuple and set](#difference-between-tuple-and-set)
3. [Difference between map() and filter()](#difference-between-map-and-filter)
4. [Difference between range() and xrange()](#difference-between-range-and-xrange)
5. [Difference between int() and eval()](#difference-between-int-and-eval)
6. [Difference between append() and extend()](#difference-between-append-and-extend)
7. [Difference between input() and raw_input() (Python 2)](#difference-between-input-and-raw_input-python-2)
8. [Difference between `for` Loop and `while` Loop](#difference-between-for-loop-and-while-loop)
9. [Difference between remove() and pop()](#difference-between-remove-and-pop)
10. [Difference between sorted() and sort()](#difference-between-sorted-and-sort)
11. [Difference between split() and partition()](#difference-between-split-and-partition)
12. [Difference between find() and index()](#difference-between-find-and-index)
13. [Difference between upper() and capitalize()](#difference-between-upper-and-capitalize)
14. [Difference between function overloading and function overriding](#difference-between-function-overloading-and-function-overriding)
15. [Difference between method overloading and method overriding](#difference-between-method-overloading-and-method-overriding)
16. [Difference between normal function and lambda function](#difference-between-normal-function-and-lambda-function)
17. [Difference between a function and a generator](#difference-between-a-function-and-a-generator)
18. [Difference between generator and iterator](#difference-between-generator-and-iterator)
19. [Difference between yield and return](#difference-between-yield-and-return)
20. [Difference between static methods and class methods](#difference-between-static-methods-and-class-methods)
21. [Difference between static methods and instance methods](#difference-between-static-methods-and-instance-methods)
22. [Difference between getattr() and setattr()](#difference-between-getattr-and-setattr)
23. [Difference between map() and filter()](#difference-between-map-and-filter-1)
24. [Difference between update() and union() in Sets](#difference-between-update-and-union-in-sets)
25. [Difference between intersection() and difference() in Sets](#difference-between-intersection-and-difference-in-sets)
26. [Difference between frozenset and set](#difference-between-frozenset-and-set)
27. [Difference between remove() and discard() in Sets](#difference-between-remove-and-discard-in-sets)
28. [Difference between Keyword Arguments and Positional Arguments](#difference-between-keyword-arguments-and-positional-arguments)
29. [Difference between *args and **kwargs](#difference-between-args-and-kwargs)
30. [Difference between Global and Local Variables](#difference-between-global-and-local-variables)
31. [Difference between global scope and local scope](#difference-between-global-scope-and-local-scope)
32. [Difference between Shallow Copy and Deep Copy](#difference-between-shallow-copy-and-deep-copy)
33. [Difference Between Class Variable and Instance Variable](#difference-between-class-variable-and-instance-variable)
34. [Difference Between Class Method and Static Method](#difference-between-class-method-and-static-method)





1. ### Difference between tuple and dictionary.

| **Feature**         | **Tuple**                                      | **Dictionary**                              |
|---------------------|----------------------------------------------|-------------------------------------------|
| **Definition**      | An **ordered** collection of elements        | A collection of **key-value** pairs      |
| **Mutable?**       | **Immutable** (cannot be modified)           | **Mutable** (can add, update, and delete items) |
| **Syntax**         | `()` (parentheses)                           | `{}` (curly braces)                      |
| **Accessing Elements** | Accessed using **indexing** (e.g., `t[0]`) | Accessed using **keys** (e.g., `d['key']`) |
| **Duplicates Allowed?** | Yes (can contain duplicate values)        | No (keys must be unique)                 |
| **Performance**     | Faster due to immutability                  | Slightly slower due to key hashing       |
| **Use Case**       | Storing **fixed** collections of values      | Storing **mapped relationships**         |

2. ### Difference between tuple and set.
| **Feature**         | **Tuple**                                  | **Set**                                 |
|---------------------|------------------------------------------|----------------------------------------|
| **Definition**      | An **ordered** collection of elements   | An **unordered** collection of unique elements |
| **Mutable?**       | **Immutable** (cannot be modified)      | **Mutable** (can add/remove elements) |
| **Syntax**         | `()` (parentheses)                      | `{}` (curly braces)                   |
| **Duplicates Allowed?** | Yes (can contain duplicate values) | No (duplicates are automatically removed) |
| **Accessing Elements** | Accessed using **indexing** (e.g., `t[0]`) | No indexing (unordered structure) |
| **Ordering**       | Maintains insertion order              | Does not maintain order (unordered) |
| **Performance**    | Faster for **fixed** data retrieval    | Faster for **membership testing** (`O(1)`) |
| **Use Case**       | Storing **fixed sequences** of values  | Storing **unique elements** for fast lookup |

3. ###  Difference between map() and filter().
| **Feature**       | **`map()`**                                      | **`filter()`**                              |
|-------------------|-------------------------------------------------|--------------------------------------------|
| **Purpose**       | Applies a function to **each element** of an iterable | Filters elements based on a **condition** |
| **Return Type**   | Returns a **map object** (can be converted to list, tuple, etc.) | Returns a **filter object** (iterable) |
| **Number of Elements in Output** | Same as input iterable | Less than or equal to input iterable (only elements that satisfy the condition) |
| **Function Type** | Uses a **transformation function** | Uses a **Boolean function** (returns `True` or `False`) |
| **Syntax**        | `map(function, iterable)` | `filter(function, iterable)` |
| **Example Usage** | `map(lambda x: x * 2, [1, 2, 3])  → [2, 4, 6]` | `filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  → [2, 4]` |
| **Use Case**      | When you need to **modify** all elements | When you need to **filter out** elements based on a condition |

4. ### Difference between range() and xrange().
| **Feature**         | **`range()`** (Python 3 & 2)           | **`xrange()`** (Python 2 Only)          |
|---------------------|---------------------------------|---------------------------------|
| **Availability**    | Available in **Python 3 & 2**   | Available **only in Python 2** (Not in Python 3) |
| **Return Type**     | Returns a **range object** (lazy evaluation in Python 3) | Returns an **xrange object** (generator-like) |
| **Memory Usage**    | Efficient in **Python 3** (lazy evaluation) but **creates a list in Python 2** | More memory efficient (does not create a list) |
| **Performance**     | Efficient in **Python 3**, but slower in **Python 2** (since it creates a list) | Faster in Python 2 (due to lazy evaluation) |
| **Iteration**       | Can be iterated multiple times | Can only be iterated once (like a generator) |
| **Syntax**         | `range(start, stop, step)` | `xrange(start, stop, step)` |

5. ### Difference between int() and eval().

| **Feature**       | **`int()`**                                      | **`eval()`**                                 |
|-------------------|-------------------------------------------------|---------------------------------------------|
| **Purpose**       | Converts a value to an **integer**               | Evaluates an **expression** as Python code |
| **Input Type**    | Works with **strings** and **numbers**           | Works with **strings containing expressions** |
| **Return Type**   | Returns an **integer** (`int`)                   | Returns **any data type** (depends on the expression) |
| **Usage**         | `int("10") → 10`                                | `eval("10 + 5") → 15` |
| **Security**      | **Safe** (Only converts to integers)             | **Unsafe** (Can execute arbitrary code, potential security risk) |
| **Use Case**      | When you need to convert **strings to integers** | When you need to evaluate **mathematical expressions** dynamically |


6. ### Difference between append() and extend().
| **Feature**       | **`append()`**                                  | **`extend()`**                                |
|-------------------|-----------------------------------------------|---------------------------------------------|
| **Purpose**       | Adds a **single element** to the list         | Adds **multiple elements** (iterable) to the list |
| **Modification**  | Adds the element as **a single item**         | Iterates through the iterable and **adds elements individually** |
| **Return Type**   | **Modifies the list in place**, returns `None` | **Modifies the list in place**, returns `None` |
| **Effect on List Length** | Increases by **1** regardless of element type | Increases by the **number of elements in the iterable** |
| **Usage**         | `list.append([1, 2]) → [[1, 2]]` (Nested list) | `list.extend([1, 2]) → [1, 2]` (Flattened) |
| **Use Case**      | When you want to add **one item** (including another list as a single element) | When you want to **merge another list or iterable** into the existing list |

Example
```python
# Using append()
my_list = [1, 2, 3]
my_list.append([4, 5])
print(my_list)  # Output: [1, 2, 3, [4, 5]]  (Nested list)

# Using extend()
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]  (Flattened list)

```

7. ### Difference between input() and raw_input() (Python 2).

| **Feature**       | **`input()` (Python 2 & 3)**                 | **`raw_input()` (Python 2 Only)**        |
|-------------------|-------------------------------------------|---------------------------------------|
| **Availability**  | Available in **Python 2 & 3**              | Available **only in Python 2** (Removed in Python 3) |
| **Return Type**   | **Evaluates input as Python expression**  | **Always returns input as a string** |
| **Usage**         | `input("Enter: ")` → If user enters `10`, returns `10` (int) | `raw_input("Enter: ")` → Always returns `'10'` (string) |
| **Security**      | **Unsafe** (Can execute arbitrary code)    | **Safe** (Treats all input as a string) |
| **Python 3 Equivalent** | `input()` is safe and behaves like `raw_input()` | Removed in Python 3 |

### Example
Example Usage in Python 2:
```python
# Using input() in Python 2
num = input("Enter a number: ")  # If user enters 10, it is treated as an integer (10)

# Using raw_input() in Python 2
text = raw_input("Enter text: ")  # If user enters 10, it is treated as a string ('10')
```
### Key Takeaways:
* **In Python 2:**

* input() evaluates the input (can be unsafe).

* raw_input() always returns a string.

* **In Python 3:**

* raw_input() was removed, and input() behaves like raw_input() in Python 2 (always returns a string).


8. ### Difference between `for` Loop and `while` Loop

```markdown
| **Feature**      | **`for` Loop**                                    | **`while` Loop**                                |
|-----------------|------------------------------------------------|------------------------------------------------|
| **Definition**  | Used for iterating over a sequence (list, tuple, string, range, etc.). | Used for executing a block of code repeatedly while a condition is true. |
| **Control Mechanism** | Controlled by an iterable (like a list or range). | Controlled by a condition (evaluates to True or False). |
| **Use Case**    | When the number of iterations is known in advance. | When the number of iterations is unknown and depends on a condition. |
| **Termination** | Terminates after the iterable is exhausted. | Terminates when the condition becomes False. |
| **Readability** | More readable for sequential iteration. | Better for condition-based loops. |
| **Example**     | `for i in range(5): print(i)` | `while i < 5: print(i); i += 1` |
```

### **Example Usage**

#### **Using `for` Loop**
```python
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
```

#### **Using `while` Loop**
```python
i = 0
while i < 5:
    print(i)
    i += 1
# Output:
# 0
# 1
# 2
# 3
# 4
```

### **Key Takeaways:**
- **Use `for` loops** when iterating over a sequence or when the number of iterations is known.
- **Use `while` loops** when looping depends on a condition rather than a fixed count.
- **`for` loops** are generally more readable and commonly used for iteration.
- **`while` loops** provide more flexibility when the loop termination condition is dynamic.

9. ###  Difference between remove() and pop().
| **Feature**       | **`remove()`**                              | **`pop()`**                               |
|-------------------|-------------------------------------------|-----------------------------------------|
| **Purpose**       | Removes a **specific value** from the list | Removes an **element by index** and returns it |
| **Arguments**     | Takes **a value** as an argument           | Takes an **index** as an argument (default: last element) |
| **Return Value**  | Returns `None` (modifies the list in place) | Returns the removed element |
| **Error Handling** | Raises `ValueError` if the value is not found | Raises `IndexError` if the index is out of range |
| **Usage**         | `list.remove(3)` (removes first occurrence of `3`) | `list.pop(2)` (removes and returns element at index `2`) |
| **Effect on List** | Shrinks list by **removing the first occurrence** of the value | Shrinks list by **removing an element at a specific position** |


#### Example Usage:
```python
# Using remove()
my_list = [1, 2, 3, 4, 3]
my_list.remove(3)  # Removes the first occurrence of 3
print(my_list)  # Output: [1, 2, 4, 3]

# Using pop()
my_list = [1, 2, 3, 4]
removed_item = my_list.pop(2)  # Removes and returns element at index 2
print(my_list)  # Output: [1, 2, 4]
print(removed_item)  # Output: 3

```
#### Key Takeaways:
* remove() removes a value (first occurrence).

* pop() removes an element at a specific index and returns it.

* remove() raises an error if the value is not found.

* pop() raises an error if the index is out of range


10. ### Difference between sorted() and sort().
| **Feature**       | **`sorted()`**                              | **`sort()`**                              |
|-------------------|-------------------------------------------|-----------------------------------------|
| **Purpose**       | Returns a **new sorted list** (does not modify original) | Sorts the list **in place** (modifies original list) |
| **Return Type**   | Returns a **new list**                     | Returns `None` (modifies the list directly) |
| **Mutability**    | **Does not change** the original list       | **Changes** the original list |
| **Works on?**     | Works on **any iterable** (list, tuple, dict keys, etc.) | Works **only on lists** |
| **Syntax**        | `sorted(iterable, key=None, reverse=False)` | `list.sort(key=None, reverse=False)` |
| **Example Usage** | `new_list = sorted(my_list)`               | `my_list.sort()` |
| **Use Case**      | When you need a **sorted copy** of data     | When you want to **sort an existing list** without creating a new one |

#### Example Usage:
```python
# Using sorted() (creates a new sorted list)
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)
print(numbers)  # Output: [3, 1, 4, 1, 5] (original remains unchanged)
print(sorted_numbers)  # Output: [1, 1, 3, 4, 5] (new sorted list)

# Using sort() (modifies the original list)
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5] (sorted in place)

```

#### Key Takeaways:
* sorted() creates a new sorted list (original remains unchanged).

* sort() modifies the list in place (no new list is created).

* sorted() works on any iterable, but sort() only works on lists.

* Use sorted() when you need a copy, and sort() when you want to modify the original list.


11. ### Difference between split() and partition().

| **Feature**       | **`split()`**                              | **`partition()`**                        |
|-------------------|------------------------------------------|-----------------------------------------|
| **Purpose**       | Splits a string into a **list of substrings** | Splits a string into **three parts**: before, separator, and after |
| **Return Type**   | Returns a **list** of substrings         | Returns a **tuple** (`before, separator, after`) |
| **Arguments**     | `split(separator, maxsplit)` (default separator: whitespace) | `partition(separator)` (only one split at first occurrence) |
| **Max Splits?**   | Yes, you can limit splits using `maxsplit` | No, always splits at **first occurrence** of separator |
| **If Separator Not Found?** | Returns **entire string as a list** | Returns `('original_string', '', '')` |
| **Example Usage** | `"a,b,c".split(',') → ['a', 'b', 'c']`  | `"a,b,c".partition(',') → ('a', ',', 'b,c')` |
| **Use Case**      | When you need to **break a string into multiple parts** | When you need to **extract text around the first occurrence** of a separator |


Example Usage:
```python
# Using split()
text = "apple,banana,cherry"
result = text.split(",")
print(result)  # Output: ['apple', 'banana', 'cherry']

# Using partition()
text = "apple,banana,cherry"
result = text.partition(",")
print(result)  # Output: ('apple', ',', 'banana,cherry')

```
**Key Takeaways:**
* split() breaks a string into multiple parts and returns a list.

* partition() splits only at the first occurrence and returns a tuple.

* If the separator is not found, split() returns the whole string as a list, while partition() returns the whole string as the first tuple element, followed by two empty strings.

12. ### Difference between find() and index().
| **Feature**       | **`find()`**                              | **`index()`**                             |
|-------------------|-----------------------------------------|-----------------------------------------|
| **Purpose**       | Returns the **index of the first occurrence** of a substring | Returns the **index of the first occurrence** of a substring |
| **Return Type**   | Returns **index** if found, otherwise `-1` | Returns **index** if found, otherwise raises `ValueError` |
| **Error Handling** | Does **not raise an error** if substring is not found | **Raises an error** if substring is not found |
| **Usage**         | `string.find("sub")` | `string.index("sub")` |
| **Performance**   | Both have **similar performance** | Both have **similar performance** |
| **Use Case**      | When you **don't want errors** and just need the index or `-1` | When the substring **must exist**, otherwise an error should occur |

#### Example Usage
```python
# Using find()
text = "hello world"
print(text.find("world"))  # Output: 6
print(text.find("Python"))  # Output: -1 (No error)

# Using index()
print(text.index("world"))  # Output: 6
print(text.index("Python"))  # Raises ValueError: substring not found
```
**Key Takeaways:**
* find() returns -1 if the substring is not found, making it safer.

* index() raises an error (ValueError) if the substring is not found.

* Use find() when checking if a substring exists without errors.

* Use index() when you are sure the substring exists and want an error if it doesn’t.


13. ### Difference between upper() and capitalize().
| **Feature**       | **`upper()`**                              | **`capitalize()`**                        |
|-------------------|------------------------------------------|-----------------------------------------|
| **Purpose**       | Converts **all characters** to uppercase | Converts **only the first character** to uppercase and the rest to lowercase |
| **Return Type**   | Returns a **new string** with all uppercase characters | Returns a **new string** with only the first letter capitalized |
| **Modification**  | Affects **entire string**                | Affects **only the first letter** of the string |
| **Example Usage** | `"hello world".upper() → "HELLO WORLD"`  | `"hello world".capitalize() → "Hello world"` |
| **Use Case**      | When you need a string in **all uppercase** | When you need to **capitalize only the first letter** of a sentence |


#### Example usage:
```python
# Using upper()
text = "hello world"
print(text.upper())  # Output: "HELLO WORLD"

# Using capitalize()
text = "hello world"
print(text.capitalize())  # Output: "Hello world"
```
**Key Takeaways:**
* upper() converts all characters to uppercase.

* capitalize() converts only the first character to uppercase and makes the rest lowercase.

* Use upper() when you need all uppercase text.

* Use capitalize() when you need only the first letter capitalized (like in a sentence).

---

## Intermediate level
| **Feature**       | **`global`**                            | **`nonlocal`**                          |
|-------------------|--------------------------------------|--------------------------------------|
| **Purpose**       | Declares a variable as **global**, meaning it belongs to the global scope | Declares a variable as **nonlocal**, meaning it belongs to an enclosing (but not global) scope |
| **Scope**         | Affects **global variables** across the entire script | Affects **variables in an enclosing function (not global scope)** |
| **Where to Use?** | Inside functions to modify a global variable | Inside nested functions to modify a variable from the outer (non-global) function |
| **Example Usage** | `global x` (Modifies `x` from global scope inside a function) | `nonlocal x` (Modifies `x` from an outer but non-global function) |
| **Works In?**     | **Any function** modifying a global variable | **Nested functions** modifying a variable from the enclosing function |
| **Error Handling** | Raises `UnboundLocalError` if a global variable is accessed before assignment | Raises `SyntaxError` if used outside a nested function |

## Example Usage:
```python
# Using global
x = 10  # Global variable

def modify_global():
    global x  # Declaring x as global
    x = 20  # Modifies the global variable

modify_global()
print(x)  # Output: 20

# Using nonlocal
def outer_function():
    y = 5  # Local variable in outer function

    def inner_function():
        nonlocal y  # Declaring y as nonlocal
        y = 15  # Modifies y from the outer function

    inner_function()
    print(y)  # Output: 15

outer_function()

```

**Key Takeaways:**
* global is used to modify global variables inside a function.

* nonlocal is used to modify variables from an enclosing function (but not global variables).

* global works anywhere inside a function, while nonlocal works only in nested functions.

* global affects global scope, while nonlocal affects enclosing function scope.

14. ###  Difference between function overloading and function overriding.
| **Feature**           | **Function Overloading**                          | **Function Overriding**                         |
|----------------------|------------------------------------------------|------------------------------------------------|
| **Definition**       | Defining multiple functions with the **same name** but **different parameters** | Redefining a method in a **child class** that is already defined in the **parent class** |
| **Method Resolution** | Determined at **compile-time** (in languages that support it) | Determined at **runtime** (dynamic method dispatch) |
| **Support in Python?** | **Not directly supported** (can be simulated using default arguments or `*args`) | **Fully supported** using **inheritance** |
| **Where It Is Used?** | **Same class** (methods have different signatures) | **Between parent and child class** (same method signature) |
| **Parameters**        | **Different** number/types of parameters | **Same** number and types of parameters |
| **Example Usage**     | `def add(a, b)` and `def add(a, b, c)` (not directly supported in Python) | Overriding `def show()` in a subclass that already exists in the parent class |

### Example Usage:
Function Overloading (Simulated in Python)
Python does not support function overloading directly, but it can be simulated using default arguments or *args:

```python
class MathOperations:
    def add(self, a, b, c=0):  # Simulating overloading using default parameters
        return a + b + c

math = MathOperations()
print(math.add(2, 3))      # Output: 5
print(math.add(2, 3, 4))   # Output: 9
```
**Function Overriding (Supported in Python)**
```python
class Parent:
    def show(self):
        print("This is the parent class method.")

class Child(Parent):
    def show(self):  # Overriding the parent class method
        print("This is the child class method.")

obj = Child()
obj.show()  # Output: "This is the child class method." (Parent's method is overridden)

```

**Key Takeaways:**
* Function Overloading → Same function name, different parameters (Python does not support it directly).

* Function Overriding → Same function name, same parameters, different classes (Supported using inheritance).

* Overloading is resolved at compile-time in some languages, while Overriding is resolved at runtime.

* Use default arguments or *args to simulate overloading in Python.

---



15. ### Difference between method overloading and method overriding.
| **Feature**           | **Method Overloading**                          | **Method Overriding**                         |
|----------------------|------------------------------------------------|------------------------------------------------|
| **Definition**       | Defining multiple methods with the **same name** but **different parameters** in the **same class** | Redefining a method in a **child class** that is already defined in the **parent class** |
| **Method Resolution** | Determined at **compile-time** (in languages that support it) | Determined at **runtime** (dynamic method dispatch) |
| **Support in Python?** | **Not directly supported** (can be simulated using default arguments or `*args`) | **Fully supported** using **inheritance** |
| **Where It Is Used?** | **Within the same class** | **Between parent and child class** |
| **Parameters**        | **Different** number/types of parameters | **Same** number and types of parameters |
| **Example Usage**     | `def add(a, b)` and `def add(a, b, c)` (not directly supported in Python) | Overriding `def show()` in a subclass that already exists in the parent class |


### Example Usage:
**Method Overloading (Simulated in Python)**
Python does not support method overloading directly, but it can be simulated using default arguments or *args:

```python
class MathOperations:
    def add(self, a, b, c=0):  # Simulating overloading using default parameters
        return a + b + c

math = MathOperations()
print(math.add(2, 3))      # Output: 5
print(math.add(2, 3, 4))   # Output: 9

```

**Method Overriding (Supported in Python)**
```python
class Parent:
    def show(self):
        print("This is the parent class method.")

class Child(Parent):
    def show(self):  # Overriding the parent class method
        print("This is the child class method.")

obj = Child()
obj.show()  # Output: "This is the child class method." (Parent's method is overridden)

```
**Key Takeaways:**
Method Overloading → Same method name, different parameters (Python does not support it directly).

Method Overriding → Same method name, same parameters, different classes (Supported using inheritance).

Overloading is resolved at compile-time in some languages, while Overriding is resolved at runtime.

Use default arguments or *args to simulate overloading in Python.

16. ### Difference between normal function and lambda function.
| **Feature**        | **Normal Function**                            | **Lambda Function**                        |
|-------------------|--------------------------------------------|-----------------------------------------|
| **Definition**    | Defined using the `def` keyword           | Defined using the `lambda` keyword     |
| **Syntax**        | Multi-line, with a function name and `return` statement | Single-line, anonymous function |
| **Function Name** | Has an explicit name (e.g., `def add()`)  | Anonymous (does not have a name unless assigned) |
| **Complexity**    | Supports multiple statements and logic    | Limited to a single expression |
| **Return Value**  | Uses `return` explicitly                  | Returns the result **implicitly** |
| **Use Case**      | Used for **complex operations** with multiple statements | Used for **short, simple operations** |
| **Readability**   | More readable for larger functions       | Less readable for complex expressions |
| **Example Usage** | `def square(x): return x * x`            | `lambda x: x * x` |


### Example Usage:
**Normal Function:**
```python
def square(x):
    return x * x

print(square(5))  # Output: 25

```
**Lambda Function:**
```python
square = lambda x: x * x
print(square(5))  # Output: 25

```
**Key Takeaways:**
Normal functions → Used for larger, multi-line logic.

Lambda functions → Used for short, simple operations (often inside map(), filter(), etc.).

Lambda functions return values implicitly, while normal functions use an explicit return.

Lambda functions are anonymous, meaning they don’t have a name unless assigned


17. ### Difference between a function and a generator.
| **Feature**         | **Function**                                 | **Generator**                             |
|--------------------|-------------------------------------------|-----------------------------------------|
| **Definition**     | A block of code that performs a task when called | A special function that yields values lazily using `yield` |
| **Keyword Used**   | Uses `return` to return a value           | Uses `yield` to produce values lazily |
| **Execution**      | Executes all at once                      | Executes **lazily** (one value at a time) |
| **Memory Usage**   | Stores all values in memory               | Uses **less memory** (stores only the current value) |
| **Iteration**      | Must be called explicitly                 | Can be iterated using `for` or `next()` |
| **State Retention** | Does **not** retain state between calls  | **Retains state** between iterations |
| **Use Case**       | When results are needed all at once       | When working with **large data** or **infinite sequences** |
| **Example Usage**  | `def func(): return [1,2,3]`              | `def gen(): yield 1; yield 2; yield 3` |

### Example Usage:
**Normal Function (Returns a List All at Once)**
```python
def normal_function():
    return [1, 2, 3]  # Returns all values at once

print(normal_function())  # Output: [1, 2, 3]
```
**Generator (Yields Values One by One)**
```python

def generator_function():
    yield 1
    yield 2
    yield 3  # Yields values lazily

gen = generator_function()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
```

**Key Takeaways:**

* Functions return all values at once, while Generators produce values one at a time using yield.

* Generators use less memory because they do not store all values at once.

* Generators retain state, meaning execution resumes from where it was last paused.

* Use functions for small data and generators for large/infinite data (like reading large files).

18. ###  Difference between generator and iterator.
| **Feature**        | **Generator**                                  | **Iterator**                                |
|-------------------|----------------------------------------------|------------------------------------------|
| **Definition**    | A special type of iterator that yields values using `yield` | Any object that implements `__iter__()` and `__next__()` |
| **How It’s Created?** | Created using a **function** with `yield` | Created using a **class** with `__iter__()` and `__next__()` |
| **State Retention** | **Automatically retains** state between calls | Must **manually maintain** state |
| **Memory Usage**   | More memory-efficient (yields values lazily) | May store all values in memory |
| **Implementation Complexity** | Easier to create (just define a function with `yield`) | Requires defining a class with `__iter__()` and `__next__()` |
| **Usage**         | Used when dealing with **large/infinite sequences** | Used when working with any iterable object |
| **Example Usage** | `def gen(): yield x` (function with `yield`) | Custom class implementing `__iter__()` and `__next__()` |


### Example Usage:
**Generator Example (Simpler and Memory Efficient)**
```python
def generator_function():
    yield 1
    yield 2
    yield 3  # Yields values lazily

gen = generator_function()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
```
**Iterator Example (Manually Defined Class)**
```python
class MyIterator:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > 3:
            raise StopIteration
        value = self.num
        self.num += 1
        return value

it = MyIterator()
print(next(it))  # Output: 1
print(next(it))  # Output: 2
print(next(it))  # Output: 3
```
### Key Takeaways:
* Generators are a type of iterator but are easier to create using yield.

* Generators automatically handle state, whereas iterators must maintain state manually.

* Generators are memory-efficient (produce values lazily), while iterators may store values.

* Use generators for large/infinite sequences and iterators for custom iteration logic.

19. ### Difference between yield and return.
| **Feature**        | **yield**                                    | **return**                              |
|-------------------|--------------------------------------------|--------------------------------------|
| **Definition**    | Pauses function execution and returns a value, but allows resumption later | Terminates function execution and returns a value |
| **Function Type** | Used in **generator functions**            | Used in **normal functions**       |
| **Memory Usage**  | **Memory-efficient** (does not store all values at once) | Stores the entire result in memory |
| **Execution Flow** | Function **suspends** at `yield` and resumes from the same point when called again | Function **ends immediately** when `return` is encountered |
| **Number of Returns** | Can return multiple values one at a time (using `next()`) | Returns a **single value** and exits |
| **State Retention** | **Retains function state** between calls | **Does not retain state** after returning |
| **Use Case**      | Used for **large datasets**, **infinite sequences**, and **lazy iteration** | Used when all values need to be returned at once |
| **Example Usage** | `def gen(): yield x` (generator function) | `def func(): return x` (normal function) |

### Example Usage:
Using return in a Normal Function (Returns All at Once)
```python
def normal_function():
    return [1, 2, 3]  # Returns all values at once

print(normal_function())  # Output: [1, 2, 3]
Using yield in a Generator (Returns One Value at a Time)
```
```python
def generator_function():
    yield 1
    yield 2
    yield 3  # Yields values lazily

gen = generator_function()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
```
### Key Takeaways:
* yield → Used in generators, allows lazy iteration, retains function state.

* return → Used in normal functions, returns once, and does not retain state.

* Generators (yield) use less memory, while functions (return) store all values at once.

* Use yield for large/infinite sequences and return for single results.

20. ### Difference between static methods and class methods.
| **Feature**            | **Static Method**                                  | **Class Method**                                |
|-----------------------|---------------------------------------------------|------------------------------------------------|
| **Definition**         | A method that doesn't take `self` or `cls` as the first argument. It's bound to the class but does not operate on instance or class variables. | A method that takes `cls` (the class itself) as the first argument, which allows access to class-level variables and methods. |
| **Syntax**             | Defined using `@staticmethod` decorator.         | Defined using `@classmethod` decorator.         |
| **Access**             | Can access **only** arguments passed to the method. It cannot access instance or class attributes. | Can access and modify **class-level attributes** but not instance-level attributes. |
| **Use Case**           | Used when a method does not need access to the class or instance, but is related to the class logically. | Used when a method needs to operate on the **class level** (i.e., accessing class variables or other class methods). |
| **First Argument**     | No special first argument (like `self` or `cls`). | Always takes `cls` as the first argument, representing the class. |
| **Calling**            | Can be called using the class or instance.       | Can be called using the class or instance, but typically used with the class. |
| **Example Usage**      | `@staticmethod` to define utility methods that do not rely on the class or instance. | `@classmethod` to modify class-level attributes or methods. |

### Example Usage:
**Static Method Example:**

A static method does not take self or cls as the first argument. It's used for utility functions that don't depend on the state of the object or the class.
```python
class MyClass:
    @staticmethod
    def greet(name):
        return f"Hello, {name}!"

print(MyClass.greet("Alice"))  # Output: Hello, Alice!
```
### Class Method Example:
A class method takes cls as the first argument. It can access and modify class-level variables and methods.

```python
class MyClass:
    class_variable = "I am a class variable."

    @classmethod
    def print_class_variable(cls):
        return cls.class_variable

print(MyClass.print_class_variable())  # Output: I am a class variable.
```
### Key Takeaways:
**Static methods** → Do not have access to class or instance attributes, but are logically related to the class.

**Class methods** → Have access to class-level attributes and can modify them.

Use static methods for utility functions, and class methods when you need to work with class-level data.






21. ### Difference between static methods and instance methods.

| **Feature**          | **Static Method**                                 | **Instance Method**                           |
|---------------------|------------------------------------------------|---------------------------------------------|
| **Definition**      | A method that doesn’t take `self` or `cls` as an argument. It’s bound to the class but does not access instance or class attributes. | A method that takes `self` as the first argument, allowing it to access and modify instance attributes. |
| **Decorator Used**  | Defined using `@staticmethod`.                   | No decorator is needed (default method type in a class). |
| **Access To**       | Cannot access **instance (`self`) or class (`cls`) attributes**. | Can access and modify **instance attributes**. |
| **First Argument**  | No `self` or `cls` required.                     | Always takes `self` as the first parameter. |
| **Use Case**        | Used for utility functions that are logically related to the class but don’t need instance-specific data. | Used when working with **object-specific data**. |
| **Calling Method**  | Can be called using the **class** or **instance**. | Can only be called on an **instance** of the class. |
| **Example Usage**   | `@staticmethod` for helper functions (e.g., data validation, calculations). | Regular methods that work with instance attributes. |

### Example Usage:
**Static Method Example:**
A static method does not require self and is used for general utility functions.

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

print(MathOperations.add(5, 10))  # Output: 15
```
### Instance Method Example:
An instance method uses self and can modify instance-specific attributes.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."

p = Person("Alice")
print(p.greet())  # Output: Hello, my name is Alice.
```
### Key Takeaways:
**Static methods** → Do not access instance (self) or class (cls) attributes, used for general utility functions.

**Instance methods** → Access and modify instance-specific attributes.

**Static methods** can be called without creating an instance, while instance methods require an object of the class.

22. ###  Difference between getattr() and setattr().
| **Feature**        | **getattr()**                                      | **setattr()**                                    |
|-------------------|--------------------------------------------------|------------------------------------------------|
| **Definition**    | Retrieves the value of an attribute from an object. | Sets (modifies) the value of an attribute in an object. |
| **Syntax**       | `getattr(object, attribute_name[, default])`      | `setattr(object, attribute_name, value)` |
| **Use Case**     | Used to **access** attributes dynamically.        | Used to **modify or create** attributes dynamically. |
| **Returns**      | Returns the **value** of the attribute.           | Returns **None** (just sets the value). |
| **Default Value** | Can take an optional default value if the attribute does not exist. | If the attribute does not exist, it creates it. |
| **Example Usage** | `getattr(obj, "name", "Default Name")`           | `setattr(obj, "age", 25)` |

### Example Usage:
**Using getattr() to Retrieve an Attribute Value**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)

# Using getattr() to get an attribute
print(getattr(p, "name"))  # Output: Alice

# Using getattr() with a default value
print(getattr(p, "gender", "Not specified"))  # Output: Not specified
```
**Using setattr() to Modify or Add an Attribute**
```python
# Using setattr() to modify an existing attribute
setattr(p, "age", 35)
print(p.age)  # Output: 35

# Using setattr() to add a new attribute
setattr(p, "gender", "Female")
print(p.gender)  # Output: Female
```
### Key Takeaways:
`getattr()` → **Retrieves** an attribute value, can provide a default if the attribute doesn’t exist.

`setattr()` → **Modifies or creates** an attribute dynamically.

`getattr() `is **useful for safe access**, while `setattr()` **helps in dynamically updating attributes**.



23. ### Difference between `map()` and `filter()`

```markdown
| **Feature**      | **map()**                                      | **filter()**                                   |
|-----------------|----------------------------------------------|----------------------------------------------|
| **Definition**  | Applies a function to each item in an iterable and returns a new iterable with transformed values. | Applies a function to each item in an iterable and returns only the items that evaluate to `True`. |
| **Function Type** | Transformational (modifies elements).      | Filtering (removes elements based on a condition). |
| **Return Type** | Returns a **map object** (an iterator with transformed values). | Returns a **filter object** (an iterator with filtered elements). |
| **Length of Output** | Same length as input iterable. | Length may be **shorter** than input, as some elements are filtered out. |
| **Function Requirement** | Function must return a value for each element. | Function must return a boolean (`True` or `False`). |
| **Usage** | When you need to modify all elements of an iterable. | When you need to **select** elements based on a condition. |
| **Example** | `map(lambda x: x*2, [1, 2, 3, 4])` → `[2, 4, 6, 8]` | `filter(lambda x: x%2==0, [1, 2, 3, 4])` → `[2, 4]` |
```

### **Example Usage**

#### **Using `map()`** (Transforming elements)
```python
numbers = [1, 2, 3, 4]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))  # Output: [2, 4, 6, 8]
```

#### **Using `filter()`** (Selecting elements based on condition)
```python
numbers = [1, 2, 3, 4]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]
```

### **Key Takeaways:**
- **Use `map()`** when you want to **modify** all elements in an iterable.
- **Use `filter()`** when you want to **select** elements that meet a condition.
- Both return **iterators**, so you need to convert them to a list to view results.



24. ### Difference between `update()` and `union()` in Sets

```markdown
| **Feature**      | **update()**                                     | **union()**                                   |
|-----------------|-------------------------------------------------|---------------------------------------------|
| **Definition**  | Modifies the original set by adding elements from another set or iterable. | Returns a new set containing all elements from both sets without modifying the original set. |
| **Mutability**  | Modifies the existing set in-place.             | Does **not** modify the original sets; returns a new set. |
| **Return Type** | Returns `None` (modifies the existing set).     | Returns a **new set** with merged elements. |
| **Usage**       | Used when you want to **extend** a set without creating a new one. | Used when you need a **new set** containing all unique elements from both sets. |
| **Example**     | `A.update(B)` → `A` now contains elements of both `A` and `B`. | `C = A.union(B)` → `C` contains elements of `A` and `B`, but `A` and `B` remain unchanged. |
```

### **Example Usage**

#### **Using `update()`** (Modifies the original set)
```python
A = {1, 2, 3}
B = {3, 4, 5}
A.update(B)
print(A)  # Output: {1, 2, 3, 4, 5}  (A is modified)
```

#### **Using `union()`** (Returns a new set)
```python
A = {1, 2, 3}
B = {3, 4, 5}
C = A.union(B)
print(C)  # Output: {1, 2, 3, 4, 5}  (A and B remain unchanged)
```

### **Key Takeaways:**
- **Use `update()`** when you want to **modify** the original set.
- **Use `union()`** when you want to **create a new set** without altering existing ones.



25. ### Difference between `intersection()` and `difference()` in Sets

```markdown
| **Feature**      | **intersection()**                              | **difference()**                               |
|-----------------|-----------------------------------------------|----------------------------------------------|
| **Definition**  | Returns a set containing only common elements between two sets. | Returns a set containing elements in the first set but not in the second. |
| **Mutability**  | Does **not** modify original sets; returns a new set. | Does **not** modify original sets; returns a new set. |
| **Usage**       | Used to find **common** elements between two sets. | Used to find **unique** elements in one set compared to another. |
| **Example**     | `A.intersection(B)` → `{3}` | `A.difference(B)` → `{1, 2}` |
```

### **Example Usage**

#### **Using `intersection()`** (Find common elements)
```python
A = {1, 2, 3}
B = {3, 4, 5}
C = A.intersection(B)
print(C)  # Output: {3}
```

#### **Using `difference()`** (Find unique elements in A)
```python
A = {1, 2, 3}
B = {3, 4, 5}
C = A.difference(B)
print(C)  # Output: {1, 2}
```

### **Key Takeaways:**
- **Use `intersection()`** to find **common** elements between sets.
- **Use `difference()`** to find **unique** elements in one set relative to another.

---

26. ### Difference between `frozenset` and `set`

```markdown
| **Feature**      | **set**                                        | **frozenset**                                   |
|-----------------|----------------------------------------------|----------------------------------------------|
| **Mutability**  | **Mutable** – elements can be added or removed. | **Immutable** – elements **cannot** be changed after creation. |
| **Usage**       | Used for **modifiable** collections of unique elements. | Used when a **fixed, hashable** set is needed (e.g., dictionary keys). |
| **Operations**  | Supports adding, removing, and updating elements. | Supports only read operations (no add/remove). |
| **Example**     | `A = {1, 2, 3}` → `A.add(4)` → `{1, 2, 3, 4}` | `B = frozenset([1, 2, 3])` → modification not allowed. |
```

### **Example Usage**

#### **Using `set`** (Mutable)
```python
A = {1, 2, 3}
A.add(4)
print(A)  # Output: {1, 2, 3, 4}
```

#### **Using `frozenset`** (Immutable)
```python
B = frozenset([1, 2, 3])
# B.add(4)  # This will raise an AttributeError
print(B)  # Output: frozenset({1, 2, 3})
```

### **Key Takeaways:**
- **Use `set`** when you need a **modifiable** collection of unique elements.
- **Use `frozenset`** when you need an **immutable, hashable** collection (e.g., for dictionary keys).



27. ### Difference between `remove()` and `discard()` in Sets

```markdown
| **Feature**      | **remove()**                                    | **discard()**                                   |
|-----------------|----------------------------------------------|----------------------------------------------|
| **Definition**  | Removes a specified element from the set. If the element is not found, it raises a `KeyError`. | Removes a specified element from the set. If the element is not found, it **does not** raise an error. |
| **Error Handling** | Raises `KeyError` if the element is missing. | Does **not** raise an error if the element is missing. |
| **Mutability**  | Modifies the original set.                    | Modifies the original set. |
| **Return Type** | Returns `None` (modifies in place).           | Returns `None` (modifies in place). |
| **Usage**       | Use when you **know** the element exists in the set. | Use when you're **not sure** if the element exists. |
| **Example**     | `A.remove(3)` → If `3` is not present, raises an error. | `A.discard(3)` → If `3` is not present, no error is raised. |
```

### **Example Usage**

#### **Using `remove()`** (Raises an error if element is missing)
```python
A = {1, 2, 3}
A.remove(2)
print(A)  # Output: {1, 3}
A.remove(5)  # Raises KeyError since 5 is not in the set.
```

#### **Using `discard()`** (No error if element is missing)
```python
A = {1, 2, 3}
A.discard(2)
print(A)  # Output: {1, 3}
A.discard(5)  # No error, even though 5 is not in the set.
```

### **Key Takeaways:**
- **Use `remove()`** when you **know** the element exists and want an error if it doesn’t.
- **Use `discard()`** when you **don’t want an error** if the element is missing.


28. ### Difference between Keyword Arguments and Positional Arguments

```markdown
| **Feature**      | **Positional Arguments**                        | **Keyword Arguments**                      |
|-----------------|-----------------------------------------------|------------------------------------------|
| **Definition**  | Arguments are passed based on their position in the function call. | Arguments are passed using parameter names, regardless of order. |
| **Order Matters?** | Yes, arguments must be in the correct order. | No, arguments can be in any order as long as names are used. |
| **Readability** | Less readable when many arguments are passed. | More readable as arguments are explicitly named. |
| **Flexibility** | Requires remembering the order of parameters. | Easier to use, especially when a function has many parameters. |
| **Mixing Allowed?** | Yes, but positional arguments must come first. | Yes, but keyword arguments must follow positional arguments. |
| **Example**     | `func(1, 2, 3)` | `func(a=1, b=2, c=3)` |
```

### **Example Usage**

#### **Using Positional Arguments**
```python
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 25)  # Output: Hello, Alice! You are 25 years old.
```

#### **Using Keyword Arguments**
```python
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(age=25, name="Alice")  # Output: Hello, Alice! You are 25 years old.
```

### **Key Takeaways:**
- **Use positional arguments** when the order is intuitive and fixed.
- **Use keyword arguments** for better readability and flexibility.
- **Mixing is allowed**, but **positional arguments must come first**.


29. ### Difference between `*args` and `**kwargs`

```markdown
| **Feature**      | **`*args`**                                      | **`**kwargs`**                                   |
|-----------------|----------------------------------------------|----------------------------------------------|
| **Definition**  | Allows a function to accept a variable number of **positional arguments**. | Allows a function to accept a variable number of **keyword arguments**. |
| **Data Type**   | Tuple (stores arguments as a tuple).          | Dictionary (stores arguments as key-value pairs). |
| **Usage**       | Used when the number of arguments is unknown and needs to be handled flexibly. | Used when the number of keyword arguments is unknown. |
| **Accessing Values** | Accessed using tuple indexing.             | Accessed using dictionary key-value pairs. |
| **Order Matters?** | Yes, values are passed based on order.      | No, values are assigned using named parameters. |
| **Example**     | `def func(*args): print(args)` → `func(1, 2, 3)` → `(1, 2, 3)` | `def func(**kwargs): print(kwargs)` → `func(a=1, b=2)` → `{'a': 1, 'b': 2}` |
```

### **Example Usage**

#### **Using `*args`** (Variable Number of Positional Arguments)
```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # Output: 10
```

#### **Using `**kwargs`** (Variable Number of Keyword Arguments)
```python
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
```

### **Key Takeaways:**
- **Use `*args`** when you want to accept multiple **positional** arguments.
- **Use `**kwargs`** when you want to accept multiple **keyword** arguments.
- **You can combine both**, but `*args` must come **before** `**kwargs` in the function signature.





30. ### Difference between Global and Local Variables

```markdown
| **Feature**      | **Global Variables**                            | **Local Variables**                             |
|-----------------|----------------------------------------------|----------------------------------------------|
| **Definition**  | Declared outside a function and accessible throughout the program. | Declared inside a function and accessible only within that function. |
| **Scope**      | Available in all functions unless modified using `global`. | Only available inside the function where it is defined. |
| **Persistence** | Exists throughout the execution of the program. | Created when the function is called and destroyed when the function exits. |
| **Modification** | Can be modified inside a function using the `global` keyword. | Cannot be directly modified outside its function. |
| **Use Case**    | Useful for constants or variables that need to be accessed globally. | Useful for temporary data specific to a function. |
| **Example**     | `x = 10` (Declared outside function, accessible inside functions) | `def func(): x = 5` (Only accessible within `func()`) |
```

### **Example Usage**

#### **Global Variable Example**
```python
x = 10  # Global variable

def show():
    print(x)  # Accessible inside the function

show()  # Output: 10
```

#### **Local Variable Example**
```python
def show():
    x = 5  # Local variable
    print(x)

show()  # Output: 5
print(x)  # Raises NameError: name 'x' is not defined
```

### **Using `global` Keyword**
```python
x = 10  # Global variable

def modify():
    global x  # Access and modify global variable
    x = 20

modify()
print(x)  # Output: 20
```

### **Key Takeaways:**
- **Global variables** are accessible anywhere in the program unless shadowed.
- **Local variables** exist only inside the function where they are declared.
- Use the `global` keyword to modify a global variable inside a function.



31. ### Difference between global scope and local scope.


```markdown
| **Feature**      | **Global Scope**                                | **Local Scope**                               |
|-----------------|----------------------------------------------|----------------------------------------------|
| **Definition**  | The region of a program where global variables are accessible, typically the entire script. | The region of a program where local variables are accessible, usually within a function. |
| **Scope**      | Available throughout the program, including inside functions (unless shadowed). | Available only within the function where it is declared. |
| **Persistence** | Exists throughout the execution of the program. | Created when the function is called and destroyed when the function exits. |
| **Modification** | Can be modified inside a function using the `global` keyword. | Cannot be directly modified outside its function. |
| **Use Case**    | Useful for constants or variables that need to be accessed globally. | Useful for temporary data specific to a function. |
| **Example**     | `x = 10` (Declared outside function, accessible inside functions) | `def func(): x = 5` (Only accessible within `func()`) |
```

### **Example Usage**

#### **Global Scope Example**
```python
x = 10  # Global variable

def show():
    print(x)  # Accessible inside the function

show()  # Output: 10
```

#### **Local Scope Example**
```python
def show():
    x = 5  # Local variable
    print(x)

show()  # Output: 5
print(x)  # Raises NameError: name 'x' is not defined
```

### **Using `global` Keyword**
```python
x = 10  # Global variable

def modify():
    global x  # Access and modify global variable
    x = 20

modify()
print(x)  # Output: 20
```

### **Key Takeaways:**
- **Global scope** means a variable is accessible anywhere in the program unless shadowed by a local variable.
- **Local scope** means a variable is only accessible within the function where it is declared.
- Use the `global` keyword to modify a global variable inside a function.


32. ### Difference between Shallow Copy and Deep Copy

```markdown
| **Feature**      | **Shallow Copy**                                   | **Deep Copy**                                    |
|-----------------|-------------------------------------------------|-------------------------------------------------|
| **Definition**  | Creates a new object but inserts references to the original elements. | Creates a new object and recursively copies all nested objects. |
| **Memory Usage** | Lower, as it only copies references.             | Higher, as it duplicates entire structures. |
| **Modification Effect** | Changes to mutable elements affect both copies. | Changes to mutable elements in the copied object do not affect the original. |
| **Use Case**    | When you need a duplicate without modifying nested elements. | When you need a completely independent copy. |
| **Example**     | `copy.copy(original_list)` | `copy.deepcopy(original_list)` |
```

### **Example Usage**

#### **Shallow Copy Example**
```python
import copy
list1 = [[1, 2], [3, 4]]
list2 = copy.copy(list1)
list2[0][0] = 99
print(list1)  # Output: [[99, 2], [3, 4]] (Original modified)
```

#### **Deep Copy Example**
```python
import copy
list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)
list2[0][0] = 99
print(list1)  # Output: [[1, 2], [3, 4]] (Original remains unchanged)
```

### **Key Takeaways:**
- **Shallow copy** copies only references, leading to unintended changes in mutable objects.
- **Deep copy** creates a fully independent object with duplicated nested elements.
- Use `copy.copy()` for shallow copies and `copy.deepcopy()` for deep copies.


33. ### Difference Between Class Variable and Instance Variable

### **1. Class Variable**
- A **class variable** is shared by **all instances** of a class.
- It is defined **inside the class**, but **outside any instance methods**.
- Modifying a class variable will affect **all instances** unless specifically overridden.

```python
class Student:
    school_name = "ABC School"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school_name)  # Output: ABC School
print(s2.school_name)  # Output: ABC School

Student.school_name = "XYZ School"  # Changing class variable
print(s1.school_name)  # Output: XYZ School
```



### **2. Instance Variable**
- An **instance variable** is specific to each **object instance**.
- It is defined using `self` inside the constructor or other methods.
- Changing it affects **only that specific object**.

```python
s1.name = "Charlie"
print(s1.name)  # Output: Charlie
print(s2.name)  # Output: Bob
```

---

### **3. Key Differences**
| Feature            | Class Variable                 | Instance Variable              |
|--------------------|--------------------------------|--------------------------------|
| Scope              | Shared across all instances    | Unique to each instance       |
| Defined In         | Class level                    | Inside constructor/method      |
| Accessed With      | ClassName.var or self.var      | Only with self.var             |
| Memory             | Stored once for the class      | Stored separately per object   |

---

### **Conclusion**
- Use **class variables** for properties common to all instances.
- Use **instance variables** for unique data in each object.

---

34. ### Difference Between Class Method and Static Method

### **1. Class Method**
- A **class method** is bound to the class and not the instance of the class.
- It takes `cls` as its first parameter, which refers to the class itself.
- It can access or modify the class state.
- Defined using the `@classmethod` decorator.

```python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

print(Person.get_count())  # Output: 0
p1 = Person("Alice")
p2 = Person("Bob")
print(Person.get_count())  # Output: 2
```

---

### **2. Static Method**
- A **static method** does not take `self` or `cls` as its first argument.
- It can't access or modify class or instance data.
- Defined using the `@staticmethod` decorator.
- Used for utility functions related to the class.

```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(3, 5))  # Output: 8
```

---

### **3. Key Differences**
| Feature            | Class Method                   | Static Method                   |
|--------------------|--------------------------------|---------------------------------|
| First Argument     | cls (class)                    | No default argument             |
| Access Class Data  | Yes                            | No                              |
| Access Instance Data| No                            | No                              |
| Use Case           | Modify class state             | Utility operations              |

---

### **Conclusion**
- Use **class methods** when you need to work with class variables or modify class state.
- Use **static methods** for general-purpose utilities that don't need access to class or instance data.


---

