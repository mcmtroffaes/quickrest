"""Simple ReST table."""

class Table:
    def __init__(self, header_fields):
        self.header_fields = header_fields
        self.rows = []

    def add_row(self, row):
        row = [elem for elem in row]
        if len(row) != len(self.header_fields):
            raise ValueError("row has wrong length")
        self.rows.append(row)

    def sort(self, header_fields=None, reverse=False):
        if header_fields is None:
            header_fields = self.header_fields
        indices = [self.header_fields.index(field) for field in header_fields]
        key = lambda row: tuple(row[index] for index in indices)
        self.rows = sorted(self.rows, key=key, reverse=reverse)

    def __str__(self):
        result = ""
        field_maxlen = [len(field) for field in self.header_fields]
        for row in self.rows:
            for i, field in enumerate(row):
                field_maxlen[i] = max(field_maxlen[i], len(str(field)))
        separator = " ".join(
            "{0:=<{1}}".format("", maxlen)
            for field, maxlen in zip(self.header_fields, field_maxlen)
            )
        result += separator
        result += "\n"
        result += " ".join(
            "{0: <{1}}".format(field, maxlen)
            for field, maxlen in zip(self.header_fields, field_maxlen))
        result += "\n"
        result += separator
        result += "\n"
        for row in self.rows:
            result += " ".join(
                "{0: <{1}}".format(field, maxlen)
                for field, maxlen in zip(row, field_maxlen))
            result += "\n"
        result += separator
        return result
