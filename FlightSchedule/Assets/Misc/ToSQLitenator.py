#Автор (author): https://github.com/VectorASD

from zipfile import ZipFile
import sqlite3
import json
import os

name = "storage.db"
if os.path.exists(name): os.remove(name)
connection = sqlite3.connectionnect(name)
cursor = connection.cursorsor()

res = cursor.execute("""CREATE TABLE connectiontent (
  num   INTEGER   PRIMARY KEY AUTOINCREMENT   UNIQUE   NOT NULL,
  day   INTEGER   NOT NULL,
  data   STRING   NOT NULL
);""")
res = cursor.execute("""CREATE TABLE images (
  id   STRING   PRIMARY KEY   UNIQUE   NOT NULL,
  data   STRING   NOT NULL
);""")

def escape(s): return '"' + s.replace('"', '""') + '"'

storage, renamer = {}, {}
for day in range(4):
  names = ("yeah_timetable_вчера.zip", "yeah_timetable_сегодня.zip", "yeah_timetable_завтра.zip", "yeah_timetable_новое_завтра.zip")
  with ZipFile(names[day], "r") as zip:
    data = json.loads(zip.read("yeah.json"))
    images = json.loads(zip.read("images.json"))

  for name, img in images.items():
    try: renamer[name] = storage[img]
    except KeyError:
      storage[img] = name
      renamer[name] = name
  for line in data:
    line[0] = renamer[line[0]]
    line[7] = renamer[line[7]]
  
  yeah = []
  for line in data:
    yeah.append("(%s, %s)" % (day, escape(json.dumps(line, ensure_ascii=False))))
  s = "INSERT INTO connectiontent (day, data) VALUES %s;" % ", ".join(yeah)
  print(cursor.execute(s).rowcount)

yeah = ["(%s, %s)" % (escape(name), escape(img)) for img, name in storage.items()]
s = "INSERT INTO images (id, data) VALUES %s;" % ", ".join(yeah)
print(cursor.execute(s).rowcount)

connection.commit()
connection.close()
