from make_slice import MakeSlice, make_slice


def test_make_slice_class():
    data: list[int] = list(range(10))
    s: slice = MakeSlice()[::-1]
    assert data[s] == data[::-1]

def test_make_slice_object():
    data: list[int] = list(range(10))
    s: slice = make_slice[::-1]
    assert data[s] == data[::-1]
