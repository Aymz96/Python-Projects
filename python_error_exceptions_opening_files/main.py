from function import *

# Create a list
customer_input = ''
food_order = []
food_menu = ['Chicken pasta', 'Lamb couscous', 'Fish Curry', 'Pizza']


while True:

    user_input = input("Would you like to order Food from the Menu,\n y/n:\n")
    if user_input == 'y':
        print(food_menu)
        customer_input = input('Which Food would you like to order?\n')
        # write_order(customer_input)

    elif customer_input == 'n':
        print('Thanks for viewing the menu. GoodBye!')
        break

    else:
        print('Wrong input, Try again')


