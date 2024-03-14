#!/usr/bin/env python3
'''Task eight's module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """'Defines a multiplier function.
    """
    return lambda x: x * multiplier
