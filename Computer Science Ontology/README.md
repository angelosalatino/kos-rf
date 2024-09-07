# Computer Science Ontology

The Computer Science Ontology (CSO) is a large-scale ontology of research areas that was automatically generated using the Klink-2 algorithm on a dataset of about 16 million publications in the field of *Computer Science*. It is developed and maintained by the [SKM team](http://skm.kmi.open.ac.uk) at the Open University in collaboration with Springer Nature. It used by Springer Nature for classifying conference proceedings in the field of Computer Science. It is also adopted by various organisations for annotating courses and characterising domain experts.

CSO is an ongoing project and with the support of a community of practitioners, it gets constantly updated with new revisions. Currently, it includes more than 14K topics and 163K semantic relationships. It mainly focuses on the field of *Computer Science*; however, since the corpus had  the algorithm inferred topics and relationships also in other fields, such as *Linguistics*, *Geometry*, *Semantics*, and others. 
CSO is organised in a thirteen-level polyhierarchical structure.

The [CSO data model](http://cso.kmi.open.ac.uk/schema/cso) (prefix *cso:*) is an extension of SKOS. 
Each topic is a *rdf:type* instance of *cso:Topic*, which is a subclass of *skos:Concept*, and has its label identified by *rdfs:label*. All topics are interlinked between each other through three relationships: *cso:superTopicOf*, *cso:relatedEquivalent*, *cso:preferentialEquivalent*. 
*cso:superTopicOf* is a subproperty of *skos:narrower*, indicating that a topic is a super-area of another one (e.g., *Semantic Web* is a super-area of *Linked Data*). *cso:relatedEquivalent* is a subproperty of *skos:related*, indicating that two topics can be treated as equivalent for the purpose of exploring research data (e.g., *Ontology Matching* and *Ontology Mapping*). 
The relationship *cso:preferentialEquivalent* is also a sub-property of *skos:related*, but it states the main label for topics belonging to a cluster of *cso:relatedEquivalent*. For instance, the topics *Ontology Matching* and *Ontology Alignment* both have their *cso:preferentialEquivalent* set to *Ontology Matching*. 

Finally, *cso:contributesTo* indicates that the research output of one topic contributes to another. 
For instance, research in Ontology Engineering contributes to Semantic Web, but arguably Ontology Engineering is not a sub-area of Semantic Web – that is, there is plenty of research in Ontology Engineering outside the Semantic Web area.

Additional relationships in CSO include: 
* *owl:sameAs* for mapping CSO topics to equivaled entities in other knowledge graphs (DBpedia, Freebase, Wikidata, YAGO, and Cyc), and 
* *schema:relatedLink* for linking CSO concepts to relevant web pages that either describe the research topics (Wikipedia articles) or provide additional information about the research domains (Microsoft Academic).


The Computer Science Ontology is available for download in various formats (N-Triples, OWL, TTL, and CSV) from the [CSO Portal](https://cso.kmi.open.ac.uk), under the [Creative Commons Attribution 4.0 International Licence (CC BY 4.0)](https://creativecommons.org/licences/by/4.0).



Springer Nature and The Open University launch a unique Computer Science Ontology [https://group.springernature.com/it/group/media/press-releases/springer-nature-and-the-open-university-launch-a-unique/16386730](https://group.springernature.com/it/group/media/press-releases/springer-nature-and-the-open-university-launch-a-unique/16386730)