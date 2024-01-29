#!/usr/bin/env python3
"""Defining a class Server and a function"""
import csv
import math
from typing import List, Tuple, Dict, Any


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
        """returns data in a specified page"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        names_of_page = []
        start_index, end_index = index_range(page, page_size)
        names_list = self.dataset()

        for name in names_list[start_index:end_index]:
            names_of_page.append(name)
        return names_of_page

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing key-value pairs of page
        informations"""
        page_infos: Any = {}
        names_of_page = self.get_page(page, page_size)

        page_infos['page_size'] = len(names_of_page)
        page_infos['page'] = page
        page_infos['data'] = names_of_page
        page_infos['next_page'] = page + 1 if len(names_of_page) > 0 else None
        page_infos['prev_page'] = page - 1 if page > 1 else None
        page_infos['total_pages'] = math.ceil(len(self.dataset()) / page_size)

        return page_infos


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
