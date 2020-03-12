# TDD Naan Factory Exercise :taco:

```python
- This exercise is going to bring together lots of concepts.
```

### Learning Outocomes:
Learning outcomes include:
```pyhton
- git
- github
- functions
- TDD 
- separation of concerns
- DRY code
- DOD
```

## Intalling and running:
To run the naan factory do the following: 

```python
import naan_factory
run_factory() 
```

### TDD - test driven development:
```python
1. Write the test
2. Run it, and read the error
3. Code and make it pass the test

**This helps with:**
- Stop over engineering
- Maintainable code 
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems
```
How it works is that we write unit tests. 

### Unit Tests:

Test single pieces of code. Like a function. 
**Base of a test:**
```python
Usually has 3 phases:
- Setup phase (know variables)
- Calling of the function / piece of code with know variables 
- Asserting for expect output
```

### User stories for Naan Factory Excercise:

```SQL
#1 
As a user, I can use the make_dough with 'water' and 'flour' to make 'dough'.

#2
As a user, I can use the bake_dough with dough to get naan. 

#3
As a user, I can user the run_factory with water and flour and get naan.
 
```
 