import customtkinter as ctk
from PIL import Image
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from jsonManager import load_soundboard_settings, save_soundboard_settings, load_soundboards

def render(parent):
    settings = load_soundboard_settings()
    soundboards = load_soundboards()
    sound_enabled = settings["enabled"]
    volume = settings["volume"]

    icon_on = ctk.CTkImage(
        light_image=Image.open("./assets/sound-on.png"),
        dark_image=Image.open("./assets/sound-on.png"),
        size=(20, 20)
    )

    icon_off = ctk.CTkImage(
        light_image=Image.open("./assets/sound-off.png"),
        dark_image=Image.open("./assets/sound-off.png"),
        size=(20, 20)
    )

    def sound_on_off():
        nonlocal sound_enabled
        sound_enabled = not sound_enabled
        save_soundboard_settings(sound_enabled, int(sound_slider.get()))

        sound_disable.configure(
            text="On" if sound_enabled else "Off",
            fg_color="#228b22" if sound_enabled else "#b22222",
            hover_color="#32cd32" if sound_enabled else "#ff4040",
            image=icon_on if sound_enabled else icon_off
        )

        state = "normal" if sound_enabled else "disabled"
        for btn in sound_buttons:
            btn.configure(state=state)
        sound_slider.configure(state=state)

    title = ctk.CTkLabel(
        parent,
        text="Soundboard",
        font=ctk.CTkFont(size=26, weight="bold")
    )
    title.pack(anchor="nw", padx=30, pady=30)

    grid = ctk.CTkFrame(parent, fg_color="transparent")
    grid.pack(padx=30, pady=10)

    for i in range(3):
        grid.grid_columnconfigure(i, weight=1)

    sound_buttons = []

    for i in range(9):
        sound = soundboards[i]
        btn_name = sound["name"] if sound else f"Empty {i+1}"
        btn_file = sound["file"] if sound else None
        
        btn = ctk.CTkButton(
            grid,
            text=btn_name,
            width=140,
            height=90,
            corner_radius=10,
            fg_color="#2b2b2b",
            hover_color="#3a3a3a",
            font=ctk.CTkFont(size=10, weight="bold")
        )
        btn.grid(row=i // 3, column=i % 3, padx=12, pady=12)
        btn.file_path = btn_file
        sound_buttons.append(btn)

    sound_lbl = ctk.CTkLabel(
        parent,
        text=f"Volume: {volume}",
        font=ctk.CTkFont(size=20)
    )
    sound_lbl.pack(pady=20)

    def update_volume(val):
        sound_lbl.configure(text=f"Volume: {int(val)}")
        save_soundboard_settings(sound_enabled, int(val))

    sound_slider = ctk.CTkSlider(
        parent,
        from_=0,
        to=100,
        width=400,
        height=15,
        corner_radius=10,
        fg_color="#2b2b2b",
        button_color="#4a90e2",
        button_hover_color="#357ABD",
        command=update_volume
    )
    sound_slider.set(volume)
    sound_slider.pack()
    
    sound_disable = ctk.CTkButton(
        parent,
        text="On" if sound_enabled else "Off",
        width=200,
        height=40,
        corner_radius=8,
        fg_color="#228b22" if sound_enabled else "#b22222",
        hover_color="#32cd32" if sound_enabled else "#ff4040",
        image=icon_on if sound_enabled else icon_off,
        font=ctk.CTkFont(size=18, weight="bold"),
        command=sound_on_off
    )
    sound_disable.pack(pady=25)
    
    state = "normal" if sound_enabled else "disabled"
    for btn in sound_buttons:
        btn.configure(state=state)
    sound_slider.configure(state=state)