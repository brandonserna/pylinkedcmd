from pylinkedcmd import usgsweb


def test_get_staff_inventory_pages():
    uw = usgsweb.UsgsWeb()
    get_pages = uw.get_staff_inventory_pages()
    assert uw
    assert type(get_pages) == list
    assert len(get_pages) > 200