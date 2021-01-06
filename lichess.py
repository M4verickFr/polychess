
import requests


class Lichess:
    
    def __init__(self):
        self.token = "iSyU2c6HksQFeor4"
        self.header = {
            "Authorization": "Bearer {}".format(self.token)
        }
        self.gameId = "cccopim4"
        
    def makeMove(self, moveUCI):
        request = requests.post("https://lichess.org/api/bot/game/" + self.gameId + "/move/" + moveUCI, headers=self.header)
        print("retour play move : " + str(request.text))
        
    def getStatusGame(self):
        request = requests.get("https://lichess.org/api/bot/game/stream/" + self.gameId, headers=self.header, stream=True)
        print("Status : ")
        print(request.text)
        

lich = Lichess()
lich.makeMove("b8a6")
lich.getStatusGame()



