import pytest
from pyoxigraph import NamedNode
from pyrdf_namespaces import Namespace


def test_basics():
    ex = Namespace("http://example.org/ns#")

    assert ex.Foo == NamedNode(value="http://example.org/ns#Foo")
    assert ex["Bar-Baz"] == NamedNode(value="http://example.org/ns#Bar-Baz")


def test_dunder_raise():
    py = Namespace("http://example.org/python/")

    with pytest.raises(AttributeError):
        py.__bool__

    py["__bool__"]
