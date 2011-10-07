import nose.tools

from quickrest.document import Document

def test_document():
    doc = Document()
    doc.add_chapter("Hello")
    doc.add_paragraph("Just to say hello.")
    doc.add_section("World")
    table = doc.add_table(["name", "age"])
    table.add_row(["Karl", 31])
    table.add_row(["Marcus", 2])
    nose.tools.assert_equal(str(doc), """\
Hello
=====

Just to say hello.

World
-----

====== ===
name   age
====== ===
Karl   31 
Marcus 2  
====== ===""")
