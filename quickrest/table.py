"""Creating ReST documents."""

from __future__ import division, absolute_import, print_function

class Table:
    def __init__(self, header_fields):
        self.header_fields = header_fields
        self.rows = []

    def add_row(self, row):
        row = [str(elem) for elem in row]
        if len(row) != len(self.header_fields):
            raise ValueError("row has wrong length")
        self.rows.append(row)

    def write(self, stream):
        field_maxlen = [len(field) for field in self.header_fields]
        for row in self.rows:
            for i, field in enumerate(row):
                field_maxlen[i] = max(field_maxlen[i], len(field))
        separator = " ".join(
            "{0:=<{1}}".format("", maxlen)
            for field, maxlen in zip(self.header_fields, field_maxlen)
            )
        print(separator, file=stream)
        print(
            " ".join(
                "{0: <{1}}".format(field, maxlen)
                for field, maxlen in zip(self.header_fields, field_maxlen)),
            file=stream,
            )
        print(separator, file=stream)
        for row in self.rows:
            print(
                " ".join(
                    "{0: <{1}}".format(field, maxlen)
                    for field, maxlen in zip(row, field_maxlen)),
                file=stream,
                )
        print(separator, file=stream)
