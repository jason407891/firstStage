import requests
from bs4 import BeautifulSoup

movie={}

pageurl="https://www.ptt.cc/bbs/movie/index.html"

#l用來控制movie字典的個數
l=0
for pagecount in range(0,3):
    # 發送 GET 請求，獲取網頁內容
    response = requests.get(pageurl)
    # 解析網頁內容
    soup = BeautifulSoup(response.text, "html.parser")
    pageurl=soup.select(".btn.wide")[1]['href']
    pageurl="https://www.ptt.cc/"+pageurl
    #取得每一個區塊
    blocks = soup.select(".r-ent")
    for block in blocks:
        title = block.select(".title")[0].text.strip()
        count_tag = block.select(".nrec")[0]
        count = count_tag.text.strip() if count_tag.text.strip() else "0"
        title_href = block.select(".title")[0].a['href'] if block.select(".title")[0].a else ""
        title_href = "https://www.ptt.cc/" + title_href if title_href else ""
        url=title_href
        #二階爬蟲
        if url:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            time = soup.select(".article-meta-value")[3].text
        else:
            time=""
        movie[l] = [title, count, title_href, time]
        l+=1

# 寫入txt檔案
with open('movie.txt', 'w', encoding='utf-8') as file:
    #movie[] = [title, count, title_href, time]
    add_string=""
    for value in movie.values():
        add_string+=value[0]+","+str(value[1])+","+value[3]+""+"\n"
        # 寫入內容到檔案
    file.write(add_string)    