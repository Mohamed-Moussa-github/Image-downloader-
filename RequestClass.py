from requests import get
from shutil import copyfileobj
from random import randint
from txthandler import T_Thandler
from os import path, mkdir
from config import Config
from html_to_json import convert
from json import dump

websites = [
    r"https://www.wallpaperflare.com/search?wallpaper=asuka&page=34",
    r"https://safebooru.org//index.php?page=dapi&s=post&q=index",
    r"https://wallpapers.com/neon-genesis-evangelion",
]


class Request:
    def getImageURLsafebooru(self, tag):
        URL = r"https://safebooru.org//index.php?page=dapi&s=post&q=index"

        limit = 100
        pid = randint(0, 100)
        tags = tag

        r = get(
            URL,
            params={
                "limt": limit,
                "pids": pid,
                "tags": tags,
            },
        )

        img_url = False
        if r.ok:
            img_url = r.text.split("<post")
            img_id = []

            ConfigFeet = Config()
            quality = ConfigFeet.getquality()

            img_url = img_url[2:]

            for i in range(len(img_url)):
                img_url[i] = img_url[i].split('"')
                img_id.append(img_url[i][21])
                img_url[i] = img_url[i][quality]

        roll = randint(0, 99)
        img_url = img_url[roll]
        img_id = img_id[roll]

        return img_url, img_id

    def downloadimgsafebooru(self, img_url, img_id):

        txthandler = T_Thandler()

        isThere = txthandler.read(img_id)

        if not isThere:

            response = get(img_url, stream=True)

            if response.ok:

                if path.isdir("downloads"):
                    with open(rf"downloads/{img_id}.png", "wb") as out_file:
                        copyfileobj(response.raw, out_file)

                    print("Downloaded sucksisfully ;3")
                    txthandler.write(img_id)
                else:
                    mkdir("downloads")
                    with open(rf"downloads/{img_id}.png", "wb") as out_file:
                        copyfileobj(response.raw, out_file)

                    print("Downloaded sucksisfully ;3")
                    txthandler.write(img_id)
                return 1
            print("Failed to download ;(")
            return -1
        print("Picture already there")
        return 0

    def downloadsafebooru(self, amount, tag):
        for i in range(amount):
            img_url, img_id = self.getImageURLsafebooru(tag)
            self.downloadimgsafebooru(img_url, img_id)

    def getimgurlwf(self, tag):
        URL = r"https://www.wallpaperflare.com/search?"

        r = get(
            URL,
            params={
                "wallpaper": tag,
                "page": randint(1, 20),
            },
        )

        print(r.url)
        try:
            rjson = convert(r.text)["html"][0]["body"][0]["main"][0]["section"][0][
                "ul"
            ][0]["li"]
        except KeyError:
            r = get(
                URL,
                params={
                    "wallpaper": tag,
                    "page": 0,
                },
            )
            rjson = convert(r.text)["html"][0]["body"][0]["main"][0]["section"][0][
                "ul"
            ][0]["li"]

        urllist = []
        for i in range(1, len(rjson)):
            urllist.append(rjson[i]["figure"][0]["a"][0]["_attributes"]["href"])

        img_url = urllist[randint(0, len(urllist) - 1)]
        img_name = img_url.split("/")[3]

        return img_url, img_name

    def downloadimgwf(self, img_url, img_name):

        txthandler = T_Thandler()

        isThere = txthandler.read(img_name)

        if not isThere:

            response = get(f"{img_url}/download", stream=True)

            img_url2 = convert(response.text)["html"][0]["body"][0]["main"][0][
                "section"
            ][0]["img"][0]["_attributes"]["src"]

            response = get(img_url2, stream=True)

            if response.ok:

                if path.isdir("downloads"):
                    with open(rf"downloads/{img_name}.png", "wb") as out_file:
                        copyfileobj(response.raw, out_file)

                    print("Downloaded sucksisfully ;3")
                    txthandler.write(img_name)
                else:
                    mkdir("downloads")
                    with open(rf"downloads/{img_name}.png", "wb") as out_file:
                        copyfileobj(response.raw, out_file)

                    txthandler.write(img_name)
                return 1

            return -1

        return 0


if __name__ == "__main__":
    Rfeet = Request()
    url, name = Rfeet.getimgurlwf("Asuka Langley Soryu")
    Rfeet.downloadimgwf(url, name)
