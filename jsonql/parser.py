# -*- coding: utf-8 -*-

from .exceptions import InvalidError, ErrOps, ErrSql


class SQLParser(object):

    def __init__(self):
        """Only support SELECT operator.

        >>> parser = SQLParser()
        >>> statement = parser.parse("select * from todolist")
        >>> statement
        <Statement: SELECT * FROM todolist>
        """
        pass

    def parse(self, sql):
        if not isinstance(sql, str):
            raise InvalidError(ErrSql, sql)
        return self._parse(sql)

    def _parse(self, sql):
        """Parse SQL statement.
        """
        sp = sql.split()
        return Statement(*sp)


class Statement(object):
    """SQL Statement"""

    def __init__(self, ttype, key, what, where):
        self.ttype = ttype.upper()
        if self.ttype not in ['SELECT']:
            raise InvalidError(ErrOps, self.ttype)
        self.key = key
        self.what = what.upper() if what else 'FROM'
        self.where = where

    def __str__(self):
        return "{0}: {1} {2} {3} {4}".format(
            self.__class__.__name__, self.ttype, self.key, self.what,
            self.where)

    def __repr__(self):
        return "<{}>".format(str(self))
