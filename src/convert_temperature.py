#!/usr/bin/env python

import os
import sys

#from converter import Converter

def convert_f_to_c(temp_f):
    temp_c = (5.0/9.0) * (temp_f - 32.0)
    return temp_c


if __name__ == "__main__":

    temp_f = float(raw_input("enter temperature in fahrenheit: "))
    temp_c = convert_f_to_c(temp_f)

    print "%s degrees C and %s degrees F" % (temp_c, temp_f)


#########
# ideas #
#########

# 1. add a function for c_to_f
# 2. add a class to store those fns
# 3. add a loop to keep asking for input until the user hits "q"
# 4. add some if statements to print different things depending on the temparature


