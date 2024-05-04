import re
from typing import Callable

def generator_numbers(text: str):
    """
    This function creates generator which iterates throw all decimals from the passed string
    """
    decimals_from_text=re.findall("\d+\.\d+",text) # we get all decimals from the string

    for elem in decimals_from_text:
        yield float(elem)

def sum_profit(text: str, func: Callable):
        
    sum_profit=0
        
    for elem in func(text):
        sum_profit += elem

    return sum_profit

