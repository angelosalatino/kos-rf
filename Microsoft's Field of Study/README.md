# Microsoft's Field of Study


Microsoft's Field of Study contains more than 704K concepts across all fields of Science. New concepts were added to this taxonomy every two weeks based on new papers. However, the whole hierarchical structure was recomputed only twice per year: end of June and December. 
This biannual update made sure that the structure of the taxonomy remains as stable as possible. As a result, newly discovered concepts can be bereft of parents for a certain period of time (up to 5.5 months).

The Fields of study taxonomy is organised in a polyhierarchical structure across 6 levels.

The top level includes 19 academic fields: *Art*, *Biology*, *Business*, *Chemistry*, *Computer science*, *Economics*, *Engineering*, *Environmental science*, *Geography*, *Geology*, *History*, *Materials science*, *Mathematics*, *Medicine*, *Philosophy*, *Physics*, *Political science*, *Psychology*, *Sociology*.

The process of generating this taxonomy is semi-automatic. The top two levels are manually generated, while the four remaining ones are automatically generated. This process consists of three steps: discovering concepts, tagging them to publications, and building the hierarchy (papers in repo). In the first phase, they leverage Wikipedia and all academic publications to identify valid entities that can represent subjects of study. In the second phase, they perform a multi-label classification in which each publication is classified with multiple fields of science. This is accomplished by firstly creating vector representations of both concepts and papers and then computing all pairwise confidence scores between concepts and publications pairs, using the cosine similarity between those vectors. In the third phase, they build the hierarchy using the subsumption approach, i.e., a concept *x* is parent of *y* if *y* occurs only in a subset of documents in which also *x* occurs in.

Through the web it is possible to find several dumps containing the most recent version of this taxonomy, such as on Zenodo [https://doi.org/10.5281/zenodo.2628216](https://doi.org/10.5281/zenodo.2628216).

Despite this, on May 2021, Microsoft announced that it is discontinuing its Microsoft Academic Graph database from the end of 2021. A nonprofit organisation, [OurResearch](https://ourresearch.org), set up the OpenAlex project, replacing MAG. 