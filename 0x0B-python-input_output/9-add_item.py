#!/usr/bin/python3
import sys
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file


def listappend(args, l=[]):
    for i in range(1, len(args)):
        l.append(args[i])
    return l


if __name__ == "__main__":
    file = "add_item.json"
    args = []
    try:
        args = load(file)
    except:
        pass
    args += listappend(sys.argv)
    save(args, file)
    load(file)
