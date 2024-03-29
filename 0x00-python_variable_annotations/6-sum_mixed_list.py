#!/usr/bin/env python3
"""Represents a function that sums up integers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of the numbers in a list as a float"""
    sum = 0

    for num in mxd_lst:
        sum += num

    return sum
