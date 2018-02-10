import string
from nltk.corpus import wordnet
from nltk.tokenize import  word_tokenize
from nltk.corpus import stopwords
f = open("QUERIES_for_training.302-450","r")
fout = open("QUERIES_for_training_Expanded.302-450","w", encoding="utf-8")
stop_words=set(stopwords.words("english"))
while 1:
    line=f.readline()
    if not line:
        break
    line=line.replace('\n','')
    line= line.split(" ",1)
    new_line=line[0]
    line[1]=line[1].lower()
    line[1]=line[1].translate(str.maketrans('','',string.punctuation))
    word_tokens = word_tokenize(line[1])
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    synonyms=[]

    count=0
    for x in filtered_sentence:
        
        for syn in wordnet.synsets(x):
            for l in syn.lemmas() :
                if(count<3):
                    if l.name() not in synonyms:
                        synonyms.append(l.name())
                        count+=1
                        
        count=0
        
    synonyms_string=' '.join(synonyms)
    new_line=" ".join([str(new_line),synonyms_string])
    synonyms=[]
    fout.write(new_line)
    fout.write('\n')

		
f.close()
fout.close()

