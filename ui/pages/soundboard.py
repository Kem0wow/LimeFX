import customtkinter as ctk

def render(parent):
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

    for i in range(9):
        btn = ctk.CTkButton(
            grid,
            text=f"Sound {i+1}",
            width=140,
            height=90,
            corner_radius=10,
            fg_color="#2b2b2b",
            hover_color="#3a3a3a"
        )
        btn.grid(row=i // 3, column=i % 3, padx=12, pady=12)