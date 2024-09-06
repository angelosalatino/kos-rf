# Subject Resource Application Ontology

The [Subject Resource Application Ontology](https://github.com/FAIRsharing/subject-ontology) is an ontology describing a variety of academic disciplines. It is produced by [FAIRsharing](https://fairsharing.org) to help organising their digital library, consisting of data standards, databases and data policies. It was initially developed in 2018 and constantly updated every year. 

FAIRsharing built SRAO using classes from publicly-available ontologies and controlled vocabularies such as
*DFG*, 
*EDAM*,
*AgroVoc*, and additional ontologies available in OBO such as
[*NCI Thesaurus*](https://ncit.nci.nih.gov/ncitbrowser/),
[*Ontology for microRNA*](https://github.com/OmniSearch/omit),
[*Ontology for Biomedical Investigations*](http://obi-ontology.org), and
[*Plant Ontology*](https://browser.planteome.org/amigo).


Currently, SRAO contains 425 concepts distributed on a seven-levels polyhierarchial structure. At the top level of SRAO we can find *Engineering Science*, *Humanities and Social Sciences*, and *Natural Science*. Then, these subjects branch off in several sub-concepts such as *Computer Science*, *Energy Engineering*, *Materials Engineering* and *Systems Engineering* under *Engineering Science*. 


SRAO builds on RDF Schema (*rdfs:*) and [OBO](http://purl.obolibrary.org/obo/) (*obo:*). The relations 
*rdfs:label* and *rdfs:comment* are used to provide respectively the label and the description of a concept.
The parent-child relationships are identified with the *rdfs:subClassOf* relation.
With the internally defined relationships, it is possible to  describe the provenance of the concept *obo:IAO\_0000412*, to define the concept *obo:IAO\_0000115*, and also to provide alternative terms with *obo:IAO\_0000118*.





SRAO can be downloaded in OWL (serialised as RDF/XML) for free with a CC-BY 4.0 licence from their GitHub repositories.