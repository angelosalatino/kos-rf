# UNESCO Thesaurus

The [UNESCO Thesaurus](http://vocabularies.unesco.org/browser/thesaurus) is a classification scheme covering several areas of Science. It is developed by the UNESCO and it is used to categorise the UNESCO Digital Library as well as libraries of many other organisations and institutions across the world. It was initially published in 1977 within a books and now it is updated regularly with minor amendments to the various concepts.

This taxonomy consists of over 4K unique concepts organised in a six-level polyhierarchical taxonomy. The top level includes seven main research areas: *Education*, *Science*, *Culture*, *Social and human sciences*, *Information and communication*, *Politics, law and economics*, and *Countries and country groupings*.  These groups of broad areas further branch off with more specific concepts.

The UNESCO Thesaurus builds on SKOS and thus the hierarchical structure is described using the  *skos:broader* and *skos:narrower* relations. Concepts (*skos:Concept*) are described according to several relations, such as *skos:altLabel*, *skos:prefLabel*, and *skos:hiddenLabel* which respectively define the various synonyms, the preferred label, and misspelled variants of the labels. Aside from English, those labels are also available in other languages, such as Russian, French, Arabic, and Spanish. 
Additional relations are *skos:related*, which defines the related concepts, and *skos:topConceptOf*, which identifies top concepts.
The UNESCO Thesaurus also reuses the *dct:created* and *dc:modified* relations from Dublin Core to define when a concept has been created and modified.

The UNESCO Thesaurus can browsed through its dedicated portal, which supports content negotiation and hence concepts can also be browsed in RDF/XML, TTL, and JSON-LD. From the same portal, it is possible to download the thesaurs for free in RDF/XML and TTL with a CC BY-SA 3.0 IGO licence.