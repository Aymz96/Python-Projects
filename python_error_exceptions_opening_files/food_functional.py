def open_a_food_file(text_file):
    try:
        with open(text_file, 'r') as file:
            food_list = file.readlines()
            for line in food_list:
                print(line.strip('\n').title())

    except FileNotFoundError as err:
        print('Check your files')
        print(err)

    finally:
        print('Program Closing')
