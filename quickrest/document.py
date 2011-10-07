"""Creating ReST documents."""

import quickrest.table

class Document:
    def __init__(self):
        self.children = []

    def add_chapter(self, title):
        self.children.append(
            "{0}\n{1:=<{2}}".format(title, "", len(title)))

    def add_section(self, title):
        self.children.append(
            "{0}\n{1:-<{2}}".format(title, "", len(title)))

    def add_subsection(self, title):
        self.children.append(
            "{0}\n{1:~<{2}}".format(title, "", len(title)))

    def add_paragraph(self, text):
        self.children.append(str(text))

    def add_table(self, header_fields):
        table = quickrest.table.Table(header_fields)
        self.children.append(table)
        return table

    def __str__(self):
        return "\n\n".join(str(child) for child in self.children)
