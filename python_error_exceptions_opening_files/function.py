
# Make a function
def new_order(access):
    try:
        with open('order.txt', 'w') as file:
            file(access + '\n')

    except FileNotFoundError as err:
        print('No such file')
        print(err)

    finally:
        print('The program has ended')

        # # use open to open a file
        # # file = open('order.txt')
        #
        # try:
        #     file = open('order.txt', 'r')  # you should close after you open a file
        #     file_line_list = file.readlines()
        # except FileNotFoundError as errmsg:
        #     print('Please check the file exists.')
        #     print(errmsg)  # prints the actual error
        #
        # print(file_line_list)
        #
        # [print(line.rstrip('\n')) for line in file_line_list]
        #
        # file.close()  # closes file