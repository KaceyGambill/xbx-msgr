import json
import requests


headers = {'X-Authorization': 'kk4so40ocs0wwsw0gc8o8kg4888c0c48og4'}
def getGamertagId():
    print('Enter gamertag: ')

    username = input()

    gtSearchPayload= {'gt': username}
    gtSearch = requests.get('https://xbl.io/api/v2/friends/search/?', gtSearchPayload, headers=headers)

    print(gtSearch.url)

    requestContent = json.loads(gtSearch.content)
    gamertagId = requestContent["profileUsers"][0]["id"]

    return gamertagId

def messagePlayer(gamertagId):
    print('Enter message: ')

    print(gamertagId)
    message = input()

    messageData = {'xuid': gamertagId, 'message': message}
    print(messageData)
    sendMessage = requests.post('https://xbl.io/api/v2/conversations', json=messageData, headers=headers)
    print(sendMessage.url)
    print(sendMessage.json())


messagePlayer(getGamertagId())

