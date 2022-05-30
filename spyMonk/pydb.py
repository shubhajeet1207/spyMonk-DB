import json
import pathlib
import logging
import random
import webbrowser

from typing import Any, Callable, List, Dict, Tuple
from .sample import sample_database






class Pydb:
    def __init__(self, connection="pydb", tablename="spymonkdb"):
        """
        create new database in current directory
        if connection isnt found then new database
        is created
        """
        self.cached_bool = False
        self.cached = None
        self.filter_bool = False
        self.filter_cache = None
        self.connection = connection


    # query result retrievers

    def all(self):
        logging.debug("Getting all results")
        self.cached_bool = True
        result = self.cached
        if not result is None:
            return result
        else:
            return self.selectall()

    def limit(self, num):
        """limit number of results

        Args:
            num (int): number to limit too

        Returns:
            List[Dict[str, Any]]: return result
        """
        logging.debug("limit all results to {}".format(num))
        table = self.all()
        return table[0:num]

    def asc(self):
        """
        ORDER BY ASC
        """
        logging.debug("all results asc")
        return self.all()

    def desc(self):
        """
        ORDER BY DESC
        """
        logging.debug("all results desc")
        return self.all()[::-1]

    # query operators
    def and_(*args):
        logging.debug("not implemented")
        raise NotImplementedError()

    def or_(*args):
        logging.debug("not implemented")
        raise NotImplementedError()

    def not_(other):
        logging.debug("not implemented")
        raise NotImplementedError()

