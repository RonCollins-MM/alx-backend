#!/usr/bin/env python3
"""
Implementing pagination in a light-weight function
"""


def index_range(page, page_size):
    """Method that implements a simple pagination algorithm.

    Parameters
    ----------
    page : int
        The logical 'page' of data that is requested

    page_size : int
        The size of each virtual page

    Returns
    -------
    tuple
        A tuple of size 2 containing the start index and end
    """

    end_index = page_size * page
    start_index = end_index - page_size
    return (start_index, end_index)
