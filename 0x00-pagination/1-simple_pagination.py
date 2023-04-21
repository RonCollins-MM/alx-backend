#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a subset of data from a dataset representing a page.

        parameters:
        ----------
        page : int
            The number of pages to be returned
        page_size : int
            The size of each page

        Returns
        -------
        List : List
            A list (page) containing lists (page contents)
        """
        assert type(page) == int
        assert type(page_size) == int
        assert (page > 0 and page_size > 0)

        new_page = []
        page_indexes = index_range(page, page_size)
        data = self.dataset()
        if page_indexes[0] > len(data):
            return []
        start = page_indexes[0]
        end = page_indexes[1]
        while start < end:
            new_page.append(data[start])
            start += 1

        return new_page


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
        A tuple of size 2 containing the start index and end index to be used
        for pagination
    """

    end_index = page_size * page
    start_index = end_index - page_size
    return (start_index, end_index)
