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


