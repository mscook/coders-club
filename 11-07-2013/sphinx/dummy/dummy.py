"""
I'm a dummy module to show you how Sphinx works

Created by Mitchell Stanton-Cook
11/07/13

I am being pulled from the modules docstrings
"""

import random

class Point_2D():
    """
    A class to represent a point in 2D space
    """
    def __init__(self, x, y):
        """
        Initiate a point in 2D space

        :param x: the x coordinate
        :param y: the y coordinate

        :type x: int
        :type y: int
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return '%i %i' % (self.x, self.y)


def generate_points(num_points):
    """
    Returns a given number of random points in range [0-100]
    
    .. warning:: this is broken

    Doctest examples:

    .. doctest::

       >>> 1+1
       3

    Test-Output example:

    .. testcode::

       1+1

    This would output:

    .. testoutput::

       2

    :param num_points: the number of random points to generate
    
    :type num_points: int
   
    :returns: a list of 2D points
    """
    for i in xrange(0, num_points):
        pass



if __name__ == "__main__":
    import doctest
    doctest.testmod()

