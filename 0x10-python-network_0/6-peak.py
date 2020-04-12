#!/usr/bin/python3
"""Find a peak"""


if __name__ == "__main__":
    def find_peak(list_of_integers):
        if not list_of_integers:
            return None
        else:
            max = list_of_integers[0]
            for i in list_of_integers:
                if max < i:
                    max = i
            return max
