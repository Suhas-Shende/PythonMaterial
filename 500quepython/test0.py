'''
What is difference between tuple and dictionary.
1)Tuple                                    2) Dictionary
-Immutable                                  -mutable
-()                                           {}
-Duplicates are allowed                      Unique key allowed
-Elements must be hashable                   key are unique
-It can access by index                      It can access by key
-It is collection of hetergenous elements   -it is collection of key-value pairs       




Diffrence between set and tuple
1)Set                                           1)Tuple                                                
-These are collection of unique elements        -Duplicates are allowed
-mutable data type (can add or remove elements  -immutable data type (cannot be modify)
-unindexed and unordered                        -indexed and ordered
-Elements can't be accessed by index            -Elements can be accessed by index
-Elements can  be added in set                  -Elemntes cant be added

mutable 
indexed ordered
syntax
accesing


Difference between map() and filter()






for loop used for iterating over iterable(list,tuple,string,range())
while loop is executing block of code based on condition


controled by iterable 

controled by condition


terminates when iterable exhasted
terminates when condition become false/break the loop





@property convert the method into read only attributes



'''

#add multiple element at the end of last of list
l=[2,3,4,5,6,7]
l1=[11,1,2,13]
l.extend(l1)   
print (l)


l=[1,2,3,4,5]
l.insert(1,5)   #insert at the index position insert(index position,elements)
print(l)

# Using global
x = 10  # Global variable

def modify_global():
    global x  # Declaring x as global
    x = 20  # Modifies the global variable

modify_global()
print(x)  # Output: 20

