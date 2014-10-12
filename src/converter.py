####################
#   Scouts
#   Copyright (c) 2014 Troop 613. All rights reserved.
#
#   This project is distributed according to the terms of the MIT license [http://www.opensource.org/licenses/MIT].
####################

__author__ = "allyn.treshansky"
__date__ = "Dec 9, 2013 4:13:03 PM"

"""
.. module:: converter

Summary of module goes here

"""

# F to C: F = (C * (9/5) + 32)
# C to F: C = (5/9) * (C - 32)

class Converter:
    """

    """

    def __init__(self):
        self.temp_c = 0.0
        self.temp_f = 0.0

    def __str__(self):
        return "%s degrees C and %s degrees F" % (self.temp_c, self.temp_f)

    def convert_f_to_c(self, temp_f=None):
        if temp_f is not None:
            self.temp_f = temp_f

        self.temp_c = (5.0/9.0) * (self.temp_f - 32.0)

    def convert_c_to_f(self, temp_c=None):
        if temp_c is not None:
            self.temp_c = temp_c

        self.temp_f = self.temp_c * (9.0/5.0) + 32.0

