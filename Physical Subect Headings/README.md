# Physical Subject Headings (PhySH)

The Physical Subject Headings (PhySH)](https://physh.aps.org) is an ontology that focus on the field of *Physics*. It is maintained by the [American Physical Society (APS)](https://www.aps.org) and it is used for indexing papers on [Physical Review](https://journals.aps.org) and [ArXiv](https://arxiv.org). The latest version of this ontology dates back to January 2019, according to the official [Github repository](https://github.com/physh-org/PhySH).
This classification scheme is crowdsourced with the support of authors, reviewers, editors and organisers of scientific conferences, so that it is constantly updated with new terms.

The current version contains a total of 3,749 concepts in a polyhierarchical structure of six levels. 

At the top level PhySH contains 18 concepts, also considered disciplines: *Plasma Physics*, 
*APS Taxonomy*, 
*Gravitation, Cosmology \& Astrophysics*, 
*Accelerators \& Beams*, 
*Statistical Physics*, 
*Polymers \& Soft Matter*, 
*Atomic, Molecular \& Optical*, 
*Fluid Dynamics*, 
*Condensed Matter \& Materials Physics*, 
*General Physics*, 
*Nonlinear Dynamics*, 
*Interdisciplinary Physics*, 
*Networks*, 
*Biological Physics*, 
*Particles \& Fields*, 
*Physics Education Research*, 
*Nuclear Physics*, 
*Quantum Information*. 
Then, PhySH further breaks down these disciplines into more narrow concepts.

These concepts are also distributed in 9 facets, i.e., broad groupings of concepts according to the general role they serve, such as *Research Areas*, *Physical Systems*, *Experimental Techniques*, *Properties*, *Techniques*, *Computational Techniques*, *Professional Topics*, *Theoretical \& Computational Techniques*, *Theoretical Techniques*. 

PhySH buils on SKOS (*skos:*), Dublin Core (*dcterms:*) and its [own schema](https://physh.org/rdf/2018/01/01/core\#) (the PhySH Schema, *physh:*). Each concept (*skos:Concept*) is described with respect to a set of properties such as label (*skos:prefLabel*), alternative labels (*skos:altLabel*), unique ID (a URI, e.g., [https://doi.org/10.29172/4e293f33-f391-4a15-ac67-df2603d45f17](https://doi.org/10.29172/4e293f33-f391-4a15-ac67-df2603d45f17) for *Electomagnetism*), and broader and narrower concepts (using *skos:broader* and *skos:narrower*) to create hierarchies of concepts. 

Instead, a discipline (*physh:Discipline*) has a title (*dcterms:title*), a brief description (*dcterms:description*), the publisher (*dcterms:publisher*), as well as the list of all its concepts (*physh:hasConcept*). One concept may belong to more than one discipline as well as more than one facet (*physh:Facet*). 


This ontology is available for download in JSON-LD, RDF Turtle, N-Triples, and RDF/XML format from the Github repository mentioned above with a CC0 1.0 Universal public domain dedication licence. 