"""
"""

class AuthenticationError(Exception):
    pass

class InternalServerError(Exception):
    pass

class BadRequestError(Exception):
    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return repr(self.reason)

class NotFoundError(Exception):
    pass
