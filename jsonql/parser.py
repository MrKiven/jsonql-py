# -*- coding: utf-8 -*-


class SQLParser(object):

    def __init__(self):
        pass

    def parse(self, sql):
        assert isinstance(sql, str), "sql must be string"

    def _parse(self, sql):
        """Parse SQL statement.
        """


class Statement(object):
    """SQL Statement"""

    def __init__(self, ttype, value):
        self.ttype = ttype
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.__str__
