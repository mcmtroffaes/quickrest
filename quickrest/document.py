"""Creating ReST documents."""

import quickrest.table

class Document:
    def __init__(self):
        self.children = []

    def add_table(self, header_fields):
        table = quickrest.table.Table(header_fields)

    def write(self, stream):
        for child in self.children:
            child.write(stream)
