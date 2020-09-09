
# coding: utf-8


import webbrowser


# In[ ]:

# Opens the given URL
webbrowser.open('https://en.wikipedia.org/wiki/Web_scraping')


# ### Downloading a web page with Request.get() function

# In[ ]:

import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')


# In[ ]:

type(res)


# In[ ]:

res.status_code == requests.codes.ok


# In[ ]:

print(res.text[:296])


# ### Check for errors

# In[ ]:

import requests
res = requests.get('https://marvelapp.com/asdf')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))


# In[ ]:



