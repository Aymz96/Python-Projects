# Import naan factory functions
# Run tests

from naan_factory_functions import *


# 1. As a user, I can use the make_dough with water and flour to make dough
print('calling make_dough with water and flour. Expect dough as a result')
print(make_dough('water', 'flour') == 'dough')
print('Got: ', make_dough('water', 'flour'))

print('calling make_dough with water and cement. Expect not dough as a result')
print(make_dough('water', 'cement') == 'not dough')
print('Got: ', make_dough('water', 'cement'))


#2 As a user, I can use the bake_dough with dough to get naan.
print('calling naan1 with bake_dough and dough. Expect naan as a result')
print(naan1('bake_dough', 'dough') == 'naan')
print('Got: ', naan1('bake_dough', 'dough'))

print('Expect not naan1 as a result')
print(naan1('dough', 'something') == 'not naan')
print('Got: ', naan1('dough', 'something'))


#3 As a user, I can use the run_factory with water and flour and get naan.
print('calling naan2 with water and flour. Expect naan as a result')
print(naan2('water', 'flour') == 'naan')
print('Got: ', naan2('water', 'flour'))

print('Expect not naan2 as a result')
print(naan2('water', 'something_new') == 'not naan')
print('Got: ', naan2('water', 'something_new'))
