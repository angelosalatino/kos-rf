# Open Biological and Biomedical Ontology (OBO)

The Open Biological and Biomedical Ontology (OBO) is a compendium of interoperable ontologies in the fields of *Biology* and *Biomedicine*. These ontologies are created and maintained by the OBO Foundry, which is a consortium of biologists with a thorough knowledge of the underlying science. 
Many datasets are currently annotated using these ontologies, such as [ArrayExpress database](https://www.ebi.ac.uk/arrayexpress/) and [Scientific Data ISA-explorer](http://scientificdata.isa-explorer.org).

OBO features more than 250 different ontologies including the well-known *Chemical Entities of Biological Interest* (CHEBI), *Gene Ontology* (GO), *Phenotypic Quality Ontology* (PATO), *Protein Ontology* (PRO), *Xenopus Anatomy Ontology* (XAO), *Zebrafish Anatomy Ontology* (ZFA) and others. 


Altogether, those ontologies count over 5.3 million unique entities distributed in a polyhierarchical structure (even if some ontologies are organised in a monohierarchic structure).

These ontology describes their entities using RDF (*rdf:*),  RDF Schema (*rdfs:*), and OBO Format metamodel (*oboInOwl:*).
%using RDF and RDF Schema data model. 
In particular, each concept is described with a set of particular properties, such as label (*rdfs:label*), the class (*rdf:type*), hierarchical relationships (*rdfs:subClassOf*), and domain-dependent properties like mass, formula and others.
Some ontologies cross-reference their entities with entities of other ontologies using the *rdfs:seeAlso* or *oboInOwl:hasDbXref*.

The largest ontology in terms of concepts is *NCBI organismal classification* (NCBITaxon), an ontology representation of the NCBI organismal taxonomy, with around 2 million unique entities and depth of 38 levels. 
The second-largest ontology is *Gazetteer* (gaz), a large, ontologically-oriented resource listing place names which can be treated as instances of environments, with 662K concepts and depth of 5 levels.
The deepest ontology, with 39 levels, is the *Vertebrate Taxonomy Ontology* (vto), providing a comprehensive hierarchy for extant and extinct vertebrates.

OBO ontologies can also be queried using the [Ontobee SPARQL endpoint](http://www.ontobee.org/sparql) developed by the University of Michigan.

All these ontologies are primarily available in OWL format, even though some of them can also be downloaded in different formats (JSON-LD, TTL, OBO). 
They can be individually fetched from the OBO Foundry website or all at once using [OBO Foundry’s crawler](https://github.com/OBOFoundry/OBO-Dashboard).