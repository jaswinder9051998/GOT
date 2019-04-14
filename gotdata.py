import praw
import numpy as np
import csv
from praw.models import MoreComments
import re
output=open('gotdata.txt', "w")
#writer = csv.writer(output)
#csv = open('gotdata.csv', "w")
#file1 = open("gotdata.txt","w",encoding="utf-8")
reddit=praw.Reddit(client_id='8R5NyRW6dRxADQ',client_secret='QOooOWKyqBbYzbhJhbQPnnFXTq0',
                   username='jasssinghhira',password='retter',user_agent='gotdata1')

subreddit=reddit.subreddit('gameofthrones')
hot_gameofthrones=subreddit.hot(limit=2)
i=0
for submission in hot_gameofthrones:
    if(i!=0):
        print(submission.title)
        comments=submission.comments
        submission.comments.replace_more(limit=30)
        for comment in submission.comments.list():
            thisbody=comment.body
            try:
                #mm=list(thisbody.split(' '))
                output.write(thisbody)
                #output.writerow(mm)
                #ll=list(thisbody.split(' '))
                #for l in ll:
                #    csv.write(l)#writer.writerow(line)
            except Exception as e:
                print("left")
                continue
    i+=1


	

