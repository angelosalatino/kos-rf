# OpenAlex Topics

OpenAlex Topics is a new system of topics and labels which can be used to accurately and succinctly describe what a paper is about. The new entity (Topics) ensures a one-to-one relationship between the topics and the higher levels of fields. 

The subfields, fields, and domains are from Scopus’s ASJC structure and give users an established structure that they might be familiar with. As opposed to other systems that apply ASJC at the journal level, OpenAlex will be applying the topics at the paper level which gives an increased level of granularity. Each topic will belong to one subfield, which will belong to one field, which will belong to one domain. 


The only missing link in creating this structure was how to connect the topics provided by CWTS to the ASJC structure. To solve this problem in an automated way, OpenAlex used a Large Language Model (LLM) to assign topics to the most likely field and using that selection, the LLM then selected the most likely subfield. This allowed our team to efficiently connect the two separate pieces of data in a way that did not make someone go through over 4,000 topics and manually assign them to a subtopic. 


[External repo](https://github.com/ourresearch/openalex-topic-classification)
