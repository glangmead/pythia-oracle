#!/usr/bin/env python
#-*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------
#  Styles, Fonts, Colors
#
##---------------------------------------------------------------------------------------

import kivy
from kivy.utils import get_color_from_hex
import random

# way more palettes that are needed, not all tested well, but shiny
palette = {

"olivine_grove" : {
    "name" : "olivine grove",
    "primary" : "8A8C7E", 		    # gray
    "secondary" : "E3DFC2",		    # yellow
    "accent1" : "809569",			# green
    "accent2" : "70553A",			# brown
    "neutral" : "2B392A",			# black
    "text" : "FFFFFF",
    "black" : "000000",
    "white" : "FFFFFF"
},

"raspberries" : {
    "name" : "raspberries",
    "primary" : "f36172",           # raspberry
    "secondary" : "f7cbe1",         # light mauve
    "accent1" : "9f2c35",           # dark raspberry red
    "accent2" : "db879d",           # mauve
    "neutral" : "5c0e19",           # very dark raspberry red
    "text" : "FFFFFF",
    "white" : "ebe3d9",
    "black" : "000000"
},

"blackberries" : {
    "name" : "blackberries",
    "primary" : "7B5E61",           # dark mauve
    "secondary" : "aeacac",         # warm gray
    "accent1" : "3d473f",           # dark olive green
    "accent2" : "bdaaad",           # mauve
    "neutral" : "1d1d2b",           # blackberry
    "text" : "FFFFFF",
    "white" : "ebe3d9",
    "black" : "000000"
},

"cherry_coffee" : {
    "name" : "cherry coffee",
    "primary" : "834422",           # cherry (swapped with brown)
    "secondary" : "f6e7c8",         # peach
    "accent1" : "903035",           # dark peach d9ad92, now a brown
    "accent2" : "a1aeb7",           # weathered blue
    "neutral" : "2c1f1f",           # dark coffee
    "text" : "FFFFFF",
    "white" : "ebe3d9",
    "black" : "000000"
},

"black_cat" : {
    "name" : "black cat",
    "primary" : "abaaaa",           # dark gray
    "secondary" : "ededed",         # white gray
    "accent1" : "5b5a5e",           # very dark gray
    "accent2" : "dddddd",           # light gray
    "neutral" : "252525",           # almost black gray
    "text" : "FFFFFF",
    "white" : "f2f2f6",
    "black" : "000000"
},

"sin_city" : {
    "name" : "sin city",
    "primary" : "abaaaa",           # dark gray
    "secondary" : "ededed",         # white gray
    "accent1" : "5b5a5e",           # very dark gray
    "accent2" : "9d2e39",           # light gray
    "neutral" : "252525",           # almost black gray
    "text" : "FFFFFF",
    "white" : "f2f2f6",
    "black" : "000000"
},

"from_hastings" : {
    "name" : "from hastings",
    "primary" : '3f2c1d',           # warm brown
    "secondary" : 'fbf0dc',         # pale cream
    "accent1" : '3b3f54',           # slate blue bdc0d1
    "accent2" : '851706',           # dark red
    "neutral" : '383626',           # chocolate brown
    "text" : "FFFFFF",
    "white" : "f2f2f6",
    "black" : "000000"
},

"gruvbox_dark" : {
    "name" : "gruvbox dark",
    "primary" : "ebdbb2",         # gruvbox cream
    "secondary" : "a89984",       # gruvbox gray
    "accent1" : "83a598",         # gruvbox red
    "accent2" : "cc241d",         # gruvbox blue
    "neutral" : "282828",         # gruvbox brown
    "text" : "FFFFFF",
    "white" : "FFFFFF",
    "black" : "000000"
},

"surf_sunset" : {
    "name" : "surf sunset",
    "primary" : "e06040",         # orange-pink
    "secondary" : "e06060",       # pink
    "accent1" : "c04040",         # red-pink
    "accent2" : "402020",         # dark brown
    "neutral" : "202020",         # near black
    "text" : "FFFFFF",
    "white" : "FFFFFF",
    "black" : "000000"
}, 
}

def setColors(palette):
    primary = get_color_from_hex(palette["primary"])
    secondary = get_color_from_hex(palette["secondary"])
    accent1 = get_color_from_hex(palette["accent1"])
    accent2 = get_color_from_hex(palette["accent2"])
    neutral = get_color_from_hex(palette["neutral"])
    text = get_color_from_hex(palette["text"])
    black = get_color_from_hex(palette["black"])
    white = get_color_from_hex(palette["white"])

    return primary, secondary, accent1, accent2, neutral, text, black, white

#----
# This saves all palettes available to a list in a text file for ease of generating backgrounds
def saveColors():
    holder = ""
    for pal in palette:
        name = palette[pal]["name"] #.replace (" ", "_")
        holder = holder + "[\"" + name + "\",\"#" + palette[pal]["primary"] + "\",\"#" + palette[pal]["secondary"] + "\",\"#"
        holder = holder + palette[pal]["accent1"] + "\",\"#" + palette[pal]["accent2"] + "\",\"#" + palette[pal]["neutral"] + "\"],\r"

        file_ = open('palettes.txt', 'w')
        file_.write(holder)
        file_.close()

# uncomment the next line to make the previous function work
#saveColors()

# different methods of setting the palette manually
#curr_palette = palette[random.choice(palette.keys())]
#curr_palette = palette["sin_city"]
#curr_palette = palette[palette.keys()[0]]

try:
    with open("./resources/defaults/current_palette.txt", "r") as config_file:
        curr_palette = palette[config_file.read()]
except:
    curr_palette = palette[random.choice(palette.keys())]

primary, secondary, accent1, accent2, neutral, textcolor, black, white = setColors(curr_palette)
