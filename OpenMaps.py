#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script that takes an address as input and opens up in the browser
the address can be in the clipboard or the passed as argument
"""

import pyperclip
import sys
import webbrowser

sys.argv  # ['mapit.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
