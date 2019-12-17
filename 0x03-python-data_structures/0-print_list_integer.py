def print_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        a = str(my_list[i]);
        if a.isdigit():
            print("{:d}".format(my_list[i]));
