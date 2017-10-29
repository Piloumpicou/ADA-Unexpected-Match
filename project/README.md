# Title

# Abstract
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?

# Research questions
A list of research questions you would like to address during the project. 

# Dataset
List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

For now, there are two datasets which seem to be of interest for our project:

- the 'Million Song Dataset' (MSD), which is the main dataset we will be working on

The files of the MSD are in HD5 format: most likely existing code snippets to handle this format/convert it to some other format which can then be processed using python/...
There are 54 attributes per song; we have yet to see which will be the most relevant for our study.

The dataset can be found at:
https://labrosa.ee.columbia.edu/millionsong/pages/getting-dataset

- possibly the 'musiXmatch dataset'
Although it is not listed in the proposed datasets, this dataset is strongly linked to the MSD, since it contains descriptions to the lyrics related to the MSD songs (roughly 779K songs covered).
The lyrics are provided as a bag of stemmed words, with the top words per song. One of the main reason behind this representation choice is that the official lyrics are copyright protected.

This dataset can be found at :
http://labrosa.ee.columbia.edu/millionsong/musixmatch

# A list of internal milestones up until project milestone 2
Add here a sketch of your planning for the next project milestone.

- Provide a way to handle the dataset easily 
(among others, getting familiar with the work already performed on this dataset: maybe existing code snippets we can reuse?)
- Explore the dataset: produce basic statistics to get a global overview of the dataset
- Define which are the most relevant features we will keep for our future analysis
- Find interestings ways of vizualising the data and our results 
- ...

# Questions for TAa
Add here some questions you have for us, in general or project-specific.

Would it be worthwhile to analyse the corresponding audio? 
(if yes, what would be good existing libraries or tools for this task?)
