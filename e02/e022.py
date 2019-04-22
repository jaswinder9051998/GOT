from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import urllib
import requests
import numpy as np
import matplotlib.pyplot as plt
import re


comment_words=' '
stopwords=set(STOPWORDS)
f=open('e02.txt','r+')
ff=open('e02ww.txt','w')
txt=f.read().replace('\n',' ')
txt=re.sub("[[].*[]]",'',txt)
#txt=re.sub('.*[:]','',txt)
txt=txt.replace(':',' ')
txt=txt.replace('.',' ')
txt=txt.replace('-',' ')
txt=txt.replace('>',' ')
txt=txt.replace('?',' ')
txt=txt.replace(',',' ')
txt=txt.replace('TYRION',' ')
txt=txt.replace('SOLDIER',' ')
txt=txt.replace('CHUCKLE',' ')
txt=txt.replace('JAIME',' ')
txt=txt.replace('BRIENNE',' ')
txt=txt.replace('well',' ')
for i in range(10):
    txt=txt.replace(str(i),' ')
txt=txt.replace('\t',' ')

txt=re.sub(' +', ' ',txt)
print(txt)
    

mask = np.array(Image.open(requests.get('http://www.clker.com/cliparts/1/7/8/0/11949912622133772893chesspieces-rook.svg.hi.png', stream=True).raw))
 
def generate_wordcloud(words, mask):
    word_cloud = WordCloud(width = 800, height =400, background_color='black',stopwords=STOPWORDS, mask=mask).generate(words)
    #plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
    word_cloud.to_file('castle.png')
    plt.figure(figsize=(20,10), facecolor ='k', edgecolor='black')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    
#Run the following to generate your wordcloud
generate_wordcloud(txt, mask)
