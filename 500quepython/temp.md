
**Lambda** is an **anonymous function** in Python, that can accept any number of arguments, but can only have a single expression. It is generally used in situations requiring an anonymous function for a short time period. 

**Lambda functions can be used in either of the two ways:**

**• Assigning lambda functions to a variable:**
```python 
mul = lambdaa, b : a * b
print(mul(2, 5))    # output => 10
```
**• Wrapping lambda functions inside another function:** 
```python
defmyWrapper(n):
   returnlambdaa : a * n
mulFive = myWrapper(5)
print(mulFive(2))    # output => 10
```


