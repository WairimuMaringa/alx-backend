#!/usr/bin/env python3
"""
Copy from task zero and implement a method that takes two
int args with default value 1 and 10
"""
import math
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popullar baby names.
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
        """ get page containing data. """
        assert(isinstance(page, int) and isinstance(page_size, int))
        assert(page > 0 and page_size > 0)
        [start, end] = index_range(page, page_size)
        return self.dataset()[start: end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return tuple. """
    return ((page - 1) * page_size, page * page_size)
