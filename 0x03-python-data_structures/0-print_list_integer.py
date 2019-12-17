def print_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        if (my_list[i] in range(0, 1000000)):
            print("{:d}".format(my_list[i]))
