import nose.tools

from quickrest.lst import Lst

def test_lst():
    lst = Lst()
    lst.add_item("hello")
    lst.add_item("world")
    nose.tools.assert_equal(str(lst), """\
* hello
* world""")
