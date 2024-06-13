from configparser import ConfigParser
from os import path, getcwd


class Config:
    def __init__(self):
        self.config = ConfigParser()
        if path.isfile(path.join(getcwd(), r"config.ini")):
            self.config.read("config.ini")
        else:
            self.config["SETTINGS"] = {"quality": "high", "src": "Safe Booru"}
            with open("config.ini", "w") as f:
                self.config.write(f)

    def getquality(self):

        match self.config["SETTINGS"]["quality"]:
            case "high":
                return 5
            case "mid":
                return 9
            case "low":
                return 15
            case _:
                return 9

    def getqualiystr(self):
        match self.config["SETTINGS"]["src"]:
            case "Safe Booru":
                return self.config["SETTINGS"]["quality"]
            case "Wallpaper Flare":
                return "high"

    def setquality(self, quality):
        self.config["SETTINGS"]["quality"] = quality
        with open("config.ini", "w") as f:
            self.config.write(f)

    def getsrc(self):
        return self.config["SETTINGS"]["src"]

    def setsrc(self, src):
        self.config["SETTINGS"]["src"] = src
        with open("config.ini", "w") as f:
            self.config.write(f)

    def canNSFW(self):
        try:
            if self.config["SETTINGS"]["nsfw"] != "in3wnefw3232nwefweow":
                return True
        except KeyError:
            return False

    def isNSFW(self):
        match self.config["SETTINGS"]["nsfw"]:
            case "True":
                return True
            case _:
                return False

    def setNSFW(self, value):
        self.config["SETTINGS"]["nsfw"] = value
        with open("config.ini", "w") as f:
            self.config.write(f)


if __name__ == "__main__":
    Chandler = Config()
