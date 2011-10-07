import nose.tools
from StringIO import StringIO

from quickrest.table import Table

def test_table_init():
    table = Table(["name", "age"])
    table.add_row(["John", 3])
    table.add_row(["Bob", 9.2])
    table.add_row(["Alice", 107])
    stream = StringIO()
    table.write(stream)
    nose.tools.assert_equal(
        stream.getvalue(), """\
===== ===
name  age
===== ===
John  3  
Bob   9.2
Alice 107
===== ===
""")
