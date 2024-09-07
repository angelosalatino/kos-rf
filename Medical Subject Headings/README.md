# Medical Subject Heading

The [Medical Subject Heading](https://www.nlm.nih.gov/mesh) (MeSH) is an ontology focussing on the field of *Medicine* and it is maintained by the National Library of Medicine (NLM) of the United States. It is currently used to index papers in PubMed (Medline), the NLM Catalog, and other NLM databases containing scientific records on *life sciences* and *biomedical* topics. National Library of Medicine manually curates MeSH and releases a new update every year, adding new terms as they appear in the scientific literature, as well as reorganising the structure of the ontology, by taking advantage of the support coming from the whole community of researchers.


The 2024 version of MeSH contains around 30K subjects, which are organised in 16 macro-categories: category *A* for *anatomic terms*, *B* for *organisms*, *C* for *diseases*, *D* for *chemicals and drugs*, up to category *Z* for *geographic locations* terms. Each category is further divided into subcategories, organised in a hierarchy from most general to most specific in up to thirteen hierarchical levels.

MeSH has a double identity, by simultaneously functioning as both monohierarchical taxonomy of descriptor codes and polyhierarchical ontology of subject headings.


In the ontological side of MeSH, each subject is described according to a set of parameters using its [own schema](http://id.nlm.nih.gov/mesh/vocab) (*mesh:*) and RDF Schema (*rdfs:*). In particular, each subject (*mesh:TopicalDescriptor*) has a label defined with *rdfs:label*, a description (*mesh:annotation*), a unique identifier (*mesh:identifier*), as well as chronological information such as date of creation (*mesh:dateCreated*), date of when it became effective (*mesh:dateCreated*), and date of last revision (*mesh:dateRevised*).  

The hierarchical structure is defined by means of *mesh:broaderDescriptor* which defines broader subjects.
In addition, subjects are associated to concepts (*mesh:Concept*) which correspond to a class of terms which are synonymous with each other. One or more concepts can be related to one another (*mesh:relatedConcept*) where one is neither broader nor narrower in meaning.
 
Within the subject descriptions there is also the tree number (*mesh:treeNumber*), which represents the point of connection with the monohierarchical side of MeSH. They are alphanumerical codes acting as roadmaps that allow to locate the MeSH terms within the tree. 

In this tree, terms are arranged in a hierarchy from the most general to the most specific, and each one of them gets assigned the alphanumerical code that indicates its location within the tree. For instance, for *Diabetes Mellitus*, at time of writing, the code is *C18.452.394.750*. Each triplet of characters, delimited by a dot, is the specific sub-branch that needs to be unfolded, for reaching the desired code. In the particular case of *Diabetes Mellitus*, it is necessary to unfold the *Nutritional and Metabolic Diseases* *C18* sub-branch, then *Metabolic Diseases* *C18.452*, *Glucose Metabolism Disorders* *C18.452.394*, and *Diabetes Mellitus* *C18.452.394.750*. In general, each specific code prepends the code of its direct general concept.

Considering that MeSH is *de facto* polyhierarchical, many subject headings may appear in more than one place in the tree. Each instance of the same term has a different code based on the branch it belongs.

For instance, *Anemia, Iron-Deficiency* has two tree numbers: *C15.378.071.196.300* and *C18.452.565.100* because we can find it under *Anemia, Hypochromic*~*C15.378.071.196* and *Iron Metabolism Disorders*~*C18.452.565*, respectively. In this case, the whole sub-branch, including *Anemia, Iron-Deficiency* and its narrow concepts, is replicated under both *Anemia, Hypochromic* and *Iron Metabolism Disorders*. For the sake of redundancy, all narrower concepts will have at least the same amount of codes of their broader concepts.



The deepest concept at level thirteen is *Cercocebus atys* having unique Id: D016665 ([Cercocebus atys](https://meshb.nlm.nih.gov/record/ui?ui=D016665)) and tree number: *B01.050.150.900.649.313.988.400.112.199.120.120.110*. 



The National Library of Medicine website provides a [SPARQL endpoint](https://id.nlm.nih.gov/mesh/query) where it possible to use SPARQL language to query and retrieve information about every single concept in MeSH.

MeSH can be downloaded for free from the NLM website in N-Triples (as RDF format), XML, ASCII, MARC format.