#!/usr/bin/python3
class LockedClass():
    def __getattribute__(self, name):
        if name != "first_name":
            return AttributeError(
                       "[AttributeError] 'LockedClass'" +
                       "object has no attribute \'" +
                       str(name)+"\'")
        return object.__getattribute__(self, name)
