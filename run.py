from functions import *


if "images" not in os.listdir():
    os.mkdir("images")
if "to_watermark" not in os.listdir():
    os.mkdir("to_watermark")
if "watermarked" not in os.listdir():
    os.mkdir("watermarked")
if api_key == "":
    raise ValueError("api_key is empty. Please insert your Pixabay api key in functions.py")

print("\nIf you want to generate random quote with background image type: 1")
print("If you want to generate random quote without background image type: 2")
print("If you want to watermark pictures type: 3")

inp = int(input())

if inp not in [1,2,3]:
    raise ValueError("Invalid input")

if inp == 1:
    n = int(input("How many pictures you want to generate: "))
    auto_generate(n, True)
elif inp == 2:
    n = int(input("How many pictures you want to generate: "))
    auto_generate(n, False)
else:
    watermark_text = input(str("Watermark text: "))
    auto_watermark(watermark_text)