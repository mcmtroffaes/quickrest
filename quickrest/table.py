"""Creating ReST documents."""

class Table:
    def __init__(self, header_fields):
        self.header_fields = header_fields
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def write(self, stream):
        field_maxlen = [len(field) for field in header_fields]
        for row in self.rows:
            for i, field in enumerate(row):
                field_maxlen[i] = max(field_maxlen[i], len(field))
        stream.writeln(
            " ".join(
                "{0:1}".format(field, maxlen)
                for field, maxlen in zip(self.header_fields, field_maxlen))
            )
        stream.writeln(
            " ".join(
                "{=:1}".format(maxlen)
                for field, maxlen in zip(self.header_fields, field_maxlen))
            )
