import customtkinter as ctk

def render(parent):
    title = ctk.CTkLabel(
        parent,
        text="Upload",
        font=ctk.CTkFont(size=26, weight="bold")
    )
    title.pack(anchor="nw", padx=30, pady=30)

    label = ctk.CTkLabel(
        parent,
        text="Upload functionality coming soon...",
        text_color="#aaaaaa"
    )
    label.pack(anchor="nw", padx=30, pady=10)