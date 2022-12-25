requestList = []
whitelist = []
approvedList = []
whitelistCount = int(input())
for i in range(whitelistCount):
    whitelisted = input()
    whitelist.append(whitelisted)
requestCount = int(input())
for j in range(requestCount):
    request = input()
    requestList.append(request)
for request in requestList:
    if request in whitelist:
        approvedList.append(request)
print(*approvedList, sep='\n')
