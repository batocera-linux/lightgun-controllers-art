#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import json
import sys

def png_to_png_with_texts(input_png_path, output_png_path, data, width=None, height=None, font_path=None):
    img_big = Image.open(input_png_path)
    ratio = img_big.width / img_big.height

    img_width  = width
    img_height = height
    if img_width is None and img_height is not None:
        img_width = int(img_height * ratio)
    if img_width is not None and img_height is None:
        img_height = int(img_width * ratio)
    if img_width is None or img_height is None:
        img_width = width
        img_height = height

    img = img_big.resize((img_width, img_height))
    draw = ImageDraw.Draw(img)

    # font
    font = {}
    if "font_size_per_height" in data:
        font_size = int(data["font_size_per_height"]*img_height)
        font[font_size] = ImageFont.truetype(font_path, font_size)

    # lines
    if "texts" in data:
        for text in data["texts"]:
            line_color = "black"
            line_size  = 2
            if "line_color" in text:
                line_color = text["line_color"]
            if "line_size" in text:
                line_size = text["line_size"]
            if "line" in text:
                points = []
                for i, v in enumerate(text["line"]):
                    if i % 2 == 1:
                        points.append((text["line"][i-1] * img_width, v * img_height))
                draw.line(points, fill=line_color, width=line_size)

    # texts
    for text in data["texts"]:
        # x, y
        x = round(text["x"]*img_width)
        y = round(text["y"]*img_height)

        # color
        color = "black"
        if "color" in data:
            color = data["color"]
        if "color" in text:
            color = text["color"]

        # font
        font_size = int(data["font_size_per_height"]*img_height)
        if "font_size_per_height" in text:
            font_size = int(text["font_size_per_height"]*img_height)
            if font_size not in font:
                font[font_size] = ImageFont.truetype(font_path, font_size)

        # alignment
        text_width = draw.textlength(text["value"], font[font_size])
        align = "left"
        if "align" in text:
            align = text["align"]
        if align == "center":
            x = x-int(text_width/2)
        if align == "right":
            x = x-text_width
        draw.text((x, y), text["value"], fill=color, font=font[font_size])

    # save
    img.save(output_png_path, "PNG")

def gun_help_replace(text, replacements):
    res = text
    for r in replacements:
        res = res.replace(r, replacements[r])
    return res

if len(sys.argv) != 4:
    print("{} <input.png> <output.png> <font.ttf>".format(sys.argv[0]))
    exit(1)

input  = sys.argv[1]
output = sys.argv[2]
ttf    = sys.argv[3]

replacements = {
    "<TRIGGER>": "TRIGGER",
    "<ACTION>": "ACTION",
    "<START>": "START",
    "<SELECT>": "SELECT",
    "<SUB1>": "SUB1",
    "<SUB2>": "SUB2",
    "<SUB3>": "SUB3",
    "<D-PAD>": "D-PAD",
}

with open((input[0:-4]+".infos").replace("/png/", "/infos/"), "r", encoding="utf-8") as file:
    data = json.load(file)

    # replace data in texts
    for n, text in enumerate(data["texts"]):
        data["texts"][n]["value"] = gun_help_replace(data["texts"][n]["value"], replacements)
    
    png_to_png_with_texts(input, output, data, font_path=ttf, height=800)
