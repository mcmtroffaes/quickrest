from __future__ import division, absolute_import, print_function

import nose.tools

from quickrest.table import Table

def test_table_init():
    table = Table(["name", "age"])
    table.add_row(["John", 3])
    table.add_row(["Bob", 9.2])
    table.add_row(["Alice", 107])
    nose.tools.assert_equal(str(table), """\
===== ===
name  age
===== ===
John  3  
Bob   9.2
Alice 107
===== ===""")
