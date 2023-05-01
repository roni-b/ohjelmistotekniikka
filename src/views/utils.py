from tkinter import ttk

def create_content_frame(canvas):
    content_frame = ttk.Frame(canvas)
    content_frame.bind(
        "<Configure>",
        lambda event: canvas.configure(
        scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=content_frame, anchor="nw")
    return content_frame
