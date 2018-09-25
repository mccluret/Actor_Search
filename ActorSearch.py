import sys, requests, webbrowser, re, time
from bs4 import BeautifulSoup

start = time.time()

def actor_imdb_url():
   while True:
      actor = str(input('Please enter an actor: '))
      actor_link = actor.replace(' ','').lower()
      find = 'imdb'
      res = requests.get('http://google.com/search?q=' + actor_link)
      res.raise_for_status()
      soup = BeautifulSoup(res.text, 'lxml')
      
      try:
         links = soup.find_all('a', href=re.compile('imdb'))
         imdb_url = ('http://google.com'+(links[0].get('href')))
         return {'actor':actor,'url':imdb_url}
         break
      
      except:
         print('There is no imdb page for that actor, try another name.')



def movies(imdb):
   new_url= stuff.get('url')
   res = requests.get(new_url)
   res.raise_for_status()
   soup = BeautifulSoup(res.text,'lxml')
   titles = []
   year_str = []
   year = []
   
   
   for a in soup.find_all('div', id=re.compile('actor-tt')):
      for title in a.find('a'):
         titles.append(title)

         print('{}) {}'.format(str(len(titles)),title))


   print()
   print('{} has featured in {} movies.'.format(stuff.get('actor').title(),str(len(titles))))         
            
stuff = actor_imdb_url()
movies(stuff.get('url'))
end = time.time()
print(end-start)





         




