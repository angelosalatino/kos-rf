# Agrovoc Thesaurus

The Agrovoc Thesaurus is an ontology in the field of *Agriculture*. Agrovoc was initially published at the beginning of the 1980s, by the Food and Agriculture Organisation (FAO) of the United Nations (UN), to index publications in agricultural science and technology. Nowadays, Agrovoc is a worldwide collaborative effort aiming at expanding its coverage, as well as adding or revising translations of concepts. Indeed, Agrovoc is one the few multilingual resources in this space, with subjects translated in up to 41 languages, such as Arabic, French, Italian, German, Japanese, Spanish, and many others.
Thanks to such a large-scale and collaborative effort, Agrovoc features monthly releases. 


The analysed version of Agrovoc contains around 41K unique concepts. Such concepts are arranged into a polyhierarchical structure consisting of 14 layers. AGROVOC top concepts are very general and high level, including *activities*, *organisms*, *subjects*, *locations*, *products*, *organism*, etc. The *subjects* concept is of interest in this analysis, which branches off into *cartography*, *gerontology*, *humanities*, *sciences*, *statistics as science*. Then, under *sciences* we can find all areas pertaining to the scope of *Agriculture*.

Each concept in the Agrovoc ontology is described according to a set of properties, using SKOS (*skos:*). In particular, *skos:broader* and *skos:narrower* are used to arrange the different concepts (*skos:Concept*) within the hierarchy. In addition, each concept has *skos:prefLabel* and *skos:altLabel* respectively used to identify the preferred and the alternative labels across the different languages. *skos:related* is used to identify similar concepts within the Agrovoc Thesaurus. *skos:exactMatch* and *skos:closeMatch* respectively identify similar and sufficiently similar concepts in external ontologies, like Wikidata, DBpedia, *Unesco Thesaurus*, and *Library of Congress Subject Headings*. 
Finally, *skos:scopeNote* is used to describe the concept in natural language.
In addition, the Agrovoc Thesaurus keeps track of changes using [Dublin Core](https://dublincore.org/specifications/dublin-core/dcmi-terms) (*dc:*), and specifically uses *dc:created* and *dc:modified* to annotate the date of creation and last modification of the concept.

Agrovoc can be browsed from the [Agrovoc Multilingual Thesaurus portal](https://agrovoc.fao.org/browse/agrovoc) as well as through its [Linked Open Data portal](http://aims.fao.org/aos/agrovoc/c_330829.html), which supports content negotiation and allows concepts to be browsed also in RDF/XML and Turtle formats. Agrovoc is also accessible through a [SPARQL endpoint](https://agrovoc.fao.org/sparql).

Agrovoc can be downloaded in RDF/XML from free from the [FAO website](http://www.fao.org/agrovoc/releases). However, only the content in English, Russian, French, Spanish, Arabic and Chinese is licenced under the international Creative Commons Attribution Licence (CC-BY IGO 3.0). Instead, copyrights of Agrovoc in other languages depend on the institutions who authored it.

Browse Agrovoc [Agrovoc Thesaurus](http://www.fao.org/agrovoc)