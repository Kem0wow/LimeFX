import customtkinter as ctk
from PIL import Image

import btnManager as btn
from pages import soundboard, upload, settings

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("LimeFX")
        self.iconbitmap("./assets/icon.ico")
        self.geometry("1200x850")
        self.minsize(900, 650)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # LEFT BAR
        self.leftbar = ctk.CTkFrame(self, width=350, fg_color="#1f1f1f")
        self.leftbar.grid(row=0, column=0, sticky="ns")
        self.leftbar.grid_propagate(False)

        # CONTENT
        self.content = ctk.CTkFrame(self, fg_color="#121212")
        self.content.grid(row=0, column=1, sticky="nsew")

        # LOGO
        logo_img = ctk.CTkImage(
            light_image=Image.open("./assets/icon-w-text.png"),
            dark_image=Image.open("./assets/icon-w-text.png"),
            size=(128, 128)
        )

        logo = ctk.CTkLabel(self.leftbar, image=logo_img, text="")
        logo.image = logo_img
        logo.pack(padx=20, anchor="w")

        # MENU
        btn.left_btn(self.leftbar, "./assets/leftbar/sound1.png", "Soundboard", self.show_soundboard)
        btn.left_btn(self.leftbar, "./assets/leftbar/upload1.png", "Upload", self.show_upload)
        btn.left_btn(self.leftbar, "./assets/leftbar/settings1.png", "Settings", self.show_settings)

        self.show_soundboard()

    def clear(self):
        for w in self.content.winfo_children():
            w.destroy()

    def show_soundboard(self):
        self.clear()
        soundboard.render(self.content)

    def show_upload(self):
        self.clear()
        upload.render(self.content)

    def show_settings(self):
        self.clear()
        settings.render(self.content)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    MainApp().run()