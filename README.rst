quickrest provides methods for easily generating restructured text in Python.

For instance::

    from quickrest.document import Document
    doc = Document()
    doc.add_chapter("Hello")
    doc.add_paragraph("Just to say hello.")
    doc.add_section("World")
    table = doc.add_table(["name", "age"])
    table.add_row(["Karl", 31])
    table.add_row(["Marcus", 2])
    print(doc)

will print::

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
