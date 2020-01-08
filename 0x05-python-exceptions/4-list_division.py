#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nl = [0] * list_length
    for i in range(0, list_length):
        try:
            a = int(my_list_1[i])
            b = int(my_list_2[i])
            r = a/b
        except IndexError:
            print("out of range")
            r = 0
        except ValueError:
            print("wrong type")
            r = 0
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        finally:
            nl[i] = r
    return (nl)
