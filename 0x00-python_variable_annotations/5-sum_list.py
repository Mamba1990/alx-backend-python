#!/usr/bin/env python3
"""Represents a function that sums up a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of numbers"""
    sum = 0

    for num in input_list:
        sum += num

    return sum
