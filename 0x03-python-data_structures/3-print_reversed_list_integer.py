def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    while (i >= 0):
        if (isinteger(my_list[i])):
            print("{:d}".format(my_list[i]))
            i -= 1
def isinteger(a):
    try:
        int(a)
        return True
    except ValueError:
        return False
