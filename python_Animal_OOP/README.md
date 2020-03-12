# OOP Basics

```python
This repo will contain our OOP basics.
```

```python
We will look at:
- Abstraction
- Encapsulation
- Inheritance
- Polymorphism
```

### Class
```SQL
- A class is a code template for creating objects. Objects have member variables and have behaviour associated with them. 
- In python a class is created by the keyword class . An object is created using the constructor of the class.
```
### Methods vs Functions 
```SQL
- Methods are functions that belong to a specific data type.
- Where functions are anonymous and anything can call and run them.
- Where as **Methods NEED the instance to be called***
```
### Instance
```SQL
- An instance method object combines a class, a class instance and any callable object (normally a user-deﬁned function).
```

### Self
```python
- The self referes to the instance of on which a method os being called.
self.name = 'ringo'
- This means that a specific object attribute name will have the strin 'ringo'
```
### Characteristics/ How an object looks
```SQL
- These are attributes that are assisned to each instance.
- They are variables assigned 
```
### Abstraction
```SQL
**The ability to hide complexity.**
We do this using:
- Documentation
    - Specify which method and how to use them.
- Inheritance ---> causes some level of abstraction

Realife examples everywhere:
- Changing gears
- Heating up food with one button
- Using our cards to pass security
```

### Encapsulation
```SQL
- In object oriented python program, you can restrict access to methods and variables. 
- This can prevent the data from being modified by accident and is known as encapsulation
- It allows a class to change its implementation without affecting other parts of the code.
```
### Inheritance
```SQL
- This is the ability to pass to child class all the mkthods and charateristics.
- This is one of the big reasons fr OOP - it means you can re-use code.

**Promise of reusable**
```python
- You do this by passing the parent class as an argument of the child class

class Animal():
    pass

class Reptile(Animal):
    pass
```
### Polymorphism
```python
- Literally means MANY FORMS.
- This is the ability to **completly overwrite methods** and, if need be, recall methods from parent class using super.
```
### .super()
```SQL
- It represetns the parent class, allows you to call methods from parents class.
Usage and case in point:
- Situations where you want to overwrite a method(say method .honk() or make a .sound() )
- You want to add new functionality to the new method.
- But still have everyhting from first method.

----->> Then you call super()  :)

Most of the times this happend with the __init__ method
- You want to add new characteristics to the child object
- And you want to keep all the original characteristics
- So you overwrite the init method and still call the orignal init method, with all the necessary arguments.
```
```python
class Animal():
    
    # original init method with age and colour_fur
    def __init__(self, age, colour_fur):
        self.age = age
        self.colour_fur = colour_fur

class Reptile(Animal):
    
    # this overwrites the original init method 
    # however, what we want is to keep all the original code and add more code
    def __init__(self, name, age, colour_f):
        # use super to call original init method
        # we need to pass the arguments for the original init to work 
        super().__init__(age, colour_f) # line that runs original init with original arguments
        self.name = name

 rt = Reptile('ringo', 10, 'Shinny gold')
```


