# Eurovoc

[EuroVoc](https://op.europa.eu/en/web/eu-vocabularies) is a multidisciplinary ontology covering the activities of the European Parliament, and it is maintained by the Publications Office of the [European Commission](https://op.europa.eu/en/home). Concepts are available in the main 23 languages of the European Union. 

EuroVoc consists of 7,439 concepts arranged in a six-levels polyhierarchical structure.
The top level includes 21 categories: *Politics*, *International Relations*, *European Union*, *Law*, *Economics*, *Trade*, *Finance*, *Social Questions*, *Education And Communications*, *Science*, *Business And Competition*, *Employment And Working Conditions*, *Transport*, *Environment*, *Agriculture, Forestry And Fisheries*, *Agri-foodstuffs*, *Production, Technology And Research*, *Energy*, *Industry*, *Geography*, *International Organisations*.

The EuroVoc ontology is built using SKOS (*skos:*). It defines the hierarchical structure by means of *skos:broader* and *skos:narrower* relations. It provides labels in all twenty-six languages with *skos:prefLabel* and *skos:altLabel*  relations.
Each concept is assigned to a unique code using the *skos:notation*  relation. Finally, the  *skos:editorialNote* relation allow editors to add additional information about the concepts.
The ontology uses also some relationships from Dublin Core (*dc:*). Specifically, it uses *dc:created* to specify the date of creation of a given concept. The *dc:modified* specifies when it has been modified, and *dc:replaces* specifies it a given concept is replacing another one.

EuroVoc is mapped to several other classification schemes via the *skos:relatedMatch* and *skos:exactMatch* relations. These include *Library of Congress Subject Headings*, *AgroVoc*, *STW*, *TheSoz*, *Unesco*, *MeSH*, *Wikidata* and others.

The [European Commission website](https://op.europa.eu/en/web/eu-vocabularies) allow users to browse EuroVoc, as well as download it in RDF/XML, MarcXML, Excel with a CC-BY 4.0 licence.