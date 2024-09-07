# EDAM

[EDAM](http://edamontology.org/page) (originally from "EMBRACE Data and Methods") is an ontology in the field of *Bioinformatics* describing topics, operations, data, and formats. It is developed by the [Institut Français de Bioinformatique](https://www.france-bioinformatique.fr), [ELIXIR Norway](https://elixir.no) and the [Network of European Bioimage Analysts](http://eubias.org/NEUBIAS), and it is supported by a wide network of contributors. 
EDAM is developed for supporting the search, publication and integration of bioinformatics tools and resources.

As already mentioned, EDAM differentiates between topics, operations, data, and formats. In this report, we will focus only on the topic section. In particular, it contains 264 concepts distributed over a polyhierarchical structure of 7 levels. 
At the top level, we find *Bioinformatics* topics such as *Biology*, *Chemistry*, *Biomedical science*, *Computational biology*, *Laboratory techniques*, *Omics*, *Medicine*, as well as other extrinsic roots such as *Physics*, *Mathematics*, *Experimental design and studies*, *Computer science*, *Informatics*, and *Literature and language*. These topics are further split in sub-topics from generic to specific.

EDAM builds on OWL (*owl:*), RDFS (*rdfs:*), and [OBO Format metamodel
](http://www.geneontology.org/formats/oboInOwl) (*oboInOwl:*). Indeed, every topic is an *owl:Class*, and the hierarchical structure between topics is defined with *rdfs:subClassOf*. Each topic is described with further properties, such as *rdfs:label* for the label, *oboInOwl:hasDefinition* for the definition of the topic, *oboInOwl:hasHumanReadableId* for a human-readable identifier, *oboInOwl:hasBroadSynonym* for broad synonyms, *oboInOwl:hasNarrowSynonym* for narrow synonyms, *oboInOwl:inSubset* to state wether it is a topic, format, operantion or data. Topics in EDAM are also mapped to external sources and ontologies such as Wikipedia and *MeSH*.

The EDAM ontology can be downloaded for free under the CC BY-SA 4.0 licence, and it is available in OWL, CSV and TSV.