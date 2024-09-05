# Art and Architecture Thesaurus

The [Art and Architecture Thesaurus](http://web.archive.org/web/20210616235001/https://www.getty.edu/research/tools/vocabularies/aat/about.html) (AAT) is an ontology describing concepts within the field of *Art and Architecture*. The development of AAT started in 1970 and was mainly driven by the necessity of art libraries and art journal indexing services to start automatising their cataloguing and indexing systems. Nowadays, AAT is used by museums, art libraries, archives, catalogers, and researchers in art and art history. 

It is currently maintained by the Getty Research Institute and it is available in English and Chinese. The latter has been developed in collaboration with the Taiwan e-Learning and Digital Archives Program (TELDAP). 

The AAT describes work types, roles, materials, styles, cultures, techniques, disciplines, and other fields in a work record. 
Specifically, it contains more than 58K concepts distributed over a polyhierarchical structure of 13 levels. 
The hierarchical structure of AAT is subdivided in eight facets, containing homogeneous classes of concepts, and hence sharing characteristics that distinguish them from members of other classes. The eight facets are: *Associated Concepts*, *Styles and Periods*, *Agents*, *Activities*, *Materials*, *Objects*, *Brand Names*, and *Physical Attributes*. Then, each facet is divided in further subclasses. 

The facet of interest for the scope of this survey, is the *Activities* facet, which, among other concepts (such as events, functions, processes and techniques), models the disciplines of interest.
These span across several knowledge domains relevant for *Arts and Architecture* such as *Humanities* and *Social Sciences*, but also cross-disciplinary fields, such as *Computer Vision* and *Natural History*.


AAT builds on the [Getty Vocabulary Program ontology](http://vocab.getty.edu/ontology) (the GVP ontology, *gvp:*) which on its turn is built upon RDF, RDFS, SKOS (*skos:*), OWL, Dublin Core and Prov-O. Owing to such rich ontology, each entity in AAT is described according to a multitude of characteristics. %Indeed, just to describe to describe all possible nuances of the hierarchical structure,
Indeed, just the hierarchical structure is described using twelve semantic relationships, which can be split into two groups. The first group consists of semantic relationship that connect one concept with its direct broaders, and it includes: 
*gvp:broader*, 
*gvp:broaderGeneric*,
*gvp:broaderInstantial*, 
*gvp:broaderPartitive*, 
*gvp:broaderPreferred*, 
*broaderNonConcept*
and *gvp:broaderNonPreferred*,
The second group contains the extended version of the previous relationships, connecting entities with all its ancestors up until root, and it consists of: 
*gvp:broaderExtended*, 
*gvp:broaderGenericExtended*, 
*gvp:broaderInstantialExtended*,
*gvp:broaderPartitiveExtended*, and 
*gvp:broaderPreferredExtended*. 

In addition, each entity is described according to a set of alternative labels and the preferred label. AAT uses the Dublin Core for describing when an entity has been created and modified, the source, the applied licence, and its contributors.


Almost 1K entities are mapped through *skos:exactMatch* to the *Library of Congress Subject Headings*.

AAT can be browsed from the [Getty linked open data portal](http://vocab.getty.edu/aat), which offers content negotiation and allows users to retrieve entitie in HTML, Turtle, NTriples, JSON and JSONLD. The whole AAT is available for download in NTriples format under the ODC-BY licence.