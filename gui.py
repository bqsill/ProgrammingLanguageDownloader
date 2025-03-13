import tkinter
import customtkinter
import os 
from main import Language

class gui():
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.language = Language()

    def run(self):
        app = customtkinter.CTk()
        app.geometry("720x480")
        app.title("Programming Language Downloader 1.0.0.(Ubuntu Only)")

        title = customtkinter.CTkLabel(app, text="Select the language you would like to download")
        title.pack()

        # Populate options menu
        langs = []
        for lang in self.language.supportedLang:
            langs += [lang.name]
        # Create options menu
        self.lang_options = customtkinter.CTkOptionMenu(app, values=langs, command=self.update_view, width = 200, height = 35)
        self.lang_options.pack()
        self.versions_options = customtkinter.CTkOptionMenu(app, values=[str(version) for version in self.language.versions[self.lang_options.get()]],width = 200, height = 35)
        self.versions_options.pack()
        self.button_select = customtkinter.CTkButton(app, text="select", command=self.lang_button)
        self.button_select.pack()         
        app.mainloop()

    def lang_button(self):
        self.language.run(self.lang_options.get(), self.versions_options.get())

    def update_view(self, selected_lang):
        self.versions_options.configure(values=[str(version) for version in self.language.versions[selected_lang]],width = 200, height = 35)

if __name__ == "__main__":
    gui_app = gui()
    gui_app.run()