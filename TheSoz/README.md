# TheSoz

[TheSoz](http://lod.gesis.org/thesoz/en.html) is an ontology in the field of \topic{Social Science*. It is maintained by [GESIS - Leibniz Institute for the Social Sciences](https://www.gesis.org), who started developing it in 2009. It is used to categorise the content in Social
Science Research Information System (SOFIS) and Social Science Literature Information System [(SOLIS)](https://git.gesis.org/open-data/solis-sofis/blob/18389fb2b6cecd7fe8d5b6b4e89d40eda33a7191/readme.md), which respectively describe research projects and scientific literature in this field.



TheSoz consists of 8,223 concepts distributed on a six-levels polyhierarchical structure. 


TheSoz ontology is entirely built using SKOS (*skos:*). The concepts are arranged within the hierarchical structure via the *skos:broader* and *skos:narrower* relations. 
Each concept (*skos:Concept*) is described according to a set of properties. Their labels are identified either with *skos:prefLabel* or *skos:altLabel*, for the preferred and the alternative labels, which are available in up to four languages: English, German, Russian and French.
*skos:historyNote* provides additional historical information. *skos:related* identifies similar concepts within the same concept scheme. Instead, with regard to identifying similar concepts in external classification schemes, TheSoz is mapped to *DBpedia*, *Agrovoc*, and *STW*  using *skos:relatedMatch* and *skos:exactMatch* relations. Specifically, the former identifies just related concept, while the latter indicates that the two concepts can be used interchangeably.



TheSoz can be browsed from its Linked Open Data portal\footnote{Linked Open Data portal of [TheSoz](http://lod.gesis.org/thesoz/en.html). This portal supports content negotiation and allows users to browse concepts in RDF/XML, RDF-TURTLE and N-Triples. TheSoz can be also downloaded for [free](http://lod.gesis.org/download-thesoz.html) with a Creative Commons Attribution-Non Commercial-No Derivs 3.0 (CC BY-NC-ND 3.0).