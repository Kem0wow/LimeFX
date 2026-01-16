import customtkinter as ctk
from PIL import Image

def left_btn(parent, icon_path, text, command):
    icon = ctk.CTkImage(
        light_image=Image.open(icon_path),
        dark_image=Image.open(icon_path),
        size=(20, 20)
    )

    btn = ctk.CTkButton(
        parent,
        text=text,
        image=icon,
        command=command,
        height=42,
        corner_radius=8,
        fg_color="#2b2b2b",
        hover_color="#3a3a3a",
        anchor="w",
        compound="left"
    )

    btn.image = icon
    btn.pack(fill="x", padx=20, pady=6)
    return btn