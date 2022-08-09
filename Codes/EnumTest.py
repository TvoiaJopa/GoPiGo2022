#!/usr/bin/python3

from enum import Enum


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

def prinsddst():
    if seas == Season.SPRING:
        print("Spring")


seas = Season.SPRING
print(seas)

prinsddst()

print(list(Season))