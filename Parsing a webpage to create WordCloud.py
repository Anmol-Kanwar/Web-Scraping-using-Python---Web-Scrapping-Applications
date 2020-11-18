

import bs4
from bs4 import BeautifulSoup
from lxml import html
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt 


page = requests.get('http://changingminds.org/disciplines/job-finding/resume/resume_power_words.htm') 



type(page) 



page = bs4.BeautifulSoup(page.text,'lxml')


type(page)


hi= page.select('title') # selecting title
hi

hi[0]

words=page.select('.quote') # selecting target class 
words


for i in page.select('.quote'): 
    print(i.text)     



i.text


cloud = WordCloud(background_color="white",max_words=300).generate(i.text)


plt.figure( figsize=(10,8) )
plt.imshow(cloud)
plt.title('Power Words for Resume')
plt.axis('off')
plt.show()


# In[ ]:



