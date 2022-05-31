# import datetime
from datetime import date, datetime, timedelta
import pytz
import os
import shutil
import json

# methods datetime
print('#' * 10 + ' datetime ' + '#' * 10)
print(dir(datetime))
# current date
# d = datetime.date.today()
d = date.today()
print('current date:', d)
# birthday = datetime.date(1987, 1, 26)
birthday = date(1987, 1, 26)
print('birthday date:', birthday)
# timedelta
# help(timedelta)
timedelta(days=1)
timedelta(hours=1)
print('timedelta between now and birthday:', d - birthday)
print('str(date):', str(d), 'ISO format:', d.strftime('%Y/%m/%d'), sep='\n')
print(d.strftime('%A'))
date_string = '2022-05-29'
print(datetime.strptime(date_string, "%Y-%m-%d"))
date3 = datetime.now()
print('date:', date3, 'timestamp:', datetime.timestamp(date3))

print('#' * 10 + ' pytz ' + '#' * 10)

print(datetime.now(pytz.UTC))
print(datetime.now(tz=pytz.timezone("Africa/Kampala")))
now = datetime.now(tz=pytz.timezone("Africa/Kampala"))
print(now.hour)
print(now.day)
print(now.isocalendar())

print('#' * 10 + ' os ' + '#' * 10)

print(os.listdir())
print(os.getcwd())
print(os.environ)
os.mkdir('my_folder')
print(os.listdir())
print(os.path.getctime('my_folder'))
print(os.path.isdir('my_folder'))
print(os.path.abspath('my_folder'))
os.removedirs('my_folder')
print(os.path.exists('my_folder'))

print('#' * 10 + ' json ' + '#' * 10)

# JavaScript Object Notation
dict1 = {"Name": "Paul", "Age": 27}
print(json.dumps(dict1, indent=2))
with open("MyJson.json", "w") as myjson:
    myjson.write(json.dumps(dict1, indent=4))
with open("MyJson.json", "r") as myjson:
    dict2 = json.loads(myjson.read())
print(type(dict2))
print(dict2)

print('#' * 10 + ' shutil ' + '#' * 10)

shutil.copy('MyJson.json', 'copy.json')
print(os.path.abspath('copy.json'))
print('File:', os.path.basename('copy.json'),
      'Size:', os.path.getsize('copy.json'),
      'Create time:', datetime.fromtimestamp(os.path.getctime('copy.json')).strftime("%Y-%m-%d"))
os.remove('MyJson.json')
os.remove('copy.json')
