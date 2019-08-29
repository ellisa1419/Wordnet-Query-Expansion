# Wordnet-Query-Expansion

Information Retrieval Project.

I have expanded TREC queries by Wordnet by adding synonyms for every token  after removing stop words, and lemmatizing.
I have used used Lucene Search engine to compare the search results with baseline results.

I have used Python NLTK to use Wordnet database to expand the query.


# EDIT
This repository got more famous than I expected and I got so many emails and messsages from students to better understand my code.

Hence, here are my brief steps to explain what I did:

1) I have used TREC data (https://trec.nist.gov/data.html)  as a dataset here. The data, which are old newspaper articles from Financial Times, is still copyrighted, and hence not available on any public sites but can easily be achieved for educational purposes.



2) I have used https://github.com/isoboroff/trec-demo code to index and search the documents. This is bit old code and one needs to understand whole code and do minor tweaks to make it run.



3) My code https://github.com/ellisa1419/Wordnet-Query-Expansion is used to read queries and use wordnet to add synonyms for the query.



4) I repeated step 2 to query the same documents using expanded queries this time and compare the results with baseline results.



5) I saw some improvement in small queries but no luck in large queries.



If you have more questions please let me know. mail me : ellisa.khoja@gmail.com
