#!/usr/bin/env python3
"""Type Checking"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return sum of list of floats

    Args:
        input_list (float): list of floats

    Returns:
        float: sum of list of floats
    """
    return (sum(input_list))