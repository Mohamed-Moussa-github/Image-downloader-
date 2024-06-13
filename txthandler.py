from os import path, getcwd, mkdir


class T_Thandler:
    def __init__(self):
        self.FILENAME = path.join(getcwd(), r"data\SAFEBOORU.txt")
        self.FILEPATH = path.join(getcwd(), r"data")
        if not path.isfile(self.FILENAME):
            if not path.isdir(self.FILEPATH):
                mkdir(self.FILEPATH)
            with open(self.FILENAME, "w") as f:
                f.write("")

    def read(self, txt):
        with open(self.FILENAME, "r") as f:
            list = f.read()
        list = list.split("\n")
        for i in list:
            if txt not in list:
                return False
        return True

    def write(self, txt):
        with open(self.FILENAME, "a") as f:
            f.write(f"{txt}\n")
