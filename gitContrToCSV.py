import requests
import json
import ast
import csv

contr = {}
token = open("token", "r")
token = token.read()
repoItem = {}
x = 0
z = 0
repos = []
with open("repos_list") as file:
    for line in file: 
        line = line.strip()
        repos.append(line)
while True:
     api = 'https://api.github.com/repos/' + repos[z] + '/commits?per_page=100&page=' + str(x) + '&access_token=' + token
     x += 1
     print api
     r = requests.get(api)
     if(r.ok):
          repoItem = json.loads(r.text or r.content)
     if not repoItem:
          print "end of list."
          z += 1
          x = 0
     for y in repoItem:
          if y['commit']['author']['email'] in contr:
               contr[y['commit']['author']['email']] += 1
          else:
               contr[y['commit']['author']['email']] = 1
          print contr
     print x
     # with open('dict.txt', 'w') as f:
     #      f.write(str(contr))
     # with open('dict.txt', "r") as data:
     #      dict1 = ast.literal_eval(data.read())
     with open('output.csv', 'wb') as output:
          writer = csv.writer(output)
          for key, value in contr.iteritems():
               writer.writerow([key, value])
     if z == len(repos):
          break
