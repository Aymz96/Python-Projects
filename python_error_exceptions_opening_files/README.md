# Error Handling Task 1

```css
I want a program to ask for food. 
As a user I should be able to ask for any amount of food.#
As I user I should be able to create different orders (different files)
As a user I should be able to read back the order to my client
```
```sql
**Acceptance criterea** 
- it should be well formated
- it should be numbered
```
### Example:
```python
> 1 - Nachos
> 2 - Diet CocaCola
``` 
```css
As a user, if I try to read a order that doens't exist it should give me an error. 
As a user I should be able to amend my order :) 
```
### DOD
 ```css
- is its own project
- git and github 
- simple documentation
- functional
- separation of concerns
- it should handle errors
```

### Clone using the command below on Terminal
````python
git clone https://git@github.com:Aymz96/Python_Projects.git
````
## run
```python
python3 main.py
```


### Working with Files and Error Handling Exceptions
```java
Error handling is the important concept of this class.
```

### Error handling
```python
- Exceptions
- Error Handling
using `try` and `except`
best practices using `with`
clean up our functions with `finally`
open, closing and writing to files
What can go wrong will go wrong
```
```java
- Assume your code will break, and what you want to do is handle the errors, gracefully.
- When you handle your errors, your code will continue to run.
```
### Best Practices
```python
**never capture all exceptions**
You never want to handle for **ALL EXCEPTION** because it can create an unstopable code.
```
- You must specify what exception you want to handle:

```python
try:
    file = open('order.txt')
except FileNotFoundError
    print('THERE HAS BEEN AN ERROR! PANIC NOW!')
```
```python
**Capture your message** 
You can capture your messages using `as`:
```
```python
try:
    file = open('order.txt')
except FileNotFoundError as error_message:
    # print('THERE HAS BEEN AN ERROR! PANIC NOW!')
```

## Definitions
#### Errors and exceptions 
```python
It's when the code actually breaks / stops. Unless handled.

**Raise**
- Key word to raise an exception in python
```
**`try:` , `except:` and `finaly:`**
```python
**open() & close()
readline()
readlines()**
Use with: 
The `with open('file') as file:` implicitly closes the files after it run the block of code.
```
