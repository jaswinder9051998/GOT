from wordcloud import WordCloud,STOPWORDS
comment_words=' '
stopwords=set(STOPWORDS)
f=open('gotdata.txt','r+')
txt=f.read().replace('\n','')
wordcloud=WordCloud(width=800,height=800,background_color='white',stopwords=stopwords,min_font_size=10).generate(txt)
wordcloud.to_file('got.png')
