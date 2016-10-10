"""
"""

class FastlyError(Exception):
    pass

class AuthenticationError(FastlyError):
    pass

class InternalServerError(FastlyError):
    pass

class BadRequestError(FastlyError):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return repr(self.reason)

class NotFoundError(FastlyError):
    pass
