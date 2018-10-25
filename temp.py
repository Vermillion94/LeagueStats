# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import requests

URL = "https://na1.api.riotgames.com"

KEY = "?api_key=RGAPI-3e013040-0cc3-42d9-99d3-e103a3b03a81"

thi = requests.get("https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/Peachaku" + KEY)

accountid = thi.json()['accountId']

URL1 = URL + "/lol/match/v3/matchlists/by-account/" + str(accountid) + KEY

thi1 = requests.get(URL1)

dictm = thi1.json()['matches']

#print(dictm)

DDRG = "http://ddragon.leagueoflegends.com/cdn/8.20.1/data/en_US/champion.json"

the3 = requests.get(DDRG)

the4 = the3.json()['data']

champKey = {}

for key, value in the4.items():
    champKey.update({value['key'] : key})

alist = []
blist = []

for x in range(len(dictm)):
    blist.append({dictm[x]['champion'] : champKey[str(dictm[x]['champion'])]})

part = 0
dictp = {}


matchid = dictm[1]['gameId']
URL2 = URL + "/lol/match/v3/timelines/by-match/" + str(matchid) + KEY
matchSpecifics = requests.get(URL2)
print(matchSpecifics.json())

#for x in range(len(dictm)):
#    matchid = dictm[x]['gameId']
#    URL2 = URL + "/lol/match/v3/matches/" + str(matchid) + KEY
#    matchSpecifics = requests.get(URL2)
#    listpid = matchSpecifics.json()['participantIdentities']
#    listp = matchSpecifics.json()['participants'] 
#    for x in range(len(listpid)):
#        if listpid[x]['player']['accountId'] == accountid:
#            part = listpid[x]['participantId']
#    alist.append({champKey[str(listp[(part-1)]['championId'])] : listp[(part-1)]['stats']['win']})
#print(matchSpecifics.json()['participantIdentities'])

#print(alist)


