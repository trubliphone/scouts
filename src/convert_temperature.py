#!/usr/bin/env python

import os
import sys

from converter import Converter

if __name__ == "__main__":

    converter = Converter()

    while True:
        choice = raw_input("choose fahrenheit (F), celsius (C) or quit (Q): ")

        if choice in ["Q", "q"]:
            break

        elif choice in ["F", "f"]:
            temp_f = float(raw_input("enter temperature in fahrenheit: "))
            converter.convert_f_to_c(temp_f)

        elif choice in ["C", "c"]:
            temp_c = float(raw_input("enter temperature in centigrade: "))
            converter.convert_c_to_f(temp_c)

        else:
            print "unkonwn choice; try again"
            continue

        print converter
