import requests
import json

x = 1
while True:
     api = 'https://api.github.com/repos/juniper/contrail-project-config/commits?page='+ str(x)
     r = requests.get(api)
     print r
     contr = {}
     if(r.ok):
          repoItem = json.loads(r.text or r.content)
          print repoItem[0]['commit']['author']['email']
     for y in repoItem:
          if repoItem:
               if repoItem[0]['commit']['author']['email'] in contr:
                    contr[repoItem[0]['commit']['author']['email']] += 1
               else:
                    contr[repoItem[0]['commit']['author']['email']] = 1

               print contr
               x += 1
          else:
               print "end of page"               
               break
