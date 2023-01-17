import requests
from bs4 import BeautifulSoup

for year in range(2018, 2023):
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={}%EB%85%84+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84&oquery=2020%EB%85%84+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84&tqi=h8iIGsprvxZsscWiRC0ssssstbG-491846".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("div", attrs={"class": "thumb"})
    for index, image in enumerate(images[:8]):
        thumbnail = image.find("img")["src"]

        image_res = requests.get(thumbnail)
        image_res.raise_for_status()
        with open("Top{} movie of {} Year.jpg".format(str(index + 1), year), "wb") as f:
            f.write(image_res.content)
