import nose.tools

from quickrest.table import Table

def test_table():
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

def test_table_grid():
    table = Table(["full\nname", "age"])
    table.add_row(["John\nSmith\nJohnson", 3])
    table.add_row(["Bob", 9.2])
    table.add_row(["Alice", 107])
    nose.tools.assert_equal(table.gridstr(), """\
+-------+---+
|full   |age|
|name   |   |
+=======+===+
|John   |3  |
|Smith  |   |
|Johnson|   |
+-------+---+
|Bob    |9.2|
+-------+---+
|Alice  |107|
+-------+---+""")
