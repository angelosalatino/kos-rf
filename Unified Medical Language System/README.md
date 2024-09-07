# Unified Medical Language System (UMLS)

The [Unified Medical Language System (UMLS)](https://www.nlm.nih.gov/research/umls) is a collection of vocabularies in the fields of *Biomedicine*. It is developed and maintained by the National Library of Medicine (NLM) of the United States and it is intended for developers to design new software systems in this field, such as retrieval of patients records and question-answering systems, and others.

Currently, UMLS features more than 200 source vocabularies including *MeSH*, *Clinical Proteomic Tumor Analysis Consortium* (CPTAC), *International Classification of Primary Care* (ICPC), *Logical Observation Identifiers Names and Codes terminology* (LOINC), *RxNorm*, *SNOMED Clinical Terminology*, *Anatomical Therapeutic Chemical Classification System*, and many others. UMLS it is also multilingual, because for a number of vocabularies, it integrates their different languages. For instance, in UMLS we can find 16 different versions of *MeSH*: English, Italian, Japanese, Spanish, French, German, Norwegian, Polish, Portuguese and other several languages.

All UMLS vocabularies were combined together by identifying equivalent entities available in the different sources and mapping them with synonym relations. This approach allowed the development of a meta-thesaurus, without imposing any restriction on the structure and the content of the different vocabularies.
The U.S. National Library of Medicine releases a new version of UMLS every 6 months, typically in May and November of each year. The latest version is 2021AA released in May 2021.

We obtained and analysed the version 2018AB. In particular, we identified more than 4 million unique concepts arranged in a polyhierarchical structure of thirty levels.

Each concept is identified with a CUI (Concept Unique Identifier) which is linked to the equivalent concepts in the different source vocabularies.
%andf it exists through its linkage towards the concepts in the different source vocabularies that are equivalent. 
For instance, the concept *C0040132* is designated for *thyroid*, and aggregates concepts from *MeSH* (code: *D013961*, label: *thyroid*), *Library of Congress Subject Headings* (code: *U004685*, label: *Thyroid gland*), *Alcohol and Other Drug Thesaurus* (code: *0000002716*, label: *thyroid*), *Foundational Model of Anatomy Ontology* (code: *9603*, label: *Glandula thyroidea*), and others. A concept in UMLS can also define its preferred label as well as its synonyms. 

Concepts in UMLS are also related to each other according to a set of relationships, such as either broader or narrower relationship, related and possibly synonymous, related but unspecified, has sibling relationship in source vocabulary, and not related. For instance, the concept *thyroid***C0040132* is broader of *C562769* (*Thyroid Dyshormonogenesis 3*); at the same time, is narrower of *C0014136* (*Endocrine System*) and it is related with *C0599541* (*thyroid transplantation*). All these relationships might be further refined according to a set of additional 595 ones, such as *component\_of*, *derives\_from*, *effect\_may\_be\_inhibited\_by*, *gene\_associated\_with\_disease*, *gene\_plays\_role\_in\_process*, *has\_causative\_agent*, *disease\_mapped\_to\_gene* and many others. 
For instance, the concept *C0004561* (*B-Lymphocytes*) and *C4682402* (*Efizonerimod*) are connected with *chemical\_or\_drug\_affects\_cell\_type\_or\_tissue*

To download UMLS users are required to sign an agreement with the U.S. National Library of Medicine. However, academics might use it for free if used for research purposes. UMLS is available in Rich Release Format (RRF) and Original Release Format (ORF) formats and the package includes scripts that easily allow users to load it into a MySQL database.

[List of source vocabularies contained in UMLS](https://www.nlm.nih.gov/research/umls/sourcereleasedocs/index.html)