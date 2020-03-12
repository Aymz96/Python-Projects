# Define our functions here

# print(test_example()) don't call function here
# This will violate the separation of concerns and
# It will run said functions when you are importing them elsewhere

from run_naan_factory import *

# 1. As a user, I can use the make_dough with water and flour to make dough
def make_dough(arg1, arg2):
    if arg1 == 'water' and arg2 == 'flour':
        return 'dough'
    else:
        return 'not dough'
    # If argument 1 is water and argument 2 is flour then return dough.
    # Else, return not dough

#2 As a user, I can use the bake_dough with dough to get naan.
def naan1(arg3, arg4):
    if arg3 == 'bake_dough' and arg4 == 'dough':
        return 'naan'
    else:
        return 'not naan'


#3 As a user, I can use the run_factory with water and flour and get naan.
def naan2(arg5, arg6):
    if arg5 == 'water' and arg6 == 'flour':
        return 'naan'
    else:
        return 'not naan'