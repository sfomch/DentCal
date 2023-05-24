import customtkinter
from tkinter import *
import os
from PIL import Image


def validate(new_value):
    try:
        if new_value == "" or new_value == "-" or new_value == "+":
            return True
        _str = str(float(new_value))
        return True
    except:
        return False


def change_appearance_mode_event(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.label3 = None
        self.textbox3_1 = None
        self.label2 = None
        self.textbox2_1 = None
        self.label = None
        self.textbox1_1 = None
        vcmd = (self.register(validate), '%P')

        self.title("Калькулятор для расчета прочности соединения композитных пломбировочных материалов")
        self.geometry("1200x750")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_image.png")),
                                                       size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")),
                                                       size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")),
                                                 size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "dark2.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "dark2.png")),
                                                 size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "dark2.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "dark2.png")),
                                                     size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Dental Calculator",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Расчет 1",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Расчет 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Расчет 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Light", "Dark", "System"],
                                                                command=change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="",
                                                                   image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.home_frame, height=500, width=250,
                                                font=customtkinter.CTkFont(size=14, weight="bold"))
        self.textbox.grid(row=1, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        # create textbox1
        self.textbox1 = customtkinter.CTkTextbox(self.second_frame, width=250,
                                                 font=customtkinter.CTkFont(size=14, weight="bold"))
        self.textbox1.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew", )
        self.textbox1.configure()

        self.entry1 = customtkinter.CTkEntry(master=self.second_frame, width=140, height=28, validate='key',
                                             validatecommand=vcmd)
        self.entry1.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)

        self.button_1 = customtkinter.CTkButton(master=self.second_frame, text="Рассчитать", width=90,
                                                command=self.getcal1)
        self.button_1.grid(row=1, column=0, sticky="w", padx=(12, 0), pady=12)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)

        # create textbox2
        self.textbox2 = customtkinter.CTkTextbox(self.third_frame, width=250,
                                                 font=customtkinter.CTkFont(size=14, weight="bold"))
        self.textbox2.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew", )
        self.textbox2.configure()

        self.entry2 = customtkinter.CTkEntry(master=self.third_frame, width=140, height=28, validate='key',
                                             validatecommand=vcmd)
        self.entry2.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)

        self.button_2 = customtkinter.CTkButton(master=self.third_frame, text="Рассчитать", width=90,
                                                command=self.getcal2)
        self.button_2.grid(row=1, column=0, sticky="w", padx=(12, 0), pady=12)

        # create fourth frame
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame.grid_columnconfigure(0, weight=1)

        # create textbox3
        self.textbox3 = customtkinter.CTkTextbox(self.fourth_frame, width=250,
                                                 font=customtkinter.CTkFont(size=14, weight="bold"))
        self.textbox3.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew", )
        self.textbox3.configure()

        self.entry3 = customtkinter.CTkEntry(master=self.fourth_frame, width=140, height=28, validate='key',
                                             validatecommand=vcmd)
        self.entry3.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)

        self.button_3 = customtkinter.CTkButton(master=self.fourth_frame, text="Рассчитать", width=90,
                                                command=self.getcal3)
        self.button_3.grid(row=1, column=0, sticky="w", padx=(12, 0), pady=12)

        # select default frame
        self.select_frame_by_name("home")

        # set default values
        self.textbox.insert("0.0",
                            "Описание:\n\n" + "Калькулятор позволяет произвести расчет прочности соединения "
                                              "композитных пломбировочных материалов с дентином зуба:\n\n" +
                            "в области вестибулярной поверхности зуба между экватором и жевательной поверхностью при "
                            "локализации дна полости 20 - 40⁰ относительно оси зуба (вкладка РАСЧЕТ 1).\n\n" +
                            "в области шейки зуба с вестибулярной поверхности при локализации дна полости параллельно "
                            " вертикальной оси зуба(вкладка РАСЧЕТ 2).\n\n" +
                            "в  области шейки зуба при локализации дна полости перпендикулярно вертикальной оси зуба("
                            "вкладка РАСЧЕТ 3).\n\n")

        self.textbox1.insert("0.0",
                             "Расчет прочности соединения композитных пломбировочных материалов с дентином зуба в "
                             "области вестибулярной поверхности зуба между экватором и жевательной поверхностью при "
                             "локализации дна полости 20 - 40⁰ относительно оси зуба.\n\n" +
                             "Введите значение максимальной нагрузки перед непосредственным разрушением образца в "
                             "диапазоне 0.1 – 17.3 (кг):")

        self.textbox2.insert("0.0",
                             "Расчет прочности соединения композитных пломбировочных материалов с дентином зуба в  "
                             "области шейки зуба с вестибулярной поверхности при локализации дна полости параллельно  "
                             "вертикальной оси зуба.\n\n" +
                             "Введите значение максимальной нагрузки перед непосредственным разрушением образца в "
                             "диапазоне 0.1 – 3.7 (кг):")

        self.textbox3.insert("0.0",
                             "Расчет прочности соединения композитных пломбировочных материалов с дентином зуба в  "
                             "области шейки зуба при локализации дна полости перпендикулярно вертикальной оси зуба "
                             ".\n\n" +
                             "Введите значение максимальной нагрузки перед непосредственным разрушением образца в "
                             "диапазоне 0.1 – 1.4 (кг):")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def getcal1(self):
        a = self.entry1.get()
        a = float(a)
        a1 = 2.2017 * a - 0.0061
        a2 = str(a1)

        self.textbox1_1 = customtkinter.CTkTextbox(self.second_frame, width=250,
                                                   font=customtkinter.CTkFont(size=14, weight="bold"))
        self.textbox1_1.grid(row=2, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.textbox1_1.insert("0.0",
                               "прочность адгезионного соединения (МПа)=\n", )
        self.label = customtkinter.CTkLabel(self.second_frame, text=a2,
                                            compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.label.grid(row=2, column=0, padx=20, pady=20)

    def getcal2(self):
        b = self.entry2.get()
        b = float(b)
        b1 = 2.1965 * b - 0.0067
        b2 = str(b1)

        self.textbox2_1 = customtkinter.CTkTextbox(self.third_frame, width=250,
                                                   font=customtkinter.CTkFont(size=14, weight="bold"))
        self.textbox2_1.grid(row=2, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.textbox2_1.insert("0.0",
                               "прочность адгезионного соединения (МПа)=\n", )
        self.label2 = customtkinter.CTkLabel(self.third_frame, text=b2,
                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.label2.grid(row=2, column=0, padx=20, pady=20)

    def getcal3(self):
        c = self.entry3.get()
        c = float(c)
        c1 = 2.1965 * c - 0.0067
        c2 = str(c1)

        self.textbox3_1 = customtkinter.CTkTextbox(self.fourth_frame, width=250,
                                                   font=customtkinter.CTkFont(size=14, weight="bold"))
        self.textbox3_1.grid(row=2, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.textbox3_1.insert("0.0",
                               "прочность адгезионного соединения (МПа)=\n", )
        self.label3 = customtkinter.CTkLabel(self.fourth_frame, text=c2,
                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.label3.grid(row=2, column=0, padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
