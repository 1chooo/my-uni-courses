# -*- coding: utf-8 -*-
"""
Date: 2023/12/11
HW: 35
Author: 林群賀
Student Number: 109601003
"""

import webbrowser
import urllib.parse

webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

address = urllib.parse.quote(input("Please input your address: "))
webbrowser.open(f"https://google.com/maps/place/{address}")
