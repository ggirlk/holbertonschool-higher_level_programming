#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square is a Ractagle yeld """

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    def __str__(self):
        return("[Square] ("+str(self.id)+") "+str(self.x)+"/"+str(self.y)+" - "+str(self.size))

    @property
    def size(self):
        return(Rectangle.__width)

    @size.setter
    def size(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        Rectangle.__width = width
        Rectangle.__height = width

    def update(self, *args, **kwargs):
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
        return {'id': self.id,
               'size': self.size,
               'x': self.x,
               'y': self.y}
