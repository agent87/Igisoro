from requests import *
from pymongo import *



api_key = "f12d4521fe878dbe91ab465f11a3c837"

latitude  = -1.955370
longitute = 30.096531

forecast = get(" https://api.darksky.net/forecast/{0}/{1},{2}".format(api_key, latitude, longitute))


print(forecast.status_code)
print(forecast.content)