import os, simpleGitHubApi as gitapi

os.chdir(os.getcwd())
os.mkdir('testResults')
userName = 'kingmak'

repoCount = gitapi.getRepoCount(userName)
print 'Total repos = %d\n' % repoCount

repoList = gitapi.getRepoList(userName)
repoName = repoList[repoList.index('simpleGitHubApi')]
print '- Repo List:'

for repo in repoList:
    print '  -', repo

print ''
repoFileList = gitapi.getRepoFileList(userName, repoName, False)
print "- %s's File List" % repoName

for repoFile in repoFileList:
    print '  -', repoFile

print ''
print 'Getting repo %s ...' % repoName,
#path = os.path.join(os.getcwd(), 'os)
gitapi.getRepo(userName, repoName, downDir = 'testResults')

print 'Got it\nGetting the zip version now ...',
gitapi.getRepoZip(userName, repoName, downDir = 'testResults')
print 'Got it\nTesting Done'
