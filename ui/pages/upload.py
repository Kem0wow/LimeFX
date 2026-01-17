import customtkinter as ctk
from tkinter import filedialog, messagebox
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from jsonManager import (load_uploaded_sounds, save_uploaded_sounds, delete_sound,
                         validate_name, cleanup_unused_files, add_or_update_sound)

def create_sound_item(parent, sound, refresh_callback):
    item_frame = ctk.CTkFrame(parent, fg_color="#2b2b2b", corner_radius=8)
    item_frame.pack(anchor="w", padx=10, pady=8, fill="x", side="top")
    
    sound_name = sound["name"][:15]
    sound_info = f"Button {sound['button']}: {sound_name}"
    info_label = ctk.CTkLabel(
        item_frame,
        text=sound_info,
        text_color="#ffffff",
        anchor="w",
        font=ctk.CTkFont(size=12, weight="bold")
    )
    info_label.pack(side="left", padx=10, pady=8, fill="x", expand=True)
    
    path_label = ctk.CTkLabel(
        item_frame,
        text=sound["file"],
        text_color="#888888",
        anchor="w",
        font=ctk.CTkFont(size=10)
    )
    path_label.pack(side="left", padx=10, pady=(0, 8), fill="x")
    
    def delete_action():
        if messagebox.askyesno("Delete", f"Delete '{sound_name}'?"):
            delete_sound(sound["button"], refresh_callback)
    
    del_btn = ctk.CTkButton(
        item_frame,
        text="✕",
        width=30,
        height=30,
        command=delete_action,
        fg_color="#b22222",
        hover_color="#ff4040",
        font=ctk.CTkFont(size=14)
    )
    del_btn.pack(side="right", padx=10, pady=8)

def refresh_sound_list(scrollable_frame, refresh_callback):
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    
    sounds = load_uploaded_sounds()
    if sounds:
        for sound in sounds:
            create_sound_item(scrollable_frame, sound, refresh_callback)
    else:
        empty_label = ctk.CTkLabel(
            scrollable_frame,
            text="No sounds uploaded yet",
            text_color="#666666"
        )
        empty_label.pack(anchor="w", padx=10, pady=10)

def render(parent):
    title = ctk.CTkLabel(
        parent,
        text="Upload",
        font=ctk.CTkFont(size=26, weight="bold")
    )
    title.pack(anchor="nw", padx=30, pady=30)

    upload_frame = ctk.CTkFrame(parent, fg_color="transparent")
    upload_frame.pack(anchor="nw", padx=30, pady=10)

    name_label = ctk.CTkLabel(upload_frame, text="Sound Name (max 15):")
    name_label.pack(anchor="nw", pady=(0, 5))

    name_entry = ctk.CTkEntry(upload_frame, width=200, placeholder_text="Enter name")
    name_entry.pack(anchor="nw", pady=(0, 10))
    
    def on_name_change(*args):
        current = name_entry.get()
        if len(current) > 15:
            name_entry.delete(0, "end")
            name_entry.insert(0, current[:15])
    name_entry.bind("<KeyRelease>", on_name_change)

    btn_label = ctk.CTkLabel(upload_frame, text="Button (1-9):")
    btn_label.pack(anchor="nw", pady=(0, 5))

    button_combo = ctk.CTkComboBox(
        upload_frame,
        values=[str(i) for i in range(1, 10)],
        width=100,
        state="readonly",
        dropdown_font=ctk.CTkFont(size=11),
        button_color="#4a90e2",
        button_hover_color="#357ABD"
    )
    button_combo.set("1")
    button_combo.pack(anchor="nw", pady=(0, 10))

    list_label = ctk.CTkLabel(
        parent,
        text="Uploaded Sounds",
        font=ctk.CTkFont(size=14, weight="bold")
    )
    list_label.pack(anchor="nw", padx=30, pady=(5, 5))

    scrollable_frame = ctk.CTkScrollableFrame(
        parent,
        width=500,
        height=200,
        fg_color="#1f1f1f"
    )
    scrollable_frame.pack(padx=30, fill="both", expand=True)

    def refresh_list():
        refresh_sound_list(scrollable_frame, refresh_list)

    def upload_file():
        file_path = filedialog.askopenfilename(
            title="Select Audio File",
            filetypes=[("Audio Files", "*.mp3 *.wav *.ogg *.mp4"), ("All Files", "*.*")]
        )
        
        if not file_path:
            return
        
        sound_name = validate_name(name_entry.get())
        button_num = int(button_combo.get())
        
        if add_or_update_sound(button_num, sound_name, f"sounds/{os.path.basename(file_path)}", file_path):
            messagebox.showinfo("Success", f"Sound '{sound_name}' uploaded to Button {button_num}!")
            name_entry.delete(0, "end")
            cleanup_unused_files()
            refresh_list()
        else:
            messagebox.showerror("Error", "Failed to upload sound")

    upload_btn = ctk.CTkButton(
        upload_frame,
        text="Upload",
        command=upload_file,
        width=150,
        height=35
    )
    upload_btn.pack(anchor="nw", pady=10)

    divider = ctk.CTkFrame(parent, fg_color="#3a3a3a", height=1)
    divider.pack(fill="x", padx=30, pady=10)

    refresh_list()