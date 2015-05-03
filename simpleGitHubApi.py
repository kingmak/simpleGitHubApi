import re, os, urllib2

def getRepoCount(userName):
    regex = r'<meta name="description" content="(.*)">'
    site = 'https://github.com/' + userName + '?tab=repositories'
    data = urllib2.urlopen(site).read()
    messyRepoCount = re.search(regex, data).group()
    return int(''.join([char for char in messyRepoCount if char.isdigit()]))
    # return int or string?

def getRepoList(userName):
    regex = r'<a href="\/' + userName + '\/(.*)">'
    site = 'https://github.com/' + userName + '?tab=repositories'
    data = urllib2.urlopen(site).read()
    repoList = re.findall(regex, data)
    return repoList

def getRepoFileList(userName, repoName, giveLink = True):
    regex = '<span class="css-truncate css-truncate-target"><a href="\/'
    regex += userName + '\/' + repoName + '\/blob\/master\/(.*)" '
    site = 'https://github.com/' + userName + '/' + repoName
    data = urllib2.urlopen(site).read()
    repoFileList = re.findall(regex, data)

    for count in range(len(repoFileList)):
        tempClean = ''
        temp = repoFileList[count]
        for char in temp:
            if char == '"':
                break
            tempClean += char
                
        repoFileList[count] = tempClean

    if giveLink:
        pattern = 'https://github.com/' + userName + '/' + repoName + '/blob/master/'
        for index in range(len(repoFileList)):
            repoFileList[index] = pattern + repoFileList[index]
      
    return repoFileList

def getFile(fileLink):
    fileLink = re.sub('github', 'raw.github', fileLink)
    blob = fileLink.find('blob')
    fileLink = fileLink[:blob] + fileLink[blob + 5:]
    return fileLink

def getRepo(userName, repoName, downDir = os.getcwd()): # download directory
    repoFileList = getRepoFileList(userName, repoName, True)

    for index in range(len(repoFileList)):
        repoFileLink = getFile(repoFileList[index])
        response = urllib2.urlopen(repoFileLink)
        data = response.read()
        
        repoFile = repoFileLink.split('/')[-1].split('.')
        fileName = repoFile[0]
        extension = ''

        if len(repoFile) > 1:
            extension = repoFile[1]

        finalFileName = [fileName if extension == '' else fileName + '.' + extension][0]
        fileWrite(data, downDir, finalFileName)
    
def getRepoZip(userName, repoName, downDir = os.getcwd()):
    repoLink = 'https://codeload.github.com/' + userName + '/' + repoName + '/zip/master'
    fileName = re.sub(' ', '-', repoName) + '-master.zip'
    response = urllib2.urlopen(repoLink)
    data = response.read()
    fileWrite(data, downDir, fileName)

def fileWrite(data, folderDir, fileName):
    File = open(os.path.join(folderDir, fileName), 'wb')
    File.write(data)
    File.close()
