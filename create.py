import os

if "images" not in os.listdir():
    os.mkdir("images")
if "to_watermark" not in os.listdir():
    os.mkdir("to_watermark")
if "watermarked" not in os.listdir():
    os.mkdir("watermarked")