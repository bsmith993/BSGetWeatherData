import urllib.request
import json
import datetime

now = datetime.datetime.now()
current_day = now.day

request = urllib.request.Request("http://api.wunderground.com/api/YOURKEYHERE/geolookup/conditions/q/MD/Williamsport.json")
response = urllib.request.urlopen(request)
encoding = response.info().get_param('charset', 'utf8')
data = json.loads(response.read().decode(encoding))

current_temp = int(data['current_observation']['temp_f'])

request = urllib.request.Request("http://api.wunderground.com/api/YOURKEYHERE/geolookup/forecast/q/MD/Williamsport.json")
response = urllib.request.urlopen(request)
encoding = response.info().get_param('charset', 'utf8')
data = json.loads(response.read().decode(encoding))

for period in data['forecast']['simpleforecast']['forecastday']:
    if period['date']['day'] == current_day:
        today_high = int(period['high']['fahrenheit'])
        

ISYServerIP = "192.168.1.144"
ISYServerPort = "80"
ISYUsername = "username"
ISYPassword = "password"
TopURL = 'http://'+ ISYServerIP + ':' + ISYServerPort
SetCurrentWeatherURL = 'http://' + ISYServerIP + ':' + ISYServerPort + '/rest/vars/set/2/3/' + str(current_temp)
SetTodayHighURL = 'http://' + ISYServerIP + ':' + ISYServerPort + '/rest/vars/set/2/4/' + str(today_high)

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, TopURL, ISYUsername, ISYPassword)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(SetCurrentWeatherURL)

password_mgr.add_password(None, TopURL, ISYUsername, ISYPassword)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
opener.open(SetTodayHighURL)
