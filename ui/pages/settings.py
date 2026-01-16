import customtkinter as ctk

def render(parent):
    title = ctk.CTkLabel(
        parent,
        text="Settings",
        font=ctk.CTkFont(size=26, weight="bold")
    )
    title.pack(anchor="nw", padx=30, pady=30)

    # --- INPUT DEVICE (MIC) ---
    mic_label = ctk.CTkLabel(parent, text="Microphone Input")
    mic_label.pack(anchor="nw", padx=30, pady=(20, 5))

    mic_devices = [
        "Default Microphone",
        "USB Microphone",
        "Virtual Cable Mic"
    ]

    mic_combo = ctk.CTkComboBox(
        parent,
        values=mic_devices,
        width=300
    )
    mic_combo.set(mic_devices[0])
    mic_combo.pack(anchor="nw", padx=30)

    # --- OUTPUT DEVICE (SOUNDBOARD) ---
    out_label = ctk.CTkLabel(parent, text="Soundboard Output")
    out_label.pack(anchor="nw", padx=30, pady=(20, 5))

    output_devices = [
        "Default Speakers",
        "Headphones",
        "Virtual Cable Output"
    ]

    out_combo = ctk.CTkComboBox(
        parent,
        values=output_devices,
        width=300
    )
    out_combo.set(output_devices[0])
    out_combo.pack(anchor="nw", padx=30)