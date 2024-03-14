#!/usr/bin/env python3
"""Represents a function that converts its arguments to a
tuple of key-value pairs.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return k, v * v
