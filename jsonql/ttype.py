# -*- coding: utf-8 -*-


TTYPE = [
    'SELECT',
    'INSERT',
    'UPDATE',
    'DELETE'
]

ErrInvalidType = (0x0100, "invalid sql operate type")


class Error(Exception):
    pass


class ParserError(Error):
    pass


class InvalidError(ParserError):

    def __init__(self, code=None, reson=None, key=None, value=None):
        self.code = code
        self.reson = code
        self.key = key
        self.value = value

    def __str__(self):
        return "{0}: {1}, {2}, {3} ==> {4}".format(
            self.__class__.__name__, self.code, self.reson, self.key,
            self.value)


def raise_invalid_error(ttype, key, value):
    code, reson = ttype
    raise InvalidError(code, reson, key, value)
