def print_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        if (isinteger(my_list[i])):
            print("{:d}".format(my_list[i]))
def isinteger(a):
    try:
        int(a)
        return True
    except ValueError:
        return False
