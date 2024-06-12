RAG stands for retrieval augmented generation.

we have a set of documents and we should be able to read all file formats and convert them into vector embedding. Also, we should able to query all those documents.

RAG Pipeline components:

1) Load datasource/Data Ingestion: File format could be .txt, .pdf, .xls, .md, etc. 

We do LTE (Load-Transform-Embed).
Load: Loading the data from different datasets.

Transform: Feature engineering. Here, we divide data into smaller chunks. e.g., A PDF has 10 pages, so we divide page by page. Because all the LLM models has context size. So based on the context size we need to send the data to LLM, hence we divide the orignal data into chunks.

Embed: Convert all the chunks of data into the vectors.


2) Vector Store: All these embedded vectors are stored inside the 'Vector Store Database'. Idea is, we should be able to query this database and get a proper response based on the context of the query.


4) Retrieve 'Most similar'




