# -*- coding: utf-8 -*-
"""
Date: 2023/12/25
Question: 02
Author: 林群賀
Student Number: 109601003
"""

import webbrowser
import urllib.parse

country_name = urllib.parse.quote(input("請輸入國名: "))
city_name = urllib.parse.quote(input("請輸入城市名: "))

webbrowser.open(f"https://www.timeanddate.com/worldclock/{country_name}/{city_name}")
