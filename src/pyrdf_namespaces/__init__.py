from dataclasses import dataclass
from functools import lru_cache

from pyoxigraph import NamedNode


@dataclass(slots=True, frozen=True)
class Namespace:
    """
    Alias a namespace prefix with Namespace. Useful to prevent yourself from writing a
    certain prefix URL over and over.

    This class basically concatenates the namespace and lname strings. Access the set
    namespace value with `Namespace.value`.

    Usage:
        >>> from pyrdf_namespaces import Namespace
        >>> ex = Namespace("http://example.org/ns#")
        >>> ex.Foo
        NamedNode(value='http://example.org/ns#Foo')
        >>> ex['Bar-Baz']
        NamedNode(value='http://example.org/ns#Bar-Baz')

        Do not use the method accessor to generate a NamedNode when the suffix starts
        and ends with `__`, e.g., `Namespace("http://example.org/python/").__bool__`.

        >>> py = Namespace("http://example.org/python/")
        >>> py.__bool__
        AttributeError: Use the ns[...] syntax for dunder namespaced terms.
        >>> py["__bool__"]
        NamedNode(value='http://example.org/python/__bool__', termType='NamedNode')
    """

    value: str

    @lru_cache()
    def expand_with(self, name: str) -> NamedNode:
        """Add `name` to the namespace prefix."""
        return NamedNode(self.value + name)

    def __getitem__(self, name: str) -> NamedNode:
        """
        Return a NamedNode for `ns[key]`, as an alternative to the `ns.key` syntax if
        `key` is not a valid Python identifier OR is a dunder name.
        """
        return self.expand_with(name)

    def __getattr__(self, name: str) -> NamedNode:
        """Return a NamedNode for `ns.key`."""
        # Only called for non-existing attributes, unlike __getattributes__
        # so not-implemented Python protocols should be skipped
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError("Use the ns[...] syntax for dunder namespaced terms.")
        return self.expand_with(name)

    def __repr__(self) -> str:
        return f"Namespace({self.value})"


__all__ = ["Namespace"]
