# -*- coding: utf-8 -*-
"""
Date: 2023/09/18
HW: 04
Author: 林群賀
Student Number: 109601003
"""

from typing import Any

# init_people = 342032486
# year_day = 365
# year = 5
# hour = 24
# minute = 60
# second = 60

# born_rate = 7
# die_rate = 13
# immigrating_rate = 45

# total_time = 365 * 5 * 24 * 60 * 60

# born_people = total_time / born_rate
# die_people = total_time / die_rate
# immigrating_people = total_time / immigrating_rate

# print(int(init_people + born_people + immigrating_people - die_people))

class Census:
    init_people = 342032486
    year_day = 365
    year = 5
    hour = 24
    minute = 60
    second = 60

    born_rate = 7
    die_rate = 13
    immigrating_rate = 45

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def __init__(self) -> None:
        pass

    def get_init_people(self,):
        return self.init_people

    def get_total_time(self,):
        total_time = self.year_day * self.year * self.hour * self.minute * self.second

        return total_time
    
    def get_born_people(self,):
        total_time = self.get_total_time()
        born_people = total_time / self.born_rate

        return born_people
    
    def get_die_people(self,):
        total_time = self.get_total_time()
        die_people = total_time / self.die_rate

        return die_people
    
    def get_immigrating_people(self,):
        total_time = self.get_total_time()
        immigrating_people = total_time / self.immigrating_rate

        return immigrating_people
    
    def get_total_people(self,):
        total_people = self.init_people + self.get_born_people() + self.get_immigrating_people() - self.get_die_people()

        return int(total_people)

census = Census()
init_people = census.get_init_people()
total_people = census.get_total_people()

print("Jan, 01:", init_people)
print("Five year later, Dec, 31:", total_people)