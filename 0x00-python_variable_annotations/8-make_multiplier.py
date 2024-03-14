#!/usr/bin/env python3
"""Represents a multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a multiplier function"""

    def worker(number: float) -> float:
        return multiplier * number

        return worker
