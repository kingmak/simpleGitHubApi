import simpleGitHubApi as gitapi

userName = 'kingmak'

repoCount = gitapi.getRepoCount(userName)
print 'Total repos = %d\n' % repoCount

repoList = gitapi.getRepoList(userName)
print '- Repo List:'

for repo in repoList:
    print '  -', repo

print ''
repoFileList = gitapi.getRepoFileList(userName, repoList[0], False)
print "- %s's File List'" % repoList[0]

for repoFile in repoFileList:
    print '  -', repoFile

print ''
print 'Getting repo %s ...' % repoList[0],
gitapi.getRepo(userName, repoList[0])

print 'Got it\nGetting the zip version now ...',
gitapi.getRepoZip(userName, repoList[0])
print 'Got it\nTesting Done'
