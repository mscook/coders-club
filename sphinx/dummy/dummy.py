"""
I'm a dummy module to show you how Sphinx works

Created by Mitchell Stanton-Cook
11/07/13
"""

import random

class Point_2D():
    """
    I do something really cool
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
    
    :param num_points: the number of random points to generate
    
    :type num_points: int
    
    :returns: a list of 2D points
    """
    for i in xrange(0, num_points):



