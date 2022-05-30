class EmptyDatabaseError(Exception):

    # Exception raised when database is empty

    def __init__(self, message="Database file is empty"):
        self.message = message
        super().__init__(self.message)


class EmptyTableError(Exception):

    # Exception raised when database table is empty

    def __init__(self, message="Table is empty"):
        self.message = message
        super().__init__(self.message)


class InvalidQueryError(Exception):

    # Exception raised when query is invalid

    def __init__(self, message):
        self.message = message
        super().__init__("InvalidQuery: {}".format(self.message))


class ValidationError(Exception):

    # Exception raised when parameter validation issue occurs

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


