# KNOWMAK


[KNOWMAK](https://gate.ac.uk/projects/knowmak/) is a broad scheme covering many areas of Science that are funded from the [European Research Area (ERA)](https://ec.europa.eu/info/research-and-innovation/strategy/strategy-2020-2024/our-digital-future/era_en). It is structured in two main ontologies: Key Enabling Technology (KET) and Societal Grand Challenge (SGC). KNOWMAK is the outcome of a project funded by the European Commission within the H2020 Framework under Grant No. 726992, which main partner is the University of Sheffield. These ontologies were developed to act as a bridge between the data sources (research publications, patents and research projects) and user queries (paper in repo).

In this report, we will focus our analysis onto the Key Enabling Technology as they describe research topics. Specifically, KET includes 72 concepts and 3,725 related terms arranged in a three-level polyhierarchical structure.
At the top level we can find *Advanced manufacturing technology*, *Advanced materials*, *Industrial biotechnology*, *Micro- and nano-electronics*, *Nanoscience and technology*, *Optics and photonics*. From these top-level areas, it further breaks down into more specific concepts.

KNOWMAK builds on an [in-house schema](http://www.gate.ac.uk/ns/ontologies/knowmak/) (*knowmak:*), OWL, RDF, RDFS, and SKOS. Every topic is a *owl:Class*, and the hierarchical structure between topics is defined with the *rdfs:subClassOf* relation. KNOWMAK identifies the labels and preferred labels among the various keywords with the *rdfs:label* and  *rdfs:prefLabel* relations. It reuses from the KNOWMAK schema the relations *knowmak:keywords*, *knowmak:patentKeywords*, and *knowmak:projectKeywords* for defining the set of relevant keywords for the topics, *knowmak:provenance* for defining the provenance of the topics, *knowmak:topicID* for defining their identifiers, and *knowmak:description* and *rdf:Description* for providing a comprehensive descriptions of the topics.

Currently KET is mapped to [*EUPRO subject index*](http://web.archive.org/web/20200927090111/https://www.risis2.eu/wp-content/uploads/2016/09/Report-Task-6-EUPRO.pdf). 

KNOWMAK, including both KET and SGC, can be downloaded from the [project website](https://gate.ac.uk/projects/knowmak/) in JSON and RDF with a CC BY-NC-SA 3.0 licence.