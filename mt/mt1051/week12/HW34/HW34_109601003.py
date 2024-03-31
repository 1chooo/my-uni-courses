# -*- coding: utf-8 -*-
"""
Date: 2023/12/11
HW: 34
Author: 林群賀
Student Number: 109601003
"""

import datetime

present_time = datetime.datetime.now()
print("Time:", present_time)

time_alert = datetime.datetime(2023, 12, 11, 9, 22, 00)
if (present_time > time_alert):
    print("Time is up!")

delta_time = datetime.timedelta(
    weeks=2, 
    days=3, hours=5, 
    minutes=15, 
    seconds=25
)
print("DeltaTime:", delta_time)

time_new = present_time + delta_time
print("Time after DelatTime is:", time_new)
