"""Simple ReST table."""

class Table:
    def __init__(self, header_fields):
        self.header_fields = header_fields
        self.rows = []

    def add_row(self, row):
        row = [str(elem) for elem in row]
        if len(row) != len(self.header_fields):
            raise ValueError("row has wrong length")
        self.rows.append(row)

    def __str__(self):
        result = ""
        field_maxlen = [len(field) for field in self.header_fields]
        for row in self.rows:
            for i, field in enumerate(row):
                field_maxlen[i] = max(field_maxlen[i], len(field))
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
