# -*- coding: utf-8 -*-

ErrOps = (0x0100, "invalid sql operate type, only support SELECT")
ErrSql = (0x0110, "invalid sql type, should be string")


class JsonqlError(Exception):
    pass


class ParserError(JsonqlError):
    pass


class BaseInvalidError(ParserError):

    def __init__(self, code=None, reson=None, stat=None):
        self.code = code
        self.reson = reson
        self.stat = stat

    def __str__(self):
        return "{0}: {1}. {2} ==> ({3} {4})".format(
            self.__class__.__name__, self.code, self.reson, self.stat,
            type(self.stat))

    def __repr__(self):
        return "<{}>".format(str(self))


class InvalidError(BaseInvalidError):
    """Invalid sql error"""

    def __init__(self, error, stat=None):
        code, reson = error
        super(InvalidError, self).__init__(code, reson, stat)
