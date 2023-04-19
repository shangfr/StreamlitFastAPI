# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:04:46 2023

@author: shangfr
"""


async def calculate(operation, x, y):
    ''' 
    Parameters
    ----------
    operation : str
        takes the string [add, sub, mul, div].
    x : float
        numbers.
    y : float
        numbers.

    Returns
    -------
    value.

    '''

    if operation == '加':
        return x+y
    elif operation == '减':
        if x > y:
            return x-y
        else:
            return y-x
    elif operation == '乘':
        return x*y
    elif operation == '除':
        return x/y
