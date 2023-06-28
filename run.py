import customtkinter
from customtkinter import filedialog
from functions import *


if api_key == "":
    raise ValueError("api_key is empty. Please insert your Pixabay api key in functions.py")


def generate_with_background():
    try:
        num = int(num_entry.get())
        auto_generate(num, True)
        show_info("Generation Complete", "Images generated successfully!")
    except ValueError:
        show_error("Error", "Invalid input for number of images.")


def generate_without_background():
    try:
        num = int(num_entry.get())
        auto_generate(num, False)
        show_info("Generation Complete", "Images generated successfully!")
    except ValueError:
        show_error("Error", "Invalid input for number of images.")


def watermark_images():
    watermark_text = watermark_entry.get()
    if watermark_text:
        auto_watermark(watermark_text)
        show_info("Watermarking Complete", "Images watermarked successfully!")
    else:
        show_error("Error", "Watermark text is empty.")



customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Create the main window
window = customtkinter.CTk()
window.title("Image Generator")
window.geometry("400x320")

# Create the widgets
title_label = customtkinter.CTkLabel(window, text="Image Generator", font=("Helvetica", 18))
title_label.pack(pady=10)

num_label = customtkinter.CTkLabel(window, text="Number of Images:")
num_label.pack()
num_entry = customtkinter.CTkEntry(window)
num_entry.pack()

bg_button = customtkinter.CTkButton(window, text="Generate with Background", command=generate_with_background)
bg_button.pack(pady=10)

no_bg_button = customtkinter.CTkButton(window, text="Generate without Background", command=generate_without_background)
no_bg_button.pack(pady=10)

watermark_label = customtkinter.CTkLabel(window, text="Watermark Text:")
watermark_label.pack()
watermark_entry = customtkinter.CTkEntry(window)
watermark_entry.pack()

watermark_button = customtkinter.CTkButton(window, text="Watermark Images", command=watermark_images)
watermark_button.pack(pady=10)

# Run the main event loop
window.mainloop()