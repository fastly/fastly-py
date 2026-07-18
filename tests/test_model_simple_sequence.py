import pytest
from fastly.model.domains_response import DomainsResponse


def test_domains_response_iteration_and_indexing():
    data = [{'name': 'a'}, {'name': 'b'}, {'name': 'c'}]
    d = DomainsResponse(data, _check_type=False)

    # len
    assert len(d) == 3

    # list conversion
    assert list(d) == data

    # indexing
    assert d[0] == data[0]
    assert d[1] == data[1]

    # slicing
    assert d[1:3] == data[1:3]

    # iteration via for
    out = []
    for it in d:
        out.append(it)
    assert out == data


def test_domains_response_empty_and_single():
    # empty
    d_empty = DomainsResponse([], _check_type=False)
    assert len(d_empty) == 0
    assert list(d_empty) == []

    # single non-sequence value should be iterable as single item
    d_single = DomainsResponse({'k': 'v'}, _check_type=False)
    assert len(d_single) == 1
    assert list(d_single) == [{'k': 'v'}]
