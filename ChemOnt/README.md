# ChemOnt

[ChemOnt](http://classyfire.wishartlab.com) is a comprehensive ontology in the field of *Chemistry* containing chemical classes of organic and inorganic compounds to characterise research papers and other scientific items. ChemOnt was developed and is currently maintained by the Wishart Research Group at the University of Alberta (CA) with the support of the [Metabolomics Innovation Centre](https://www.metabolomicscentre.ca). ChemOnt is adopted by several online databases such as [PubChem](https://pubchem.ncbi.nlm.nih.gov), [DrugBank](http://www.drugbank.ca), [HMDB](http://www.hmdb.ca), [ECMDB](http://www.ecmdb.ca), [YMDB](http://www.ymdb.ca), [T3DB](http://www.t3db.ca), [ChEBI](https://www.ebi.ac.uk/chebi), [LIPID MAPS](https://www.lipidmaps.org), and [MassBank of North America](http://mona.fiehnlab.ucdavis.edu).


Its latest version (v2.1), which dates back to 2016, includes 4825 concepts arranged in an eleven-levels monohierarchical structure.
It has been designed taking inspiration from the original Linnaean biological taxonomy, classifying chemical concepts based on shared characteristics (paper in repo). At the top level, we find the two main *Kingdoms*: *organic compounds* (whose structure contains at least one carbon atom) and *inorganic compounds* (which lack carbon–hydrogen bonds). At the second, third and fourth level there are respectively superclasses, classes and subclasses, organising the different compounds at different levels of granularity. At further lower levels, there are even more specialised compounds.

ChemOnt describes each concept according to an identifier (e.g., *CHEMONTID:0002448* for *Benzenoids*), and a set of properties such as name, description, url, parent node, number of chemical entities, and related concepts from other ontologies. Indeed, ChemOnt is mapped to *ChEBI*, *LIPID MAPS*, and partially mapped to the *MeSH* thesaurus.


ChemOnt can be browsed through its [web portal](http://classyfire.wishartlab.com/tax_nodes) which supports content negotiation and allows users to retrieve entities in JSON.
Also, it can be download for free, in OBO format and JSON, however the authors retain all copyright. 