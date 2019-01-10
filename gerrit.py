import requests
import json
contr = {}
f= open("contr.txt", "w+")
token = open("token", "r")
token = token.read()
x = 1
lines = []
with open("stats") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!
print lines


while True:
     for z in lines:
          # print z
          api = 'https://api.github.com/repos/' + z + '/commits?per_page=100&page=' + str(x) + '&access_token=' + token
          print api
#           r = requests.get(api)
#           print r
     
#           if(r.ok):
#                repoItem = json.loads(r.text or r.content)
#                # print repoItem[0]['commit']['author']['email']
#           if not repoItem:
#                print "end of list."
#                # z += 1
          
#           for y in repoItem:
#                if y['commit']['author']['email'] in contr:
#                     contr[y['commit']['author']['email']] += 1
#                     x += 1
#                else:
#                     contr[y['commit']['author']['email']] = 1
#                x += 1
#                print x
#                # print contr
          
         
          
     
#      # f.close()
#      print x
     

# with open('dict.txt', 'w') as f:
#      f.write(str(contr))
