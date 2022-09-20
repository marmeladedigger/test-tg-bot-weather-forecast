from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('465fadcef53d3043729eecf26d40f3d6')
mgr = owm.weather_manager()

place=input("Input your city/country:")
observation = mgr.weather_at_place(place)
w = observation.weather

status=w.detailed_status
print("In "+place+" now "+str(w.detailed_status))

temp=w.temperature('celsius')["temp"]      
print("Now temperature "+str(temp))
if temp<10:
    print("It is cold outside, wear your jacket")
elif temp>10:
    print("It is warm outside, you can wear only hoodie")
elif temp>20:
    print("It is hot outside, wear t-shirt and shorts")

wind=w.wind()["speed"]
print("Now wind speed "+str(wind))
if wind<10:
    print("It is windy outside")
else:
    print("It is calm outside")

clouds=w.clouds
print("Clouds "+str(clouds))

humidity=w.humidity
print("Humidity "+str(humidity))




