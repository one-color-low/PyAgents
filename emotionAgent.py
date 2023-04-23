import placeAgent, weatherAgent
import datetime

class EmotionAgent:
    happy: int
    sad: int
    angry: int

    def __init__(self) -> None:
        self.happy = 0
        self.sad = 0
        self.angry = 0

    def updateEmotion(self, place: placeAgent.PlaceAgent, weather: weatherAgent.WeatherAgent, dt: datetime.datetime):

        if 30 < place.longitude < 40: # 温帯
            self.happy += 1
        
        if weather.sunny == True:
            self.happy += 2
        
        if weather.cloudy == True:
            self.sad += 1

        if weather.rainy == True:
            self.sad += 2

        if 21 < dt.hour < 24: # 夜
            self.sad += 1
        
        if 12 < dt.hour < 15: # 昼
            self.happy += 1