import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from jsonManager import load_settings, save_settings

def render(parent):
    settings = load_settings()
    
    title = ctk.CTkLabel(
        parent,
        text="Settings",
        font=ctk.CTkFont(size=26, weight="bold")
    )
    title.pack(anchor="nw", padx=30, pady=30)

    mic_label = ctk.CTkLabel(parent, text="Microphone Input")
    mic_label.pack(anchor="nw", padx=30, pady=(20, 5))

    mic_devices = ["Default Microphone", "USB Microphone", "Virtual Cable Mic"]

    def on_mic_change(value):
        save_settings(value, out_combo.get())

    mic_combo = ctk.CTkComboBox(
        parent,
        values=mic_devices,
        width=300,
        command=on_mic_change,
        state="readonly",
        dropdown_font=ctk.CTkFont(size=11),
        button_color="#4a90e2",
        button_hover_color="#357ABD"
    )
    mic_combo.set(settings["input_device"])
    mic_combo.pack(anchor="nw", padx=30)

    out_label = ctk.CTkLabel(parent, text="Soundboard Output")
    out_label.pack(anchor="nw", padx=30, pady=(20, 5))

    output_devices = ["Default Speakers", "Headphones", "Virtual Cable Output"]

    def on_output_change(value):
        save_settings(mic_combo.get(), value)

    out_combo = ctk.CTkComboBox(
        parent,
        values=output_devices,
        width=300,
        command=on_output_change,
        state="readonly",
        dropdown_font=ctk.CTkFont(size=11),
        button_color="#4a90e2",
        button_hover_color="#357ABD"
    )
    out_combo.set(settings["output_device"])
    out_combo.pack(anchor="nw", padx=30)

    bg_btn = ctk.CTkButton(
        parent,
        text="Run in Background",
        width=200,
        height=40,
        command=lambda: print("Run in bg")
    )
    bg_btn.pack(anchor="nw", padx=30, pady=(30, 0))