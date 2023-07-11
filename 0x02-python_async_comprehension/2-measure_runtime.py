#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime"""
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
