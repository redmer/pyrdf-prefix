from pyoxigraph import NamedNode

from pyrdf_namespaces.namespace import PredefinedNamespace


class SD(PredefinedNamespace):
    """SPARQL 1.1 Service Description"""

    # Conversion-Date: 2024-09-30T10:48+00:00
    # Source: https://www.w3.org/ns/sparql-service-description.ttl

    _nsBaseIri = "http://www.w3.org/ns/sparql-service-description#"
    _issueWarning = True
    _withContainerMembershipProperty = False
    _nonPyIdentifiers = ()

    Aggregate: NamedNode
    """An instance of sd:Aggregate represents an aggregate that may be used in a SPARQL aggregate query (for instance in a HAVING clause or SELECT expression) besides the standard list of supported aggregates COUNT, SUM, MIN, MAX, AVG, GROUP_CONCAT, and SAMPLE."""
    BasicFederatedQuery: NamedNode
    """sd:BasicFederatedQuery, when used as the object of the sd:feature property, indicates that the SPARQL service supports basic federated query using the SERVICE keyword as defined by SPARQL 1.1 Federation Extensions."""
    Dataset: NamedNode
    """An instance of sd:Dataset represents a RDF Dataset comprised of a default graph and zero or more named graphs."""
    DereferencesURIs: NamedNode
    """sd:DereferencesURIs, when used as the object of the sd:feature property, indicates that a SPARQL service will dereference URIs used in FROM/FROM NAMED and USING/USING NAMED clauses and use the resulting RDF in the dataset during query evaluation."""
    EmptyGraphs: NamedNode
    """sd:EmptyGraphs, when used as the object of the sd:feature property, indicates that the underlying graph store supports empty graphs. A graph store that supports empty graphs MUST NOT remove graphs that are left empty after triples are removed from them."""
    EntailmentProfile: NamedNode
    """An instance of sd:EntailmentProfile represents a profile of an entailment regime. An entailment profile MAY impose restrictions on what constitutes valid RDF with respect to entailment."""
    EntailmentRegime: NamedNode
    """An instance of sd:EntailmentRegime represents an entailment regime used in basic graph pattern matching (as described by SPARQL 1.1 Query Language)."""
    Feature: NamedNode
    """An instance of sd:Feature represents a feature of a SPARQL service. Specific types of features include functions, aggregates, languages, and entailment regimes and profiles. This document defines five instances of sd:Feature: sd:DereferencesURIs, sd:UnionDefaultGraph, sd:RequiresDataset, sd:EmptyGraphs, and sd:BasicFederatedQuery."""
    Function: NamedNode
    """An instance of sd:Function represents a function that may be used in a SPARQL SELECT expression or a FILTER, HAVING, GROUP BY, ORDER BY, or BIND clause."""
    Graph: NamedNode
    """An instance of sd:Graph represents the description of an RDF graph."""
    GraphCollection: NamedNode
    """An instance of sd:GraphCollection represents a collection of zero or more named graph descriptions. Each named graph description belonging to an sd:GraphCollection MUST be linked with the sd:namedGraph predicate."""
    Language: NamedNode
    """An instance of sd:Language represents one of the SPARQL languages, including specific configurations providing particular features or extensions. This document defines three instances of sd:Language: sd:SPARQL10Query, sd:SPARQL11Query, and sd:SPARQL11Update."""
    NamedGraph: NamedNode
    """An instance of sd:NamedGraph represents a named graph having a name (via sd:name) and an optional graph description (via sd:graph)."""
    RequiresDataset: NamedNode
    """sd:RequiresDataset, when used as the object of the sd:feature property, indicates that the SPARQL service requires an explicit dataset declaration (based on either FROM/FROM NAMED clauses in a query, USING/USING NAMED clauses in an update, or the appropriate SPARQL Protocol parameters)."""
    SPARQL10Query: NamedNode
    """sd:SPARQL10Query is an sd:Language representing the SPARQL 1.0 Query language."""
    SPARQL11Query: NamedNode
    """sd:SPARQL11Query is an sd:Language representing the SPARQL 1.1 Query language."""
    SPARQL11Update: NamedNode
    """sd:SPARQLUpdate is an sd:Language representing the SPARQL 1.1 Update language."""
    Service: NamedNode
    """An instance of sd:Service represents a SPARQL service made available via the SPARQL Protocol."""
    UnionDefaultGraph: NamedNode
    """sd:UnionDefaultGraph, when used as the object of the sd:feature property, indicates that the default graph of the dataset used during query and update evaluation (when an explicit dataset is not specified) is comprised of the union of all the named graphs in that dataset."""
    availableGraphs: NamedNode
    """Relates an instance of sd:Service to a description of the graphs which are allowed in the construction of a dataset either via the SPARQL Protocol, with FROM/FROM NAMED clauses in a query, or with USING/USING NAMED in an update request, if the service limits the scope of dataset construction."""
    defaultDataset: NamedNode
    """Relates an instance of sd:Service to a description of the default dataset available when no explicit dataset is specified in the query, update request or via protocol parameters."""
    defaultEntailmentRegime: NamedNode
    """Relates an instance of sd:Service with a resource representing an entailment regime used for basic graph pattern matching. This property is intended for use when a single entailment regime by default applies to all graphs in the default dataset of the service. In situations where a different entailment regime applies to a specific graph in the dataset, the sd:entailmentRegime property should be used to indicate this fact in the description of that graph."""
    defaultGraph: NamedNode
    """Relates an instance of sd:Dataset to the description of its default graph."""
    defaultSupportedEntailmentProfile: NamedNode
    """Relates an instance of sd:Service with a resource representing a supported profile of the default entailment regime (as declared by sd:defaultEntailmentRegime)."""
    endpoint: NamedNode
    """The SPARQL endpoint of an sd:Service that implements the SPARQL Protocol service. The object of the sd:endpoint property is an IRI."""
    entailmentRegime: NamedNode
    """Relates a named graph description with a resource representing an entailment regime used for basic graph pattern matching over that graph."""
    extensionAggregate: NamedNode
    """Relates an instance of sd:Service to an aggregate that may be used in a SPARQL aggregate query (for instance in a HAVING clause or SELECT expression) besides the standard list of supported aggregates COUNT, SUM, MIN, MAX, AVG, GROUP_CONCAT, and SAMPLE"""
    extensionFunction: NamedNode
    """Relates an instance of sd:Service to a function that may be used in a SPARQL SELECT expression or a FILTER, HAVING, GROUP BY, ORDER BY, or BIND clause."""
    feature: NamedNode
    """Relates an instance of sd:Service with a resource representing a supported feature."""
    graph: NamedNode
    """Relates a named graph to its graph description."""
    inputFormat: NamedNode
    """Relates an instance of sd:Service to a format that is supported for parsing RDF input; for example, via a SPARQL 1.1 Update LOAD statement, or when URIs are dereferenced in FROM/FROM NAMED/USING/USING NAMED clauses."""
    languageExtension: NamedNode
    """Relates an instance of sd:Service to a resource representing an implemented extension to the SPARQL Query or Update language."""
    name: NamedNode
    """Relates a named graph to the name by which it may be referenced in a FROM/FROM NAMED clause. The object of the sd:name property is an IRI."""
    namedGraph: NamedNode
    """Relates an instance of sd:GraphCollection (or its subclass sd:Dataset) to the description of one of its named graphs. The description of such a named graph MUST include the sd:name property and MAY include the sd:graph property."""
    propertyFeature: NamedNode
    """Relates an instance of sd:Service to a resource representing an implemented feature that extends the SPARQL Query or Update language and that is accessed by using the named property."""
    resultFormat: NamedNode
    """Relates an instance of sd:Service to a format that is supported for serializing query results."""
    supportedEntailmentProfile: NamedNode
    """Relates a named graph description with a resource representing a supported profile of the entailment regime (as declared by sd:entailmentRegime) used for basic graph pattern matching over that graph."""
    supportedLanguage: NamedNode
    """Relates an instance of sd:Service to a SPARQL language (e.g. Query and Update) that it implements."""
