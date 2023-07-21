import csv
import json
import urllib.request

url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"


response = urllib.request.urlopen(url)
data = response.read().decode()
attraction = json.loads(data)


def get_attr(view):
    with open("attraction.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["景點名稱", "區域", "經度","緯度","第一張圖檔網址"])
        for attraction in view['result']['results']:
            name = attraction["stitle"]
            description = attraction["address"]
            description = description[:3]
            latitude = attraction["latitude"]
            longitude = attraction["longitude"]
            image = attraction['file']
            position = image.lower().find(".jpg")
            image=image[:position]+".jpg"
            writer.writerow([name, description, latitude, longitude, image])

def get_mrt(view):
    mrt={}
    for attraction in view['result']['results']:
        mrtstation=attraction['MRT']
        #新增到字典的value
        if mrtstation in mrt:
            mrt[mrtstation].append(attraction['stitle'])
        else:
            #新建一個字典key
            mrt[mrtstation]=[attraction['stitle']]
    with open("mrt.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        print(mrt)
        for mrt_station, attractions in mrt.items():
            attractions_str = []
            attractions_str.append(mrt_station)
            for i in attractions:
                attractions_str.append(i)
            writer.writerow(attractions_str)

    
get_attr(attraction)
get_mrt(attraction)