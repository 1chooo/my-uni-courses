# -*- coding: utf-8 -*-

""" 
Draw Windows 
"""

while True:
    window = (input(""))
    if window == "stop":
        break
    width = int(input(""))
    height = int(input(""))
    frameSize = int(input(""))
    floor = int(input(""))
    sign = input("")

    for j in range(floor):

        for i in range(1, frameSize + 1):
            print((sign * width) * int(window))

        for i in range(1, (height - 2 * frameSize) + 1):
            print((sign * frameSize + (' ' * (width - 2 * frameSize))
                   + sign * frameSize) * int(window))

        for i in range(1, frameSize + 1):
            print((sign * width) * int(window))