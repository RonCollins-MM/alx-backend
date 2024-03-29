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
        Use assert to verify that both arguments are integers greater than 0
        Use index_range to find the correct indexes
        to paginate the dataset correctly
        and return the appropriate page of the dataset
        (i.e. the correct list of rows)
        """
        assert (isinstance(page, int) and isinstance(page_size, int)
                and page > 0 and page_size > 0)
        range = index_range(page, page_size)
        self.dataset()
        return self.__dataset[range[0]:range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Method that returns a hyperpage - pages containing data as well as
        metadata on the data.

        Parameters
        ----------
        page : int
            Current page number requested
        page_size : int
            Size of current page

        Returns
        -------
        dict
            The dictionary returned contains the following keys:
                * page_size: the length of the returned dataset page
                * page: the current page number
                * data: the dataset page (equivalent to return from previous
                task)
                * next_page: number of the next page, None if no next page
                * prev_page: number of the previous page, None if no previous
                page
                * total_pages: the total number of pages in the dataset as an
                integer

        """
        hyperm_page = {}
        total_pages = 0
        hyperm_page.update({'page': page})
        hyperm_page.update({'data': self.get_page(page, page_size)})
        hyperm_page.update({'page_size': len(hyperm_page['data'])})
        start_index = index_range(page, page_size)[0]
        if start_index <= 0:
            hyperm_page.update({'prev_page': None})
        else:
            hyperm_page.update({'prev_page': page - 1})
        end_index = index_range(page, page_size)[1]
        if end_index >= len(self.__dataset):
            hyperm_page.update({'next_page': None})
        else:
            hyperm_page.update({'next_page': page + 1})
        total_pages = math.ceil(len(self.__dataset) / page_size)
        hyperm_page.update({'total_pages': total_pages})

        return hyperm_page


def index_range(page, page_size):
    """
    function named index_range that takes two integer arguments:
    page and page_size.
    The function should return a tuple of size two containing:
    a start index and an end index corresponding to
    the range of indexes to return in a list
    for those particular pagination parameters.
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    previous = (page - 1) * page_size
    return (previous, previous + page_size)
