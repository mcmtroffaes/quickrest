"""Creating ReST documents."""

import itertools
import quickrest.table
import quickrest.lst
import textwrap

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
        self.children.append(text)

    def add_table(self, header_fields):
        table = quickrest.table.Table(header_fields)
        self.children.append(table)
        return table

    def add_lst(self):
        lst = quickrest.lst.Lst()
        self.children.append(lst)
        return lst

    def add_verbatim(self, text):
        self.add_paragraph("::")
        lines = text.splitlines()
        self.add_paragraph(
            u"\n".join(
                itertools.chain(
                    *(textwrap.wrap(
                        line,
                        width=80,
                        initial_indent=u'  ',
                        subsequent_indent=u'  ') if line else [u'']
                      for line in lines))))

    def page_break(self):
        self.add_paragraph("""
.. raw:: pdf

   PageBreak

""")

    def add_spacer(self, x, y):
        self.add_paragraph("""
.. raw:: pdf

   Spacer {0} {1}

""".format(x, y))

    def __str__(self):
        return "\n\n".join(str(child) for child in self.children)

    def __nonzero__(self):
        return bool(self.children)

    def writepdf(self, filename, args=None):
        """Export document to a pdf file."""
        import rst2pdf.createpdf
        if args is None:
            args = []
        if not filename.endswith(".pdf"):
            txtfile = filename + ".txt"
        else:
            txtfile = filename.replace(".pdf", ".txt")
        with open(txtfile, "wb") as stream:
            stream.write(str(self))
        rst2pdf.createpdf.main([txtfile] + args)

    def writehtml(self, filename):
        """Export document to a html file."""
        from docutils.core import publish_string
        with open(filename, "wb") as stream:
            stream.write(publish_string(source=str(self), writer_name="html"))
