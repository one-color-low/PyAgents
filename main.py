import weatherAgent, placeAgent, emotionAgent
import datetime

# ----------- input -----------
dt_now = datetime.datetime.now()

weather = weatherAgent.WeatherAgent()
weather.sunny = True
# weather.rainy = True
weather.cloudy = True

place = placeAgent.PlaceAgent()
place.longitude = 80
place.latitude = 120
place.prefecture = "Tokyo"

emotion = emotionAgent.EmotionAgent()
emotion.updateEmotion(place=place, weather=weather, dt=dt_now)

# ----------- output -----------
output_pic_id = ""

emotion_array = [emotion.happy, emotion.sad, emotion.angry]
emotion_max = max(emotion_array)
emotion_min = min(emotion_array)

if emotion.happy == emotion_max:
    output_pic_id = "happy"
elif emotion.sad == emotion_max:
    output_pic_id = "sad"
elif emotion.angry == emotion_max:
    output_pic_id = "angry"

print(output_pic_id)

print(emotion.happy, emotion.sad, emotion.angry)