import customtkinter
from PIL import Image
from os import path, getcwd
from RequestClass import Request
from config import Config
from sys import exit
from subprocess import Popen


namedic_sf = {
    "Ayanami Rei": "ayanami_rei",
    "Souryuu Asuka Langley": "souryuu_asuka_langley",
    "Ikari Shinji": "ikari_shinji",
    "Katsuragi Misato": "katsuragi_misato",
    "Akagi Ritsuko": "akagi_ritsuko",
    "Ikari Gendou": "ikari_gendou",
}

combobox_sf = [
    "Souryuu Asuka Langley",
    "Ayanami Rei",
    "Ikari Shinji",
    "Katsuragi Misato",
    "Akagi Ritsuko",
    "Ikari Gendou",
]

combobox_wf = [
    "Asuka Langley Soryu",
    "Neon Genesis Evangelion",
    "Ayanami Rei",
    "Ikari Shinji",
    "Katsuragi Misato",
    "Akagi Ritsuko",
]

combobox_sf_quality = ["high", "mid", "low"]
combobox_wf_quality = ["high"]

list_series = ["Neon Genesis Evangelion"]


class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Asuka downloader")
        self.geometry("500x400")
        self.minsize(500, 400)
        self.resizable(width=False, height=False)

        self.wm_iconbitmap(path.join(getcwd(), r"data\icon2.ico"))

        self.Rhandler = Request()
        self.configHandler = Config()

        self.icon2 = customtkinter.CTkImage(
            Image.open(path.join(getcwd(), r"data\iconcircle.png")),
            size=(100, 100),
        )

        self.myfont = customtkinter.CTkFont(family="BodoniFLF", size=18)

        self.main_frm = customtkinter.CTkFrame(
            master=self, bg_color="#242424", fg_color="#242424"
        )

        self.enter_frm = customtkinter.CTkFrame(master=self)

        self.option_frm = customtkinter.CTkFrame(master=self)

        self.iconlabel = customtkinter.CTkLabel(
            master=self.main_frm,
            image=self.icon2,
            text="",
            bg_color="#242424",
            fg_color="#242424",
        ).grid(
            pady=2,
        )

        self.enter_btn = customtkinter.CTkButton(
            master=self.main_frm,
            text="Enter",
            font=self.myfont,
            command=self.loadEnterFrame,
        )
        self.enter_btn.grid(pady=16)

        self.opt_btn = customtkinter.CTkButton(
            master=self.main_frm,
            text="Options",
            font=self.myfont,
            command=self.loadOptionframe,
        )
        self.opt_btn.grid(pady=16)

        self.exit_btn = customtkinter.CTkButton(
            master=self.main_frm, text="Exit", command=exit, font=self.myfont
        )
        self.exit_btn.grid(pady=16)

        self.main_frm.grid()

        self.Myframes = [self.main_frm, self.enter_frm, self.option_frm]

        # print(self.grid_slaves())

    def loadMainframe(self):

        self.enter_frm.grid_remove()

        self.option_frm.grid_remove()

        self.icon2 = customtkinter.CTkImage(
            Image.open(path.join(getcwd(), r"data\iconcircle.png")),
            size=(100, 100),
        )

        self.myfont = customtkinter.CTkFont(family="BodoniFLF", size=18)

        self.main_frm = customtkinter.CTkFrame(
            master=self, bg_color="#242424", fg_color="#242424"
        )

        self.enter_frm = customtkinter.CTkFrame(master=self)

        self.option_frm = customtkinter.CTkFrame(master=self)

        self.iconlabel = customtkinter.CTkLabel(
            master=self.main_frm,
            image=self.icon2,
            text="",
            bg_color="#242424",
            fg_color="#242424",
        ).grid(
            pady=2,
        )

        self.enter_btn = customtkinter.CTkButton(
            master=self.main_frm,
            text="Enter",
            font=self.myfont,
            command=self.loadEnterFrame,
        )
        self.enter_btn.grid(pady=16)

        self.opt_btn = customtkinter.CTkButton(
            master=self.main_frm,
            text="Options",
            font=self.myfont,
            command=self.loadOptionframe,
        )
        self.opt_btn.grid(pady=16)

        self.exit_btn = customtkinter.CTkButton(
            master=self.main_frm, text="Exit", command=exit, font=self.myfont
        )
        self.exit_btn.grid(pady=16)

        self.main_frm.grid()

    def loadEnterFrame(self):
        self.main_frm.grid_remove()

        self.backbtn = customtkinter.CTkButton(
            master=self.enter_frm,
            text="Back",
            font=self.myfont,
            width=20,
            command=self.loadMainframe,
        )
        self.backbtn.grid(row=0, column=0, padx=0, pady=10, sticky="nw")

        self.lbshow = customtkinter.CTkLabel(
            master=self.enter_frm, text="Series chosen:", font=self.myfont
        ).grid(padx=10, pady=16, row=1, column=0, sticky="w")

        self.cbseries = customtkinter.CTkComboBox(
            master=self.enter_frm,
            justify="center",
            values=list_series,
            font=self.myfont,
            width=275,
            dropdown_font=self.myfont,
            state="readonly",
            command=self.setchcharacter,
        )

        self.cbseries.grid(
            padx=10,
            pady=16,
            row=1,
            column=1,
        )

        self.cbseries.set(list_series[0])

        self.chrlabel = customtkinter.CTkLabel(
            master=self.enter_frm, text="Character chosen: ", font=self.myfont
        ).grid(
            padx=10,
            pady=16,
            row=2,
            column=0,
            sticky="w",
        )

        self.combobox = customtkinter.CTkComboBox(
            master=self.enter_frm,
            justify="center",
            values=self.getsrclist(),
            font=self.myfont,
            width=275,
            dropdown_font=self.myfont,
            state="readonly",
        )
        self.combobox.grid(padx=2, row=2, column=1, sticky="w", columnspan=1)
        self.combobox.set("Souryuu Asuka Langley")

        self.questionLabel = customtkinter.CTkLabel(
            master=self.enter_frm,
            text="Number of pictures: ",
            font=self.myfont,
        ).grid(pady=16, padx=(10, 0), row=3, column=0, sticky="w")

        self.entry1 = customtkinter.CTkEntry(
            master=self.enter_frm,
            width=275,
            height=30,
            justify="center",
            font=("BodoniFLF", 18),
            validate="key",
            validatecommand=(self.register(self.validateentry), "%P"),
        )
        self.entry1.grid(pady=16, padx=10, row=3, column=1, sticky="w")

        self.enterbtn = customtkinter.CTkButton(
            master=self.enter_frm,
            text="Confirm",
            font=self.myfont,
            width=150,
            height=30,
            hover_color="green",
            command=self.button_calback,
        )
        self.enterbtn.grid(pady=16, padx=10, row=4, column=0, columnspan=2)

        self.btnOpenfolder = customtkinter.CTkButton(
            master=self.enter_frm,
            text="Open Folder",
            font=self.myfont,
            command=self.openFLD,
        )
        self.btnOpenfolder.grid(pady=16, padx=10, row=5, columnspan=2)

        self.progressframe = customtkinter.CTkFrame(
            master=self.enter_frm, fg_color="#242424"
        )
        self.progressbar = customtkinter.CTkFrame(
            master=self.progressframe,
            fg_color="#242424",
        )
        self.progressbar.grid_propagate(False)
        self.progressbar.configure(width=0, height=16)
        self.progressbar.grid(row=6, columnspan=2)

        self.progressframe.grid_propagate(False)
        self.progressframe.configure(width=200, height=16)
        self.progressframe.grid(row=6, columnspan=2)

        self.enter_frm.configure(fg_color="#242424", bg_color="#242424")
        self.enter_frm.grid()

    def getsrclist(self):
        match self.configHandler.getsrc():
            case "Safe Booru":
                return combobox_sf
            case "Wallpaper Flare":
                return combobox_wf

    def setchcharacter(self, value):
        match value:
            case "Neon Genesis Evangelion":
                match self.configHandler.getsrc():
                    case "Safe Booru":
                        self.combobox.configure(values=combobox_sf)
                    case "Wallpaper Flare":
                        self.combobox.configure(values=combobox_wf)

    def openFLD(self):
        pathfld = path.join(getcwd(), "downloads")
        Popen(f"explorer {pathfld}")

    def button_calback(self):
        if self.entry1.get() != "":
            if self.enterbtn.cget("text") == "Confirm":
                self.entry1.configure(state="disabled")
                self.enterbtn.configure(state="disabled")
                self.cbseries.configure(state="disabled")
                self.enterbtn.configure(
                    text="Wait for download to complete ;3", text_color_disabled="black"
                )
                self.combobox.configure(state="disabled")

                self.progressbar.configure(fg_color="green")
                self.progressframe.configure(fg_color="black")

                self.update()

                match self.configHandler.getsrc():
                    case "Safe Booru":
                        y = 1
                        z = 0
                        while y <= int(self.entry1.get()):
                            z += 1
                            img_url, img_id = self.Rhandler.getImageURLsafebooru(
                                namedic_sf[self.combobox.get()]
                            )
                            match self.Rhandler.downloadimgsafebooru(img_url, img_id):
                                case -1:
                                    print("Failed to download ")
                                case 0:
                                    print("Dupe")

                                case 1:
                                    print("Downloaded normally")
                                    y += 1

                            self.progressbar.configure(
                                width=y / int(self.entry1.get()) * 200, bg_color="green"
                            )

                            self.update()

                            if z > 99:
                                break

                    case "Wallpaper Flare":
                        y = 1
                        z = 0
                        while y <= int(self.entry1.get()):
                            z += 1
                            img_url, img_name = self.Rhandler.getimgurlwf(
                                self.combobox.get()
                            )
                            match self.Rhandler.downloadimgwf(img_url, img_name):
                                case 1:
                                    print("Downloaded normally")
                                    y += 1
                                case 0:
                                    print("Dupe")
                                case -1:
                                    print("Failed to download")

                            self.progressbar.configure(
                                width=y / int(self.entry1.get()) * 200, bg_color="green"
                            )

                            self.update()

                            if z > 99:
                                break

                self.progressbar.configure(width=200)
                self.enterbtn.configure(
                    text="Download complete!", fg_color="green", font=self.myfont
                )

                self.lbretry = customtkinter.CTkLabel(
                    master=self.enter_frm,
                    text="Download complete!",
                    fg_color="green",
                    width=160,
                    font=self.myfont,
                )
                self.lbretry.grid(pady=16, padx=10, row=4, column=0, columnspan=2)
                self.lbretry.bind("<Enter>", self.on_enter)
                self.update()

            elif self.enterbtn.cget("text") == "Recommence Operation":

                self.entry1.configure(state="normal")
                self.enterbtn.configure(state="normal")
                self.enterbtn.configure(text="Confirm", text_color_disabled="black")
                self.combobox.configure(state="readonly")
                self.cbseries.configure(state="readonly")

                self.progressbar.configure(fg_color="#242424")
                self.progressframe.configure(fg_color="#242424")

                self.update()

    def on_enter(self, event):
        self.enterbtn.configure(
            state="normal",
            text="Recommence Operation",
            fg_color="#1F6AA5",
            text_color="white",
        )
        self.lbretry.grid_remove()
        self.enterbtn.update()

    def validateentry(self, input):
        if input.isdigit():
            return True
        elif input == "":
            return True
        return False

    def savesettings(self):
        self.configHandler.setquality(self.cbquality.get())
        self.configHandler.setsrc(self.cbsrc.get())
        if self.configHandler.canNSFW():
            self.configHandler.setNSFW(self.cbnsfw.get())

    def loadOptionframe(self):
        self.main_frm.grid_remove()

        self.optrow = 0

        self.backbtn = customtkinter.CTkButton(
            master=self.option_frm,
            text="Back",
            font=self.myfont,
            width=20,
            command=self.loadMainframe,
        )
        self.backbtn.grid(row=self.optrow, column=0, padx=0, pady=10, sticky="nw")

        self.checkIfNSFW()

        self.Lbsrc = customtkinter.CTkLabel(
            master=self.option_frm, text="Source", font=self.myfont
        )
        self.Lbsrc.grid(
            row=self.optrow + 1, column=1, padx=(90, 0), pady=(50, 0), sticky="e"
        )

        self.cbsrc = customtkinter.CTkComboBox(
            master=self.option_frm,
            justify="center",
            values=["Safe Booru", "Wallpaper Flare"],
            font=self.myfont,
            dropdown_font=self.myfont,
            state="readonly",
            width=200,
            command=self.setcbqualitylist,
        )
        self.cbsrc.grid(row=self.optrow + 1, column=3, padx=10, pady=(50, 0))
        self.cbsrc.set(self.configHandler.getsrc())

        self.Lbquality = customtkinter.CTkLabel(
            master=self.option_frm, text="Quality", font=self.myfont
        )
        self.Lbquality.grid(
            row=self.optrow + 2, column=1, padx=(90, 0), pady=50, sticky="e"
        )

        self.cbquality = customtkinter.CTkComboBox(
            master=self.option_frm,
            justify="center",
            values=self.getqualitylist(),
            font=self.myfont,
            dropdown_font=self.myfont,
            state="readonly",
            width=200,
        )
        self.cbquality.grid(row=self.optrow + 2, column=3, padx=10, pady=50)

        self.cbquality.set(self.configHandler.getqualiystr())

        self.btnsave = customtkinter.CTkButton(
            master=self.option_frm,
            text="Save",
            font=self.myfont,
            command=self.savesettings,
            width=210,
        )

        self.btnsave.grid(
            row=self.optrow + 3, column=1, columnspan=3, padx=(75, 0), pady=16
        )

        self.option_frm.grid(sticky="nsew")

    def checkIfNSFW(self):
        if self.configHandler.canNSFW():
            self.lbnsfw = customtkinter.CTkLabel(
                master=self.option_frm, text="NSFW", font=self.myfont
            ).grid(row=self.optrow + 1, column=1, padx=(90, 0))
            self.cbnsfw = customtkinter.CTkComboBox(
                master=self.option_frm,
                justify="center",
                values=["True", "False"],
                font=self.myfont,
                dropdown_font=self.myfont,
                command=self.setsources,
                width=200,
                state="readonly",
            )
            self.cbnsfw.set("True" if self.configHandler.isNSFW() else "False")
            self.cbnsfw.grid(row=self.optrow + 1, column=3)
            self.optrow += 1

    def setsources(self, value):
        if value == "True":
            window = customtkinter.CTkToplevel(self)
            window.geometry("200x200")
            window.title("Asuka downloader")
            window.resizable(False, False)

            window.wm_iconbitmap(path.join(getcwd(), r"data\icon2.ico"))

            # create label on CTkToplevel window

            label = customtkinter.CTkLabel(
                window, text="Sorry \n Can't coom tonight ;(", font=("BodoniFLF", 20)
            )
            label.pack(expand=True)  # , sticky="fill")

            window.mainloop()

    def getqualitylist(self):
        match self.cbsrc.get():
            case "Wallpaper Flare":
                return combobox_wf_quality
            case "Safe Booru":
                return combobox_sf_quality

    def setcbqualitylist(self, value):
        match value:
            case "Wallpaper Flare":
                self.cbquality.configure(values=combobox_wf_quality)
            case "Safe Booru":
                self.cbquality.configure(values=combobox_sf_quality)
        self.update()


if __name__ == "__main__":
    app = GUI()
    app.rowconfigure(0, weight=1)
    app.columnconfigure(0, weight=1)
    app.mainloop(0)
