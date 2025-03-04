"""test for make_slice.py."""

from __future__ import annotations

from make_slice import MakeSlice, make_slice


def test_make_slice_class() -> None:
    """Test the MakeSlice class."""
    data: list[int] = list(range(10))
    s: slice = MakeSlice()[::-1]
    assert data[s] == data[::-1]


def test_make_slice_object() -> None:
    """Test the make_slice object."""
    data: list[int] = list(range(10))
    s: slice = make_slice[::-1]
    assert data[s] == data[::-1]
