# <font size=111 color="#0094ff"> 2018's Best hit Recipe </font>

# Abstract
<!--
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?
-->

How amazing would it be to have your own song played in front of thousands of people for the first time (like during Balélec!) and a few weeks later, it figures in the top hits of the summer 2018 although you are absolutely not gifted for music ?!

But despite having no artistic talent, we have a few data science analysis skills and would like to use them in order to fulfil our dream. We will explore the Million Song Dataset, which contains an impressive selection of songs descriptions. We will also correlate it with a few other datasets related to it in order to gather as many features as possible on what makes a song successful.

In the end, we want to find the best ingredients making a song popular. Since we are not yet worldwide well-known artists, we will need to work mostly on "unknown" artists having produced popular songs.

# Research questions
<!--
A list of research q)uestions you would like to address during the project. 
-->

- What kind of correlation can we find between popular (hotness) songs and loudness, energy, danceability, key, pitch, tempo, ...

- Where does the (popular) music come from ? (geographically) Can we visualize how the music is 'linked', throughout the world ?

- Was the music better before ? Are there more "bad song" today than in the nineties ?

# Dataset
<!--
List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.
-->

For now, there are four datasets which seem to be of interest for our project:

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

- The Echo Nest Taste Profile Subset
This dataset is linked to the first one as well. It provides triplets of [user - song - play count]

- R2 - Yahoo! Music User Ratings of Songs with Artist, Album, and Genre Meta Information, v. 1.0
This dataset can be obtain on demand for a research purpose only. It could be very useful to integrate the ratings of songs in our data.


# A list of internal milestones up until project milestone 2
<!--
Add here a sketch of your planning for the next project milestone.
-->
  
- 1-5 November: 
  - get access to the data and the cluster, install libraries if needed
  - provide a way to handle the dataset easily 
               
- 6-12 November:
  - make some research on work that could be useful for our project already done on the MSD 
  - explore the different datasets, get a global overview of them using basic statistics

- 13-19 November:
  - dive more deeply into the datasets and the analysis of the data
  - take care of missing value, find the most popular songs, the most popular autors, ...
             
- 20-26 November:
  - select the useful data, the most relevant features for the analysis
  - think about interestings ways of vizualising the data and the results
  - plan for milestone 3, in order to find the most popular songs and their characteristic features

# Questions for TAa
<!--
Add here some questions you have for us, in general or project-specific.
-->

Would it be worthwhile to analyse the corresponding audio? 
(if yes, what would be good existing libraries or tools for this task?)
(And secondly, do you know someone involved in the music program of Balélec?)
