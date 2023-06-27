import requests
import random
import textwrap
import os
from PIL import Image, ImageDraw, ImageFont


api_key = "" # insert you api key here

def get_random_image_url():
    url = f"https://pixabay.com/api/?key={api_key}&q=night&image_type=photo&min_width=1080&min_height=1080"
    #in url you can modify q= to get images you want. Example: q=yellow+flowers
    response = requests.get(url)
    data = response.json()
    photos = data["hits"]
    random_photo = random.choice(photos)
    image_url = random_photo["largeImageURL"]
    return image_url


def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    quote = response.json()["content"]
    author = response.json()["author"]
    return f"{quote}\n                                      - {author}"


def save_image(image_url, quote_text, output_file, background:bool):
    if background:
        image = Image.open(requests.get(image_url, stream=True).raw)
        image = image.resize((1080, 1080))
        image = image.convert("RGB")
    else:
        image = Image.open(("bg.jpg"))
        image = image.convert("RGB")

    f = ["CookbookNormalRegular-6YmjD", "ComicLemon-mLx6V", "CookbookBoldBold-ywv3M"] #fonts
    l = [70, 40, 70] #sizes of fonts
    pick = random.randint(0, len(f)-1) #picking random font

    quote_font = ImageFont.truetype(f"fonts/{f[pick]}.ttf", l[pick])
    quote_lines = textwrap.wrap(quote_text, width=30)

    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textbbox((0, 0), quote_lines[0], font=quote_font)[2:]
    x = (image.width - text_width) // 2
    y = (image.height - text_height * len(quote_lines)) // 2

    # additional font styling
    shadow_color = (0, 0, 0)  # shadow color
    shadow_offset = 3  # shadow offset in pixels

    for line in quote_lines:
        # draw shadow text
        shadow_x = x + shadow_offset
        shadow_y = y + shadow_offset
        draw.text((shadow_x, shadow_y), line, font=quote_font, fill=shadow_color)

        # draw main text
        draw.text((x, y), line, font=quote_font, fill=(255, 255, 255))
        y += text_height

    image.save(output_file)


def add_quote(quote): #this will save quote to quotes.txt
    q = open("quotes.txt", "a")
    q.write(f"{quote}\n")
    q.close()


def check_for_quote(quote): # this will check if quote is in quotes.txt
    q = open("quotes.txt", "r")
    if quote in q:
        return True
    return False


def add_watermarks(input_image_path, output_image_path, watermark_text):
    # Load the input image
    image = Image.open(input_image_path).convert("RGBA")

    # Create a transparent overlay image for the watermark
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))

    # Load a font for the watermark
    font = ImageFont.truetype("arial.ttf", 50)

    # Create a drawing object
    draw = ImageDraw.Draw(overlay)

    # Get the dimensions of the image and watermark text
    image_width, image_height = image.size
    text_width, text_height = draw.textsize(watermark_text, font=font)

    # Calculate the positions to place the watermarks
    margin = 200
    x_positions = [margin, image_width - text_width - margin]
    y_positions = [margin, image_height - text_height - margin]

    # Add watermarks at each position
    for x in x_positions:
        for y in y_positions:
            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    # Composite the overlay onto the original image
    watermarked = Image.alpha_composite(image, overlay)

    # Save the watermarked image
    watermarked.save(output_image_path, format='PNG')

    print(f"Watermark added successfully.")


def auto_watermark(watermark_text):     #this will go through every picture that is in "to_watermark"
    dirs = os.listdir("to_watermark")   #folder and it'll watermark it, and move it to "watermarked"
    for image_name in dirs:
        add_watermarks(f"to_watermark/{image_name}", f"watermarked/{image_name}", watermark_text)
        os.remove(f"to_watermark/{image_name}")


def auto_generate(num, background:bool):
    image_url = ""
    while num > 0:
        if background:
            image_url = get_random_image_url()
        quote = get_random_quote()

        if not check_for_quote(quote):
            add_quote(quote)

            # save the image with the quote
            output_file = f"images/image_{num}.jpg"
            save_image(image_url, quote, output_file, background)
            num -= 1
            print(num+1)
        else:
            num += 1
            print("Duplicate")
