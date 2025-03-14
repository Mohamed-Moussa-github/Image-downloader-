import ctkinter
import txthandler


def main():
    txthandler.T_Thandler()
    app = ctkinter.GUI()
    app._set_appearance_mode("dark")
    app.rowconfigure(0, weight=1)
    app.columnconfigure(0, weight=1)
    app.mainloop()


if __name__ == "__main__":
    main()
