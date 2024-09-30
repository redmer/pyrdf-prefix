# pyrdf-namespaces

This project provides a `Namespace` class and instances of them for many popular RDF vocabularies.
It is designed to be used with pyoxigraph.

## Usage

```py
from pyoxigraph import NamedNode
from pyrdf_namespaces import Prefix

EX = Prefix('https://example.org/ns#')
assert EX.Sponge == NamedNode('https://example.org/ns#Sponge')
assert EX['Crusty-Crab'] == NamedNode('https://example.org/ns#Crusty-Crab')
```

It also predefines many well-known prefixes, like `rdf`, `
