import requests
import json
import ast
import csv

contr = {}
git_token = open("token", "r")
git_token = git_token.read()
repo_response = {}
x = 0
z = 0
repos = []
with open("repos_list") as file:
    for line in file: 
        line = line.strip()
        repos.append(line)
while z != len(repos):
     api = 'https://api.github.com/repos/{repository}/commits?per_page=100&page={pageNum}&access_token={gitToken}'.format(repository=repos[z], gitToken=git_token, pageNum=str(x))
     x += 1
     print "repository: {repository} page: {pageNum}".format(pageNum=x, repository=repos[z])
     r = requests.get(api)
     if(r.ok):
          repo_response = json.loads(r.text or r.content)
     if not repo_response:
          print "end of list."
          z += 1
          x = 0
     for y in repo_response:
          if y['commit']['author']['email'] in contr:
               contr[y['commit']['author']['email']] += 1
          else:
               contr[y['commit']['author']['email']] = 1     
     with open('output.csv', 'wb') as output:
          writer = csv.writer(output)
          for key, value in contr.iteritems():
               writer.writerow([key, value])