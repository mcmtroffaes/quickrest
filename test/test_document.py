import nose.tools

from quickrest.document import Document

def test_document():
    doc = Document()
    nose.tools.assert_false(doc)
    doc.add_chapter("Hello")
    nose.tools.assert_true(doc)
    doc.add_paragraph("Just to say hello.")
    doc.add_section("World")
    table = doc.add_table(["name", "age"])
    table.add_row(["Karl", 31])
    table.add_row(["Marcus", 2])
    doc.add_verbatim("""Hello world!
How are things today?

Couldn't be better, thank you very much.""")
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
====== ===

::

  Hello world!
  How are things today?

  Couldn't be better, thank you very much.""")
