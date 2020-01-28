#!/usr/bin/python3
""" Square Module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square is a Ractagle yeld """

    def __init__(self, size, x=0, y=0, id=None):
        """ Square constructor """
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Square definition """
        return("[Square] (" + str(self.id) + ") " +
               str(self.x) + "/" + str(self.y) + " - " +
               str(self.size))

    @property
    def size(self):
        """ size getter """
        return(Rectangle.__width)

    @size.setter
    def size(self, width):
        """ size setter """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        Rectangle.__width = width
        Rectangle.__height = width

    def update(self, *args, **kwargs):
        """ update square values """
        i = 0
        attr = ['id', 'size', 'x', 'y']
        kw = list(set(kwargs.keys()))
        for k in args:
            if k:
                exec("self.%s = %d" % (attr[i], k))
            i += 1
        for k in kw:
            exec("self.%s = %d" % (k, kwargs[k]))

    def to_dictionary(self):
        """ attributes to dictionary """
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
