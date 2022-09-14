## Prompt Engineering: In-context learning with GPT-3 (LLM)

#### Project Overview

A client has a system that collects news artifacts from web pages, tweets, facebook posts, etc. The client is interested in scoring a given new artifact against a topic. The client has hired experts to score a few of these news items in the range from 0 to 10; a score of 0 means the news item is totally NOT relevant while a score of 10 means the news item is very relevant. The range of results between 0 and 10 signifies the  degree of relevance of the news item to the topic.
The client wants to explore how useful existing LLMs such as GPT-3 are for this task. You are hired as a consultant to explore the efficiency of GPT3-like LLMs to this task. If your recommendation is positive, you must demonstrate that your strategies to design prompts are reproducible and produce a consistent result.
You should also set up an MLOps pipeline that helps automate the task of using different LLMs and different topics. Your pipeline should also allow future improvements in the prompt design to be integrated without breaking the system. A centralized log system should be incorporated into your pipeline to help monitor outputs, cost, performance, and other relevant artifacts.
Why this project?
The complexity, cost, and skills required to produce LLMs is immense. Only larger companies and other international groups are able to train LLMs at the size of hundreds of billions of parameters. Given the benefit of LLMs to drive business and society, it is useful to learn to use these monster AI models for multiple use in business and social problems.
The need for specialized skills in prompt engineering will grow fast as more and and more companies start building their business around LLMs and similar products such as DALL-E 2, MidJourney, Bloom, etc.

#### Data
There are two datasets you will use for this project

##### Data 1:

This data comes from the client described above.  The columns of this data are as follows

Domain - the base URL or a reference to the source these item comes from
Title - title of the item - the content of the item
Description - the content of the item
Body - the content of the item
Link - URL to the item source (it may not functional anymore sometime)
Timestamp - timestamp that this item was collected at
Analyst_Average_Score -  target variable - the score to be estimated
Analyst_Rank - score as rank
Reference_Final_Score - Not relevant for now - it is a transformed quantity


##### Data 2:


The data are job descriptions ( together named entities)  and  relationships between entities in json format. To understand more about where the data comes from, read How to Train a Joint Entities and Relation Extraction Classifier using BERT Transformer with spaCy 3 | by Walid Amamou | Towards Data Science

Dataset 1: For development and training
Dataset 2: For testing and final reporting


#### Skills:
Accessing Deep Learning Models using APIs
Prompt Engineering
Formulating and designing test and training strategies
Central Logging systems
MLOps  with DVC, CML, and MLFlow

#### Knowledge:
Deep Learning algorithms: transformers, attention, multi-head attention
Machine learning
Hyperparameter tuning
Model comparison & selection
Experiment analysis
data privacy, data security, ethical use of data. The 8 principles of responsible machine learning

#### notebooks
#### Entity Extraction
Extract name entities from text using only a few examples.

<img src="https://raw.githubusercontent.com/cohere-ai/notebooks/main/notebooks/images/keyword-extraction-gpt-models.png" style="width:100%; max-width:400px" alt="Extract name entities from text using only a few examples" />
